import Chinese_process
import English

import re

from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTextEdit, QHBoxLayout, \
    QPushButton
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtCore import Qt, QEvent, QTimer
from PySide6.QtGui import QFont


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主窗口
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        # self.setGeometry(0, 0, 900, 500)
        self.setWindowTitle("Predictor")
        self.set_background_image("bg3.png")

        # 创建垂直布局
        main_layout = QVBoxLayout(central_widget)

        # 创建水平布局
        label_layout = QHBoxLayout()

        # 创建 QLabel
        self.language_label = QLabel(
            "<div style='font-size: 25pt; text-align: center; font-family: Arial;font-weight: bold;'>中文模式</div>",
            self)
        self.language_label.setAlignment(Qt.AlignCenter)
        self.language_label.setFixedSize(250, 100)

        # 创建 QLabel
        self.mode_label = QLabel(
            "<div style='font-size: 25pt; text-align: center; font-family: Arial;font-weight: bold;'>预测关闭</div>",
            self)
        self.mode_label.setAlignment(Qt.AlignCenter)
        self.mode_label.setFixedSize(250, 100)

        label_layout.addWidget(self.language_label)
        label_layout.addWidget(self.mode_label)

        # 创建 QTextEdit
        self.text_edit = QTextEdit(self)

        # 设置 QTextEdit 的字体大小
        text_edit_font = QFont()
        text_edit_font.setPointSize(16)
        self.text_edit.setFont(text_edit_font)

        # 设置 QTextEdit 的固定大小为 1000x500
        self.text_edit.setFixedSize(800, 400)
        self.text_edit.move(700 - self.text_edit.width() / 2, 200)

        # 创建水平布局
        button_layout = QHBoxLayout()

        button_style = "QPushButton { background-color: grey; color: white; border: 2px solid #4CAF50; border-radius: 8px; font-size: 18px; }"
        self.button1 = QPushButton("1", self)
        self.button1.setStyleSheet(button_style)

        self.button2 = QPushButton("2", self)
        self.button2.setStyleSheet(button_style)

        self.button3 = QPushButton("3", self)
        self.button3.setStyleSheet(button_style)

        self.button4 = QPushButton("4", self)
        self.button4.setStyleSheet(button_style)

        # 创建两个额外的按钮
        extra_button_style = "QPushButton { background-color: grey; color: white; border: 2px solid #4285f4; border-radius: 8px; font-size: 18px; }"
        self.button_before = QPushButton("<-", self)
        self.button_before.setStyleSheet(extra_button_style)

        self.button_next = QPushButton("->", self)
        self.button_next.setStyleSheet(extra_button_style)

        # 设置按钮的大小
        button_size = (150, 50)
        self.button1.setFixedSize(*button_size)
        self.button2.setFixedSize(*button_size)
        self.button3.setFixedSize(*button_size)
        self.button4.setFixedSize(*button_size)
        self.button_before.setFixedSize(*button_size)
        self.button_next.setFixedSize(*button_size)

        # 设置 QPushButton 的字体大小
        button_font = QFont()
        button_font.setPointSize(12)
        self.button1.setFont(button_font)
        self.button2.setFont(button_font)
        self.button3.setFont(button_font)
        self.button4.setFont(button_font)
        button_font.setPointSize(16)
        self.button_before.setFont(button_font)
        self.button_next.setFont(button_font)

        # 将 QPushButton 放置在水平布局中
        button_layout.addWidget(self.button_before)
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.button4)
        button_layout.addWidget(self.button_next)

        # 将 QLabel、QTextEdit 和 水平布局 放置在垂直布局中
        main_layout.addLayout(label_layout)
        main_layout.addWidget(self.text_edit, alignment=Qt.AlignCenter)
        main_layout.addLayout(button_layout)

        # 初始化
        self.current_language = "ch"
        self.current_input = ''
        self.left_current_input = ''
        self.right_current_input = ''
        self.input_used_to_suggest = ''
        self.last_suggestion = []
        self.start_pos = 0
        self.previous_cursor_pos = 0
        self.shift_pressed_lens = 0
        self.suggest_enable = 0
        self.cursor_pos = 0

        # 创建定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_input)
        self.timer.start(20)  # 每隔0.02秒更新一次

        # 创建按键事件
        self.button1.clicked.connect(self.on_button1_click)
        self.button2.clicked.connect(self.on_button2_click)
        self.button3.clicked.connect(self.on_button3_click)
        self.button4.clicked.connect(self.on_button4_click)
        self.button_before.clicked.connect(self.on_button_before_click)
        self.button_next.clicked.connect(self.on_button_next_click)

    def on_button_click_blink(self, sender):
        # 创建按钮闪烁效果
        animation = QPropertyAnimation(sender, b"styleSheet", self)
        animation.setDuration(20)  # 设置动画持续时间（毫秒）

        # 切换按钮样式表，实现闪烁效果
        animation.setStartValue(sender.styleSheet())
        animation.setEndValue("background-color: yellow;")

        # 在动画完成时，恢复按钮原始样式
        animation.finished.connect(lambda: sender.setStyleSheet(sender.styleSheet()))

        # 启动动画
        animation.start()

    def set_background_image(self, image_path):
        # 创建一个 QPalette 对象
        palette = QPalette()

        # 使用 QPixmap 加载背景图片
        background_pixmap = QPixmap(image_path)

        # 将背景图片填充到 QPalette
        palette.setBrush(QPalette.Window, background_pixmap)

        # 设置 QPalette 到窗口
        self.setPalette(palette)

    def keyPressEvent(self, event):
        # 检测Shift键是否被按下
        if event.key() == Qt.Key_Shift:
            self.shift_pressed_lens = len(self.text_edit.toPlainText())
        # 检测Ctrl键是否被按下
        if event.modifiers() & Qt.ControlModifier:
            self.suggest_on_off()

    def keyReleaseEvent(self, event):
        # 检测同时按下 Shift 和其他键
        if event.key() == Qt.Key_Shift:
            if len(self.text_edit.toPlainText()) == self.shift_pressed_lens:
                self.switch_language()
        # 判断按键
        elif self.button1.isEnabled() and event.key() == Qt.Key_1:
            self.input_used_to_suggest = self.input_used_to_suggest[:-1]
            self.left_current_input = self.left_current_input[:-1]
            self.text_edit.setText(self.left_current_input + self.right_current_input)
            self.cursor_pos = self.cursor_pos - 1
            self.on_button1_click()
        elif self.button2.isEnabled() and event.key() == Qt.Key_2:
            self.input_used_to_suggest = self.input_used_to_suggest[:-1]
            self.left_current_input = self.left_current_input[:-1]
            self.text_edit.setText(self.left_current_input + self.right_current_input)
            self.cursor_pos = self.cursor_pos - 1
            self.on_button2_click()
        elif self.button3.isEnabled() and event.key() == Qt.Key_3:
            self.input_used_to_suggest = self.input_used_to_suggest[:-1]
            self.left_current_input = self.left_current_input[:-1]
            self.text_edit.setText(self.left_current_input + self.right_current_input)
            self.cursor_pos = self.cursor_pos - 1
            self.on_button3_click()
        elif self.button4.isEnabled() and event.key() == Qt.Key_4:
            self.input_used_to_suggest = self.input_used_to_suggest[:-1]
            self.left_current_input = self.left_current_input[:-1]
            self.text_edit.setText(self.left_current_input + self.right_current_input)
            self.cursor_pos = self.cursor_pos - 1
            self.on_button4_click()

    def switch_language(self):
        if self.current_language == "en":
            new_language_text = "中文模式"
            self.current_language = "ch"
        else:
            new_language_text = "English Mode"
            self.current_language = "en"

        # 设置字体为 Arial，字体大小为 25，粗体
        font = QFont("Arial", 25)
        font.setBold(True)

        # 直接设置 mode 标签的文本属性和字体
        self.language_label.setText(new_language_text)
        self.language_label.setFont(font)

    # 设置按键颜色
    def set_button_state(self):
        enabled_button_style = "QPushButton { background-color: green; color: white; border: 2px solid #4CAF50; border-radius: 8px; font-size: 18px; }"
        disabled_button_style = "QPushButton { background-color: grey; color: grey; border: 2px solid #A9A9A9; border-radius: 8px; font-size: 18px; }"
        # 根据 enable 参数设置按钮的状态和样式
        buttons = [self.button1, self.button2, self.button3, self.button4, self.button_before, self.button_next]

        for button in buttons:
            button.setStyleSheet(enabled_button_style if button.isEnabled() else disabled_button_style)

    # 预测开/关
    def suggest_on_off(self):
        if self.suggest_enable == 0:
            self.suggest_enable = 1
            new_mode_text = "预测开启"
            if len(self.input_used_to_suggest) != 0:
                self.text_suggest()
        else:
            self.suggest_enable = 0
            new_mode_text = "预测关闭"
            self.button4.setText("")
            self.button3.setText("")
            self.button2.setText("")
            self.button1.setText("")
            self.button1.setEnabled(False)
            self.button2.setEnabled(False)
            self.button3.setEnabled(False)
            self.button4.setEnabled(False)
            self.button_next.setEnabled(False)
            self.button_before.setEnabled(False)
        self.set_button_state()

        # 设置字体为 Arial，字体大小为 25，粗体
        font = QFont("Arial", 25)
        font.setBold(True)

        # 直接设置 mode 标签的文本属性和字体
        self.mode_label.setText(new_mode_text)
        self.mode_label.setFont(font)

    # 写入文件
    def write_to_file(self):
        if self.current_language == "ch":
            self.write_to_Chinesefile(self.input_used_to_suggest)
        else:
            self.write_to_Englishfile(self.input_used_to_suggest)

    def write_to_Englishfile(self, text):
        file_path = "English_input.txt"
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text + '\n')

    def write_to_Chinesefile(self, text):
        file_path = "Chinese_input.txt"
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text + '\n')

    # 获取光标位置
    def get_cursor_position(self):
        cursor = self.text_edit.textCursor()
        self.cursor_pos = cursor.position()

    # 设置光标位置
    def set_cursor_position(self, lens):
        # 设置光标位置
        cursor = self.text_edit.textCursor()
        cursor.setPosition(self.cursor_pos + lens)
        self.text_edit.setTextCursor(cursor)

        # 将焦点设置回文本编辑框
        self.text_edit.setFocus()

    # 读取光标前所需文本
    def get_input_used_to_suggest(self):
        if self.current_language == 'ch':
            start = self.cursor_pos - 1
            my_re = re.compile(r'[A-Za-z,."?!]', re.S)
            while start >= 0:
                res = re.findall(my_re, self.current_input[start])
                if len(res):
                    break
                start -= 1
        else:
            start = self.cursor_pos - 1
            my_re = re.compile(r'[\u4e00-\u9fa5，。！？、；：“”‘’（）【】]', re.S)
            while start >= 0:
                res = re.findall(my_re, self.current_input[start])
                if len(res):
                    break
                start -= 1
        return self.current_input[start + 1:self.cursor_pos]

    # 获取文本框内容
    def get_input(self):
        self.get_cursor_position()
        # 实时读取 Text 的内容
        self.current_input = self.text_edit.toPlainText()
        self.left_current_input = self.current_input[:self.cursor_pos]
        self.right_current_input = self.current_input[self.cursor_pos:]

        # 获取用于预测的文本
        self.input_used_to_suggest = self.get_input_used_to_suggest()

        if len(self.input_used_to_suggest) == 0:
            self.button4.setText("")
            self.button3.setText("")
            self.button2.setText("")
            self.button1.setText("")
            self.button1.setEnabled(False)
            self.button2.setEnabled(False)
            self.button3.setEnabled(False)
            self.button4.setEnabled(False)
            self.button_next.setEnabled(False)
            self.button_before.setEnabled(False)
        elif self.suggest_enable == 1:
            if self.previous_cursor_pos != self.cursor_pos:
                self.start_pos = 0
                self.previous_cursor_pos = self.cursor_pos
            if self.input_used_to_suggest[-1] != "1" and self.input_used_to_suggest[-1] != "2" and \
                    self.input_used_to_suggest[-1] != "3" and self.input_used_to_suggest[-1] != "4":
                self.text_suggest()
        self.set_button_state()

    def set_buttom_text(self):
        if len(self.last_suggestion) > 0:
            if self.start_pos + 3 < len(self.last_suggestion):
                self.button4.setEnabled(True)
                self.button4.setText("4." + self.last_suggestion[self.start_pos + 3])
            else:
                self.button4.setText("")
                self.button4.setEnabled(False)

            if self.start_pos + 2 < len(self.last_suggestion):
                self.button3.setEnabled(True)
                self.button3.setText("3." + self.last_suggestion[self.start_pos + 2])
            else:
                self.button3.setText("")
                self.button3.setEnabled(False)

            if self.start_pos + 1 < len(self.last_suggestion):
                self.button2.setEnabled(True)
                self.button2.setText("2." + self.last_suggestion[self.start_pos + 1])
            else:
                self.button2.setText("")
                self.button2.setEnabled(False)

            if self.start_pos < len(self.last_suggestion):
                self.button1.setEnabled(True)
                self.button1.setText("1." + self.last_suggestion[self.start_pos])
            else:
                self.button1.setText("")
                self.button1.setEnabled(False)

            if self.start_pos + 4 >= len(self.last_suggestion):
                self.button_next.setText("")
                self.button_next.setEnabled(False)
            else:
                self.button_next.setText("->")
                self.button_next.setEnabled(True)
            if self.start_pos < 4:
                self.button_before.setText("")
                self.button_before.setEnabled(False)
            else:
                self.button_before.setText("<-")
                self.button_before.setEnabled(True)
        else:
            self.button4.setText("")
            self.button3.setText("")
            self.button2.setText("")
            self.button1.setText("")
            self.button4.setEnabled(False)
            self.button3.setEnabled(False)
            self.button2.setEnabled(False)
            self.button1.setEnabled(False)
            self.button_next.setEnabled(False)
            self.button_before.setEnabled(False)

    # 文本预测
    def text_suggest(self):
        if self.current_language == "ch":
            cut_input = list(self.input_used_to_suggest)
            last_five_words = "".join(cut_input[-5:])
            self.last_suggestion = Chinese_process.next_word(last_five_words, 16)
            self.set_buttom_text()
        else:
            cut_input = self.input_used_to_suggest.lower().rstrip().split()
            if len(cut_input) <= 1:
                self.last_suggestion = English.next_words(cut_input[0])
            else:
                self.last_suggestion = English.next_words((cut_input[-2], cut_input[-1]))
            self.set_buttom_text()

        self.set_button_state()

    # 设置文本框内容
    def set_text_edit_text(self, last_suggestion, start_pos):
        if self.current_language == 'ch':
            self.text_edit.setText(self.left_current_input + last_suggestion + self.right_current_input)
            self.input_used_to_suggest = self.input_used_to_suggest + last_suggestion
            lens = len(self.last_suggestion[start_pos])
        else:
            if self.last_suggestion[start_pos] not in ['.', ',', '!', '?']:
                self.text_edit.setText(self.left_current_input + ' ' + last_suggestion + self.right_current_input)
                self.input_used_to_suggest = self.input_used_to_suggest + ' ' + last_suggestion
            else:
                self.text_edit.setText(self.left_current_input + last_suggestion + ' ' + self.right_current_input)
                self.input_used_to_suggest = self.input_used_to_suggest + last_suggestion + ' '
            lens = len(self.last_suggestion[start_pos]) + 1
        return lens

    def on_button1_click(self):
        lens = self.set_text_edit_text(self.last_suggestion[self.start_pos], self.start_pos)

        self.start_pos = 0

        self.set_cursor_position(lens)

        self.set_button_state()
        self.on_button_click_blink(self.button1)

        self.write_to_file()

    def on_button2_click(self):
        lens = self.set_text_edit_text(self.last_suggestion[self.start_pos + 1], self.start_pos + 1)

        self.start_pos = 0

        self.set_cursor_position(lens)

        self.set_button_state()
        self.on_button_click_blink(self.button2)

        self.write_to_file()

    def on_button3_click(self):
        lens = self.set_text_edit_text(self.last_suggestion[self.start_pos + 2], self.start_pos + 2)

        self.start_pos = 0

        self.set_cursor_position(lens)

        self.set_button_state()
        self.on_button_click_blink(self.button3)

        self.write_to_file()

    def on_button4_click(self):
        lens = self.set_text_edit_text(self.last_suggestion[self.start_pos + 3], self.start_pos + 3)

        self.start_pos = 0

        self.set_cursor_position(lens)

        self.set_button_state()
        self.on_button_click_blink(self.button4)

        self.write_to_file()

    def on_button_before_click(self):
        self.button_next.setText("->")
        if self.start_pos >= 4:
            self.start_pos -= 4
            self.button_before.setText("<-")
            self.button_next.setText("->")
            self.button_next.setEnabled(True)
        else:
            self.start_pos = 0
            self.button_before.setEnabled(False)
            self.button_before.setText("")
            self.button_next.setText("->")

        self.set_buttom_text()
        self.set_button_state()
        self.on_button_click_blink(self.button_before)

    def on_button_next_click(self):
        if self.start_pos + 4 < len(self.last_suggestion):
            self.start_pos += 4
            self.button_before.setText("<-")
            self.button_next.setText("->")
            self.button_before.setEnabled(True)
        else:
            self.start_pos = len(self.last_suggestion) - 4
            self.button_next.setEnabled(False)
            self.button_before.setText("<-")
            self.button_next.setText("")

        self.set_buttom_text()
        self.set_button_state()
        self.on_button_click_blink(self.button_next)
