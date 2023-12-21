import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # 통합된 LineEdit 위젯 생성
        self.display = QLineEdit("")

        # 통합된 LineEdit 레이아웃 설정
        layout_display = QFormLayout()
        layout_display.addRow("Display:", self.display)

        # 사칙연산 버튼 레이아웃
        layout_operation = QHBoxLayout()
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("*")
        button_division = QPushButton("/")
        button_plus.clicked.connect(lambda: self.button_operation_clicked("+"))
        button_minus.clicked.connect(lambda: self.button_operation_clicked("-"))
        button_product.clicked.connect(lambda: self.button_operation_clicked("*"))
        button_division.clicked.connect(lambda: self.button_operation_clicked("/"))
        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)

        # =, Clear, Backspace 버튼 레이아웃
        layout_clear_equal = QHBoxLayout()
        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        # 숫자 버튼 레이아웃
        layout_number = QGridLayout()
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number: self.number_button_clicked(num))
            if number > 0:
                x, y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        # 소숫점과 00 버튼
        button_dot = QPushButton(".")
        button_double_zero = QPushButton("00")
        button_dot.clicked.connect(lambda: self.number_button_clicked("."))
        button_double_zero.clicked.connect(lambda: self.number_button_clicked("00"))
        layout_number.addWidget(button_dot, 3, 2)
        layout_number.addWidget(button_double_zero, 3, 0)

        # 최종 레이아웃 설정
        main_layout.addLayout(layout_display)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        current_text = self.display.text()
        self.display.setText(current_text + str(num))

    def button_operation_clicked(self, operation):
        current_text = self.display.text()
        self.display.setText(current_text + operation)

    def button_equal_clicked(self):
        try:
            current_text = self.display.text()
            result = eval(current_text)
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")

    def button_clear_clicked(self):
        self.display.setText("")

    def button_backspace_clicked(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
