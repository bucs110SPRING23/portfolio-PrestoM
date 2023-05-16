import pygame
from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Initializes the Surface Class
        args: 
            - self (obj)
            - filename (str); an image file in the form of a string
            - x (int); x coordinate of rectangle
            - y (int); y coordinate of rectangle
            - h (int); height of rectangle
            - w (int); width of rectangle
        """
        self.image = filename
        self.rect = Rectangle(x, y, h, w)
    
    def getRect(self):
        """
        Returns the rectange object stored in self.rect
        args:
            -self (obj)
        return:
            self.rect (obj); returns the rectangle object initiliazed in the __init__ function 
        """
        return self.rect
