##
# @file gui.py
# @brief calculator graphic user interface
# @author Jakub Kontrík <xkontr020@vutbr.cz>


from PyQt5 import QtCore, QtGui, QtWidgets
from math_lib_interface import MathLibInterface
_Interface = MathLibInterface()

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(425, 625)
        Calculator.setMinimumSize(QtCore.QSize(425, 625))
        self.Calculator=Calculator
        Calculator.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Calculator.setStyleSheet("QMainWindow{\n"
"    background-color: #333333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Front = QtWidgets.QGridLayout()
        self.Front.setHorizontalSpacing(0)
        self.Front.setVerticalSpacing(1)
        self.Front.setObjectName("Front")
        self.HelpB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpB.sizePolicy().hasHeightForWidth())
        self.HelpB.setSizePolicy(sizePolicy)
        self.HelpB.setStyleSheet("QPushButton{\n"
"    background-color: #333333;\n"
"    border: 2px solid #333333;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #404040;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"\n"
"")
        self.HelpB.setObjectName("HelpB")
        self.Front.addWidget(self.HelpB, 0, 1, 1, 1)
        self.Keyboard = QtWidgets.QGridLayout()
        self.Keyboard.setContentsMargins(-1, 10, -1, -1)
        self.Keyboard.setSpacing(3)
        self.Keyboard.setObjectName("Keyboard")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button8.sizePolicy().hasHeightForWidth())
        self.Button8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button8.setFont(font)
        self.Button8.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button8.setDefault(False)
        self.Button8.setObjectName("Button8")
        self.Keyboard.addWidget(self.Button8, 3, 1, 1, 1)
        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button9.sizePolicy().hasHeightForWidth())
        self.Button9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button9.setFont(font)
        self.Button9.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button9.setObjectName("Button9")
        self.Keyboard.addWidget(self.Button9, 3, 2, 1, 1)
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button3.sizePolicy().hasHeightForWidth())
        self.Button3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button3.setFont(font)
        self.Button3.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button3.setObjectName("Button3")
        self.Keyboard.addWidget(self.Button3, 5, 2, 1, 1)
        self.AddB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddB.sizePolicy().hasHeightForWidth())
        self.AddB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.AddB.setFont(font)
        self.AddB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.AddB.setObjectName("AddB")
        self.Keyboard.addWidget(self.AddB, 5, 3, 1, 1)
        self.PointB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointB.sizePolicy().hasHeightForWidth())
        self.PointB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.PointB.setFont(font)
        self.PointB.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.PointB.setObjectName("PointB")
        self.Keyboard.addWidget(self.PointB, 6, 0, 1, 1)
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button6.sizePolicy().hasHeightForWidth())
        self.Button6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button6.setFont(font)
        self.Button6.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button6.setIconSize(QtCore.QSize(16, 16))
        self.Button6.setObjectName("Button6")
        self.Keyboard.addWidget(self.Button6, 4, 2, 1, 1)
        self.ModuloB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModuloB.sizePolicy().hasHeightForWidth())
        self.ModuloB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ModuloB.setFont(font)
        self.ModuloB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.ModuloB.setObjectName("ModuloB")
        self.Keyboard.addWidget(self.ModuloB, 0, 0, 1, 1)
        self.DeleteB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteB.sizePolicy().hasHeightForWidth())
        self.DeleteB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.DeleteB.setFont(font)
        self.DeleteB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.DeleteB.setObjectName("DeleteB")
        self.Keyboard.addWidget(self.DeleteB, 0, 2, 1, 2)
        self.ClearAllB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearAllB.sizePolicy().hasHeightForWidth())
        self.ClearAllB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ClearAllB.setFont(font)
        self.ClearAllB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.ClearAllB.setObjectName("ClearAllB")
        self.Keyboard.addWidget(self.ClearAllB, 0, 1, 1, 1)
        self.Button0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button0.sizePolicy().hasHeightForWidth())
        self.Button0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button0.setFont(font)
        self.Button0.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button0.setObjectName("Button0")
        self.Keyboard.addWidget(self.Button0, 6, 1, 1, 1)
        self.PowerB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PowerB.sizePolicy().hasHeightForWidth())
        self.PowerB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.PowerB.setFont(font)
        self.PowerB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.PowerB.setObjectName("PowerB")
        self.Keyboard.addWidget(self.PowerB, 1, 1, 1, 1)
        self.RootB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RootB.sizePolicy().hasHeightForWidth())
        self.RootB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.RootB.setFont(font)
        self.RootB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.RootB.setObjectName("RootB")
        self.Keyboard.addWidget(self.RootB, 1, 2, 1, 1)
        self.DivideB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DivideB.sizePolicy().hasHeightForWidth())
        self.DivideB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.DivideB.setFont(font)
        self.DivideB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.DivideB.setObjectName("DivideB")
        self.Keyboard.addWidget(self.DivideB, 1, 3, 1, 1)
        self.MultiplyB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MultiplyB.sizePolicy().hasHeightForWidth())
        self.MultiplyB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.MultiplyB.setFont(font)
        self.MultiplyB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.MultiplyB.setObjectName("MultiplyB")
        self.Keyboard.addWidget(self.MultiplyB, 3, 3, 1, 1)
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button2.setFont(font)
        self.Button2.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button2.setObjectName("Button2")
        self.Keyboard.addWidget(self.Button2, 5, 1, 1, 1)
        self.EqualityB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EqualityB.sizePolicy().hasHeightForWidth())
        self.EqualityB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.EqualityB.setFont(font)
        self.EqualityB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.EqualityB.setObjectName("EqualityB")
        self.Keyboard.addWidget(self.EqualityB, 6, 2, 1, 2)
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button4.sizePolicy().hasHeightForWidth())
        self.Button4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button4.setFont(font)
        self.Button4.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button4.setObjectName("Button4")
        self.Keyboard.addWidget(self.Button4, 4, 1, 1, 1)
        self.SubB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubB.sizePolicy().hasHeightForWidth())
        self.SubB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.SubB.setFont(font)
        self.SubB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.SubB.setObjectName("SubB")
        self.Keyboard.addWidget(self.SubB, 4, 3, 1, 1)
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button7.sizePolicy().hasHeightForWidth())
        self.Button7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button7.setFont(font)
        self.Button7.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button7.setObjectName("Button7")
        self.Keyboard.addWidget(self.Button7, 3, 0, 1, 1)
        self.FactB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FactB.sizePolicy().hasHeightForWidth())
        self.FactB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.FactB.setFont(font)
        self.FactB.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color: #933cab;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #a446be;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ae59c5;\n"
