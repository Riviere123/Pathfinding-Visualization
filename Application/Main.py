import pygame
import Map
import math

#Initialize Pygame
pygame.init()

#Map Variables
mapX, mapY = 45, 20
nodeSize = 40 #size to display for each node
diaganolMovement = False #Allows you to make diaganol moves on the map when set to true
targetNode = None
startNode = None


#Creates screen Space
FPS = 60
WIDTH, HEIGHT = mapX * nodeSize, mapY * nodeSize
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #this is a surface
WHITE = (255,255,255)
GREY = (190,190,190)
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255,128,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (102,0,204)

##GRADIENT COLORS
STRENGTH = 2.5
COLOR1 = (250, 110, 110)
COLOR2 = (239, 101, 114)
COLOR3 = (227, 93, 117)
COLOR4 = (214, 86, 120)
COLOR5 = (200, 80, 122)
COLOR6 = (185, 75, 123)
COLOR7 = (170, 70, 123)
COLOR8 = (155, 67, 122)
COLOR9 = (139, 63, 120)
COLOR10 = (122, 60, 117)
COLOR11 = (106, 57, 113)
COLOR12 = (90, 53, 108)
COLOR13 = (74, 50, 102)
COLOR14 = (59, 46, 96)
COLOR15 = (43, 42, 88)


#Window Title
pygame.display.set_caption("Pathfinding")

#Our draw function
def draw_window():
    screen.fill(GREY)
    node_display()
    pygame.display.update()

#Draws the path and nodes to the screen
def node_display():
    count = 0
    for node in Map.grid:
        if node.passable == True:
            if node.fScore/STRENGTH == 0:
                pygame.draw.rect(screen,WHITE,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 5:
                pygame.draw.rect(screen,COLOR1,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 10:
                pygame.draw.rect(screen,COLOR2,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 15:
                pygame.draw.rect(screen,COLOR3,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 20:
                pygame.draw.rect(screen,COLOR4,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 25:
                pygame.draw.rect(screen,COLOR5,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 30:
                pygame.draw.rect(screen,COLOR6,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 35:
                pygame.draw.rect(screen,COLOR7,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes
            elif node.fScore/STRENGTH <= 40:
                pygame.draw.rect(screen,COLOR8,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes 
            elif node.fScore/STRENGTH <= 45:
                pygame.draw.rect(screen,COLOR9,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes 
            elif node.fScore/STRENGTH <= 50:
                pygame.draw.rect(screen,COLOR10,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes 
            elif node.fScore/STRENGTH <= 55:
                pygame.draw.rect(screen,COLOR11,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes 
            elif node.fScore/STRENGTH <= 60:
                pygame.draw.rect(screen,COLOR12,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes 
            elif node.fScore/STRENGTH <= 65:
                pygame.draw.rect(screen,COLOR13,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes 
            elif node.fScore/STRENGTH > 65:
                pygame.draw.rect(screen,COLOR14,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for nodes                                

            pygame.draw.rect(screen,BLACK,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize), 2)#Outline color
        elif node.passable == False:
            pygame.draw.rect(screen,BLACK,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for Wall  
        if node.target == True:
            pygame.draw.rect(screen,GREY,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for Target
        if node.start == True:
            pygame.draw.rect(screen,GREY,pygame.Rect(node.posX * nodeSize, node.posY * nodeSize, nodeSize, nodeSize))#Color for Start


    currentNode = Map.GetTargetNode()
    startNode = Map.GetStartNode()
    while currentNode != startNode and currentNode != None and startNode != None and currentNode.parent:
        pygame.draw.line(screen,WHITE,(currentNode.posX * nodeSize + (nodeSize/2), currentNode.posY * nodeSize + (nodeSize/2)), (currentNode.parent.posX * nodeSize + (nodeSize/2), currentNode.parent.posY * nodeSize + (nodeSize/2)),2)
        currentNode = currentNode.parent  



#Game Loop
def main():
    Map.MapSetup(mapX,mapY,diaganolMovement)
    clock = pygame.time.Clock() #Controls the speed of the while loop
    running = True
    while running:
        clock.tick(FPS) #Sets the speed of the clock(FPS)
        
        for event in pygame.event.get(): #Iterates through all possible events(Controls go here)
            if event.type == pygame.QUIT: #if the event type quit is exectured.
                running = False #break the game runnning loop
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                mouseX = math.ceil(pos[0]/nodeSize)-1
                mouseY = math.ceil(pos[1]/nodeSize)-1
                #print(f"{math.ceil(pos[0]/nodeSize)-1},{math.ceil(pos[1]/nodeSize)-1}") #prints node the mouse is over.
                for node in Map.grid:
                    if node.posX == mouseX and node.posY == mouseY:
                        node.passable = False
            if event.type == pygame.MOUSEBUTTONUP:
                Map.FindPath()
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                mouseX = math.ceil(pos[0]/nodeSize)-1
                mouseY = math.ceil(pos[1]/nodeSize)-1
                #print(f"{math.ceil(pos[0]/nodeSize)-1},{math.ceil(pos[1]/nodeSize)-1}") #prints node the mouse is over.
                for node in Map.grid:
                    if node.posX == mouseX and node.posY == mouseY:
                        node.passable = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: #Q key event
                    pos = pygame.mouse.get_pos()
                    mouseX = math.ceil(pos[0]/nodeSize)-1
                    mouseY = math.ceil(pos[1]/nodeSize)-1
                    for node in Map.grid:
                        node.start = False
                        if node.posX == mouseX and node.posY == mouseY and node.target == False:
                            node.start = True
                    Map.FindPath()
                if event.key == pygame.K_w: #W key event
                    pos = pygame.mouse.get_pos()
                    mouseX = math.ceil(pos[0]/nodeSize)-1
                    mouseY = math.ceil(pos[1]/nodeSize)-1
                    for node in Map.grid:
                        node.target = False
                        if node.posX == mouseX and node.posY == mouseY and node.start == False:
                            node.target = True
                    Map.FindPath() 
                if event.key == pygame.K_SPACE: #Space Key Event
                    Map.earlyBreak = not Map.earlyBreak
                    Map.FindPath()
        draw_window() #Method that is drawing the objects to the screen
    pygame.quit()

if __name__ == "__main__":
    main()