#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import core.style_transfer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui.Ui_window import Ui_MainWindow

class win(Ui_MainWindow, QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn_select_content.clicked.connect(self.btn_select_content_clicked)
		self.btn_style_transfer.clicked.connect(self.run_style_transfer)
		self.show()

	def run_style_transfer(self):
		content_path = self.content_img_name
		style_path = 'img/style_img/The_Great_Wave_off_Kanagawa.jpg'
		output_path = 'img/output_img/face2_output.jpg'
		progress_path = 'img/output_img/output_pro/' + 'face2_output_iterations_'
		
		best, best_loss = style_transfer.run_style_transfer(
			content_path, style_path, progress_path, num_iterations=1000, content_weight=1e4, style_weight=1e-2)
		plt.imsave(output_path, best)
		show_results(best, content_path, style_path)

	def btn_select_content_clicked(self):
		self.content_img_name = QFileDialog.getOpenFileName(self, "Select content image",
			".", "Image Files(*.jpg *.jpeg *.png)")[0]
		if len(self.content_img_name):
			self.updataImage(self.content_img_name, self.content_img_label)

	def updataImage(self, imageName, img_label):
		pixmap = QPixmap(imageName)
		scaredPixmap = pixmap.scaled(479, 299, aspectRatioMode=Qt.KeepAspectRatio)
		img_label.setPixmap(scaredPixmap)
		img_label.setAlignment(Qt.AlignCenter)
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = win()
	sys.exit(app.exec_())