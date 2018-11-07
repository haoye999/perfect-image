# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/haoye/Documents/perfect-image/window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 797)
        MainWindow.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(46, 52, 54);\n"
"    font: 11pt \"Ubuntu\";\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(18, 6, 6);\n"
"    color: rgb(186, 189, 182);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 460, 1021, 301))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.style_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.style_layout.setContentsMargins(0, 0, 0, 0)
        self.style_layout.setObjectName("style_layout")
        self.style_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.style_1.setObjectName("style_1")
        self.style_layout.addWidget(self.style_1)
        self.style_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.style_2.setEnabled(True)
        self.style_2.setTextFormat(QtCore.Qt.RichText)
        self.style_2.setObjectName("style_2")
        self.style_layout.addWidget(self.style_2)
        self.style_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.style_3.setText("")
        self.style_3.setTextFormat(QtCore.Qt.PlainText)
        self.style_3.setObjectName("style_3")
        self.style_layout.addWidget(self.style_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 360, 481, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.btns_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.btns_layout.setContentsMargins(30, 0, 30, 0)
        self.btns_layout.setSpacing(50)
        self.btns_layout.setObjectName("btns_layout")
        self.btn_select_content = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_select_content.setObjectName("btn_select_content")
        self.btns_layout.addWidget(self.btn_select_content)
        self.btn_get_foreground = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_get_foreground.setObjectName("btn_get_foreground")
        self.btns_layout.addWidget(self.btn_get_foreground)
        self.btn_foreground_view = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_foreground_view.setObjectName("btn_foreground_view")
        self.btns_layout.addWidget(self.btn_foreground_view)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(600, 40, 481, 301))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.output_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.output_layout.setContentsMargins(0, 0, 0, 0)
        self.output_layout.setObjectName("output_layout")
        self.output_img_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.output_img_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.output_img_label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.output_img_label.setText("")
        self.output_img_label.setTextFormat(QtCore.Qt.AutoText)
        self.output_img_label.setScaledContents(False)
        self.output_img_label.setWordWrap(False)
        self.output_img_label.setOpenExternalLinks(False)
        self.output_img_label.setObjectName("output_img_label")
        self.output_layout.addWidget(self.output_img_label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 481, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.content_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")
        self.content_img_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.content_img_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.content_img_label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.content_img_label.setText("")
        self.content_img_label.setTextFormat(QtCore.Qt.AutoText)
        self.content_img_label.setScaledContents(False)
        self.content_img_label.setWordWrap(False)
        self.content_img_label.setOpenExternalLinks(False)
        self.content_img_label.setObjectName("content_img_label")
        self.content_layout.addWidget(self.content_img_label)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(600, 360, 481, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.btns_layout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.btns_layout_2.setContentsMargins(30, 0, 30, 0)
        self.btns_layout_2.setSpacing(50)
        self.btns_layout_2.setObjectName("btns_layout_2")
        self.btn_args = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_args.setObjectName("btn_args")
        self.btns_layout_2.addWidget(self.btn_args)
        self.btn_style_transfer = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_style_transfer.setObjectName("btn_style_transfer")
        self.btns_layout_2.addWidget(self.btn_style_transfer)
        self.btn_progress = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_progress.setObjectName("btn_progress")
        self.btns_layout_2.addWidget(self.btn_progress)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.style_1.setText(_translate("MainWindow", "TextLabel"))
        self.style_2.setText(_translate("MainWindow", "TextLabel"))
        self.btn_select_content.setText(_translate("MainWindow", "选择"))
        self.btn_get_foreground.setText(_translate("MainWindow", "前景"))
        self.btn_foreground_view.setText(_translate("MainWindow", "查看"))
        self.btn_args.setText(_translate("MainWindow", "参数"))
        self.btn_style_transfer.setText(_translate("MainWindow", "生成"))
        self.btn_progress.setText(_translate("MainWindow", "进度"))

