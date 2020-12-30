"""
UI | Pathfinding Visualizer
"""
import pygame

blue  = (100,100,255)
darkBlue = (30,30,60)



class button():
    def __init__(self, position, width, height, text=''):
        self.color = '#7E85B1'
        self.x = position[0]
        self.y = position[1]
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont('comicsans', 30)

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),border_radius=5)
        
        if self.text != '':
            font = self.font
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False