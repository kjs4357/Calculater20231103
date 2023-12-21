import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QLabel, QLineEdit, QPushButton


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_equation_solution = QFormLayout()
        layout_buttons = QGridLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("Equation: ")
        label_solution = QLabel("Solution: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_equation, self.equation)
        layout_equation_solution.addRow(label_solution, self.solution)

        ### 숫자 및 연산자 버튼 생성하고, layout_buttons 레이아웃에 추가
        button_grid = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("/", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("*", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("-", 2, 3),
            ("0", 3, 0),
            ("00", 3, 1),
            (".", 3, 2),
            ("+", 3, 3),
            ("=", 4, 0, 1, 4)  # Merge the last button to span multiple columns
        ]

        for text, row, col, row_span, col_span in button_grid:
            button = QPushButton(text)
            layout_buttons.addWidget(button, row, col, row_span, col_span)
            button.clicked.connect(lambda state, text=text: self.button_clicked(text))

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)
        self.setWindowTitle("Calculator")
        self.show()

    #################
    ### functions ###
    #################
    def button_clicked(self, text):
        if text == "=":
            equation = self.equation.text()
            try:
                result = eval(equation)
                self.solution.setText(str(result))
            except Exception as e:
                self.solution.setText("Error")
        else:
            current_equation = self.equation.text()
            new_equation = current_equation + text
            self.equation.setText(new_equation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
