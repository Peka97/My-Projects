import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from desigh import Ui_MainWindow
from generate_panel import Generator


class Fallout(QMainWindow, Generator):
    def __init__(self):
        super(Fallout, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.text_attempts.setText(f"4 ATTEMPT(S) LEFT: {'█ █ █ █ '}")
        self.ui.text_code.setText(Generator.generate_panel(self))
        self.attempts = 4
        self.coincidences = 0

        QFontDatabase.addApplicationFont("font.ttf")

        self.ui.btn_enter.clicked.connect(lambda: self.game(self.ui.text_word.toPlainText()))

    def game(self, user_enter):
        print(self.secret)
        self.coincidences = 0
        if user_enter == self.secret:
            self.ui.text_attempts.setText(
                f"{self.attempts} ATTEMPT(S) LEFT: {'█ ' * self.attempts}{'  ' * (4 - self.attempts)}\t\t>{user_enter}: Exact match!")
        else:
            for letter_1, letter_2 in zip(user_enter, self.secret):
                if letter_1 == letter_2:
                    self.coincidences += 1
            self.attempts -= 1
            self.ui.text_attempts.setText(
                f"{self.attempts} ATTEMPT(S) LEFT: {'█ ' * self.attempts}{'  ' * (4 - self.attempts)}\t\t>{user_enter}: {self.coincidences} match. Try again")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Fallout()
    window.show()

    sys.exit(app.exec())

    # game = Fallout()
    # game.start()
