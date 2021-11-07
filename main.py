import pygame
import math

clicked = False
value = 1

pygame.init()
dtheta = math.pi / 6
ratio = 0.75 #branch length ratio
branch_width = 15
petal_width = 4
petal_radius = 15
petal_ratio = 0.5
color = ([[110, 60, 59], [73, 117, 66], [229, 106, 179]])
color_array = ([120, 78, 45], [138, 89, 55], [157, 99, 66], [175, 110, 76],
               [26, 136, 40], [66, 155, 70], [100, 173, 98],
               [249, 163, 203], [252, 188, 215], [255, 206, 230])
init = False
spinval = 1
font = pygame.font.SysFont('Constantia', 15)

class spinBox:
    font = pygame.font.Font(None, 20)

    def __init__(self, position):
        self.rect = pygame.Rect(position, (20, 20))
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((255,255,255))

    def draw(self, surface):
        # global value
        global spinval
        global clicked

        #Draw SpinBox onto surface
        textline = spinBox.font.render(str(spinval), True, (0, 0, 0))

        self.image.fill((255,255,255))

        # init increment & decrement button
        incr = button(90, 7, '+')
        decr = button(120, 7, '-')

        # adding logic to on button press event (increase/decrease, recalculate height, redraw tree, refresh)
        if incr.draw_button():
            print('Up')
            spinval += 1
            if spinval > 10:
                spinval = 10
            screen.fill((255, 255, 255))
            R = get_height(spinval)
            len = 600 / R
            init_component3(screen, WIDTH / 2, HEIGHT, len, math.pi / 2, 1)
            pygame.display.update()

        if decr.draw_button():
            print('Down')
            spinval -= 1
            if spinval < 1:
                spinval = 1
            screen.fill((255, 255, 255))
            R = get_height(spinval)
            len = 600 / R
            init_component3(screen, WIDTH / 2, HEIGHT, len, math.pi / 2, 1)
            pygame.display.update()

        self.image.blit(textline, (5, (self.rect.height - textline.get_height()) // 2))
        surface.blit(self.image, self.rect)

class button():
    # colours for button and text
    button_col = (220,220,220)
    hover_col = (220,220,220)
    click_col = (220,220,220)
    text_col = (0, 0, 0)
    width = 30
    height = 20

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        screen.blit(text_img, (self.x + 13, self.y + 3))
        return action

def init_component3(screen, x, y, height, theta, level):
    xx = int(spinval)
    if level == xx + 1: # break recursive when recursive level > spinbox value
        return 0

    # odd even level equation for branch len
    if (level % 2 == 0 and level < 8):
        len = math.sqrt((4/3) * math.pow(height,2))
    else:
        len = height

    # print(f'level {level}, len {len}, height {height}')

    # # coloring component based on length
    # if len >= 60:
    #     component_color = color[0]
    # elif len < 60 and level <= 7:
    #     component_color = color[1]
    # else:
    #     component_color = color[2]

    if (level >= 1 and level <= 7):
        x2 = x - int(len * math.cos(theta))
        y2 = y - int(len * math.sin(theta))
        pygame.draw.lines(screen, color_array[level-1], True, ((x, y), (x2, y2)), branch_width - (2 * (level - 1)))
        init_component3(screen, x2, y2, height * ratio, theta - dtheta, level+1)
        init_component3(screen, x2, y2, height * ratio, theta + dtheta, level+1)

    elif (level >= 8 and level <= 10):
        pygame.draw.circle(screen, color_array[level-1], (x, y), (petal_radius / math.pow(2, (level % 8))), petal_width - (1 * (level % 8)))
        for i in range(1,7):
            x2 = x - int((petal_radius/math.pow(2, (level % 8))) * math.cos(math.pi/3 * i))
            y2 = y - int((petal_radius/math.pow(2, (level % 8))) * math.sin(math.pi/3 * i))
            init_component3(screen, x2, y2, petal_radius, theta, level+1)

def get_height(level):
    if level > 1 and level < 8:
        R = get_height(level-1) + math.pow(ratio, level-1)
    elif level >= 8:
        R = get_height(level - 1)
    elif level == 1 or level == 0:
        R = 1
    return R


WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen.fill((255, 255, 255))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render("Level ", 1, (0, 0, 0))
    screen.blit(label, (10, 11))

    # create new spinBox instance called *spinBox1*
    spinBox1 = spinBox((60, 10))
    spinBox1.draw(screen)


    R = get_height(spinval)

    if spinval >= 1:
         len = 600 / R

    init_component3(screen, WIDTH / 2, HEIGHT, len, math.pi / 2, 1)

    pygame.display.update()
    pygame.display.flip()
pygame.quit()


