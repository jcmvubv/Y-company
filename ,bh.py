import pygame
import numpy

# Class for location of icons
class IconLocation(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, icon):
        super().__init__()
        #self.image = pygame.image.load("Assets/"+icon+".png")
        #self.rect = self.image.get_rect()
        #self.rect.x = pos_x
        #self.rect.y = pos_y
    def set_image(self, image):
        self.image = image

def start():
    global total_coins
    # Generate three random icon
    rand_icons = numpy.random.choice(icons, 3, p=icons_proba)
    # Draw the random icons on the correct location
    loc_left.set_image(icon_dict[rand_icons[0]])
    loc_middle.set_image(icon_dict[rand_icons[1]])
    loc_right.set_image(icon_dict[rand_icons[2]])

    # Reward if there are three identical icons
    if rand_icons[0] == rand_icons[1] == rand_icons[2]:
        # Get reward from a dict
        coins = icon_reward_dict[rand_icons[0]]
        total_coins += coins

# Setup the window
pygame.init()
width = 700
height = 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Slot Machine Game ")
logo = pygame.image.load('assets/jackpot.png')
pygame.display.set_icon(logo)
white = [250, 250, 250]
screen.fill(white)

# Load background image
background = pygame.image.load('assets/jackpot.png')
police_total_coins = pygame.font.SysFont("Comic Sans MS", 50)
police_menu = pygame.font.SysFont("Comic Sans MS", 25)

# Load location icons
# No equation to do location ... just try and then adjust it
height_location = height / 2 - 13
Location = pygame.sprite.Group()
loc_left = IconLocation(102, height_location, "instagram")
loc_middle = IconLocation(192, height_location, "twitter")
loc_right = IconLocation(282, height_location, "linkedin")

# Group location
Location.add(loc_left)
Location.add(loc_middle)
Location.add(loc_right)

# Location of icons menu
Location_menu = pygame.sprite.Group()
first_loc = IconLocation(480, 200, "youtube")
second_loc = IconLocation(480, 260, "linkedin")
third_loc = IconLocation(480, 330, "facebook")
fourth_loc = IconLocation(480, 400, "instagram")
fifth_loc = IconLocation(480, 466, "twitter")

# Group location_menu
Location_menu.add(first_loc)
Location_menu.add(second_loc)
Location_menu.add(third_loc)
Location_menu.add(fourth_loc)
Location_menu.add(fifth_loc)




# Coins of the player
total_coins = 500

# Stock the social media icons in list
# Youtube = Jacpot +200$ (see later)
icons = ["Facebook", "Instagram", "Twitter", "LinkedIn", "Youtube"]
# Probability of evry icon to appear
icons_proba = [0.2, 0.25, 0.35, 0.15, 0.05]

# Stock on dict every icon with that reward
icon_reward_dict = {
    "Facebook": 25,
    "Instagram": 20,
    "Twitter": 15,
    "LinkedIn": 35,
    "Youtube": 200 # bq youtube = jackpot (but low proba 5%)
}

# Stock every icon associate to a image
icon_dict = {
    "Facebook": pygame.image.load("assets/star.png"),
    "Instagram": pygame.image.load("assets/coin.png"),
    "Twitter": pygame.image.load("assets/money.png"),
    "LinkedIn": pygame.image.load("assets/diamond.png"),
    "Youtube": pygame.image.load("assets/health.gif")
}



# Main loop
run = True
while run:
    screen.fill(white)
    # Draw the bg image
    screen.blit(background, (0, 0))
    # Draw icon image
    Location.draw(screen)
    # Print the coins of the player
    text = police_total_coins.render("Total "+str(total_coins)+"$", True, (0, 0, 0))
    screen.blit(text, (400, 0))
    # Print menu reward for each icon
    yt_menu = police_menu.render("X3  +200$", True, (0, 0, 0))
    screen.blit(yt_menu, (550, 215))
    lk_menu = police_menu.render("X3  +35", True, (0, 0, 0))
    screen.blit(lk_menu, (550, 275))
    fb_menu = police_menu.render("X3  +25", True, (0, 0, 0))
    screen.blit(fb_menu, (550, 345))
    insta_menu = police_menu.render("X3  +20", True, (0, 0, 0))
    screen.blit(insta_menu, (550, 415))
    tw_menu = police_menu.render("X3  +15", True, (0, 0, 0))
    screen.blit(tw_menu, (550, 480))




    # Draw icon image of the menu
    Location_menu.draw(screen)
    # Update screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
        # Chek if key is pressed
        if event.type == pygame.KEYDOWN:
            # 1 click = 1 try ====> -15$
            if total_coins >= 15:
                total_coins -= 15
                start()









