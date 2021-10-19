from random import choice

from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Family(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Family.ui', None)
        self.ui.show()

        self.program = [self.ui.line_1, self.ui.line_2, self.ui.line_3, self.ui.line_4, self.ui.line_5, self.ui.line_6, self.ui.line_7, self.ui.line_8]
        self.ui.push_btn.clicked.connect(self.makeIt)

        self.boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
        self.girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
        self.family = []
    
    def makeIt(self):
        try:
            self.family.clear()
            while len(self.family) != (len(self.boys) + len(self.girls)) // 2:
                my_list = []
                boy_choice = choice(self.boys)
                girl_choice = choice(self.girls)
                
                flag = True
                for i in range(len(self.family)):
                    if self.family[i][0] == boy_choice or self.family[i][1] == girl_choice:
                        flag = False
                        break
                    
                if flag:
                    my_list.append(boy_choice)
                    my_list.append(girl_choice)
                    self.family.append(my_list)
            
            for i in range(8):
                text = self.family[i][0] + '💘' + self.family[i][1]
                self.program[i].setText(text)
            
            print(self.family)
        
        except:
            print('Error!')
            pass

app = QApplication([])
window = Family()
app.exec()