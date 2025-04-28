from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1000, 800)

        font = QtGui.QFont()
        font.setFamily("맑은 고딕")  # 글꼴 통일
        font.setPointSize(12)
        font.setBold(True)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet("""
            QWidget {
                background-color: #f0faff;
                font-family: '맑은 고딕';
                font-size: 12pt;
                font-weight: bold;
            }
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1a252f;
            }
            QLabel#resultLabel {
                background-color: white;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
            }
            QTextEdit#logBox {
                background-color: #e8f4f8;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
            }
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                width: 20px;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # 상단 제목
        self.titleLabel = QtWidgets.QLabel("부비동염(X-ray) 판별 시스템", self.centralwidget)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet("font-size: 24px; color: #2c3e50; font-weight: bold;")
        self.verticalLayout.addWidget(self.titleLabel)

        # 버튼 영역
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.uploadButton = QtWidgets.QPushButton("X-ray 이미지를 업로드 하세요", self.centralwidget)
        self.judgeButton = QtWidgets.QPushButton("이미지 판별하기", self.centralwidget)
        self.buttonLayout.addWidget(self.uploadButton)
        self.buttonLayout.addWidget(self.judgeButton)
        self.verticalLayout.addLayout(self.buttonLayout)

        # 이미지 출력
        self.imagePreview = QtWidgets.QLabel("이미지 출력화면", self.centralwidget)
        self.imagePreview.setAlignment(QtCore.Qt.AlignCenter)
        self.imagePreview.setMinimumHeight(400)
        self.imagePreview.setStyleSheet("background-color: white; border: 2px solid gray;")
        self.verticalLayout.addWidget(self.imagePreview)

        # 결과 출력
        self.resultLabel = QtWidgets.QLabel("결과 출력창", self.centralwidget)
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.resultLabel)

        # 로그 출력
        self.logBox = QtWidgets.QTextEdit(self.centralwidget)
        self.logBox.setPlaceholderText("처리 로그 출력창")
        self.logBox.setObjectName("logBox")
        self.verticalLayout.addWidget(self.logBox)

        # 퍼센트 진행 바
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setValue(0)
        self.verticalLayout.addWidget(self.progressBar)

        mainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
