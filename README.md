# Pathfinding Visualization
You can launch Run.exe in Bin to run a standalone copy of the python script. <br>
This will allow you to avoid installing pygame and running it from main.py
<br>
<br>
Otherwise you will need Pygame installed to run the script since it is a dependancy. 
Command to install pygame: pip install pygame
Run Main.py
A grid of squares should apear.

Controls:<br>
LMB: Place walls<br>
RMB: Delete walls<br>
Q: Place the start point<br>
W: Place the end point<br>
SpaceBar: Toggles early break (if enabled the algorithm will break as soon as the path has been found.)<br>
<br>
Once you place the start and end node the grid should now show as a heatmap. The heatmap represents the score(if you're familiar with A*) of each node. The A* pathfinding alogrithm is a popular method for finding the shortest path from two points. If you look at the RZU-7 project you can see it also implemented in game form where the AI is capable of traversing its environment based on nodes and decision trees.


Variables:
In Main.py you can tweak the following variables<br>
mapX and mapY: controls quantity of nodes, mapX=horizontal mapY=vertical<br>
nodeSiz: the displayed size of each node<br>
STRENGTH: this is a constant that i'm using to manipulate how and when the gradient of color changes.<br>
COLOR1-15: these are the colors in the color gradient. I could have tweened between two colors but for simplicity I found a visualy apealing color gradient and used those two colors.
