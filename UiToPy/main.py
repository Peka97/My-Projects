import sys, os

from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog, QMessageBox
from desigh import Ui_MainWindow


class Converter(QMainWindow):
    def __init__(self):
        super(Converter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path_file_in = None

        # menubar
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        # menu
        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)
        fileMenu.addAction("Открыть", self.open_file)
        fileMenu.addSeparator()
        fileMenu.addAction("Выход", sys.exit)

        # buttons
        self.ui.btn.clicked.connect(self.convert_file)

    def convert_file(self) -> None:
        """Функция выполняет конвертацию файлов. Тип файла определяет самостоятельно, на выход предлагает диагологое
        окно для указания пути сохранения"""

        if self.path_file_in is None:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Выберите файл в верхнем меню, а затем нажмите \"Конвертировать\"")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec()
        else:
            fname = QFileDialog.getSaveFileName(self)[0]
            if str(self.path_file_in).endswith('.qrc'):
                os.system(f'pyside6-rcc {self.path_file_in} -o {fname + ".py"}')
                error = QMessageBox()
                error.setWindowTitle("Информация")
                error.setText("Успешно!")
                error.setIcon(QMessageBox.Information)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec()
            elif str(self.path_file_in).endswith('.ui'):
                os.system(f'pyside6-uic {self.path_file_in} -o {fname + ".py"}')
                error = QMessageBox()
                error.setWindowTitle("Информация")
                error.setText("Успешно!")
                error.setIcon(QMessageBox.Information)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec()
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Выбран не корректный файл.\nУбедитесь в том, что файл имеет расширение .ui или .qrc")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec()

    def open_file(self) -> None:
        """Функция открытия файла в MenuBar"""

        fname = QFileDialog.getOpenFileName(self)[0]
        self.path_file_in = fname


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Converter()
    window.show()

    sys.exit(app.exec())
