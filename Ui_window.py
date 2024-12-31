import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QSlider, QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from pyqtgraph import PlotWidget

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(0, 0, 1177, 842)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 74);")

        # Central widget and layout
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainVerticalLayout = QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)

        # Top layout (graphLayout)
        self.graphLayout = QHBoxLayout()
        self.graphLayout.setObjectName("graphLayout")
        self.graphLayout.setSpacing(10)  # add some spacing between both left and right layouts
        self.mainVerticalLayout.addLayout(self.graphLayout)

        # Left Vertical Layout
        self.leftVerticalLayout = QVBoxLayout()
        self.leftVerticalLayout.setObjectName("leftVerticalLayout")
        self.graphLayout.addLayout(self.leftVerticalLayout)

        self.leftVerticalLayout.addSpacing(20)  # Top margin for left graph

        self.inputLabel_1 = QLabel("")
        self.inputLabel_1.setObjectName("inputLabel_1")
        self.inputLabel_1.setStyleSheet("color: white; border: 1px solid white; border-radius: 6px; padding: 4px; font-size: 20px; margin-right: 100px;")
        self.leftVerticalLayout.addWidget(self.inputLabel_1)

        self.leftGraphWidget = PlotWidget()
        self.leftGraphWidget.setObjectName("leftGraphWidget")
        self.leftGraphWidget.setBackground((0, 0, 35))
        self.leftGraphWidget.setFixedHeight(250)
        self.leftVerticalLayout.addWidget(self.leftGraphWidget)

        self.leftVerticalLayout.addSpacing(20)  # Bottom margin for left graph

        self.leftGraphBtnsLayout = QHBoxLayout()
        self.leftGraphBtnsLayout.setObjectName("leftGraphBtnsLayout")
        self.leftVerticalLayout.addLayout(self.leftGraphBtnsLayout)

        self.browseBtn_1 = QPushButton("Browse")
        self.browseBtn_1.setObjectName("browseBtn_1")
        self.startBtn_1 = QPushButton("Start")
        self.startBtn_1.setObjectName("startBtn_1")
        self.pauseBtn_1 = QPushButton("Pause")
        self.pauseBtn_1.setObjectName("pauseBtn_1")

        for btn in [self.browseBtn_1, self.startBtn_1, self.pauseBtn_1]:
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("background-color: rgb(0, 85, 255); border-radius: 12px; font-size: 20px; font-weight:bold; color: rgb(232, 232, 232); padding: 12px; margin: 2px;")
            self.leftGraphBtnsLayout.addWidget(btn)

        self.leftVerticalLayout.addSpacing(10)  # Space between buttons and slider

        self.slider_1 = QSlider(Qt.Horizontal)
        self.slider_1.setObjectName("slider_1")
        self.slider_1.setCursor(Qt.PointingHandCursor)
        self.leftVerticalLayout.addWidget(self.slider_1)

        # Right Vertical Layout
        self.rightVerticalLayout = QVBoxLayout()
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")
        self.rightVerticalLayout.setContentsMargins(20, 0, 0, 0)  # Add margin-left to the right layout
        self.graphLayout.addLayout(self.rightVerticalLayout)

        self.rightVerticalLayout.addSpacing(20)  # Top margin for right graph

        self.inputLabel_2 = QLabel("")
        self.inputLabel_2.setObjectName("inputLabel_2")
        self.inputLabel_2.setStyleSheet("color: white; border: 1px solid white; border-radius: 6px; padding: 4px; font-size: 20px; margin-right: 100px;")
        self.rightVerticalLayout.addWidget(self.inputLabel_2)

        self.rightGraphWidget = PlotWidget()
        self.rightGraphWidget.setObjectName("rightGraphWidget")
        self.rightGraphWidget.setBackground((0, 0, 35))
        self.rightGraphWidget.setFixedHeight(250)
        self.rightVerticalLayout.addWidget(self.rightGraphWidget)

        self.rightVerticalLayout.addSpacing(20)  # Bottom margin for right graph

        self.rightGraphBtnsLayout = QHBoxLayout()
        self.rightGraphBtnsLayout.setObjectName("rightGraphBtnsLayout")
        self.rightVerticalLayout.addLayout(self.rightGraphBtnsLayout)

        self.browseBtn_2 = QPushButton("Browse")
        self.browseBtn_2.setObjectName("browseBtn_2")
        self.startBtn_2 = QPushButton("Start")
        self.startBtn_2.setObjectName("startBtn_2")
        self.pauseBtn_2 = QPushButton("Pause")
        self.pauseBtn_2.setObjectName("pauseBtn_2")

        for btn in [self.browseBtn_2, self.startBtn_2, self.pauseBtn_2]:
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("background-color: rgb(0, 85, 255); border-radius: 12px; font-size: 20px; font-weight:bold; color: rgb(232, 232, 232); padding: 12px; margin: 2px;")
            self.rightGraphBtnsLayout.addWidget(btn)

        self.rightVerticalLayout.addSpacing(10)  # Space between buttons and slider

        self.slider_2 = QSlider(Qt.Horizontal)
        self.slider_2.setObjectName("slider_2")
        self.slider_2.setCursor(Qt.PointingHandCursor)
        self.rightVerticalLayout.addWidget(self.slider_2)

        # Button Layout (Result button)
        self.resultBtnLayout = QHBoxLayout()
        self.resultBtnLayout.setObjectName("resultBtnLayout")
        self.mainVerticalLayout.addLayout(self.resultBtnLayout)

        self.resultBtn = QPushButton("Result")
        self.resultBtn.setObjectName("resultBtn")
        self.resultBtn.setCursor(Qt.PointingHandCursor)
        self.resultBtn.setStyleSheet("background-color: rgb(0, 85, 255); border-radius: 12px; font-size: 30px; font-weight:bold; color: rgb(232, 232, 232); padding: 12px; margin-top: 20; margin-bottom: 30; margin-left: 420; margin-right: 420;")
        self.resultBtnLayout.addWidget(self.resultBtn)

        # Table Layout
        self.tableLayout = QHBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.mainVerticalLayout.addLayout(self.tableLayout)

        self.dataTable = QTableWidget(0, 2)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setHorizontalHeaderLabels(["Song", "Score"])

        font = QFont()
        font.setPointSize(15)
        font.setBold(True)

        # Styling the table and its header
        self.dataTable.setStyleSheet(""
            "QTableWidget {"
            "    background-color: rgb(0, 0, 74);"
            "    color: rgb(230, 230, 230);"
            "    gridline-color: rgb(230, 230, 230);"
            "}"
            "QHeaderView::section {"
            "    background-color: rgb(0, 0, 74);"
            "    color: rgb(230, 230, 230);"
            "    font-size: 25px;"
            "    font-weight: bold;"
            "    border: 1px solid white;"
            "}"
        "")

        header = self.dataTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setDefaultAlignment(Qt.AlignCenter)

        vertical_header = self.dataTable.verticalHeader()
        vertical_header.setSectionResizeMode(QHeaderView.Stretch)

        self.tableLayout.addWidget(self.dataTable)

        # Adding 5 rows with default data
        for i in range(5):
            self.dataTable.insertRow(i)
            item1 = QTableWidgetItem(f"")
            item1.setTextAlignment(Qt.AlignCenter)
            self.dataTable.setItem(i, 0, item1)

            item2 = QTableWidgetItem(f"")
            item2.setTextAlignment(Qt.AlignCenter)
            self.dataTable.setItem(i, 1, item2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.retranslateUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
