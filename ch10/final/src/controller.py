import pygame
import src.cocktail as cocktail
import src.meal as meal
import src.button as button

class Controller:
    def __init__(self):
        '''
        Initializes all necessary info to combine the use of the cocktail recipes and meal recipes apis and display them on a simple pygame gui
        arg(s): none
        return: none
        '''
        pygame.init()
        self.STATE = "GENERATE"
        self.window_w = 800
        self.window_h = 700
        self.display = pygame.display.set_mode((self.window_w, self.window_h))

        self.ing = None
        self.meal, self.selected_meal = None, None
        self.chosen_tail_num = None
        self.tails = []

        self.op_genned = False
        self.meal_chose = False

        self.op1_w, self.op1_h, self.op1_x, self.op1_y, self.op1_button = None, None, None, None, None
        self.op2_w, self.op2_h, self.op2_x, self.op2_y, self.op2_button = None, None, None, None, None
        self.op3_w, self.op3_h, self.op3_x, self.op3_y, self.op3_button = None, None, None, None, None

        self.gen_button_w = 100
        self.gen_button_h = 50
        self.gen_button_x = (self.window_w/2) - (self.gen_button_w/2)
        self.gen_button_y = self.window_h/2
        self.gen_button = button.Button(self.gen_button_x, self.gen_button_y, text="Generate", w=self.gen_button_w, h=self.gen_button_h)
    
    def __str__(self):
        return self.STATE

    def gen_ing(self, chosen_tail):
        '''
        generates an ingredient to be used from the selected cocktail
        arg(s): (cocktail object) chosen_tail - the cocktail object that the user selects in the gui
        return: none
        '''
        chosen_tail.generate_ings()
        chosen_tail.choose_ing()
        self.ing = chosen_tail.ing
    
    def gen_meal(self):
        '''
        initializes variables that contain data for a meal that shares a common ingredient with the selected cocktail
        arg(s): none
        return: none
        '''
        self.meal = meal.Meal(self.ing)
        self.selected_meal = self.meal.get_meal()

    def mainloop(self):
        '''
        where everything comes together (the main gui loop)
        arg(s): none
        return: none
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display.fill("white")
            
            if self.STATE == "GENERATE":
                self.genloop() 
            elif self.STATE == "CHOOSE":
                self.chooseloop()     
            elif self.STATE == "CHOSEN":
                self.chosenloop()          
          
            pygame.display.flip()

    def genloop(self):
        '''
        The main loop for the generation screen (the first gui screen)
        arg(s): none
        return: none
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.gen_button.rect.collidepoint(pygame.mouse.get_pos()) and self.STATE == "GENERATE":
                self.STATE = "CHOOSE"
            
        if self.gen_button.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, "gray", self.gen_button.rect)

        self.display.blit(self.gen_button.text, self.gen_button.rect)

    def gen_options(self):
        '''
        generates 3 cocktail options for the user to select from
        arg(s): none
        return: none
        '''
        self.tails = []
        self.tail1 = cocktail.Cocktail()
        self.tail2 = cocktail.Cocktail()
        self.tail3 = cocktail.Cocktail()
        self.tails.append(self.tail1)
        self.tails.append(self.tail2)
        self.tails.append(self.tail3)

        self.op1_w = 100
        self.op1_h = 50
        self.op1_x = self.window_w/2
        self.op1_y = 150
        self.op1_button = button.Button(self.op1_x, self.op1_y, text=f"{self.tail1.tail_name}")
        self.op1_button.change_pos(self.op1_x - (self.op1_button.w / 2), self.op1_y)

        self.op2_w = 100
        self.op2_h = 50
        self.op2_x = self.window_w/2
        self.op2_y = 300
        self.op2_button = button.Button(self.op2_x, self.op2_y, text=f"{self.tail2.tail_name}")
        self.op2_button.change_pos(self.op2_x - (self.op2_button.w / 2), self.op2_y)

        self.op3_w = 100
        self.op3_h = 50
        self.op3_x = self.window_w/2
        self.op3_y = 450
        self.op3_button = button.Button(self.op3_x, self.op3_y, text=f"{self.tail3.tail_name}")
        self.op3_button.change_pos(self.op3_x - (self.op3_button.w / 2), self.op3_y)

    def chooseloop(self):
        '''
        the main loop for when the user is prompted to choose a cocktail
        arg(s): none
        return: none
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.op1_button.rect.collidepoint(pygame.mouse.get_pos()) and self.STATE == "CHOOSE":
                self.STATE = "CHOSEN"
                self.chosen_tail_num = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and self.op2_button.rect.collidepoint(pygame.mouse.get_pos()) and self.STATE == "CHOOSE":
                self.STATE = "CHOSEN"
                self.chosen_tail_num = 1
            elif event.type == pygame.MOUSEBUTTONDOWN and self.op3_button.rect.collidepoint(pygame.mouse.get_pos()) and self.STATE == "CHOOSE":
                self.STATE = "CHOSEN"
                self.chosen_tail_num = 2
                
        if not self.op_genned:
            self.gen_options()
            self.op_genned = True
    
        if self.op1_button.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, "gray", self.op1_button.rect)
        elif self.op2_button.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, "gray", self.op2_button.rect)
        elif self.op3_button.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, "gray", self.op3_button.rect)

        prompt_x = self.window_w/4
        prompt_y = 50
        prompt = button.Text((prompt_x, prompt_y), color="black", font = 32, text=f"Choose a Cocktail:") 

        self.display.blit(prompt.font_,prompt.pos)
        self.display.blit(self.op1_button.text,self.op1_button.rect)
        self.display.blit(self.op2_button.text,self.op2_button.rect)
        self.display.blit(self.op3_button.text,self.op3_button.rect)
        

    def chosenloop(self):
        '''
        the main loop for when the user chooses a cocktail (for the gui screen matching the chosen cocktail with a meal based on a random common ingredient)
        arg(s): none
        return: none
        '''
        tail = self.tails[self.chosen_tail_num] #chosen cocktail
        if not self.meal_chose:
            self.gen_ing(tail)
            self.gen_meal()
            self.meal_chose = True
        cocktail = button.Text((100, 110), color="black", font = 32, text=f"Cocktail: {tail.tail_name}")
        tick = button.Text((100, 170), color="black", font = 32, text=f"Meal with the same ingredient: {self.selected_meal}")
        ingr = button.Text((100, 230), color="black", font = 32, text=f"Same Ingredient: {self.ing}")


        reroll_w = 100
        reroll_h = 50
        reroll_x = self.window_w/2
        reroll_y = 300
        reroll_button = button.Button(reroll_x, reroll_y, text=f"Look for Another Ingredient")      

        back_w = 100
        back_h = 50
        back_x = self.window_w/4
        back_y = 500
        back_button = button.Button(back_x, back_y, text=f"< Back")  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and reroll_button.rect.collidepoint(pygame.mouse.get_pos()) and self.STATE == "CHOSEN":
                self.meal_chose = False     
            elif event.type == pygame.MOUSEBUTTONDOWN and back_button.rect.collidepoint(pygame.mouse.get_pos()) and self.STATE == "CHOSEN":
                self.STATE = "GENERATE"
                self.op_genned = False

        if reroll_button.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, "gray", reroll_button.rect)
        
        if back_button.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, "gray", back_button.rect)

        self.display.blit(cocktail.font_, cocktail.pos)
        self.display.blit(tick.font_, tick.pos)
        self.display.blit(ingr.font_, ingr.pos)
        self.display.blit(reroll_button.text, reroll_button.rect)
        self.display.blit(back_button.text, back_button.rect)