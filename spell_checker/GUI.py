import shutil
from PyQt5.QtWidgets import *
import sys
from dictionary import create_dictionary_for_main as create_dict
from dictionary import dictionary_compilation
from spell_checker import utils, spell_checker


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.dictionary = create_dict.create_dictionary()
        self.letter_dict = create_dict.letter_dictionary(self.dictionary)

        self.input_label = QLabel('Input')
        self.output_label = QLabel('Output')

        self.button_check = QPushButton('Check')
        self.button_check.clicked.connect(self.check)

        self.button_number = QPushButton('Mistakes limit')
        self.button_number.clicked.connect(self.set_limit)

        self.button_add = QPushButton('Add dictionary')
        self.button_add.clicked.connect(self.add_dictionary)

        self.output_text = QTextEdit()
        self.input_text = QTextEdit()
        self.input_text.setAcceptRichText(False)

        self.result_string, self.text = '', ''
        self.ac, self.pr = 0, 0
        self.limit = float('inf')

        self.add_dict, self.set_lim = None, None

        self.initUI()

    def initUI(self):
        self.setLayout(self.grid)
        self.grid.addWidget(self.input_label, 2, 0)
        self.grid.addWidget(self.output_label, 2, 3)

        self.grid.addWidget(self.button_number, 3, 2)
        self.grid.addWidget(self.button_check, 4, 2)
        self.grid.addWidget(self.button_add, 5, 2)

        self.grid.addWidget(self.input_text, 3, 0, 5, 2)
        self.grid.addWidget(self.output_text, 3, 3, 5, 2)

        self.move(300, 150)
        self.setWindowTitle('SpellChecker')

        self.show()

    def check(self):
        self.limit = \
            self.set_lim.get_number() if self.set_lim else float('inf')
        self.text = self.input_text.toPlainText()
        self.text = utils.make_correct_line(self.text)
        self.output_text.clear()
        self.result_string = ''

        if len(self.text) > self.limit:
            limit_text = self.text[0:self.limit + 1]
            for word in limit_text:
                self.result_string += spell_checker.spell_checker(
                    self.dictionary,
                    self.letter_dict,
                    word)
        else:
            for word in self.text:
                self.result_string += spell_checker.spell_checker(
                    self.dictionary,
                    self.letter_dict,
                    word)
        self.output_text.append(self.result_string)

    def add_dictionary(self):
        self.add_dict = AddDictionary(self)
        self.add_dict.show()

    def set_limit(self):
        self.set_lim = Limit(self)
        self.set_lim.show()


class AddDictionary(QMainWindow):
    def __init__(self, parent):
        super(AddDictionary, self).__init__(parent)

        self.textEdit = QLineEdit()
        self.text = QTextEdit()
        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        open_file = QAction('Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open new File')
        open_file.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(open_file)
        self.setWindowTitle('File dialog')
        self.show()

    def show_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Find file', '',
                                                'Text files (*.txt)')[0]
        try:
            shutil.copy(file_name, dictionary_compilation.LIBRARY)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

        self.selection_box()

    def selection_box(self):
        message = 'reload dictionary now?'
        reply = QMessageBox.question(self, 'Message', message,
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply:
            dictionary_compilation.main_dict()
        else:
            pass


class Limit(QMainWindow):
    def __init__(self, parent):
        super(Limit, self).__init__(parent)
        self.error_dialog = QErrorMessage()
        self.btn = QPushButton('Set number', self)
        self.le = QLineEdit(self)
        self.number = float('inf')
        self.initUI()

    def initUI(self):
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.set_number)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input number')
        self.show()

    def set_number(self):
        self.number = self.le.text()
        try:
            self.number = int(self.number)
            self.close()
        except:
            self.le.clear()
            self.error_dialog.showMessage('Enter the number')
            self.error_dialog.exec_()

    def get_number(self):
        return self.number


def main_gui():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_gui()
