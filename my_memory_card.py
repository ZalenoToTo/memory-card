#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QApplication, QPushButton, QRadioButton,
    QLabel, QHBoxLayout, QVBoxLayout,QGroupBox,
    QButtonGroup
)
from random import shuffle, randint
app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle('Memory Card')
window.total = 0
window.score = 0
radioBox = QGroupBox("Варианты")
labelBox = QGroupBox()
grp_btn = QButtonGroup()

l = QLabel()
l2 = QLabel('Правильно/Неправильно')
l1 = QLabel('Правильно')
Layoutv22 = QVBoxLayout()

Layoutv22.addWidget(l2,alignment = Qt.AlignLeft)
Layoutv22.addWidget(l1,alignment = Qt.AlignCenter)
labelBox.setLayout(Layoutv22)
labelBox.hide()

q1 = QRadioButton()
q2 = QRadioButton()
q3 = QRadioButton()
q4 = QRadioButton()
answers=[q1,q2,q3,q4]

glav_button = QPushButton("Ответить")

hLayout_ans = QHBoxLayout()
vLayout_ans1 = QVBoxLayout()
vLayout_ans2 = QVBoxLayout()

vLayout_ans1.addWidget(q1,alignment = Qt.AlignCenter)
vLayout_ans1.addWidget(q2,alignment = Qt.AlignCenter )

vLayout_ans2.addWidget(q3,alignment = Qt.AlignCenter )
vLayout_ans2.addWidget(q4,alignment = Qt.AlignCenter )

hLayout_ans.addLayout(vLayout_ans1)
hLayout_ans.addLayout(vLayout_ans2)

grp_btn.addButton(q1)
grp_btn.addButton(q2)
grp_btn.addButton(q3)
grp_btn.addButton(q4)
radioBox.setLayout(hLayout_ans)
trueOrFalse = 0
class Question():
    def __init__(self,question,right,wrong1,wrong2,wrong3):
        self.question = question
        self.right = right
        self.wrong1= wrong1
        self.wrong2 =wrong2
        self.wrong3= wrong3
        
def click_ok():
    global questions_list
    if trueOrFalse%2 == 0:
        next_question(questions_list)
        return
        
    check_answer()


    

def check_answer():
    
    if answers[0].isChecked():
        l2.setText('Правильно')
        window.score +=1
    else:
        l2.setText('Неправильно')
    show_result()
    
def next_question(q):
    current_question = randint(0,len(q)-1)
    shuffle(answers)
    answers[0].setText(q[current_question].right)
    answers[1].setText(q[current_question].wrong1)
    answers[2].setText(q[current_question].wrong2)
    answers[3].setText(q[current_question].wrong3)
    show_correct(q,current_question)
    show_qustion(q)

def show_qustion(q):
    global trueOrFalse,l
    trueOrFalse += 1
    window.total +=1
    if window.total!=0:
        print('',window.total,'\n',window.score,'\n',window.score/window.total *100)
    labelBox.hide()
    radioBox.show()
    
    grp_btn.setExclusive(False)
    
    q1.setChecked(False)
    q2.setChecked(False)
    q3.setChecked(False)
    q4.setChecked(False)
    
    glav_button.setText('Ответить')
    
def show_result():
    global trueOrFalse,l
    trueOrFalse += 1
    radioBox.hide()
    
    labelBox.show()
    glav_button.setText('Следующий вопрос')

def show_correct(q,current_question):
    l1.setText(q[current_question].right)
    l.setText(q[current_question].question)


questions_list = [Question("Какой национальности не существует?","Смурфы","Энцы",
    "Чулымцы","Алеуты"),Question("иональности не существует?","Срфы","цы",
    "Чулыцы","Алуты"),Question("Какой национальнос существует?","Смрфы","цы",
    "Чулымцы","Алуты"),Question("насти не существует?","Смрфы","нцы",
    "Чулмцы","Алеы")]

next_question(questions_list)
TheBestLayout_v = QVBoxLayout()

TheBestLayout_v.addWidget(l,alignment = Qt.AlignCenter)
TheBestLayout_v.addWidget(radioBox,alignment = Qt.AlignCenter)
TheBestLayout_v.addWidget(labelBox,alignment = Qt.AlignCenter)
TheBestLayout_v.addWidget(glav_button,alignment = Qt.AlignCenter)

glav_button.clicked.connect(click_ok)

window.setLayout(TheBestLayout_v)
window.show()
app.exec_()