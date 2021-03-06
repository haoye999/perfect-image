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
        MainWindow.resize(1141, 882)
        MainWindow.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(60, 59, 55);\n"
"    color: rgb(186, 189, 182);\n"
"    font: 11pt \"Ubuntu\";\n"
"}\n"
"QPushButton\n"
"{\n"
"    alternate-background-color: rgb(60, 59, 55);\n"
"    background-color: rgb(79, 75, 75);\n"
"}\n"
"QLabel#lbl_content_img, QLabel#lbl_output_img, QLabel#lbl_progress_img\n"
"{\n"
"    font: 57 42pt \"Ubuntu\";\n"
"    color: rgb(233, 185, 110);\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"\n"
"QSlider\n"
"{\n"
"    selection-background-color: rgb(233, 185, 110);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    color: rgb(245, 226, 143);\n"
"}\n"
"QProgressBar\n"
"{\n"
"    font: 57 italic 13pt \"Ubuntu\";\n"
"    color: rgb(206, 92, 0);\n"
"    selection-background-color: rgb(233, 185, 110);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 390, 1021, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.btns_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.btns_layout.setContentsMargins(90, 0, 90, 0)
        self.btns_layout.setSpacing(100)
        self.btns_layout.setObjectName("btns_layout")
        self.btn_select_content = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_select_content.setObjectName("btn_select_content")
        self.btns_layout.addWidget(self.btn_select_content)
        self.btn_get_foreground = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_get_foreground.setObjectName("btn_get_foreground")
        self.btns_layout.addWidget(self.btn_get_foreground)
        self.btn_mixup = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_mixup.setObjectName("btn_mixup")
        self.btns_layout.addWidget(self.btn_mixup)
        self.btn_foreground_view = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_foreground_view.setObjectName("btn_foreground_view")
        self.btns_layout.addWidget(self.btn_foreground_view)
        self.btn_style_transfer = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_style_transfer.setObjectName("btn_style_transfer")
        self.btns_layout.addWidget(self.btn_style_transfer)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(600, 40, 481, 301))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.output_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.output_layout.setContentsMargins(0, 0, 0, 0)
        self.output_layout.setObjectName("output_layout")
        self.lbl_output_img = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lbl_output_img.setSizeIncrement(QtCore.QSize(0, 0))
        self.lbl_output_img.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lbl_output_img.setText("")
        self.lbl_output_img.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_output_img.setScaledContents(False)
        self.lbl_output_img.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_output_img.setWordWrap(False)
        self.lbl_output_img.setOpenExternalLinks(False)
        self.lbl_output_img.setObjectName("lbl_output_img")
        self.output_layout.addWidget(self.lbl_output_img)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 481, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.content_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")
        self.lbl_content_img = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_content_img.setSizeIncrement(QtCore.QSize(0, 0))
        self.lbl_content_img.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lbl_content_img.setText("")
        self.lbl_content_img.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_content_img.setScaledContents(False)
        self.lbl_content_img.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_content_img.setWordWrap(False)
        self.lbl_content_img.setOpenExternalLinks(False)
        self.lbl_content_img.setObjectName("lbl_content_img")
        self.content_layout.addWidget(self.lbl_content_img)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 490, 1021, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_style = QtWidgets.QWidget()
        self.tab_style.setObjectName("tab_style")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_style)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 1021, 321))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.style_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.style_layout.setContentsMargins(30, 20, 30, 20)
        self.style_layout.setSpacing(50)
        self.style_layout.setObjectName("style_layout")
        self.frame_style_1 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame_style_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_style_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_style_1.setObjectName("frame_style_1")
        self.lbl_style_1 = QtWidgets.QLabel(self.frame_style_1)
        self.lbl_style_1.setGeometry(QtCore.QRect(18, 20, 251, 181))
        self.lbl_style_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_style_1.setObjectName("lbl_style_1")
        self.radioButton_style_1 = QtWidgets.QRadioButton(self.frame_style_1)
        self.radioButton_style_1.setGeometry(QtCore.QRect(140, 240, 92, 23))
        self.radioButton_style_1.setStyleSheet("")
        self.radioButton_style_1.setText("")
        self.radioButton_style_1.setObjectName("radioButton_style_1")
        self.style_layout.addWidget(self.frame_style_1)
        self.frame_style_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame_style_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_style_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_style_2.setObjectName("frame_style_2")
        self.lbl_style_2 = QtWidgets.QLabel(self.frame_style_2)
        self.lbl_style_2.setGeometry(QtCore.QRect(18, 20, 251, 181))
        self.lbl_style_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_style_2.setObjectName("lbl_style_2")
        self.radioButton_style_2 = QtWidgets.QRadioButton(self.frame_style_2)
        self.radioButton_style_2.setGeometry(QtCore.QRect(140, 240, 92, 23))
        self.radioButton_style_2.setText("")
        self.radioButton_style_2.setObjectName("radioButton_style_2")
        self.style_layout.addWidget(self.frame_style_2)
        self.frame_style_3 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame_style_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_style_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_style_3.setObjectName("frame_style_3")
        self.lbl_style_3 = QtWidgets.QLabel(self.frame_style_3)
        self.lbl_style_3.setGeometry(QtCore.QRect(18, 20, 251, 181))
        self.lbl_style_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_style_3.setObjectName("lbl_style_3")
        self.radioButton_style_3 = QtWidgets.QRadioButton(self.frame_style_3)
        self.radioButton_style_3.setGeometry(QtCore.QRect(140, 240, 92, 23))
        self.radioButton_style_3.setText("")
        self.radioButton_style_3.setObjectName("radioButton_style_3")
        self.style_layout.addWidget(self.frame_style_3)
        self.tabWidget.addTab(self.tab_style, "")
        self.tab_args = QtWidgets.QWidget()
        self.tab_args.setObjectName("tab_args")
        self.slider_iterations = QtWidgets.QSlider(self.tab_args)
        self.slider_iterations.setGeometry(QtCore.QRect(230, 60, 561, 20))
        self.slider_iterations.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.slider_iterations.setStyleSheet("")
        self.slider_iterations.setMaximum(2000)
        self.slider_iterations.setProperty("value", 1000)
        self.slider_iterations.setOrientation(QtCore.Qt.Horizontal)
        self.slider_iterations.setObjectName("slider_iterations")
        self.label = QtWidgets.QLabel(self.tab_args)
        self.label.setGeometry(QtCore.QRect(130, 60, 67, 17))
        self.label.setObjectName("label")
        self.lbl_iterations = QtWidgets.QLabel(self.tab_args)
        self.lbl_iterations.setGeometry(QtCore.QRect(840, 60, 67, 17))
        self.lbl_iterations.setObjectName("lbl_iterations")
        self.label_5 = QtWidgets.QLabel(self.tab_args)
        self.label_5.setGeometry(QtCore.QRect(130, 160, 67, 17))
        self.label_5.setObjectName("label_5")
        self.lbl_content_weight = QtWidgets.QLabel(self.tab_args)
        self.lbl_content_weight.setGeometry(QtCore.QRect(840, 160, 67, 17))
        self.lbl_content_weight.setObjectName("lbl_content_weight")
        self.slider_content_weight = QtWidgets.QSlider(self.tab_args)
        self.slider_content_weight.setGeometry(QtCore.QRect(230, 160, 561, 20))
        self.slider_content_weight.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.slider_content_weight.setStyleSheet("")
        self.slider_content_weight.setMaximum(10000)
        self.slider_content_weight.setSingleStep(1)
        self.slider_content_weight.setPageStep(100)
        self.slider_content_weight.setProperty("value", 1000)
        self.slider_content_weight.setOrientation(QtCore.Qt.Horizontal)
        self.slider_content_weight.setObjectName("slider_content_weight")
        self.label_7 = QtWidgets.QLabel(self.tab_args)
        self.label_7.setGeometry(QtCore.QRect(130, 260, 67, 17))
        self.label_7.setObjectName("label_7")
        self.lbl_style_weight = QtWidgets.QLabel(self.tab_args)
        self.lbl_style_weight.setGeometry(QtCore.QRect(840, 260, 67, 17))
        self.lbl_style_weight.setObjectName("lbl_style_weight")
        self.slider_style_weight = QtWidgets.QSlider(self.tab_args)
        self.slider_style_weight.setGeometry(QtCore.QRect(230, 260, 561, 20))
        self.slider_style_weight.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.slider_style_weight.setStyleSheet("")
        self.slider_style_weight.setMaximum(100)
        self.slider_style_weight.setProperty("value", 10)
        self.slider_style_weight.setOrientation(QtCore.Qt.Horizontal)
        self.slider_style_weight.setObjectName("slider_style_weight")
        self.tabWidget.addTab(self.tab_args, "")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 360, 41, 21))
        self.label_4.setObjectName("label_4")
        self.progressBar_transfer = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_transfer.setGeometry(QtCore.QRect(150, 360, 841, 23))
        self.progressBar_transfer.setProperty("value", 0)
        self.progressBar_transfer.setObjectName("progressBar_transfer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_select_content.setText(_translate("MainWindow", "选择图片"))
        self.btn_get_foreground.setText(_translate("MainWindow", "提取前景"))
        self.btn_mixup.setText(_translate("MainWindow", "融合图片"))
        self.btn_foreground_view.setText(_translate("MainWindow", "查看前景"))
        self.btn_style_transfer.setText(_translate("MainWindow", "生成"))
        self.lbl_style_1.setText(_translate("MainWindow", "style_img1"))
        self.lbl_style_2.setText(_translate("MainWindow", "style_img2"))
        self.lbl_style_3.setText(_translate("MainWindow", "style_img3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_style), _translate("MainWindow", "选择风格/框架"))
        self.label.setText(_translate("MainWindow", "迭代次数："))
        self.lbl_iterations.setText(_translate("MainWindow", "1000"))
        self.label_5.setText(_translate("MainWindow", "内容权重："))
        self.lbl_content_weight.setText(_translate("MainWindow", "1e3"))
        self.label_7.setText(_translate("MainWindow", "风格权重："))
        self.lbl_style_weight.setText(_translate("MainWindow", "1e-2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_args), _translate("MainWindow", "参数"))
        self.label_4.setText(_translate("MainWindow", "进度："))

