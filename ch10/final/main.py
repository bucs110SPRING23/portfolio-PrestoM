import pygame
from src import controller

def main():
    pygame.init()
    control = controller.Controller()
    control.mainloop()

if __name__ == "__main__":
    main()
