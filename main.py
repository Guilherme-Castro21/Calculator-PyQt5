import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy)

class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(350, 500)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 35px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(
            QPushButton('+'), 1, 3, 1, 1,
            None,
            'background: #9F9F9F; color: #fff; font-weight: 700; font-size: 30px;')
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #EC3016; color: #fff; font-weight: 700; font-size: 30px;'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(
            QPushButton('-'), 2, 3, 1, 1,
            None,
            'background: #9F9F9F; color: #fff; font-weight: 700; font-size: 30px;')
        self.add_btn(
            QPushButton('←'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: #696969 ; color: #fff; font-weight: 700; font-size: 30px;'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(
            QPushButton('/'), 3, 3, 1, 1,
            None,
            'background: #9F9F9F; color: #fff; font-weight: 700; font-size: 30px;')
        self.add_btn(
            QPushButton('='), 3, 4, 2, 1,
            self.eval_equal,
            'background: #1432AD; color: #fff; font-weight: 700; font-size: 30px;'
        )

        self.add_btn(QPushButton('0'), 4, 0, 1, 1)
        self.add_btn(QPushButton('00'), 4, 1, 1, 1)
        self.add_btn(QPushButton('.'), 4, 2, 1, 1)
        self.add_btn(
            QPushButton('*'), 4, 3, 1, 1,
            None,
            'background: #9F9F9F; color: #fff; font-weight: 700; font-size: 30px;')

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, row_span, col_span, function=None, style=None):
        self.grid.addWidget(btn, row, col, row_span, col_span)

        if function is None:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(function)

        if style:
            btn.setStyleSheet(style)
        else:
            btn.setStyleSheet('font-size: 30px;')

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_equal(self):
        try:
            self.display.setText(
                f'{eval(self.display.text())}'
            )
        except Exception:
            self.display.setText('Invalid Calculation')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
