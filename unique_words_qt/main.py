import sys
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QPushButton, QApplication, QTextEdit, QGridLayout)


class MainApplication(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Get unique words", self)
        btn.clicked.connect(self.buttonClicked)

        self.full_text = QTextEdit()
        self.unique_text = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.full_text, 1, 1)
        grid.addWidget(self.unique_text, 1, 2)
        grid.addWidget(btn, 2, 2)
        self.setLayout(grid)

        self.resize(500, 500)
        self.center()
        self.setWindowTitle("Unique words")

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonClicked(self):
        text = self.full_text.toPlainText()
        text_list = str(text).lower().split()
        text = sorted(set(text_list))
        self.unique_text.setText('\n'.join(text))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainApplication()
    sys.exit(app.exec_())