import pygame

class Text:
    def __init__(self, pos=(0,0), font=72, text="TEST", color="red"):
        '''
        The function __init__ for class Text sets the self variables equal to positions, sizes, and fonts, stores x and y variables, and initializes the Font
        args: (tuple) pos - position of the text
              (int) font - fontsize of the text
              (string) text - text to be displayed
              (string) = color of the text
        return: none
        '''
        self.text = text
        self.pos = pos
        self.font = font
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.disp = pygame.font.Font(None, self.font)
        self.font_ = self.disp.render(self.text, True, self.color)
        self.size = self.font_.get_size()


    def set_pos(self, new_pos):
        '''
        The sets a new position for the text
        arg(s): (tuple) new_pos - the new position that text will move to 
        return: none
        '''
        self.pos = new_pos

class Button:
    def __init__(self, x, y, text, w=None, h=None, color="black"):
        '''
        The function __init__ for the class Button is responsible for initializing the variable information from the buttons, such as the x and y coordinates, and the height and width information.
        args: (int) x - x position of the button
              (int) y - y position of the button
              (string) text - text to be displayed on the button
              (int) w - width of the button
              (int) h - height of the button
              (string) color - color of the text on the button
        return: none
        '''
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.txt = text
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render(self.txt, True, color)
        if w == None and h == None:
            self.rect = self.text.get_rect()
            self.w = self.rect.width
            self.h = self.rect.height
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.rect = pygame.Rect(self.x, self.y, w, h)

    def change_pos(self, x, y):
        '''
        The sets a new position for the button
        arg(s): (int) x - the new x position that text will move to 
                (int) y - the new y position that text will move to
        return: none
        '''
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
