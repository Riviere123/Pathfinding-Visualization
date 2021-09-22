from Node import Node
grid = []
earlyBreak = False #if True stops scoring nodes as soon as the target is found.

#Sets the nodes neighbors
def SetNeighbors(grid, diagonals):
	for node in grid:
		for next_node in grid:
			if node == next_node:
				continue
			if(node.posX == next_node.posX):
				if(node.posY - next_node.posY == 1): #North
					node.neighbors.append(next_node)
					continue
				if(node.posY - next_node.posY == -1): #South
					node.neighbors.append(next_node)
					continue
			if(node.posY == next_node.posY):
				if(node.posX - next_node.posX == 1): #West
					node.neighbors.append(next_node)
					continue
				if(node.posX - next_node.posX == -1): #East
					node.neighbors.append(next_node)
					continue
			if diagonals:
				if(node.posX - next_node.posX == 1):
					if(node.posY - next_node.posY == 1): #North West
						node.neighbors.append(next_node)
						continue
					if(node.posY - next_node.posY == -1): #South West
						node.neighbors.append(next_node)
						continue
				if(node.posX - next_node.posX == -1):
					if(node.posY - next_node.posY == 1): #North East
						node.neighbors.append(next_node)
						continue
					if(node.posY - next_node.posY == -1): #South East
						node.neighbors.append(next_node)
						continue

#Generates the Nodes to fill all x and y values.
def CreateMap(width,height): 
	for x in range(0,width):
		for y in range(0,height):
			grid.append(Node(x,y))

#returns the manhatten distance from node to target
def ManhattenDistance(node,target): 
	h = abs(node.posX - target.posX) + abs(node.posY - target.posY)
	return h

#Calls clear nodes then sets the map scores and parents accordingly.
def FindPath():
	ClearNodes()
	Target = None
	Start = None
	for node in grid: #Sets the start and target nodes
		if node.start == True:
			Start = node
		if node.target == True:
			Target = node
	if Target == None or Start == None: #If their is no start or target node we return out of the method.
		return "no target node or no start node"
	openlist=[]
	closedlist=[]
	openlist.append(Start)
	while openlist:
		selected = openlist[0]
		for node in openlist: #Get the lowest fScore node in the list
			if selected.fScore > node.fScore:
				selected = node
		openlist.remove(selected)
		closedlist.append(selected)
		if selected == Target and earlyBreak:
			break
		for neighbor in selected.neighbors: #Cycle through the current nodes neighbors
			if neighbor in closedlist or neighbor.passable == False: #If it's in the closed list or is obstructed we continue onto next neighbor
				continue
			if neighbor not in openlist: #If it's not in the open list it has not been checked, we add it to the open list and asign its scores.
				openlist.append(neighbor)
				neighbor.parent = selected
				neighbor.gScore = selected.gScore + 1
				neighbor.hScore = ManhattenDistance(neighbor,Target)
				neighbor.fScore = neighbor.gScore + neighbor.hScore
			elif neighbor in openlist: #If the neighbor has a score we check if moving from current node yields a better score. If it does we change the scores and parent
				gScore = selected.gScore + 1
				hScore = ManhattenDistance(neighbor,Target)
				fScore = gScore + hScore
				if neighbor.fScore > fScore:
					neighbor.parent = selected
					neighbor.gScore = selected.gScore + 1
					neighbor.hScore = ManhattenDistance(neighbor,Target)
					neighbor.fScore = neighbor.gScore + neighbor.hScore
	if Target in closedlist: #if the target is in the closed list
		print("Path Found")
		return True
	else:
		print("No Path Found")
		return False

#calls create map and setneighbors method in order to get the map ready for use.
def MapSetup(x,y,diagonals): 
	CreateMap(x,y)
	SetNeighbors(grid,diagonals)

#Returns the node that has the target value set to true.
def GetTargetNode(): 
	for node in grid:
		if node.target == True:
			return node

#Returns the node that has the start value set to true.
def GetStartNode(): 
	for node in grid:
		if node.start == True:
			return node

#Clears the nodes parent and scores
def ClearNodes(): 
	for node in grid:
		node.gScore = 0
		node.hScore = 0
		node.fScore = 0
		node.parent = None