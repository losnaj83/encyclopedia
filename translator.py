from PyQt5.QtWidgets import *
import difflib
import sys
import json


data = json.load(open('data/data.json'))

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Translator')
        self.setGeometry(50,50,350,350)
        self.UI()


    def UI(self):


        self.inputBox=QLineEdit(self)
        self.inputBox.setPlaceholderText('Index word')
        self.inputBox.move(50, 50)

        translateButton = QPushButton("Translate", self)
        translateButton.move(200,50)
        translateButton.clicked.connect(self.translator)

        findButton = QPushButton('Find',self)
        findButton.move(210, 135)
        findButton.clicked.connect(self.find)

        self.combo = QComboBox(self)
        self.combo.move(110, 135)

        self.resultLabel = QLabel(self)
        self.resultLabel.setStyleSheet("background-color:#c0c0c0;border: 3px solid gray")
        self.resultLabel.setGeometry(20, 180, 300, 150)
        self.resultLabel.setWordWrap(True)
        self.show()

    def find(self):
        name = self.combo.currentText()
        output = data[name.lower()]
        outputstr = str()
        for n in output:
            outputstr = outputstr + n + '\n'
        self.resultLabel.setText(f'{outputstr}')

    def translator(self):
        name = self.inputBox.text().lower()


        def ifvalid(self, arg):
            try:
                return data[arg.lower()]
            except KeyError:
                return None

        output = ifvalid(self, name)

        if ifvalid(self, name) is not None:
            self.combo.clear()
            outputStr = str()
            for n in output:
                outputStr = outputStr + n + '\n'

            self.resultLabel.setText(f'{outputStr}')


        else:
            closeMatch = difflib.get_close_matches(name, data)
            self.combo.clear()
            self.combo.addItems(closeMatch)
            self.resultLabel.setText(f'Couldnt find the word you are looking for\n'
                                     f'Did you mean any of the words in the menu above?\n')

            # output =str(output).replace("']", '').replace("['", ''.replace("','", ''))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':  main()