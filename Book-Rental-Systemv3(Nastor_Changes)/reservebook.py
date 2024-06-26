# Form implementation generated from reading ui file 'reservebook.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ReserveDialog(object):
    def setupUi(self, ReserveDialog):
        ReserveDialog.setObjectName("ReserveDialog")
        ReserveDialog.resize(609, 326)
        ReserveDialog.setStyleSheet("background:rgb(72, 72, 72)")
        self.label_5 = QtWidgets.QLabel(parent=ReserveDialog)
        self.label_5.setGeometry(QtCore.QRect(90, 104, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=ReserveDialog)
        self.label_6.setGeometry(QtCore.QRect(40, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=ReserveDialog)
        self.label_7.setGeometry(QtCore.QRect(28, 154, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.bookscbox = QtWidgets.QComboBox(parent=ReserveDialog)
        self.bookscbox.setGeometry(QtCore.QRect(180, 74, 371, 22))
        self.bookscbox.setStyleSheet(" background: white")
        self.bookscbox.setObjectName("bookscbox")
        self.Confirm = QtWidgets.QPushButton(parent=ReserveDialog)
        self.Confirm.setGeometry(QtCore.QRect(70, 260, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Confirm.setFont(font)
        self.Confirm.setStyleSheet("QPushButton {\n"
"                background-color: rgb(6, 217, 66);\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(50, 255, 100);\n"
"            }")
        self.Confirm.setFlat(False)
        self.Confirm.setObjectName("Confirm")
        self.label_4 = QtWidgets.QLabel(parent=ReserveDialog)
        self.label_4.setGeometry(QtCore.QRect(120, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.rentfeefield = QtWidgets.QLineEdit(parent=ReserveDialog)
        self.rentfeefield.setGeometry(QtCore.QRect(180, 205, 371, 22))
        self.rentfeefield.setStyleSheet(" background: white")
        self.rentfeefield.setFrame(False)
        self.rentfeefield.setObjectName("rentfeefield")
        self.startdate = QtWidgets.QPushButton(parent=ReserveDialog)
        self.startdate.setGeometry(QtCore.QRect(180, 150, 371, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.startdate.setFont(font)
        self.startdate.setStyleSheet("QPushButton {\n"
"                background-color: rgb(255, 170, 0);\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(255, 196, 78);\n"
"            }")
        self.startdate.setFlat(False)
        self.startdate.setObjectName("startdate")
        self.Cancel = QtWidgets.QPushButton(parent=ReserveDialog)
        self.Cancel.setGeometry(QtCore.QRect(320, 260, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("QPushButton {\n"
"                background-color: rgb(200, 46, 18);\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(255, 100, 100);\n"
"            }")
        self.Cancel.setObjectName("Cancel")
        self.customercbox = QtWidgets.QComboBox(parent=ReserveDialog)
        self.customercbox.setGeometry(QtCore.QRect(180, 110, 371, 22))
        self.customercbox.setStyleSheet(" background: white")
        self.customercbox.setObjectName("customercbox")
        self.frame = QtWidgets.QFrame(parent=ReserveDialog)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(220, 4, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")

        self.retranslateUi(ReserveDialog)
        QtCore.QMetaObject.connectSlotsByName(ReserveDialog)

    def retranslateUi(self, ReserveDialog):
        _translate = QtCore.QCoreApplication.translate
        ReserveDialog.setWindowTitle(_translate("ReserveDialog", "Reserve Book"))
        self.label_5.setText(_translate("ReserveDialog", "Customer:"))
        self.label_6.setText(_translate("ReserveDialog", "Reservation Fee:"))
        self.label_7.setText(_translate("ReserveDialog", "Reservation Date:"))
        self.Confirm.setText(_translate("ReserveDialog", "Confirm"))
        self.label_4.setText(_translate("ReserveDialog", "Books:"))
        self.startdate.setText(_translate("ReserveDialog", "Date of Reservation"))
        self.Cancel.setText(_translate("ReserveDialog", "Cancel"))
        self.label.setText(_translate("ReserveDialog", "Reserve Book"))
