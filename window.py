#!/usr/bin/python

import sys
import time
from random import random
from PySide.QtCore import *
from PySide.QtGui import *

class Board:
	def __init__(self, born_prob):
		self.numrow = 50
		self.numcol = 70

		self.matrix = [[0 for i in xrange(self.numcol)] for i in xrange(self.numrow)]
		self.init_matrix(born_prob)

	def init_matrix(self, born_prob):
		mat = self.matrix
		for i in range(self.numrow):
			for j in range(self.numcol):
				if random() <= born_prob:
					mat[i][j] = 1
				else:
					mat[i][j] = 0

	def init_pattern(self, pattern):
		mat = self.matrix
		for r in range(self.numrow):
			for c in range(self.numcol):
				mat[r][c] = 0

		""" Get from http://www.youtube.com/watch?v=9kIgfBsjMuQ """
		if pattern == "cauldron":
			mat[20][30:41] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
			mat[21][30:41] = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
			mat[22][30:41] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
			mat[23][30:41] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[24][30:41] = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0]
			mat[25][30:41] = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]
			mat[26][30:41] = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
			mat[27][30:41] = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
			mat[28][30:41] = [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]
			mat[29][30:41] = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
			mat[30][30:41] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[31][30:41] = [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
			mat[32][30:41] = [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0]
		elif pattern == "roteightor":
			mat[20][28:42] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[21][28:42] = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
			mat[22][28:42] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
			mat[23][28:42] = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
			mat[24][28:42] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
			mat[25][28:42] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[26][28:42] = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
			mat[27][28:42] = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
			mat[28][28:42] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[29][28:42] = [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
			mat[30][28:42] = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
			mat[31][28:42] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
			mat[32][28:42] = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
			mat[33][28:42] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
		elif pattern == "superstring":
			mat[16][12:57] = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[17][12:57] = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
			mat[18][12:57] = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
			mat[19][12:57] = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
			mat[20][12:57] = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[21][12:57] = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[22][12:57] = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[23][12:57] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[24][12:57] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[25][12:57] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[26][12:57] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[27][12:57] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[28][12:57] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[29][12:57] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[30][12:57] = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[31][12:57] = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[32][12:57] = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			mat[33][12:57] = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
			mat[34][12:57] = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
			mat[35][12:57] = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
			mat[36][12:57] = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			

	def get_neighbour_number(self, row, col):
		neighbour_count = 0
		mat = self.matrix
		numrow = self.numrow
		numcol = self.numcol

		if row > 0 and col > 0:
			neighbour_count += mat[row-1][col-1]
		if row > 0:
			neighbour_count += mat[row-1][col]
		if row > 0 and col < numcol-1:
			neighbour_count += mat[row-1][col+1]
		if col > 0:
			neighbour_count += mat[row][col-1]
		if col < numcol-1:
			neighbour_count += mat[row][col+1]
		if row < numrow-1 and col > 0:
			neighbour_count += mat[row+1][col-1]
		if row < numrow-1:
			neighbour_count += mat[row+1][col]
		if row < numrow-1 and col < numcol-1:
			neighbour_count += mat[row+1][col+1]

		return neighbour_count

	def next_state_matrix(self):
		new_matrix = [[0 for i in xrange(self.numcol)] for i in xrange(self.numrow)]
		mat = self.matrix
		for r in range(self.numrow):
			for c in range(self.numcol):
				neighbour_num = self.get_neighbour_number(r, c)

				if mat[r][c] == 1 and (neighbour_num < 2 or neighbour_num > 3):
					new_matrix[r][c] = 0
				elif mat[r][c] == 1:
					new_matrix[r][c] = 1
				elif mat[r][c] == 0 and neighbour_num == 3:
					new_matrix[r][c] = 1
				else:
					new_matrix[r][c] = 0

		self.matrix = new_matrix

	def get_numrow(self):
		return self.numrow

	def get_numcol(self):
		return self.numcol

	def get_matrix(self):
		return self.matrix

class BoardWidget(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		self.initUI()

	def initUI(self):
		self.setMinimumSize(722, 522)

	def updateBoard(self, board):
		self.board = board

	def paintEvent(self, event):
		painter = QPainter(self)

		board = self.board

		numrow = board.get_numrow()
		numcol = board.get_numcol()
		cellsize = self.cellsize = 10
		x_offset = 10
		y_offset = 10

		horizon_line_size = numcol * cellsize
		vertical_line_size = numrow * cellsize

		painter.setPen(QPen(QColor(Qt.black), 1))

		for i in range(numrow+1):
			x1 = x_offset
			y1 = y_offset + (i * cellsize)
			x2 = x1 + horizon_line_size
			y2 = y1
			painter.drawLine(x1, y1, x2, y2)

		for i in range(numcol+1):
			x1 = x_offset + (i * cellsize)
			y1 = y_offset
			x2 = x1
			y2 = y1 + vertical_line_size
			painter.drawLine(x1, y1, x2, y2)

		mat = board.get_matrix()
		for i in range(numrow):
			for j in range(numcol):
				if mat[i][j] == 1:
					x1 = x_offset + (j * cellsize) + 1
					y1 = y_offset + (i * cellsize) + 1
					w = cellsize - 1
					h = cellsize - 1
					painter.fillRect(x1, y1, w, h, Qt.green)

class GameOfLifeWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)

		self.prob = 0.3
		self.active = False
		self.board = Board(self.prob)

		self.initUI()

		self.board_widget.updateBoard(self.board)
		self.board_widget.repaint()
		self.board_widget.setFocus()

	def initUI(self):
		self.setWindowTitle("Conway's Game of Life")
		self.setMinimumSize(QSize(850, 580))

		# Show update timer
		self.update_timer = QTimer(self)
		self.update_timer.timeout.connect(self.updateAction)

		# Show statusbar
		self.statusBar().showMessage("Ready")

		# Show board
		self.board_widget = BoardWidget(self)
		self.board_widget.show()

		# Show run button
		self.active_bttn = QPushButton("Run", self)
		self.active_bttn.setCheckable(True)
		self.active_bttn.move(724, 10)
		palette = QPalette(self.active_bttn.palette())
		palette.setColor(QPalette.Button, QColor('green'))
		self.active_bttn.setPalette(palette)
		self.active_bttn.clicked[bool].connect(self.activeAction)

		# Show reset button
		self.reset_bttn = QPushButton("Reset", self)
		self.reset_bttn.move(724, 50)
		self.reset_bttn.clicked[bool].connect(self.resetAction)

		self.prob_label = QLabel("Live Prob.", self)
		self.prob_label.move(724, 80)

		self.prob_box = QLineEdit(self)
		self.prob_box.move(724, 110)
		self.prob_box.setText(str(self.prob))
		self.prob_box.textChanged[str].connect(self.probBoxAction)

		self.speed_label = QLabel("Speed", self)
		self.speed_label.move(724, 140)

		self.speed_combo = QComboBox(self)
		self.speed_map = {
			1 : 1,
			2 : 0.5,
			3 : 0.3,
			4 : 0.2,
			5 : 0.1,
			6 : 0.05,
			7 : 0.02,
		}
		for i in self.speed_map.keys():
			self.speed_combo.addItem(str(i))
		self.speed_combo.move(724, 170)
		self.speed_combo.activated[str].connect(self.selectSpeedAction)

		default_speed = 4
		self.speed_combo.setCurrentIndex(default_speed-1)
		self.update_timer.start(self.speed_map[default_speed] * 1000)

		self.next_bttn = QPushButton("Next", self)
		self.next_bttn.move(724, 200)
		self.next_bttn.clicked[bool].connect(self.nextAction)

		self.pattern_label = QLabel("Select Pattern", self)
		self.pattern_label.move(10, 522)

		self.pattern_combo = QComboBox(self)
		self.pattern_combo.addItem("cauldron")
		self.pattern_combo.addItem("roteightor")
		self.pattern_combo.addItem("superstring")
		self.pattern_combo.move(120, 522)
		self.pattern_combo.activated[str].connect(self.selectPatternAction)

		self.show()

	def keyPressEvent(self, event):
		key = event.key()

		if key == Qt.Key_R:
			self.active = not self.active

	def activeAction(self, pressed):
		palette = QPalette(self.active_bttn.palette())
		if pressed:
			self.active = True
			palette.setColor(QPalette.Button, QColor('red'))
			self.statusBar().showMessage("Running")
		else:
			self.active = False
			palette.setColor(QPalette.Button, QColor('green'))
			self.statusBar().showMessage("Ready")
		self.active_bttn.setPalette(palette)

	def selectSpeedAction(self, text):
		interval = self.speed_map[int(text)] * 1000
		self.update_timer.setInterval(interval)

	def selectPatternAction(self, text):
		self.board.init_pattern(text)
		self.board_widget.updateBoard(self.board)
		self.board_widget.repaint()

	def resetAction(self, event):
		self.board.init_matrix(self.prob)
		self.board_widget.updateBoard(self.board)
		self.board_widget.repaint()

	def probBoxAction(self, text):
		self.prob = float(text)

	def nextAction(self, event):
		self.board.next_state_matrix()
		self.board_widget.updateBoard(self.board)
		self.board_widget.repaint()

	def updateAction(self):
		#QApplication.processEvents()
		if self.active:
			self.update()
			self.board.next_state_matrix()
			self.board_widget.updateBoard(self.board)
			self.board_widget.repaint()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = GameOfLifeWindow()
	sys.exit(app.exec_())
