#Node stores the values for each grid square
class Node:
	def __init__(self, posX, posY):
		self.posX = posX
		self.posY = posY
		self.passable = True
		self.gScore = 0
		self.hScore = 0
		self.fScore = 0
		self.parent = None
		self.neighbors = []
		self.start = False
		self.target = False