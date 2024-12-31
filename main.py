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
        #self.browseButton.clicked.connect(self.browseFile)
        #self.resultButton.clicked.connect(self.computeResult)
        self.show()

    """def browseFile(self):
        # Open file dialog to select a WAV file
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Music File", "", "Audio Files (*.wav)")
        if filePath:
            self.loadedFile = filePath
            print(self.loadedFile)
        else:
            QtWidgets.QMessageBox.warning(self, "No File", "No file was selected!")
    
    def computeResult(self):
        if not self.loadedFile:
            QtWidgets.QMessageBox.warning(self, "No File", "Please load a file first!")
            return
        
        hashString = ComputeHashedFeatures.processHash(self.loadedFile)
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

        QtWidgets.QMessageBox.information(self, "Comparison Results", resultsText)"""
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
