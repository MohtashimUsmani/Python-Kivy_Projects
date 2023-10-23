from kivy.app import App
from kivy.lang import Builder


class Tictactoe(App):
    def build(self):
        return Builder.load_file('thelab.kv')

    turn = 'X'
    winner = False

    def end_game(self, btn1, btn2, btn3):
        self.winner = True
        btn1.color = 'green'
        btn2.color = 'green'
        btn3.color = 'green'
        self.disable_all_button()
        self.root.ids.score.text = f'{btn1.text} Wins!'

    def draw(self):
        if self.winner is False and \
                self.root.ids.btn1.disabled is True and \
                self.root.ids.btn2.disabled is True and \
                self.root.ids.btn3.disabled is True and \
                self.root.ids.btn4.disabled is True and \
                self.root.ids.btn5.disabled is True and \
                self.root.ids.btn6.disabled is True and \
                self.root.ids.btn7.disabled is True and \
                self.root.ids.btn8.disabled is True and \
                self.root.ids.btn9.disabled is True:
            self.root.ids.score.text = 'Draw'
            self.root.ids.btn1.color = 'red'
            self.root.ids.btn2.color = 'red'
            self.root.ids.btn3.color = 'red'
            self.root.ids.btn4.color = 'red'
            self.root.ids.btn5.color = 'red'
            self.root.ids.btn6.color = 'red'
            self.root.ids.btn7.color = 'red'
            self.root.ids.btn8.color = 'red'
            self.root.ids.btn9.color = 'red'

    def disable_all_button(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def win(self):
        if (self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.
                text == self.root.ids.btn3.text):
            self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

        if (self.root.ids.btn4.text != '' and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.
                text == self.root.ids.btn6.text):
            self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

        if (self.root.ids.btn7.text != '' and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.
                text == self.root.ids.btn9.text):
            self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

            # up Down
        if (self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.
                text == self.root.ids.btn7.text):
            self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

        if (self.root.ids.btn2.text != '' and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.
                text == self.root.ids.btn8.text):
            self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

        if (self.root.ids.btn3.text != '' and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.
                text == self.root.ids.btn9.text):
            self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

            # Diagonal
        if (self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.
                text == self.root.ids.btn9.text):
            self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        if (self.root.ids.btn3.text != '' and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.
                text == self.root.ids.btn7.text):
            self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

        self.draw()

    def presser(self, btn):
        if self.turn == 'X':
            btn.text = 'X'
            btn.disabled = True
            self.root.ids.score.text = 'O\'s Turn'
            self.turn = 'O'
        else:
            btn.text = 'O'
            btn.disabled = True
            self.root.ids.score.text = 'X\'s Turn'
            self.turn = 'X'

        self.win()

    def restart(self):
        self.turn = 'X'
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn2.text = ''
        self.root.ids.btn3.text = ''
        self.root.ids.btn4.text = ''
        self.root.ids.btn5.text = ''
        self.root.ids.btn6.text = ''
        self.root.ids.btn7.text = ''
        self.root.ids.btn8.text = ''
        self.root.ids.btn9.text = ''
        self.root.ids.btn1.text = ''

        self.root.ids.btn2.color = 'red'
        self.root.ids.btn3.color = 'red'
        self.root.ids.btn4.color = 'red'
        self.root.ids.btn5.color = 'red'
        self.root.ids.btn6.color = 'red'
        self.root.ids.btn7.color = 'red'
        self.root.ids.btn8.color = 'red'
        self.root.ids.btn9.color = 'red'
        self.root.ids.btn1.color = 'red'

        self.root.ids.score.text = 'X\'s Turn'


Tictactoe().run()
