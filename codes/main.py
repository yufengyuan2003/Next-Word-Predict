import predict
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class StartWindow(QMainWindow):
    # 创建主窗口
    def __init__(self):
        super().__init__()


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Predictor")
        self.set_background_image("bg2.png")

        # 创建垂直布局
        main_layout = QVBoxLayout(central_widget)

        # introduction_label
        self.introduction_label = QLabel("<div style='font-size: 25pt; text-align: center;font-family: 黑体;font-weight: bold;'>欢迎使用“Context-aware Prediction System”!</div>", self)

        # 创建context_label
        context = """
           <div style='font-size: 20pt; text-align: center;font-family: 黑体;font-weight: bold;'>
               <p>使用说明：</p>
               <p>1. Shift用于切换中英文</p>
               <p>2. Ctrl键用于开启/关闭预测</p>
               <p>3. 如果预测处于开启状态，按键1，2，3，4将被用于选择预测内容，</p>
               <p>如需输入1，2，3，4请关闭预测后再输入</p>
            </div>
        """
        self.context_label = QLabel(context, self)
        self.context_label.setAlignment(Qt.AlignCenter)


        # 设置 context_label 的字体大小
        text_edit_font = QFont()
        text_edit_font.setPointSize(18)
        self.context_label.setFont(text_edit_font)

        # 设置 context_label 的固定大小
        self.context_label.setFixedSize(1000, 500)
        self.context_label.move(450 - self.context_label.width() / 2, 200)

        # 创建水平布局
        button_layout = QHBoxLayout()

        # 创建四个 QPushButton
        self.start_button = QPushButton("开始", self)

        # 设置按钮的大小
        button_size = (150, 50)
        self.start_button.setFixedSize(*button_size)

        # 设置 QPushButton 的字体大小
        button_font = QFont()
        button_font.setPointSize(12)
        self.start_button.setFont(button_font)

        # 将 QLabel、QTextEdit 和 水平布局 放置在垂直布局中
        main_layout.addWidget(self.introduction_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        main_layout.addWidget(self.context_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.start_button,alignment=Qt.AlignCenter)


        self.main_window = predict.MyMainWindow()
        # 创建按键事件
        self.start_button.clicked.connect(self.show_main_window)
    
    def set_background_image(self, image_path):
        # 创建一个 QPalette 对象
        palette = QPalette()

        # 使用 QPixmap 加载背景图片
        background_pixmap = QPixmap(image_path)

        # 将背景图片填充到 QPalette
        palette.setBrush(QPalette.Window, background_pixmap)

        # 设置 QPalette 到窗口
        self.setPalette(palette)

    def show_main_window(self):
        # 关闭开始界面窗口

        # 创建并显示主窗口
        self.main_window.show()
        self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            print("1")


if __name__ == "__main__":
    app = QApplication([])

    # 创建并显示开始界面窗口
    start_window = StartWindow()
    start_window.show()

    # 进入主循环
    app.exec()
