#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import style_transfer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Ui_window import Ui_MainWindow
import matplotlib.pyplot as plt
from foreground import getcutimage
import cv2 as cv
from goalimg import *
import os


class win(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_tab_style()
        self.init_args_imgs()
        self.init_buttons()
        self.init_tab_args()
        self.show()

    def init_buttons(self):
        self.btn_select_content.clicked.connect(
            self.btn_select_content_clicked)
        self.btn_style_transfer.clicked.connect(self.run_style_transfer)
        self.btn_get_foreground.clicked.connect(self.run_get_foreground)
        self.btn_foreground_view.clicked.connect(self.run_foreground_view)
        self.btn_mixup.clicked.connect(self.run_mixup)

    def run_mixup(self):
        rows, cols, channels = self.foreground_img.shape
        bigimg = cv2.resize(
            self.foreground_img, (int(cols*1.4), int(rows*1.4)), cv2.INTER_LINEAR)
        self.foreground_img, self.foreground_img_small = addimage(bigimg, self.style_path, 140, 100, 1)
        self.content_path = str.split(self.content_path, sep='.')[0] + '_foreground_added.jpg'
        self.content_small_path = str.split(self.content_path, sep='.')[0] + '_small_foreground_added.jpg'
        cv.imwrite(self.content_path, self.foreground_img)
        cv.imwrite(self.content_small_path, self.foreground_img_small)
        img = cv.imread(self.content_path, 1)
        cv.imshow('mix image', img)

    def run_foreground_view(self):
        img = cv.imread(self.content_path, 1)
        # print(str.split(self.content_path, sep='.')[0] + '_foreground.jpg')
        cv.imshow('mix image', img)
        # cv.waitKey()

    def run_get_foreground(self):
        self.foreground_img_path = str.split(self.content_path, sep='.')[
            0] + '_foreground.jpg'
        getcutimage(self.content_path)
        self.foreground_img = cv.imread(self.foreground_img_path, 1)
        self.foreground_img = cropimage(self.foreground_img)
        cv.imwrite(self.foreground_img_path, self.foreground_img)


    def init_args_imgs(self):
        self.content_path = 'img/content_img/star/hand.jpg'
        self.style_path = "img/style_img/night.jpg"
        self.output_path = 'img/output_img/output.jpg'
        self.progress_path = str.split(self.content_path, sep='.')[0] + '_iterations_'

        self.num_iterations = 1000
        self.content_weight = 1e4
        self.style_weight = 1e-2

        # self.updataImage(self.content_path, self.lbl_content_img)
        # self.updataImage(self.output_path, self.lbl_output_img)

    def init_tab_args(self):
        def change_iterations_num(value):
            self.lbl_iterations.setText(str(value))
            self.num_iterations = value

        def change_content_weight(value):
            self.lbl_content_weight.setText(str(value))
            self.content_weight = value

        def change_style_weight(value):
            self.lbl_style_weight.setText(str(value / 1000))
            self.style_weight = value / 1000
        self.slider_iterations.valueChanged.connect(change_iterations_num)
        self.slider_content_weight.valueChanged.connect(change_content_weight)
        self.slider_style_weight.valueChanged.connect(change_style_weight)

    def init_tab_style(self):
        self.style1_path = 'img/style_img/The_Great_Wave_off_Kanagawa.jpg'
        self.style2_path = 'img/style_img/night.jpg'
        self.style3_path = 'img/style_img/fire.jpg'

        self.updataImage(self.style1_path, self.lbl_style_1)
        self.updataImage(self.style2_path, self.lbl_style_2)
        self.updataImage(self.style3_path, self.lbl_style_3)

        self.radioButtongroup_style = QButtonGroup(self)
        self.radioButtongroup_style.addButton(self.radioButton_style_1, 1)
        self.radioButtongroup_style.addButton(self.radioButton_style_2, 2)
        self.radioButtongroup_style.addButton(self.radioButton_style_3, 3)
        self.radioButton_style_1.setChecked(True)

        self.lbl_style_1.mouseDoubleClickEvent = self.dc_select_style_1
        self.lbl_style_2.mouseDoubleClickEvent = self.dc_select_style_2
        self.lbl_style_3.mouseDoubleClickEvent = self.dc_select_style_3

    def dc_select_style_1(self, event):
        self.radioButton_style_1.setChecked(True)
        self.style_path = self.style1_path

    def dc_select_style_2(self, event):
        self.radioButton_style_2.setChecked(True)
        self.style_path = self.style2_path

    def dc_select_style_3(self, event):
        self.radioButton_style_3.setChecked(True)
        self.style_path = self.style3_path

    def run_style_transfer(self):
        self.progress_path = str.split(self.content_path, sep='.')[0] + '_progress_iterations_'
        best, best_loss = style_transfer.run_style_transfer(
            self.content_path, self.style_path, self.progress_path, self.progressBar_transfer,
            self.lbl_output_img, num_iterations=self.num_iterations,
            content_weight=self.content_weight, style_weight=self.style_weight)
        plt.imsave(self.output_path, best)
        self.updataImage(self.output_path, self.lbl_output_img)
        self.progressBar_transfer.setValue(100)
        # show_results(best, content_path, style_path)

    def btn_select_content_clicked(self):
        self.content_path = QFileDialog.getOpenFileName(self, "Select content image",
                                                        ".", "Image Files(*.jpg *.jpeg *.png)")[0]
        if len(self.content_path):
            self.updataImage(self.content_path, self.lbl_content_img)

    def updataImage(self, imageName, img_label):
        pixmap = QPixmap(imageName)
        scaredPixmap = pixmap.scaled(
            479, 299, aspectRatioMode=Qt.KeepAspectRatio)
        img_label.setPixmap(scaredPixmap)
        img_label.setAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = win()
    sys.exit(app.exec_())
