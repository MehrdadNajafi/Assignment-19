import random
from functools import partial

from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.ui.hand_btn1.clicked.connect(partial(self.check_Game, '🤚'))
        self.ui.hand_btn2.clicked.connect(partial(self.check_Game, '✋'))
        self.ui.newgame_btn.clicked.connect(self.newGame)
        self.ui.check_label.setText('Start the Game\nby choosing\n🤚 or ✋')
        self.rand = [0, 1]

        self.p1_score = 0
        self.p2_score = 0
        self.p3_score = 0

        self.count = 0

    def check_Game(self, choice = None):
        if self.count < 5:
            self.count += 1
            if choice == '🤚':
                self.ui.textbox_1.setText(choice)
            elif choice == '✋':
                self.ui.textbox_1.setText(choice)
            
            rand = random.choice(self.rand)
            if rand == 0:
                self.ui.textbox_2.setText('🤚')
            elif rand == 1:
                self.ui.textbox_2.setText('✋')
            
            rand = random.choice(self.rand)
            if rand == 0:
                self.ui.textbox_3.setText('🤚')
            elif rand == 1:
                self.ui.textbox_3.setText('✋')

            p1 = self.ui.textbox_1.text()
            p2 = self.ui.textbox_2.text()
            p3 = self.ui.textbox_3.text()

            if p1 == p2 == p3:
                self.ui.check_label.setText(f'Round {self.count}\nDraw')
            elif p1 == p2 :
                self.ui.check_label.setText(f'Round {self.count}\nPlayer 3 wins')
                self.p3_score += 1
                self.ui.player3_score.setText(f'Player 3 : {self.p3_score}')
            elif p1 == p3:
                self.ui.check_label.setText(f'Round {self.count}\nPlayer 2 wins')
                self.p2_score += 1
                self.ui.player2_score.setText(f'Player 2 : {self.p2_score}')
            elif p2 == p3:
                self.ui.check_label.setText(f'Round {self.count}\n Player 1 wins')
                self.p1_score += 1
                self.ui.player1_score.setText(f'Player 1 : {self.p1_score}')
        else:
            if self.p1_score == self.p2_score == self.p3_score:
                self.ui.check_label.setText('Draw\nPress new Game')
            elif self.p1_score == self.p2_score and self.p1_score > self.p3_score:
                winner = 'Player 1 and Player 2'
            elif self.p1_score == self.p3_score and self.p1_score > self.p2_score:
                winner = 'Player 1 and Player 3'
            elif self.p2_score == self.p3_score and self.p2_score > self.p1_score:
                winner = 'Player 2 and Player 3'
            else:
                winner_score = max(self.p1_score, self.p2_score, self.p3_score)
                if winner_score == self.p1_score:
                    winner = 'Player 1'
                elif winner_score == self.p2_score:
                    winner = 'Player 2'
                elif winner_score == self.p3_score:
                    winner = 'Player 3'
            self.ui.check_label.setText(f'{winner} wins the game\nPress New Game')

    def newGame(self):
        self.count = 0
        self.p1_score = 0
        self.p2_score = 0
        self.p3_score = 0
        self.ui.check_label.setText('Start the Game\nby choosing\n🤚 or ✋')
        self.ui.textbox_1.setText('')
        self.ui.textbox_2.setText('')
        self.ui.textbox_3.setText('')
        self.ui.player1_score.setText(f'Player 1 : {self.p1_score}')
        self.ui.player2_score.setText(f'Player 2 : {self.p1_score}')
        self.ui.player3_score.setText(f'Player 3 : {self.p1_score}')
        
app = QApplication([])
window = Game()
app.exec()