#Pathfinding Visualization
 
You can run the standalone run.exe file in the Bin folder to run the program.

Otherwise you will need Pygame installed to run the script since it is a dependancy. 

Command to install pygame: pip install pygame

Run Main.py

A grid of squares should apear.

Controls:
LMB: Place walls
RMB: Delete walls
Q: Place the start point
W: Place the end point
Space: Toggle Early Termination on and off.(this stops the algorithm once the targetnode is found)

Once you place the start and end node the grid should now show as a heatmap. The heatmap represents the score(if you're familiar with A*) of each node. The A* pathfinding alogrithm is a popular method for finding the shortest path from two points. If you look at the RZU-7 project you can see it also implemented in game form where the AI is capable of traversing its environment based on nodes and decision trees.


Variables:
In Main.py you can tweak the following variables
mapX and mapY: controls quantity of nodes, mapX=horizontal mapY=vertical
nodeSiz: the displayed size of each node
STRENGTH: this is a constant that i'm using to manipulate how and when the gradient of color changes.
COLOR1-15: these are the colors in the color gradient. I could have tweened between two colors but for simplicity I found a visualy apealing color gradient and used those two colors.
