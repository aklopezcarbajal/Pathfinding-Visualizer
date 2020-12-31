"""
UI | Pathfinding Visualizer
"""
import pygame

#Background
background = '#55708D'

#Buttons
outline_color = '#153C62'
button_color = '#4E6E91'
font_color = '#07111D'

#Grid
unvisited_color = '#A2A6BE'
visited_color = '#373660'
inQueue_color = '#408289'
path_color = '#873E59'
obstacle_color = '#243547'

class button():
    def __init__(self, position, width, height, text=''):
        self.color = button_color
        self.x = position[0]
        self.y = position[1]
        self.width = width
        self.height = height
        self.text = text
        
    def draw(self,win):
        #pygame.draw.rect(win, outline_color, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),border_radius=5)
        
        if self.text != '':
            font = pygame.font.SysFont('arial', 20)
            text = font.render(self.text, 1, font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False