from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1145, 937)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:black;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.topRowLayout = QtWidgets.QHBoxLayout()
        self.topRowLayout.setSpacing(400)
        self.topRowLayout.setContentsMargins(0, 40, 0, 0)
        self.topRowLayout.setObjectName("topRowLayout")

        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseButton.setStyleSheet("background-color: #00FFFF; border-radius: 12px; font-size: 30px; font-weight:bold; padding: 12px; margin-left: 50;")
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setText("Browse")
        self.topRowLayout.addWidget(self.browseButton)

        self.inputCombo = QtWidgets.QComboBox(self.centralwidget)
        self.inputCombo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inputCombo.setStyleSheet("background-color: #444444; color: white; border: 1px solid white; border-radius: 6px; padding: 8px; font-size: 30px; font-weight: bold; margin-right: 30;")
        self.inputCombo.setObjectName("inputCombo")
        self.inputCombo.addItems(["Input 1", "Input 2"])
        self.topRowLayout.addWidget(self.inputCombo)

        self.verticalLayout.addLayout(self.topRowLayout)

        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setSpacing(220)
        self.inputLayout.setContentsMargins(0, 117, 0, 0)
        self.inputLayout.setObjectName("inputLayout")

        self.input1 = QtWidgets.QLabel(self.centralwidget)
        self.input1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input1.setStyleSheet(" color: white; border: 1px solid white; border-radius: 6px; padding: 4px; font-size: 30px; margin-bottom: 50; margin-right: 50; margin-left:50; height: 100;")
        self.input1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.input1.setObjectName("input1")
        self.inputLayout.addWidget(self.input1)

        self.input2 = QtWidgets.QLabel(self.centralwidget)
        self.input2.setStyleSheet(" color: white; border: 1px solid white; border-radius: 6px; padding: 4px; font-size: 30px; margin-bottom: 50; margin-left: 50; margin-right: 50;")
        self.input2.setObjectName("input2")
        self.inputLayout.addWidget(self.input2)

        self.verticalLayout.addLayout(self.inputLayout)

        self.slidersLayout = QtWidgets.QHBoxLayout()
        self.slidersLayout.setSpacing(250)
        self.slidersLayout.setContentsMargins(40, 0, 40, 85)
        self.slidersLayout.setObjectName("slidersLayout")

        self.slider1 = QtWidgets.QSlider(self.centralwidget)
        self.slider1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.slider1.setStyleSheet("background-color: black;")
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.slidersLayout.addWidget(self.slider1)

        self.slider2 = QtWidgets.QSlider(self.centralwidget)
        self.slider2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.slider2.setStyleSheet("background-color: black;")
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.slidersLayout.addWidget(self.slider2)

        self.verticalLayout.addLayout(self.slidersLayout)

        self.resultButton = QtWidgets.QPushButton(self.centralwidget)
        self.resultButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultButton.setStyleSheet("background-color: #00FFFF; border-radius: 12px; font-size: 30px; font-weight:bold; padding: 12px; margin-top: 20; margin-bottom: 30; margin-left: 420; margin-right: 420;")
        self.resultButton.setObjectName("resultButton")
        self.resultButton.setText("Result")
        self.verticalLayout.addWidget(self.resultButton)

        self.tableLayout = QtWidgets.QVBoxLayout()
        self.tableLayout.setSpacing(0)
        self.tableLayout.setContentsMargins(150, 0, 150, 0)
        self.tableLayout.setObjectName("tableLayout")

        self.outputTable = QtWidgets.QTableWidget(self.centralwidget)
        self.outputTable.setEnabled(True)
        self.outputTable.setAutoFillBackground(False)
        self.outputTable.setStyleSheet(
            """
            QTableWidget {
                background-color: black;
                gridline-color: white;
                color: white;
            }

            QHeaderView::section {
                background-color: black;
                color: white;
                border: 1px solid white;
                font-size: 20px;
                font-weight: bold;
            }

            QTableWidget::item {
                border: none;
                color: white;
            }

            QTableCornerButton::section {
                background-color: black;
                border: 1px solid white;
            }
            """
        )
        self.outputTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputTable.setMidLineWidth(0)
        self.outputTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.outputTable.setGridStyle(QtCore.Qt.SolidLine)
        self.outputTable.setRowCount(0)
        self.outputTable.setColumnCount(3)
        self.outputTable.setHorizontalHeaderLabels(["Song name", "Singer", "Score"])
        header = self.outputTable.horizontalHeader()
        header.setDefaultSectionSize(265)
        header.setHighlightSections(True)
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.outputTable.setObjectName("outputTable")

        self.tableLayout.addWidget(self.outputTable)
        self.verticalLayout.addLayout(self.tableLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shazam-like app"))
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
