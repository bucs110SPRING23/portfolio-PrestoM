class Rectangle:
    def __init__(self, x, y, h, w):
        """
        Initializes the rectangle object
        args:
            - self (obj)
            - x (int); x coordinate of rectangle
            - y (int); y coordinate of rectangle
            - h (int); height of rectangle
            - w (int); width of rectangle
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w) 

    def __str__(self):
        """
        returns a string of rectangle information
        args:
            - self (obj)
        return: 
            returns a string contaning the coordinates, width and heigh of the rectangle 
        """
        return f"(x : {self.x}, y : {self.y}) width: {self.width}, height: {self.height}"