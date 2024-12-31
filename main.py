from PyQt5 import QtWidgets
from Ui_window import Ui_MainWindow
from pathlib import Path
import ComputeHashedFeatures
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
        self.playingStatus = [False, False]

        self.audioGraphs = [self.leftGraphWidget, self.rightGraphWidget]
        self.fileLabels = [self.inputLabel_1, self.inputLabel_2]
        self.browseButtons = [self.browseBtn_1, self.browseBtn_2]
        self.playButtons = [self.startBtn_1, self.startBtn_2]
        self.pauseButtons = [self.pauseBtn_1, self.pauseBtn_2]
        self.sliders = [self.slider_1, self.slider_2]
    
    def addEventListeners(self):
        for button in self.browseButtons:
            button.clicked.connect(self.browseFile)
        
        for button in self.playButtons:
            button.clicked.connect(self.playAudio)
        
        for button in self.pauseButtons:
            button.clicked.connect(self.pauseAudio)

        self.resultBtn.clicked.connect(self.computeResult)

    def browseFile(self):
        # Open file dialog to select a WAV file
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Audio File", "", "Audio Files (*.wav)")
        if filePath:
            if self.sender() == self.browseButtons[0]:
                self.loadedFiles[0] = filePath
                self.fileLabels[0].setText(filePath[7 : -4])
            else:
                self.loadedFiles[1] = filePath
                self.fileLabels[1].setText(filePath[7 : -4])
        else:
            QtWidgets.QMessageBox.warning(self, "No File", "No File Was Selected!")
    
    def playAudio(self):
        if self.sender() == self.playButtons[0]:
            if self.loadedFiles[0] != None and self.playingStatus[0] == False:
                self.playingStatus[0] = True
        else:
            if self.loadedFiles[1] != None and self.playingStatus[1] == False:
                self.playingStatus[1] = True
    
    def pauseAudio(self):
        if self.sender() == self.pauseButtons[0]:
            if self.loadedFiles[0] != None and self.playingStatus[0] == True:
                self.playingStatus[0] = False
        else:
            if self.loadedFiles[1] != None and self.playingStatus[1] == True:
                self.playingStatus[1] = False
        
    def computeResult(self):
        if self.loadedFiles[0] == None and self.loadedFiles[1] == None:
            QtWidgets.QMessageBox.warning(self, "No File", "Please Load A File First!")
            return
        
        hashString = ComputeHashedFeatures.processHash(self.loadedFiles[0])
        loadedHash = imagehash.hex_to_hash(hashString)

        databaseFolder = Path("./task5_hashes")
        comparisons = []

        for jsonFile in databaseFolder.glob("*.json"):
            with open(jsonFile, "r") as f:
                data = json.load(f)
                storedHash = imagehash.hex_to_hash(data["featuresHash"])  # Convert stored hash back to imagehash object
                distance = loadedHash - storedHash  # Compute Hamming distance (number of positions at which two binary strings of equal length are different)
                similarityPercentage = (1 - (distance / 64)) * 100 # perceptual hashes are usually 64 bits
                comparisons.append((jsonFile.name, similarityPercentage))

        # Sort by descending similarity
        comparisons.sort(key=lambda x: x[1], reverse=True)

        # Display results
        resultsText = "Similarity Results:\n\n"
        for fileName, similarityPercentage in comparisons:
            resultsText += f"{fileName}: Percentage = {similarityPercentage}\n\n"

        QtWidgets.QMessageBox.information(self, "Comparison Results", resultsText)
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
