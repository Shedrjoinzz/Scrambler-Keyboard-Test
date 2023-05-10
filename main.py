import sys, keyboard, webbrowser, resources

from PyQt5 import QtCore
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QWidget,
                             QPushButton,
                             QLabel,
                             QComboBox,
                             QLabel)
from PyQt5.QtCore import (QPropertyAnimation,
                          QPoint,
                          QParallelAnimationGroup)
from PyQt5.QtGui import QIcon, QPixmap

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(":/icons/logo.png"), QIcon.Selected, QIcon.On)
        self.setWindowIcon(self.icon)
        self.setWindowTitle("Scrambler Keyboard Test")
        self.setStyleSheet("background-color: #191818")
        self.Style = """
            QPushButton {
                border: 1px solid silver;
                color: white;
                border-radius: 5px;
            }
            QWidget {
                border: 1px solid silver;
                border-radius: 5px;
            }
            QPushButton#button_active_Num_Lock {
                background-color: grey;
                border-radius: 7px;
                border: none;
            }
            QPushButton#button_active_Caps_Lock {
                background-color: grey;
                border-radius: 7px;
                border: none;
            }
            QPushButton#button_active_Scroll_Lock {
                background-color: grey;
                border-radius: 7px;
                border: none;
            }
            QPushButton#Button_Menu {
                border: 1px solid #00AEFF;
                color: white;
            }
            QPushButton#Button_Menu:pressed {
                color: #00AEFF;
            }
            QPushButton#GitHubButton {
                color: #fff;
                background-color: #080B0F;
                font-size: 16px;
                font: bold;
                border-radius: 5px;
                border: none;
            }

            QPushButton#GitHubButton:hover {
                background-color: #12151A;
                font-size: 17px;
            }

            QPushButton#GitHubButton:presseded {
                background-color: #080B0F
            }
            QPushButton#TelegramButton {
                color: #fff;
                background-color: #208FFF;
                font-size: 18px;
                border-radius: 5px;
                border: none;
            }

            QPushButton#TelegramButton:hover {
                background-color: #46A0FC;
                font-size: 19px;
            }

            QPushButton#TelegramButton:presseded {
                background-color: #208FFF
            }
            QPushButton#CloseButton {
                color: #fff;
                font-size: 20px;
                border-radius: 10;
                border: none;
                background-color: #333232
            }
            QPushButton#CloseButton:hover {
                background-color: #191818
            }
            QLabel {
                color: white;
                background-color: none;
                border: none;
            }
            QWidget#Panel_Menu {
                background-color: #1E1E1F;
                border-radius: 0px;
                border: none;
            }
        """

        self.button_Esc = QPushButton('Esc', self)
        self.button_Esc.setStyleSheet(self.Style)
        self.button_Esc.setGeometry(50, 20, 50, 50)

        self.button_F1 = QPushButton('F1', self)
        self.button_F1.setStyleSheet(self.Style)
        self.button_F1.setGeometry(150, 20, 50, 50)

        self.button_F2 = QPushButton('F2', self)
        self.button_F2.setStyleSheet(self.Style)
        self.button_F2.setGeometry(210, 20, 50, 50)

        self.button_F3 = QPushButton('F3', self)
        self.button_F3.setStyleSheet(self.Style)
        self.button_F3.setGeometry(270, 20, 50, 50)

        self.button_F4 = QPushButton('F4', self)
        self.button_F4.setStyleSheet(self.Style)
        self.button_F4.setGeometry(330, 20, 50, 50)

        self.button_F5 = QPushButton('F5', self)
        self.button_F5.setStyleSheet(self.Style)
        self.button_F5.setGeometry(410, 20, 50, 50)
        
        self.button_F6 = QPushButton('F6', self)
        self.button_F6.setStyleSheet(self.Style)
        self.button_F6.setGeometry(470, 20, 50, 50)

        self.button_F7 = QPushButton('F7', self)
        self.button_F7.setStyleSheet(self.Style)
        self.button_F7.setGeometry(530, 20, 50, 50)

        self.button_F8 = QPushButton('F8', self)
        self.button_F8.setStyleSheet(self.Style)
        self.button_F8.setGeometry(590, 20, 50, 50)

        self.button_F9 = QPushButton('F9', self)
        self.button_F9.setStyleSheet(self.Style)
        self.button_F9.setGeometry(670, 20, 50, 50)

        self.button_F10 = QPushButton('F10', self)
        self.button_F10.setStyleSheet(self.Style)
        self.button_F10.setGeometry(730, 20, 50, 50)

        self.button_F11 = QPushButton('F11', self)
        self.button_F11.setStyleSheet(self.Style)
        self.button_F11.setGeometry(790, 20, 50, 50)

        self.button_F12 = QPushButton('F12', self)
        self.button_F12.setStyleSheet(self.Style)
        self.button_F12.setGeometry(850, 20, 50, 50)

        self.button_Prt_Scrn = QPushButton('Prt\nScrn', self)
        self.button_Prt_Scrn.setStyleSheet(self.Style)
        self.button_Prt_Scrn.setGeometry(930, 20, 50, 50)

        self.button_Scroll_Lock = QPushButton('Scroll\nLock', self)
        self.button_Scroll_Lock.setStyleSheet(self.Style)
        self.button_Scroll_Lock.setGeometry(990, 20, 50, 50)

        self.button_Pause_Break = QPushButton('Pause\nBreak', self)
        self.button_Pause_Break.setStyleSheet(self.Style)
        self.button_Pause_Break.setGeometry(1050, 20, 50, 50)

        self.button_E_ = QPushButton('~', self)
        self.button_E_.setStyleSheet(self.Style)
        self.button_E_.setGeometry(50, 100, 50, 50)

        self.button_1 = QPushButton('1', self)
        self.button_1.setStyleSheet(self.Style)
        self.button_1.setGeometry(110, 100, 50, 50)

        self.button_2 = QPushButton('2', self)
        self.button_2.setStyleSheet(self.Style)
        self.button_2.setGeometry(170, 100, 50, 50)

        self.button_3 = QPushButton('3', self)
        self.button_3.setStyleSheet(self.Style)
        self.button_3.setGeometry(230, 100, 50, 50)

        self.button_4 = QPushButton('4', self)
        self.button_4.setStyleSheet(self.Style)
        self.button_4.setGeometry(290, 100, 50, 50)
        
        self.button_5 = QPushButton('5', self)
        self.button_5.setStyleSheet(self.Style)
        self.button_5.setGeometry(350, 100, 50, 50)

        self.button_6 = QPushButton('6', self)
        self.button_6.setStyleSheet(self.Style)
        self.button_6.setGeometry(410, 100, 50, 50)

        self.button_7 = QPushButton('7', self)
        self.button_7.setStyleSheet(self.Style)
        self.button_7.setGeometry(470, 100, 50, 50)

        self.button_8 = QPushButton('8', self)
        self.button_8.setStyleSheet(self.Style)
        self.button_8.setGeometry(530, 100, 50, 50)

        self.button_9 = QPushButton('9', self)
        self.button_9.setStyleSheet(self.Style)
        self.button_9.setGeometry(590, 100, 50, 50)

        self.button_0 = QPushButton('0', self)
        self.button_0.setStyleSheet(self.Style)
        self.button_0.setGeometry(650, 100, 50, 50)

        self.button_minus_ = QPushButton('-\n_', self)
        self.button_minus_.setObjectName("button_minus_")
        self.button_minus_.setStyleSheet(self.Style)
        self.button_minus_.setGeometry(710, 100, 50, 50)

        self.button_plus_equals = QPushButton('+\n=', self)
        self.button_plus_equals.setStyleSheet(self.Style)
        self.button_plus_equals.setGeometry(770, 100, 50, 50)

        self.button_Back = QPushButton('<-- Back', self)
        self.button_Back.setStyleSheet(self.Style)
        self.button_Back.setGeometry(830, 100, 70, 50)

        self.button_Ins = QPushButton('Ins', self)
        self.button_Ins.setStyleSheet(self.Style)
        self.button_Ins.setGeometry(930, 100, 50, 50)

        self.button_Home = QPushButton('Home', self)
        self.button_Home.setStyleSheet(self.Style)
        self.button_Home.setGeometry(990, 100, 50, 50)

        self.button_Page_Up = QPushButton('Page\nUp', self)
        self.button_Page_Up.setStyleSheet(self.Style)
        self.button_Page_Up.setGeometry(1050, 100, 50, 50)

        self.button_Num_Lock = QPushButton('Num\nLock', self)
        self.button_Num_Lock.setStyleSheet(self.Style)
        self.button_Num_Lock.setGeometry(1150, 100, 50, 50)

        self.button_slesh = QPushButton('/', self)
        self.button_slesh.setStyleSheet(self.Style)
        self.button_slesh.setGeometry(1210, 100, 50, 50)

        self.button_mult = QPushButton('*', self)
        self.button_mult.setStyleSheet(self.Style)
        self.button_mult.setGeometry(1270, 100, 50, 50)

        self.button_minus = QPushButton('-', self)
        self.button_minus.setStyleSheet(self.Style)
        self.button_minus.setGeometry(1330, 100, 50, 50)

        self.button_Tab = QPushButton('Tab', self)
        self.button_Tab.setStyleSheet(self.Style)
        self.button_Tab.setGeometry(50, 160, 80, 50)

        self.button_Q = QPushButton('Q', self)
        self.button_Q.setStyleSheet(self.Style)
        self.button_Q.setGeometry(140, 160, 50, 50)

        self.button_W = QPushButton('W', self)
        self.button_W.setStyleSheet(self.Style)
        self.button_W.setGeometry(200, 160, 50, 50)

        self.button_E = QPushButton('E', self)
        self.button_E.setStyleSheet(self.Style)
        self.button_E.setGeometry(260, 160, 50, 50)

        self.button_R = QPushButton('R', self)
        self.button_R.setStyleSheet(self.Style)
        self.button_R.setGeometry(320, 160, 50, 50)

        self.button_T = QPushButton('T', self)
        self.button_T.setStyleSheet(self.Style)
        self.button_T.setGeometry(380, 160, 50, 50)

        self.button_Y = QPushButton('Y', self)
        self.button_Y.setStyleSheet(self.Style)
        self.button_Y.setGeometry(440, 160, 50, 50)

        self.button_U = QPushButton('U', self)
        self.button_U.setStyleSheet(self.Style)
        self.button_U.setGeometry(500, 160, 50, 50)

        self.button_I = QPushButton('I', self)
        self.button_I.setStyleSheet(self.Style)
        self.button_I.setGeometry(560, 160, 50, 50)

        self.button_O = QPushButton('O', self)
        self.button_O.setStyleSheet(self.Style)
        self.button_O.setGeometry(620, 160, 50, 50)

        self.button_P = QPushButton('P', self)
        self.button_P.setStyleSheet(self.Style)
        self.button_P.setGeometry(680, 160, 50, 50)

        self.button_bracked_left = QPushButton('{', self)
        self.button_bracked_left.setStyleSheet(self.Style)
        self.button_bracked_left.setGeometry(740, 160, 40, 50)
 
        self.button_bracked_right = QPushButton('}', self)
        self.button_bracked_right.setStyleSheet(self.Style)
        self.button_bracked_right.setGeometry(790, 160, 40, 50)

        self.button_Enter = QPushButton('Enter\n<--', self)
        self.button_Enter.setStyleSheet(self.Style)
        self.button_Enter.setGeometry(840, 160, 60, 50)

        self.button_Del = QPushButton('Del', self)
        self.button_Del.setStyleSheet(self.Style)
        self.button_Del.setGeometry(930, 160, 50, 50)

        self.button_End = QPushButton('End', self)
        self.button_End.setStyleSheet(self.Style)
        self.button_End.setGeometry(990, 160, 50, 50)

        self.button_Page_Down = QPushButton('Page\nDown', self)
        self.button_Page_Down.setStyleSheet(self.Style)
        self.button_Page_Down.setGeometry(1050, 160, 50, 50)

        self.button_7_ = QPushButton('7\nHome', self)
        self.button_7_.setStyleSheet(self.Style)
        self.button_7_.setGeometry(1150, 160, 50, 50)

        self.button_8_ = QPushButton('8', self)
        self.button_8_.setStyleSheet(self.Style)
        self.button_8_.setGeometry(1210, 160, 50, 50)

        self.button_9_ = QPushButton('9\nPage\nUp', self)
        self.button_9_.setStyleSheet(self.Style)
        self.button_9_.setGeometry(1270, 160, 50, 50)

        self.button_plus = QPushButton('+', self)
        self.button_plus.setStyleSheet(self.Style)
        self.button_plus.setGeometry(1330, 160, 50, 110)

        self.button_Caps_Lock = QPushButton('Caps\nLock', self)
        self.button_Caps_Lock.setStyleSheet(self.Style)
        self.button_Caps_Lock.setGeometry(50, 220, 90, 50)

        self.button_A = QPushButton('A', self)
        self.button_A.setStyleSheet(self.Style)
        self.button_A.setGeometry(150, 220, 50, 50)

        self.button_S = QPushButton('S', self)
        self.button_S.setStyleSheet(self.Style)
        self.button_S.setGeometry(210, 220, 50, 50)

        self.button_D = QPushButton('D', self)
        self.button_D.setStyleSheet(self.Style)
        self.button_D.setGeometry(270, 220, 50, 50)
        
        self.button_F = QPushButton('F', self)
        self.button_F.setStyleSheet(self.Style)
        self.button_F.setGeometry(330, 220, 50, 50)

        self.button_G = QPushButton('G', self)
        self.button_G.setStyleSheet(self.Style)
        self.button_G.setGeometry(390, 220, 50, 50)

        self.button_H = QPushButton('H', self)
        self.button_H.setStyleSheet(self.Style)
        self.button_H.setGeometry(450, 220, 50, 50)


        self.button_J = QPushButton('J', self)
        self.button_J.setStyleSheet(self.Style)
        self.button_J.setGeometry(510, 220, 50, 50)

        self.button_K = QPushButton('K', self)
        self.button_K.setStyleSheet(self.Style)
        self.button_K.setGeometry(570, 220, 50, 50)

        self.button_L = QPushButton('L', self)
        self.button_L.setStyleSheet(self.Style)
        self.button_L.setGeometry(630, 220, 50, 50)
        
        self.button_two_dot = QPushButton(':', self)
        self.button_two_dot.setStyleSheet(self.Style)
        self.button_two_dot.setGeometry(690, 220, 50, 50)

        self.button_QUOTE_two = QPushButton('"', self)
        self.button_QUOTE_two.setStyleSheet(self.Style)
        self.button_QUOTE_two.setGeometry(750, 220, 50, 50)

        self.button_LINE_UP = QPushButton('|', self)
        self.button_LINE_UP.setStyleSheet(self.Style)
        self.button_LINE_UP.setGeometry(810, 220, 90, 50)

        self.button_4_ = QPushButton('4', self)
        self.button_4_.setStyleSheet(self.Style)
        self.button_4_.setGeometry(1150, 220, 50, 50)

        self.button_5_ = QPushButton('5', self)
        self.button_5_.setStyleSheet(self.Style)
        self.button_5_.setGeometry(1210, 220, 50, 50)

        self.button_6_ = QPushButton('6', self)
        self.button_6_.setStyleSheet(self.Style)
        self.button_6_.setGeometry(1270, 220, 50, 50)

        self.button_Shift = QPushButton('Shift', self)
        self.button_Shift.setStyleSheet(self.Style)
        self.button_Shift.setGeometry(50, 280, 120, 50)

        self.button_Z = QPushButton('Z', self)
        self.button_Z.setStyleSheet(self.Style)
        self.button_Z.setGeometry(180, 280, 50, 50)

        self.button_X = QPushButton('X', self)
        self.button_X.setStyleSheet(self.Style)
        self.button_X.setGeometry(240, 280, 50, 50)

        self.button_C = QPushButton('C', self)
        self.button_C.setStyleSheet(self.Style)
        self.button_C.setGeometry(300, 280, 50, 50)

        self.button_V = QPushButton('V', self)
        self.button_V.setStyleSheet(self.Style)
        self.button_V.setGeometry(360, 280, 50, 50)

        self.button_B = QPushButton('B', self)
        self.button_B.setStyleSheet(self.Style)
        self.button_B.setGeometry(420, 280, 50, 50)

        self.button_N = QPushButton('N', self)
        self.button_N.setStyleSheet(self.Style)
        self.button_N.setGeometry(480, 280, 50, 50)

        self.button_M = QPushButton('M', self)
        self.button_M.setStyleSheet(self.Style)
        self.button_M.setGeometry(540, 280, 50, 50)

        self.button_left_ = QPushButton('<', self)
        self.button_left_.setStyleSheet(self.Style)
        self.button_left_.setGeometry(600, 280, 50, 50)

        self.button_right_ = QPushButton('>', self)
        self.button_right_.setStyleSheet(self.Style)
        self.button_right_.setGeometry(660, 280, 50, 50)

        self.button_Question = QPushButton('?', self)
        self.button_Question.setStyleSheet(self.Style)
        self.button_Question.setGeometry(720, 280, 50, 50)
        
        self.button_Shift2 = QPushButton('Shift', self)
        self.button_Shift2.setStyleSheet(self.Style)
        self.button_Shift2.setGeometry(780, 280, 120, 50)

        self.button_Up = QPushButton('^', self)
        self.button_Up.setStyleSheet(self.Style)
        self.button_Up.setGeometry(990, 280, 50, 50)

        self.button_1_ = QPushButton('1\nEnd', self)
        self.button_1_.setStyleSheet(self.Style)
        self.button_1_.setGeometry(1150, 280, 50, 50)

        self.button_2_ = QPushButton('2', self)
        self.button_2_.setStyleSheet(self.Style)
        self.button_2_.setGeometry(1210, 280, 50, 50)

        self.button_3_ = QPushButton('3\nPage\nDown', self)
        self.button_3_.setStyleSheet(self.Style)
        self.button_3_.setGeometry(1270, 280, 50, 50)

        self.button_Ent = QPushButton('Ent', self)
        self.button_Ent.setStyleSheet(self.Style)
        self.button_Ent.setGeometry(1330, 280, 50, 110)

        self.button_Ctrl = QPushButton('Ctrl', self)
        self.button_Ctrl.setStyleSheet(self.Style)
        self.button_Ctrl.setGeometry(50, 340, 70, 50)

        self.button_Win = QPushButton('Win', self)
        self.button_Win.setStyleSheet(self.Style)
        self.button_Win.setGeometry(130, 340, 70, 50)

        self.button_Alt = QPushButton('Alt', self)
        self.button_Alt.setStyleSheet(self.Style)
        self.button_Alt.setGeometry(210, 340, 70, 50)

        self.button_Space = QPushButton('Space', self)
        self.button_Space.setStyleSheet(self.Style)
        self.button_Space.setGeometry(290, 340, 320, 50)

        self.button_Alt2 = QPushButton('Alt', self)
        self.button_Alt2.setStyleSheet(self.Style)
        self.button_Alt2.setGeometry(620, 340, 70, 50)

        self.button_FN = QPushButton('FN', self)
        self.button_FN.setStyleSheet(self.Style)
        self.button_FN.setGeometry(700, 340, 70, 50)

        self.button_Light = QPushButton('Light', self)
        self.button_Light.setStyleSheet(self.Style)
        self.button_Light.setGeometry(780, 340, 55, 50)

        self.button_Ctrl2 = QPushButton('Ctrl', self)
        self.button_Ctrl2.setStyleSheet(self.Style)
        self.button_Ctrl2.setGeometry(845, 340, 55, 50)

        self.button_left = QPushButton('<', self)
        self.button_left.setStyleSheet(self.Style)
        self.button_left.setGeometry(930, 340, 50, 50)

        self.button_Down = QPushButton('Down', self)
        self.button_Down.setStyleSheet(self.Style)
        self.button_Down.setGeometry(990, 340, 50, 50)

        self.button_D_Right= QPushButton('>', self)
        self.button_D_Right.setStyleSheet(self.Style)
        self.button_D_Right.setGeometry(1050, 340, 50, 50)

        self.button_0_Ins = QPushButton('0\nIns', self)
        self.button_0_Ins.setStyleSheet(self.Style)
        self.button_0_Ins.setGeometry(1150, 340, 110, 50)
        self.button_0_Ins.setEnabled(False)

        self.button_del2 = QPushButton('.\nDel', self)
        self.button_del2.setStyleSheet(self.Style)
        self.button_del2.setGeometry(1270, 340, 50, 50)

        self.panel_active = QWidget(self)
        self.panel_active.setGeometry(1150, 20, 230, 65)
        self.panel_active.setStyleSheet(self.Style)

        self.button_active_Num_Lock = QPushButton(self)
        self.button_active_Num_Lock.setObjectName("button_active_Num_Lock")
        self.button_active_Num_Lock.setGeometry(1200, 30, 15, 15)
        self.button_active_Num_Lock.setStyleSheet(self.Style)

        self.label_Num_Lock = QLabel('Num\nLock', self)
        self.label_Num_Lock.setGeometry(1200, 45, 40, 40)
        self.label_Num_Lock.setStyleSheet(self.Style)

        self.button_active_Caps_Lock = QPushButton(self)
        self.button_active_Caps_Lock.setObjectName("button_active_Caps_Lock")
        self.button_active_Caps_Lock.setGeometry(1260, 30, 15, 15)
        self.button_active_Caps_Lock.setStyleSheet(self.Style)

        self.label_Caps_Lock = QLabel('Caps\nLock', self)
        self.label_Caps_Lock.setGeometry(1260, 45, 40, 40)
        self.label_Caps_Lock.setStyleSheet(self.Style)

        self.button_active_Scroll_Lock = QPushButton(self)
        self.button_active_Scroll_Lock.setObjectName("button_active_Scroll_Lock")
        self.button_active_Scroll_Lock.setGeometry(1320, 30, 15, 15)
        self.button_active_Scroll_Lock.setStyleSheet(self.Style)

        self.label_Scroll_Lock = QLabel('Scroll\nLock', self)
        self.label_Scroll_Lock.setGeometry(1320, 45, 40, 40)
        self.label_Scroll_Lock.setStyleSheet(self.Style)

        self.active_Num_Lock = False
        self.active_Caps_Lock = False
        self.active_Scroll_Lock = False

        self.active_print_screen = True
        self.active_space_button = True

        self.Button_Left = True
        self.Button_Up = True 
        self.Button_Down = True 
        self.Button_Right = True

        self.Button_Menu = QPushButton("Menu", self)
        self.Button_Menu.setGeometry(1410, 20, 70, 50)
        self.Button_Menu.setObjectName("Button_Menu")
        self.Button_Menu.setStyleSheet(self.Style)
        self.Button_Menu.clicked.connect(self.PanelOpen)

        self.Panel_Menu = QWidget(self)
        self.Panel_Menu.setGeometry(1700, 0, 200, 400)
        self.Panel_Menu.setObjectName("Panel_Menu")
        self.Panel_Menu.setStyleSheet(self.Style)

        self.keyboardFunction = "True"
        
        self.keyboard_function()


        self.button_Esc.setEnabled(True)

        self.TelegramButton = QPushButton("Telegram", self)
        self.TelegramButton.setObjectName("TelegramButton")
        self.TelegramButton.setStyleSheet(self.Style)
        self.TelegramButton.setGeometry(1700, 100, 150, 30)
        self.TelegramButton.clicked.connect(self.openTelegramWebBrowser)

        self.GitHubButton = QPushButton("GitHub", self)
        self.GitHubButton.setObjectName("GitHubButton")
        self.GitHubButton.setStyleSheet(self.Style)
        self.GitHubButton.setGeometry(1700, 150, 150, 30)
        self.GitHubButton.clicked.connect(self.openGitHubWebBrowser)

        self.label_checkbox_title = QLabel('Keyboard pressed color', self)
        self.label_checkbox_title.setGeometry(1700, 230, 150, 20)
        self.label_checkbox_title.setStyleSheet("color: white; background-color: none; font-size: 13px;")

        self.list_color = ['Light Blue', 'Orange', 'Green', 'Purple', 'Red', 'Yellow', 'Pink', 'Grey', 'Coral']
        self.CheckBox_Color_Keyboard_Pressed = QComboBox(self)
        self.CheckBox_Color_Keyboard_Pressed.setGeometry(1700, 250, 150, 20)
        for i in self.list_color:
            self.CheckBox_Color_Keyboard_Pressed.addItem(i)
        self.CheckBox_Color_Keyboard_Pressed.setStyleSheet("color: white; background-color: #1E1E1F;")
        self.CheckBox_Color_Keyboard_Pressed.activated.connect(self.add_color_keyboard_pressed)

        self.CloseButton = QPushButton("✕", self)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(self.Style)
        self.CloseButton.setGeometry(1700, 20, 30, 30)
        self.CloseButton.clicked.connect(self.PanelClose)

        self.anim_group = QParallelAnimationGroup()
        self.AnimationPanel = QPropertyAnimation(self.Panel_Menu, b"pos")
        self.AnimationTelegramButton = QPropertyAnimation(self.TelegramButton, b"pos")
        self.AnimationGitHubButton = QPropertyAnimation(self.GitHubButton, b"pos")
        self.AnimationLabelCheckBoxTitle = QPropertyAnimation(self.label_checkbox_title, b"pos")
        self.AnimationCheckBoxColorKeyboardPressed = QPropertyAnimation(self.CheckBox_Color_Keyboard_Pressed, b"pos")
        self.AnimationCloseButton = QPropertyAnimation(self.CloseButton, b"pos")

        self.StylePressed = "background-color: #00AEFF; border-radius: 5px;"

    def add_color_keyboard_pressed(self):
        if self.CheckBox_Color_Keyboard_Pressed.currentText() == "Light Blue": 
            self.StylePressed = f"background-color: #00AEFF; border-radius: 5px;" 
        else:
            self.StylePressed = f"background-color: {self.CheckBox_Color_Keyboard_Pressed.currentText().lower()}; border-radius: 5px;"
            
    def PanelOpen(self):
        self.keyboardFunction = "False"

        self.AnimationPanel.setEndValue(QPoint(1300, 0))  # Geometry Animation PanelOpen
        self.AnimationPanel.setDuration(200)

        self.AnimationTelegramButton.setEndValue(QPoint(1320, 100))  # Geometry Animation PanelOpen
        self.AnimationTelegramButton.setDuration(200)

        self.AnimationGitHubButton.setEndValue(QPoint(1320, 150))  # Geometry Animation PanelOpen
        self.AnimationGitHubButton.setDuration(200)

        self.AnimationCloseButton.setEndValue(QPoint(1320, 20))  # Geometry Animation PanelOpen
        self.AnimationCloseButton.setDuration(200)

        self.AnimationLabelCheckBoxTitle.setEndValue(QPoint(1320, 230))  # Geometry Animation PanelOpen
        self.AnimationLabelCheckBoxTitle.setDuration(200)

        self.AnimationCheckBoxColorKeyboardPressed.setEndValue(QPoint(1320, 250))  # Geometry Animation PanelOpen
        self.AnimationCheckBoxColorKeyboardPressed.setDuration(200)

        self.start_animation()

    def PanelClose(self):
        self.keyboardFunction = "True"
        self.AnimationPanel.setEndValue(QPoint(1700, 0))  # Geometry Animation PanelOpen
        self.AnimationPanel.setDuration(200)

        self.AnimationTelegramButton.setEndValue(QPoint(1700, 100))  # Geometry Animation PanelOpen
        self.AnimationTelegramButton.setDuration(200)

        self.AnimationGitHubButton.setEndValue(QPoint(1700, 150))  # Geometry Animation PanelOpen
        self.AnimationGitHubButton.setDuration(200)

        self.AnimationCloseButton.setEndValue(QPoint(1700, 20))  # Geometry Animation PanelOpen
        self.AnimationCloseButton.setDuration(200)

        self.AnimationLabelCheckBoxTitle.setEndValue(QPoint(1700, 230))  # Geometry Animation PanelOpen
        self.AnimationLabelCheckBoxTitle.setDuration(200)

        self.AnimationCheckBoxColorKeyboardPressed.setEndValue(QPoint(1700, 250))  # Geometry Animation PanelOpen
        self.AnimationCheckBoxColorKeyboardPressed.setDuration(200)

        self.start_animation()
    
    def start_animation(self):
        self.anim_group.addAnimation(self.AnimationPanel)
        self.anim_group.addAnimation(self.AnimationTelegramButton)
        self.anim_group.addAnimation(self.AnimationGitHubButton)
        self.anim_group.addAnimation(self.AnimationCloseButton)
        self.anim_group.addAnimation(self.AnimationLabelCheckBoxTitle)
        self.anim_group.addAnimation(self.AnimationCheckBoxColorKeyboardPressed)
        self.anim_group.start()

    def openTelegramWebBrowser(self):
        webbrowser.open('https://t.me/ProgramsCreator/')

    def openGitHubWebBrowser(self):
        webbrowser.open('https://github.com/Shedrjoinzz/')

    def keyboard_function(self):
        if self.keyboardFunction == "True":
            keyboard.add_hotkey('SNAPSHOT', lambda: self.PrintScreen())
            keyboard.add_hotkey('Space', lambda: self.SpaceButton())
            keyboard.add_hotkey('Left', lambda: self.Left())
            keyboard.add_hotkey('Up', lambda: self.Up())
            keyboard.add_hotkey('Down', lambda: self.Down())
            keyboard.add_hotkey('Right', lambda: self.Right())
        elif self.keyboardFunction == "False":
            pass
    
    def SpaceButton(self):
        if self.active_space_button:
            self.active_space_button = False
            self.button_Space.setStyleSheet(self.StylePressed)
        else:
            self.active_space_button = True
            self.button_Space.setStyleSheet(self.Style)

    def PrintScreen(self):
        if self.active_print_screen:
            self.active_print_screen = False
            self.button_Prt_Scrn.setStyleSheet(self.StylePressed)
        else:
            self.active_print_screen = True
            self.button_Prt_Scrn.setStyleSheet(self.Style)

    def Left(self):
        if self.Button_Left:
            self.Button_Left = False
            self.button_left.setStyleSheet(self.StylePressed)
        else:
            self.Button_Left = True
            self.button_left.setStyleSheet(self.Style)

    def Up(self):
        if self.Button_Up:
            self.Button_Up = False
            self.button_Up.setStyleSheet(self.StylePressed)
        else:
            self.Button_Up = True
            self.button_Up.setStyleSheet(self.Style)
    
    def Down(self):
        if self.Button_Down:
            self.Button_Down = False
            self.button_Down.setStyleSheet(self.StylePressed)
        else:
            self.Button_Down = True
            self.button_Down.setStyleSheet(self.Style)
    
    def Right(self):
        if self.Button_Right:
            self.Button_Right = False
            self.button_D_Right.setStyleSheet(self.StylePressed)
        else:
            self.Button_Right = True
            self.button_D_Right.setStyleSheet(self.Style)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.button_Esc.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F1:
            self.button_F1.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F2:
            self.button_F2.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F3:
            self.button_F3.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F4:
            self.button_F4.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F5:
            self.button_F5.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F6:
            self.button_F6.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F7:
            self.button_F7.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F8:
            self.button_F8.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F9:
            self.button_F9.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F10:
            self.button_F10.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F11:
            self.button_F11.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F12:
            self.button_F12.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_ScrollLock:
            self.button_Scroll_Lock.setStyleSheet(self.StylePressed)
            if self.active_Scroll_Lock == False:
                self.active_Scroll_Lock = True
                self.button_active_Scroll_Lock.setStyleSheet("background-color: #00AEFF; border-radius: 7px;")
            else:
                self.active_Scroll_Lock = False
                self.button_active_Scroll_Lock.setStyleSheet(self.Style)
            
                

        if event.key() == 16777224:
            self.button_Pause_Break.setStyleSheet(self.StylePressed)

        if event.key() == 96:
            self.button_E_.setStyleSheet(self.StylePressed)

        if event.key() == 49:
            self.button_1.setStyleSheet(self.StylePressed)
            self.button_1_.setStyleSheet(self.StylePressed)

        if event.key() == 50:
            self.button_2.setStyleSheet(self.StylePressed)
            self.button_2_.setStyleSheet(self.StylePressed)

        if event.key() == 51:
            self.button_3.setStyleSheet(self.StylePressed)
            self.button_3_.setStyleSheet(self.StylePressed)

        if event.key() == 52:
            self.button_4.setStyleSheet(self.StylePressed)
            self.button_4_.setStyleSheet(self.StylePressed)
        
        if event.key() == 53:
            self.button_5.setStyleSheet(self.StylePressed)
            self.button_5_.setStyleSheet(self.StylePressed)

        if event.key() == 54:
            self.button_6.setStyleSheet(self.StylePressed)
            self.button_6_.setStyleSheet(self.StylePressed)

        if event.key() == 55:
            self.button_7.setStyleSheet(self.StylePressed)
            self.button_7_.setStyleSheet(self.StylePressed)

        if event.key() == 56:
            self.button_8.setStyleSheet(self.StylePressed)
            self.button_8_.setStyleSheet(self.StylePressed)

        if event.key() == 57:
            self.button_9.setStyleSheet(self.StylePressed)
            self.button_9_.setStyleSheet(self.StylePressed)

        if event.key() == 48:
            self.button_0.setStyleSheet(self.StylePressed)
            self.button_0_Ins.setStyleSheet(self.StylePressed)

        if event.key() == 45:
            self.button_minus_.setStyleSheet(self.StylePressed)
            self.button_minus.setStyleSheet(self.StylePressed)

        if event.key() == 61:
            self.button_plus_equals.setStyleSheet(self.StylePressed)
        if event.key() == 16777219:
            self.button_Back.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_CapsLock:
            self.button_Caps_Lock.setStyleSheet(self.StylePressed)
            self.button_active_Caps_Lock.setStyleSheet(self.StylePressed)
            if self.active_Caps_Lock == False:
                self.active_Caps_Lock = True
                self.button_active_Caps_Lock.setStyleSheet("background-color: #00AEFF; border-radius: 7px;")
            else:
                self.active_Caps_Lock = False
                self.button_active_Caps_Lock.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_NumLock:
            self.button_Num_Lock.setStyleSheet(self.StylePressed)
            if self.active_Num_Lock == False:
                self.active_Num_Lock = True
                self.button_active_Num_Lock.setStyleSheet("background-color: #00AEFF; border-radius: 7px;")
            else:
                self.active_Num_Lock = False
                self.button_active_Num_Lock.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_A:
            self.button_A.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_S:
            self.button_S.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_D:
            self.button_D.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_F:
            self.button_F.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_G:
            self.button_G.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_H:
            self.button_H.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_J:
            self.button_J.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_K:
            self.button_K.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_L:
            self.button_L.setStyleSheet(self.StylePressed)

        if event.key() == 59:
            self.button_two_dot.setStyleSheet(self.StylePressed)
        
        if event.key() == 39:
            self.button_QUOTE_two.setStyleSheet(self.StylePressed)

        if event.key() == 92:
            self.button_LINE_UP.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_Shift:
            self.button_Shift.setStyleSheet(self.StylePressed)
            self.button_Shift2.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_Z:
            self.button_Z.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_X:
            self.button_X.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_C:
            self.button_C.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_V:
            self.button_V.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_B:
            self.button_B.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_N:
            self.button_N.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_M:
            self.button_M.setStyleSheet(self.StylePressed)

        if event.key() == 44:
            self.button_left_.setStyleSheet(self.StylePressed)

        if event.key() == 46:
            self.button_right_.setStyleSheet(self.StylePressed)
        
        if event.key() == 16777223:
            self.button_Del.setStyleSheet(self.StylePressed)
            self.button_del2.setStyleSheet(self.StylePressed)
        
        if event.key() == 16777222:
            self.button_Ins.setStyleSheet(self.StylePressed)

        if event.key() == 16777232:
            self.button_Home.setStyleSheet(self.StylePressed)
        
        if event.key() == 16777238:
            self.button_Page_Up.setStyleSheet(self.StylePressed)
        
        if event.key() == 16777233:
            self.button_End.setStyleSheet(self.StylePressed)
        
        if event.key() == 16777239:
            self.button_Page_Down.setStyleSheet(self.StylePressed)

        if event.key() == 47:
            self.button_Question.setStyleSheet(self.StylePressed)
            self.button_slesh.setStyleSheet(self.StylePressed)

        if event.key() == 42:
            self.button_mult.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_Q:
            self.button_Q.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_W:
            self.button_W.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_E:
            self.button_E.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_R:
            self.button_R.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_T:
            self.button_T.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_Y:
            self.button_Y.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_U:
            self.button_U.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_I:
            self.button_I.setStyleSheet(self.StylePressed)
        
        if event.key() == QtCore.Qt.Key_O:
            self.button_O.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_P:
            self.button_P.setStyleSheet(self.StylePressed)

        if event.key() == 91:
            self.button_bracked_left.setStyleSheet(self.StylePressed)

        if event.key() == 93:
            self.button_bracked_right.setStyleSheet(self.StylePressed)

        if event.key() == 16777220:
            self.button_Enter.setStyleSheet(self.StylePressed)

        if event.key() == 43:
            self.button_plus.setStyleSheet(self.StylePressed)

        if event.key() == QtCore.Qt.Key_Control:
            self.button_Ctrl.setStyleSheet(self.StylePressed)
            self.button_Ctrl2.setStyleSheet(self.StylePressed)

        if event.key() == 16777250:
            self.button_Win.setStyleSheet(self.StylePressed)

        if event.key() == 16777251:
            self.button_Alt.setStyleSheet(self.StylePressed)
            self.button_Alt2.setStyleSheet(self.StylePressed)
        
        if event.key() == 16777221:
            self.button_Ent.setStyleSheet(self.StylePressed)

        return super().keyPressEvent(event)

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.button_Esc.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F1:
            self.button_F1.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F2:
            self.button_F2.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F3:
            self.button_F3.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F4:
            self.button_F4.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F5:
            self.button_F5.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F6:
            self.button_F6.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F7:
            self.button_F7.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F8:
            self.button_F8.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F9:
            self.button_F9.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F10:
            self.button_F10.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F11:
            self.button_F11.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F12:
            self.button_F12.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_ScrollLock:
            self.button_Scroll_Lock.setStyleSheet(self.Style)

        if event.key() == 16777224:
            self.button_Pause_Break.setStyleSheet(self.Style)

        if event.key() == 96:
            self.button_E_.setStyleSheet(self.Style)

        if event.key() == 16777223:
            self.button_Del.setStyleSheet(self.Style)
            self.button_del2.setStyleSheet(self.Style)

        if event.key() == 16777222:
            self.button_Ins.setStyleSheet(self.Style)

        if event.key() == 16777232:
            self.button_Home.setStyleSheet(self.Style)
        
        if event.key() == 16777238:
            self.button_Page_Up.setStyleSheet(self.Style)
        
        if event.key() == 16777233:
            self.button_End.setStyleSheet(self.Style)
        
        if event.key() == 16777239:
            self.button_Page_Down.setStyleSheet(self.Style)

        if event.key() == 16777221:
            self.button_Ent.setStyleSheet(self.Style)

        if event.key() == 49:
            self.button_1.setStyleSheet(self.Style)
            self.button_1_.setStyleSheet(self.Style)

        if event.key() == 50:
            self.button_2.setStyleSheet(self.Style)
            self.button_2_.setStyleSheet(self.Style)

        if event.key() == 51:
            self.button_3.setStyleSheet(self.Style)
            self.button_3_.setStyleSheet(self.Style)

        if event.key() == 52:
            self.button_4.setStyleSheet(self.Style)
            self.button_4_.setStyleSheet(self.Style)

        if event.key() == 53:
            self.button_5.setStyleSheet(self.Style)
            self.button_5_.setStyleSheet(self.Style)

        if event.key() == 54:
            self.button_6.setStyleSheet(self.Style)
            self.button_6_.setStyleSheet(self.Style)

        if event.key() == 55:
            self.button_7.setStyleSheet(self.Style)
            self.button_7_.setStyleSheet(self.Style)


        if event.key() == 56:
            self.button_8.setStyleSheet(self.Style)
            self.button_8_.setStyleSheet(self.Style)

        if event.key() == 57:
            self.button_9.setStyleSheet(self.Style)
            self.button_9_.setStyleSheet(self.Style)
            
        if event.key() == 48:
            self.button_0.setStyleSheet(self.Style)
            self.button_0_Ins.setStyleSheet(self.Style)

        if event.key() == 45:
            self.button_minus_.setStyleSheet(self.Style)
            self.button_minus.setStyleSheet(self.Style)

        if event.key() == 61:
            self.button_plus_equals.setStyleSheet(self.Style)
        if event.key() == 16777219:
            self.button_Back.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_CapsLock:
            self.button_Caps_Lock.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_A:
            self.button_A.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_S:
            self.button_S.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_D:
            self.button_D.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_F:
            self.button_F.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_G:
            self.button_G.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_H:
            self.button_H.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_J:
            self.button_J.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_K:
            self.button_K.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_L:
            self.button_L.setStyleSheet(self.Style)
        
        if event.key() == 59:
            self.button_two_dot.setStyleSheet(self.Style)
        
        if event.key() == 39:
            self.button_QUOTE_two.setStyleSheet(self.Style)

        if event.key() == 92:
            self.button_LINE_UP.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_Shift:
            self.button_Shift.setStyleSheet(self.Style)
            self.button_Shift2.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_Z:
            self.button_Z.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_X:
            self.button_X.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_C:
            self.button_C.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_V:
            self.button_V.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_B:
            self.button_B.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_N:
            self.button_N.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_M:
            self.button_M.setStyleSheet(self.Style)

        if event.key() == 44:
            self.button_left_.setStyleSheet(self.Style)
        
        if event.key() == 46:
            self.button_right_.setStyleSheet(self.Style)
            self.button_del2.setStyleSheet(self.Style)

        if event.key() == 47:
            self.button_Question.setStyleSheet(self.Style)
            self.button_slesh.setStyleSheet(self.Style)    
        
        if event.key() == 42:
            self.button_mult.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_NumLock:
            self.button_Num_Lock.setStyleSheet(self.Style)


        if event.key() == QtCore.Qt.Key_Q:
            self.button_Q.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_W:
            self.button_W.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_E:
            self.button_E.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_R:
            self.button_R.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_T:
            self.button_T.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_Y:
            self.button_Y.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_U:
            self.button_U.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_I:
            self.button_I.setStyleSheet(self.Style)
        
        if event.key() == QtCore.Qt.Key_O:
            self.button_O.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_P:
            self.button_P.setStyleSheet(self.Style)

        if event.key() == 91:
            self.button_bracked_left.setStyleSheet(self.Style)

        if event.key() == 93:
            self.button_bracked_right.setStyleSheet(self.Style)

        if event.key() == 16777220:
            self.button_Enter.setStyleSheet(self.Style)

        if event.key() == 43:
            self.button_plus.setStyleSheet(self.Style)

        if event.key() == QtCore.Qt.Key_Control:
            self.button_Ctrl.setStyleSheet(self.Style)
            self.button_Ctrl2.setStyleSheet(self.Style)
        
        if event.key() == 16777250:
            self.button_Win.setStyleSheet(self.Style)

        if event.key() == 16777251:
            self.button_Alt.setStyleSheet(self.Style)
            self.button_Alt2.setStyleSheet(self.Style)

        return super().keyReleaseEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(1500, 400)
    window.show()
    sys.exit(app.exec_())