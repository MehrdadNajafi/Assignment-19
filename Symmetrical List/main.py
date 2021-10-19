from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Symmetry(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.ui.check_btn.clicked.connect(self.check_list)

    def check_list(self):
        try:
            numbers = str(self.ui.textbox_1.text())
            num_list = numbers.split(',')
            for i in range(len(num_list)):
                num_list[i] = float(num_list[i])
            
            mid_index = len(num_list) // 2

            if len(num_list) % 2 != 0 :
                first_list = num_list[0 : mid_index]
                second_list = num_list[(mid_index + 1) :]

            elif len(num_list) % 2 == 0 :
                first_list = num_list[0 : mid_index]
                second_list = num_list[mid_index :]

            second_list.reverse()

            if first_list == second_list:
                self.ui.textbox_2.setText('Yes')
            else:
                self.ui.textbox_2.setText('No')
        
        except:
            print('Error!')
            pass

app = QApplication([])
window = Symmetry()
app.exec()