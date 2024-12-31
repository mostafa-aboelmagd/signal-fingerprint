from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from Ui_window import Ui_MainWindow
import pyqtgraph as pg
import ComputeHashedFeatures
from pathlib import Path
import numpy as np
import librosa
import sounddevice as sd
import json
import sys
import imagehash

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Load the UI file
        self.setupUi(self)
        self.setupVariables()
        self.addEventListeners()
        self.show()
    
    def setupVariables(self):
        self.loadedFiles = [None, None]
        self.samplingRates = [0, 0]
        self.playingStatus = [False, False]
        self.similarityResults = []

        self.audioGraphs = [self.leftGraphWidget, self.rightGraphWidget]
        self.fileLabels = [self.inputLabel_1, self.inputLabel_2]
        self.browseButtons = [self.browseBtn_1, self.browseBtn_2]
        self.playButtons = [self.startBtn_1, self.startBtn_2]
        self.pauseButtons = [self.pauseBtn_1, self.pauseBtn_2]
        self.sliders = [self.slider_1, self.slider_2]
        for slider in self.sliders:
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(0)
            slider.setTickInterval(10)
            slider.setSingleStep(10)
            slider.setEnabled(False)
    
    def addEventListeners(self):
        for button in self.browseButtons:
            button.clicked.connect(self.browseFile)
        
        for button in self.playButtons:
            button.clicked.connect(self.playAudio)
        
        for button in self.pauseButtons:
            button.clicked.connect(self.pauseAudio)
        
        for slider in self.sliders:
            slider.valueChanged.connect(self.updateSliders)

        self.resultBtn.clicked.connect(self.computeResult)

    def browseFile(self):
        # Open file dialog to select a WAV file
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Audio File", "", "Audio Files (*.wav)")
        if filePath:
            if self.sender() == self.browseButtons[0]:
                if self.loadedFiles[1] is None:
                    self.sliders[0].setValue(100)
                else:
                    for slider in self.sliders:
                        slider.setEnabled(True)

                self.loadedFiles[0], self.samplingRates[0] = librosa.load(filePath, sr=None)
                self.fileLabels[0].setText(Path(filePath).name[8 : -4])
                self.plotAudioWaveform(self.loadedFiles[0], self.samplingRates[0], self.audioGraphs[0])
            else:
                if self.loadedFiles[0] is None:
                    self.sliders[1].setValue(100)
                else:
                    for slider in self.sliders:
                        slider.setEnabled(True)

                self.loadedFiles[1], self.samplingRates[1] = librosa.load(filePath, sr=None)
                self.fileLabels[1].setText(Path(filePath).name[8 : -4])
                self.plotAudioWaveform(self.loadedFiles[1], self.samplingRates[1], self.audioGraphs[1])
        
            self.playingStatus[0] = False
            self.playingStatus[1] = False
            sd.stop()
    
    def plotAudioWaveform(self, loadedAudio, samplingRate, graphWidget):
        # Create time axis
        duration = librosa.get_duration(y=loadedAudio, sr=samplingRate)
        time = np.linspace(0., duration, len(loadedAudio))

        # Plot waveform using pyqtgraph
        graphWidget.clear()  # Clear previous plots
        graphWidget.plot(time, loadedAudio, pen=pg.mkPen(color='b', width=1))

        # Set labels and title
        graphWidget.setLabel("left", "Amplitude")
        graphWidget.setLabel("bottom", "Time (s)")
    
    def playAudio(self):
        if self.sender() == self.playButtons[0]:
            if self.loadedFiles[0] is not None and self.playingStatus[0] == False:
                self.playingStatus[0] = True
                self.playingStatus[1] = False
                sd.stop()
                sd.play(self.loadedFiles[0], self.samplingRates[0])
        else:
            if self.loadedFiles[1] is not None and self.playingStatus[1] == False:
                self.playingStatus[1] = True
                self.playingStatus[0] = False
                sd.stop()
                sd.play(self.loadedFiles[1], self.samplingRates[1])
    
    def pauseAudio(self):
        if self.sender() == self.pauseButtons[0]:
            if self.loadedFiles[0] is not None and self.playingStatus[0] == True:
                self.playingStatus[0] = False
                sd.stop()
        else:
            if self.loadedFiles[1] is not None and self.playingStatus[1] == True:
                self.playingStatus[1] = False
                sd.stop()
        
    def updateSliders(self):
        # Temporarily disconnect the valueChanged signal to avoid infinite loop
        self.sliders[0].blockSignals(True)
        self.sliders[1].blockSignals(True)

        if self.sender() == self.sliders[0]:
            self.sliders[1].setValue(100 - self.sliders[0].value())
        else:
            self.sliders[0].setValue(100 - self.sliders[1].value())
        
        self.sliders[0].blockSignals(False)
        self.sliders[1].blockSignals(False)
        
    def computeResult(self):
        if self.loadedFiles[0] is None and self.loadedFiles[1] is None:
            return
        
        self.similarityResults = []

        if self.loadedFiles[0] is not None and self.loadedFiles[1] is not None:
            # Get the lengths of both signals
            len1 = len(self.loadedFiles[0])
            len2 = len(self.loadedFiles[1])

            # Pad zeros to the shorter signal
            if len1 < len2:
                loadedAudio1 = np.pad(self.loadedFiles[0], (0, len2 - len1), mode="constant")
                loadedAudio2 = self.loadedFiles[1]
            else:
                loadedAudio1 = self.loadedFiles[0]
                loadedAudio2 = np.pad(self.loadedFiles[1], (0, len1 - len2), mode="constant")

            weightedSignal = (self.sliders[0].value() / 100.0) * loadedAudio1 +  (self.sliders[1].value() / 100.0) * loadedAudio2
            samplingRate = self.samplingRates[0]

        elif self.loadedFiles[0] is not None:
            weightedSignal = self.loadedFiles[0]
            samplingRate = self.samplingRates[0]
        else:
            weightedSignal = self.loadedFiles[1]
            samplingRate = self.samplingRates[1]

        hashObject = ComputeHashedFeatures.processHash(weightedSignal, samplingRate)
        databaseFolder = Path("./task5_hashes")

        for jsonFile in databaseFolder.glob("*.json"):
            with open(jsonFile, "r") as f:
                distances = []
                data = json.load(f)

                for key in data:
                    loadedFeatureHash = imagehash.hex_to_hash(hashObject[key]) # Converts hexadecimal hash of our browsed signals into imagehash object
                    storedFeatureHash = imagehash.hex_to_hash(data[key])
                    distances.append(loadedFeatureHash - storedFeatureHash) # Computes Hamming distance (number of positions at which two binary strings of equal length are different)
                
                averageDistance = 0
                for distance in distances:
                    averageDistance += distance
                averageDistance /= len(distances)

                similarityPercentage = (1 - (averageDistance / 255)) * 100
                self.similarityResults.append((jsonFile.name[8 : -5], similarityPercentage))

        # Sort by descending similarity and get the top 10
        self.similarityResults.sort(key=lambda x: x[1], reverse=True)
        self.similarityResults = self.similarityResults[ : min(10, len(self.similarityResults))]

        self.showResult()
    
    def showResult(self):
        # Clear the table before inserting new data
        self.dataTable.setRowCount(0)

        # Populate the table with the comparison results
        for fileName, similarityPercentage in self.similarityResults:
            rowPosition = self.dataTable.rowCount()
            self.dataTable.insertRow(rowPosition)

            # Create and style table items
            fileItem = QTableWidgetItem(fileName)
            fileItem.setTextAlignment(Qt.AlignCenter)
            scoreItem = QTableWidgetItem(f"{similarityPercentage:.2f}%")
            scoreItem.setTextAlignment(Qt.AlignCenter)

            self.dataTable.setItem(rowPosition, 0, fileItem)
            self.dataTable.setItem(rowPosition, 1, scoreItem)
                
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