"}\n"
"")
        self.FactB.setObjectName("FactB")
        self.Keyboard.addWidget(self.FactB, 1, 0, 1, 1)
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button5.sizePolicy().hasHeightForWidth())
        self.Button5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button5.setFont(font)
        self.Button5.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button5.setObjectName("Button5")
        self.Keyboard.addWidget(self.Button5, 4, 0, 1, 1)
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button1.setFont(font)
        self.Button1.setStyleSheet("QPushButton{\n"
"    background-color: #878787;\n"
"    border: 2px solid #8c8c8c;\n"
"    border-radius: 28px;\n"
"    padding: 6px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #999999;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6a6a6;\n"
"}\n"
"\n"
"")
        self.Button1.setObjectName("Button1")
        self.Keyboard.addWidget(self.Button1, 5, 0, 1, 1)
        self.Front.addLayout(self.Keyboard, 2, 1, 1, 2)
        self.Display = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display.sizePolicy().hasHeightForWidth())
        self.Display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Display.setFont(font)
        self.Display.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Display.setStyleSheet("QLineEdit{\n"
"    background-color: #d9d9d9;\n"
"}\n"
"")
        self.Display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Display.setReadOnly(True)
        self.Display.setObjectName("Display")
        self.Front.addWidget(self.Display, 1, 1, 1, 2)
        self.Display.setText("0")
        self.Front.setColumnStretch(1, 3)
        self.Front.setColumnStretch(2, 20)
        self.Front.setRowStretch(1, 6)
        self.Front.setRowStretch(2, 18)
        self.gridLayout.addLayout(self.Front, 0, 0, 1, 1)
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 22))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)

        self.retranslateUi(Calculator)
        self.Button0.clicked.connect(self.numPressed)
        self.Button1.clicked.connect(self.numPressed)
        self.Button2.clicked.connect(self.numPressed)
        self.Button3.clicked.connect(self.numPressed)
        self.Button4.clicked.connect(self.numPressed)
        self.Button5.clicked.connect(self.numPressed)
        self.FactB.clicked.connect(self.funcPressed)
        self.ModuloB.clicked.connect(self.funcPressed)
        self.MultiplyB.clicked.connect(self.funcPressed)
        self.PointB.clicked.connect(self.funcPressed)
        self.EqualityB.clicked.connect(self.eqPressed)
        self.DivideB.clicked.connect(self.funcPressed)
        self.DeleteB.clicked.connect(self.removePressed)
        self.ClearAllB.clicked.connect(self.removePressed)
        self.Button9.clicked.connect(self.numPressed)
        self.AddB.clicked.connect(self.funcPressed)
        self.Button8.clicked.connect(self.numPressed)
        self.Button7.clicked.connect(self.numPressed)
        self.Button6.clicked.connect(self.numPressed)
        self.PowerB.clicked.connect(self.funcPressed)
        self.RootB.clicked.connect(self.funcPressed)
        self.SubB.clicked.connect(self.funcPressed)
        self.HelpB.clicked.connect(self.helpBPressed)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        helpIcon = QtGui.QPixmap("dependencies/help_icon.svg")
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.HelpB.setIcon(QtGui.QIcon(helpIcon))
        self.HelpB.setIconSize(QtCore.QSize(24, 24))
        self.Button8.setText(_translate("Calculator", "8"))
        self.Button8.setShortcut(_translate("Calculator", "8"))
        self.Button9.setText(_translate("Calculator", "9"))
        self.Button9.setShortcut(_translate("Calculator", "9"))
        self.Button3.setText(_translate("Calculator", "3"))
        self.Button3.setShortcut(_translate("Calculator", "3"))
        self.AddB.setText(_translate("Calculator", "+"))
        self.AddB.setShortcut(_translate("Calculator", "+"))
        self.PointB.setText(_translate("Calculator", "."))
        self.PointB.setShortcut(_translate("Calculator", "."))
        self.Button6.setText(_translate("Calculator", "6"))
        self.Button6.setShortcut(_translate("Calculator", "6"))
        self.ModuloB.setText(_translate("Calculator", "%"))
        self.ModuloB.setShortcut(_translate("Calculator", "%"))
        self.DeleteB.setText(_translate("Calculator", "DEL"))
        self.DeleteB.setShortcut(_translate("Calculator", "Backspace"))
        self.ClearAllB.setText(_translate("Calculator", "C"))
        self.ClearAllB.setShortcut(_translate("Calculator", "Del"))
        self.Button0.setText(_translate("Calculator", "0"))
        self.Button0.setShortcut(_translate("Calculator", "0"))
        self.PowerB.setText(_translate("Calculator", "^"))
        self.PowerB.setShortcut(_translate("Calculator", "^"))
        self.RootB.setText(_translate("Calculator", "√"))
        self.DivideB.setText(_translate("Calculator", "/"))
        self.DivideB.setShortcut(_translate("Calculator", "/"))
        self.MultiplyB.setText(_translate("Calculator", "*"))
        self.MultiplyB.setShortcut(_translate("Calculator", "*"))
        self.Button2.setText(_translate("Calculator", "2"))
        self.Button2.setShortcut(_translate("Calculator", "2"))
        self.EqualityB.setText(_translate("Calculator", "="))
        self.EqualityB.setShortcut(_translate("Calculator", "Return"))
        self.Button4.setText(_translate("Calculator", "5"))
        self.Button4.setShortcut(_translate("Calculator", "5"))
        self.SubB.setText(_translate("Calculator", "-"))
        self.SubB.setShortcut(_translate("Calculator", "-"))
        self.Button7.setText(_translate("Calculator", "7"))
        self.Button7.setShortcut(_translate("Calculator", "7"))
        self.FactB.setText(_translate("Calculator", "!"))
        self.FactB.setShortcut(_translate("Calculator", "!"))
        self.Button5.setText(_translate("Calculator", "4"))
        self.Button5.setShortcut(_translate("Calculator", "4"))
        self.Button1.setText(_translate("Calculator", "1"))
        self.Button1.setShortcut(_translate("Calculator", "1"))

    def numPressed(self):
        global lastBut
        butVal = self.Calculator.sender()
        displayVal = self.Display.text()
        if(displayVal == "0" or lastBut == self.EqualityB.text()):
            self.Display.setText(butVal.text())
        else:
            self.Display.setText(displayVal+butVal.text())
        lastBut = butVal


    def removePressed(self):
        global pointButPressed
        global lastBut
        butPressed = self.Calculator.sender().text()
        if (self.Display.text()[-1]=="."):
            pointButPressed=False
        if (butPressed == self.DeleteB.text()):
            ui.Display.setText(ui.Display.text()[:-1])
        if (butPressed == self.ClearAllB.text() or self.Display.text()==""):
            pointButPressed = False
            self.Display.setText("0")
        lastBut = ui.Display.text()[-1]

    def funcPressed(self):
        global lastBut
        global pointButPressed
        functionButtons = [self.MultiplyB.text(), self.DivideB.text(), self.AddB.text(), self.SubB.text(),
                         self.PowerB.text(), self.FactB.text(), self.RootB.text(), self.ModuloB.text()]
        butVal = self.Calculator.sender().text()
        if (butVal == self.SubB.text()):
            if (self.Display.text()=="0"):
                self.Display.setText(butVal)
                return
            self.Display.setText(ui.Display.text()+butVal)
            lastBut = butVal
            return
        if (lastBut == self.SubB.text()):
            return

        if (butVal != self.PointB.text()):
            pointButPressed = False
        elif (butVal == self.PointB.text()):
            if (pointButPressed or lastBut in functionButtons):
                return
            pointButPressed = True
        if (self.Display.text()[-1]==self.PointB.text()):
            pass
        elif (lastBut in functionButtons):
                if (butVal != self.PointB.text()):
                    self.Display.setText(self.Display.text()[:-1]+butVal)
                else:
                    pointButPressed = False
                    return
        elif (lastBut == self.PointB.text()):
            return
        else:
            self.Display.setText(ui.Display.text()+butVal)
        lastBut = butVal

    def eqPressed(self):
        global lastBut
        global pointButPressed
        pointButPressed = False
        try:
            result = str(_Interface.calc_expression(self.Display.text().replace("√", "~")))
            self.Display.setText(result)
        except ZeroDivisionError:
            self.Display.setText("MathError!")
        except ValueError:
            self.Display.setText("MathError!")
        except SyntaxError:
            self.Display.setText("SyntaxError!")
        for i in self.Display.text():
            if i == self.PointB.text():
                pointButPressed = True

        lastBut = self.Calculator.sender().text()
    def helpBPressed(self):
        import webbrowser
        path = 'help.pdf'
        webbrowser.open_new(path)






if __name__ == "__main__":
    import sys
    global pointButPressed
    global lastBut
    lastBut = 0
    pointButPressed = False
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
