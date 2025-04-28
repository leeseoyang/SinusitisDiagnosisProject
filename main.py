import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from ui import Ui_mainWindow  # UI 클래스 가져오기

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("부비부비동")
        self.resize(1000, 800)

        self.model = load_model("best_model.h5", compile=False)  # 모델 로드

        self.image_path = None
        self.ui.uploadButton.clicked.connect(self.upload_image)
        self.ui.judgeButton.clicked.connect(self.predict_image)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "X-ray 이미지 선택", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path).scaled(
                self.ui.imagePreview.width(), self.ui.imagePreview.height(),
                QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.ui.imagePreview.setPixmap(pixmap)
            self.ui.logBox.append(f"✅ 이미지 업로드 완료: {file_path}")

    def predict_image(self):
        if not self.image_path:
            QMessageBox.warning(self, "오류", "먼저 이미지를 업로드 하세요.")
            return

        try:
            image = Image.open(self.image_path).convert("RGB")
            image = image.resize((60, 60))  # 모델 입력 사이즈에 맞춤
            image = np.array(image) / 255.0
            image = np.expand_dims(image, axis=0)

            prediction = self.model.predict(image)
            class_idx = np.argmax(prediction)
            prob = float(np.max(prediction))
            class_label = self.get_class_label(class_idx)

            self.ui.resultLabel.setText(f"예측 결과: {class_label} ({prob*100:.2f}%)")
            self.ui.logBox.append(f"🔍 예측 클래스: {class_label} | 확률: {prob:.4f}")
            self.ui.progressBar.setValue(int(prob * 100))  # 퍼센트 표시

        except Exception as e:
            self.ui.resultLabel.setText("❌ 예측 실패")
            self.ui.logBox.append(f"에러: {str(e)}")
            self.ui.progressBar.setValue(0)

    def get_class_label(self, idx):
        classes = {
            0: "정상",
            1: "좌측 부비동",
            2: "우측 부비동",
            3: "양측"
        }
        return classes.get(idx, f"알 수 없음 ({idx})")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
