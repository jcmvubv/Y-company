from email.mime import image
import pygame
import pymunk
import pymunk.pygame_util
import math
pygame.init()
SCREEN_WIDTH = 1200 
SCREEN_HEIGHT = 640 
BOTTOM_PANEL = 50 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + BOTTOM_PANEL))
pygame.display.set_caption("Pool Game yousef ayman")
clock = pygame.time.Clock()
FPS = 120
BG = (50,50,50)

dia = 36
shoot = True
force = 0
power = False

pock = 66
pott = []

cue_image = pygame.image.load('assets/images/cue.png').convert_alpha()
t_image = pygame.image.load('assets/images/table.png').convert_alpha()
balls_imgs = []
for imo in range(1,17):
    ball_img = pygame.image.load(f'assets/images/ball_{imo}.png').convert_alpha()
    balls_imgs.append(ball_img)

space = pymunk.Space()
#space.gravity = (0,500)
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(screen)
def create_ball(radius,pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = 5
    shape.elasticity = 0.8 
    move = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    move.max_bias = 0 
    move.max_force = 1000 
    space.add(body,shape,move)
    return shape

balls = [] 
rows = 5 
for col in range(5): 
    for row in range(rows):
        pos = (250 + (col * (dia + 1)), 267 + (row * (dia + 1)) + (col * dia / 2) )
        new_ball = create_ball(dia / 2, pos )
        balls.append(new_ball)
    rows -= 1
pos = (888,SCREEN_HEIGHT / 2)
new1_ball = create_ball(dia /2 ,pos)
balls.append(new1_ball)

pockets = [
  (55, 63),
  (592, 48),
  (1134, 64),
  (55, 616),
  (592, 629),
  (1134, 616)
]

borders = [
  [(88, 56), (109, 77), (555, 77), (564, 56)],
  [(621, 56), (630, 77), (1081, 77), (1102, 56)],
  [(89, 621), (110, 600),(556, 600), (564, 621)],
  [(622, 621), (630, 600), (1081, 600), (1102, 621)],
  [(56, 96), (77, 117), (77, 560), (56, 581)],
  [(1143, 96), (1122, 117), (1122, 560), (1143, 581)]
]
def create_border(poly_d):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position=((0,0))
    shape = pymunk.Poly(body, poly_d)
    shape.elasticity = 0.8 
    space.add(body,shape)
for b in borders:
    create_border(b)

class Cue():
    def __init__(self, pos):
        self.original_image = cue_image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect  = self.image.get_rect()
        self.rect.center = pos
    def update(self, angle):
        self.angle = angle

    def draw(self, surface):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        surface.blit(self.image, 
                     (
                    self.rect.centerx - self.image.get_width() / 2,
                    self.rect.centery - self.image.get_height() / 2
                     )
                     )
cue = Cue(balls[-1].body.position)        

run = True
while run:
    screen.fill(BG)
    screen.blit(t_image, (0,0))

    shoot = True
    for ball in balls:
        if int(ball.body.velocity[0]) != 0 or int(ball.body.velocity[1]) != 0:
            shoot = False

    if shoot == True:
        mouse_pos = pygame.mouse.get_pos()
        cue.rect.center = balls[-1].body.position
        x_dist = balls[-1].body.position[0] - mouse_pos[0]
        y_dist = -(balls[-1].body.position[1] - mouse_pos[1])
        cue_angle = math.degrees(math.atan2(y_dist,x_dist))
        cue.update(cue_angle)
        cue.draw(screen)
    if power == True :
        force += 100
    if power == False and shoot == True :
        x_impulse = math.cos(math.radians(cue_angle))
        y_impulse = math.sin(math.radians(cue_angle))
        balls[-1].body.apply_impulse_at_local_point((force * - x_impulse,force * y_impulse),(0,0))
    
    for i, ball in enumerate(balls):
        for pocket in pockets:
            ball_x_dist = abs(ball.body.position[0]- pocket[0])
            ball_y_dist = abs(ball.body.position[1]- pocket[1])
            ball_dist = math.sqrt((ball_x_dist ** 2) + (ball_y_dist ** 2))
            if ball_dist <= pock / 2 :
                if i == len(balls) -1 :
                    cue_ball_potted = True
                    ball.body.position = (-100,-100)
                    ball.body.velocity = (0.0 , 0.0)
                else:
                    space.remove(ball.body)
                    balls.remove(ball)
                    pott.append(balls_imgs[i])
                    balls_imgs.pop(i)
    
    for i, imo in enumerate(balls):
        screen.blit(balls_imgs[i], (imo.body.position[0]- imo.radius, imo.body.position[1]- imo.radius))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and shoot == True :
            power = True
        if event.type == pygame.MOUSEBUTTONUP and shoot == True :
            power = False
            x_impulse = math.cos(math.radians(cue_angle))
            y_impulse = math.sin(math.radians(cue_angle))
            balls[-1].body.apply_impulse_at_local_point((force * - x_impulse,force * y_impulse),(0,0))
            force = 0 

        if event.type == pygame.QUIT:
            run = False
    clock.tick(FPS)
    space.step(1 / FPS)
    #space.debug_draw(draw_options)
    pygame.display.update()
pygame.quit()