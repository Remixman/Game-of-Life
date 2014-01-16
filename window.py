#!/usr/bin/python

import sys
import time
from random import random
from PySide.QtCore import *
from PySide.QtGui import *

class GameOfLifeWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)

		self.setWindowTitle("Conway's Game of Life")
		self.setMinimumSize(QSize(800, 600))

		self.numrow = 50
		self.numcol = 70

		self.matrix = [[0 for i in xrange(self.numcol)] for i in xrange(self.numrow)]
		self.init_matrix(0.3)

	def paintEvent(self, event):
		painter = QPainter(self)

		numrow = self.numrow
		numcol = self.numcol
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

		mat = self.matrix
		for i in range(numrow):
			for j in range(numcol):
				if mat[i][j] == 1:
					x1 = x_offset + (j * cellsize) + 1
					y1 = y_offset + (i * cellsize) + 1
					w = cellsize - 1
					h = cellsize - 1
					painter.fillRect(x1, y1, w, h, Qt.green)

	def run(self):
		self.show()

		while True:
			self.update()
			QApplication.processEvents()
			self.get_next_state_matrix()
			time.sleep(0.2)

	def init_matrix(self, born_prob):
		mat = self.matrix
		for i in range(self.numrow):
			for j in range(self.numcol):
				if random() <= born_prob:
					mat[i][j] = 1

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

	def get_next_state_matrix(self):
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

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = GameOfLifeWindow()
	main_window.run()
	sys.exit(app.exec_())