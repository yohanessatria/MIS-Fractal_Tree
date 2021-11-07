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
# spinval = value
spinval = 1
font = pygame.font.SysFont('Constantia', 15)

class spinBox:
    font = pygame.font.Font(None, 20)

    def __init__(self, position):
        self.rect = pygame.Rect(position, (20, 20))
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((255,255,255))

        # self.buttonRects = [pygame.Rect(50,5,30,20),
        #                      pygame.Rect(85,5,30,20)]


    def draw(self, surface):
        # global value
        global spinval
        global clicked
        #Draw SpinBox onto surface
        # textline = spinBox.font.render(str(value), True, (255,255,255))
        textline = spinBox.font.render(str(spinval), True, (0, 0, 0))

        self.image.fill((255,255,255))

        #increment button
        # pygame.draw.rect(self.image, (255,255,255), self.buttonRects[0])
        # pygame.draw.polygon(self.image, (0,0,0), [(55,20), (65,8), (75,20)])
        incr = button(90, 7, '+')
        #decrement button
        # pygame.draw.rect(self.image, (255,255,255), self.buttonRects[1])
        # pygame.draw.polygon(self.image, (0,0,0), [(90,8), (100,20), (110,8)])
        decr = button(120, 7, '-')

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

        # pos = pygame.mouse.get_pos()
        # if self.rect.collidepoint(pos):
        #     # print(pygame.mouse.get_pressed()[0])
        #     if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        #         clicked = True
        #         # value += 1
        #         # print(value)
        #         spinval += 1
        #         print(spinval)
        #         screen.fill((255, 255, 255))
        #         R = get_height(spinval)
        #         len = 600 / R
        #         init_component3(screen, WIDTH / 2, HEIGHT, len, math.pi / 2, 1)
        #         pygame.display.update()


        # if pygame.mouse.get_pressed()[0] == 0:
        #     clicked = False
        #
        self.image.blit(textline, (5, (self.rect.height - textline.get_height()) // 2))

        surface.blit(self.image, self.rect)
#
#     def increment(self):
#         spinval += 1
#
#     def decrement(self):
#         spinval -= 1
#
#     # def __call__(self, position):
#     #     #enumerate through all button rects
#     #     for idx, btnR in enumerate(self.buttonRects):
#     #         #create a new pygame rect with absolute screen position
#     #         btnRect = pygame.Rect((btnR.topleft[0] + self.rect.topleft[0],
#     #                                btnR.topleft[1] + self.rect.topleft[1]), btnR.size)
#     #
#     #         if btnRect.collidepoint(position):
#     #             if idx == 0:
#     #                 self.increment()
#     #             else:
#     #                 self.decrement()


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
        # text_len = text_img.get_width()
        screen.blit(text_img, (self.x + 13, self.y + 3))
        return action
#
# def init_component(screen, x, y, len, theta, level):
#     color = ([[103, 52, 0], [131, 66, 0], [150, 75, 0], [164, 85, 10],
#               [77, 140, 45], [101, 160, 71], [121, 176, 101],
#               [249, 163, 203], [252, 188, 215], [255, 206, 230]])
#
#     if (level <=0):
#         x2 = int(x - len * math.cos(theta))
#         y2 = int(y - len * math.sin(theta))
#         print(f'level = {level} || {x2}, {y2}')
#         pygame.draw.lines(screen, color[level], True, ((x, y), (x2, y2)), branch_width - (2 * (level - 1)))
#         init_component(screen, x2, y2, len * ratio, theta - dtheta, level+1)
#         init_component(screen, x2, y2, len * ratio, theta + dtheta, level+1)
#
#     elif (level >= 7 and level <= 9):
#         pygame.draw.circle(screen, color[level], (x, y), (petal_radius/math.pow(2, (level % 7))), petal_width - (level % 7))
#         for i in range(1,7):
#             x2 = int(x - len/2 * math.cos(math.pi/3 * i))
#             y2 = int(y - len/2 * math.sin(math.pi/3 * i))
#             init_component(screen, x2, y2, petal_radius, theta, level+1)
#
# def init_component2(screen, x, y, len, theta, level):
#
#     if level == 0:
#         #clear canvas
#         pass
#
#     elif level == 1:
#         x2 = int(x - len * math.cos(theta))
#         y2 = int(y - len * math.sin(theta))
#         print(f'level = {level} || {x}, {y} || {x2}, {y2}')
#         pygame.draw.lines(screen, color[level], True, ((x, y), (x2, y2)), branch_width - (2 * (level - 1)))
#
#     elif level >= 2 and level < 8:
#         x2 = int(x - len * math.cos(theta))
#         y2 = int(y - len * math.sin(theta))
#         init_component2(screen, )
#         # pygame.draw.lines(screen, color[level], True, ((x, y), (x2, y2)), branch_width - (2 * (level - 1)))
#         # init_component(screen, x2, y2, len * ratio, theta - dtheta, level-1)
#         # init_component(screen, x2, y2, len * ratio, theta + dtheta, level-1)
#
#     elif level >= 8 and level <= 10:
#         pygame.draw.circle(screen, color[level], (x, y), (petal_radius / math.pow(2, (level % 7))),
#                            petal_width - (level % 7))
#         for i in range(1,7):
#             x2 = int(x - len/2 * math.cos(math.pi/3 * i))
#             y2 = int(y - len/2 * math.sin(math.pi/3 * i))
#             init_component(screen, x2, y2, petal_radius, theta, level+1)
#
#     # if (level <=6):
#     #     x2 = int(x - len * math.cos(theta))
#     #     y2 = int(y - len * math.sin(theta))
#     #     # print(f'level = {level} || {x2}, {y2}')
#     #
#     #     pygame.draw.lines(screen, color[level], True, ((x, y), (x2, y2)), branch_width - (2 * (level - 1)))
#     #     init_component(screen, x2, y2, len * ratio, theta - dtheta, level+1)
#     #     init_component(screen, x2, y2, len * ratio, theta + dtheta, level+1)
#     #
#     # elif (level >= 7 and level <= 9):
#     #     pygame.draw.circle(screen, color[level], (x, y), (petal_radius/math.pow(2, (level % 7))), petal_width - (level % 7))
#     #     for i in range(1,7):
#     #         x2 = int(x - len/2 * math.cos(math.pi/3 * i))
#     #         y2 = int(y - len/2 * math.sin(math.pi/3 * i))
#     #         init_component(screen, x2, y2, petal_radius, theta, level+1)
#
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
        # x2 = int(x - len * math.cos(theta))
        # y2 = int(y - len * math.sin(theta))
        x2 = x - int(len * math.cos(theta))
        y2 = y - int(len * math.sin(theta))
        pygame.draw.lines(screen, color_array[level-1], True, ((x, y), (x2, y2)), branch_width - (2 * (level - 1)))
        # pygame.draw.lines(screen, component_color, True, ((x, y), (x2, y2)), branch_width - (2 * (level - 1)))
        # pygame.draw.lines(screen, component_color, True, ((x, y), (x2, y2)), 1)
        init_component3(screen, x2, y2, height * ratio, theta - dtheta, level+1)
        init_component3(screen, x2, y2, height * ratio, theta + dtheta, level+1)

    elif (level >= 8 and level <= 10):
        # print(f'level {level}, radius {petal_radius/math.pow(2, (level % 8))}')
        # print(f'level {level}, {petal_width - (1 * (level%8))}')
        pygame.draw.circle(screen, color_array[level-1], (x, y), (petal_radius / math.pow(2, (level % 8))), petal_width - (1 * (level % 8)))
        # pygame.draw.circle(screen, component_color, (x, y), (petal_radius/math.pow(2, (level % 8))), petal_width - (1 * (level % 8)))
        # pygame.draw.circle(screen, component_color, (x, y), (petal_radius / math.pow(2, (level % 8))), 1)
        for i in range(1,7):
            # x2 = int(x - (petal_radius / math.pow(2, (level % 8))) * math.cos(math.pi / 3 * i))
            # y2 = int(y - (petal_radius / math.pow(2, (level % 8))) * math.sin(math.pi / 3 * i))
            x2 = x - int((petal_radius/math.pow(2, (level % 8))) * math.cos(math.pi/3 * i))
            y2 = y - int((petal_radius/math.pow(2, (level % 8))) * math.sin(math.pi/3 * i))
            # pygame.draw.lines(screen, component_color, True, ((x, y), (x2, y2)), 1)
            # print(f'level {level}, {x}, {y} || {x2}, {y2}')
            init_component3(screen, x2, y2, petal_radius, theta, level+1)

def get_height(level):
    if level > 1 and level < 8:
    # if level > 1:
        R = get_height(level-1) + math.pow(ratio, level-1)
    elif level >= 8:
        R = get_height(level - 1)# + (petal_radius/math.pow(2, (level % 8)))
    elif level == 1 or level == 0:
        R = 1
    # print(R)
    return R

def get_total_petal_rad(level):
    if level == 0:
        return petal_radius / math.pow(2, (level))
    else:
        return get_total_petal_rad(level - 1) + petal_radius / math.pow(2, (level))


WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen.fill((255, 255, 255))

# down = button(75, 350, 'Down')
# up = button(325, 350, 'Up')

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((255, 255, 255))

    # if up.draw_button():
    #     print('Up')
    #     spinval += 1
    # if down.draw_button():
    #     print('Down')
    #     spinval -= 1

    # pygame.draw.rect(screen, [0,0,0], [0, 300, 1200, 600])
    # pygame.draw.line(screen, (0,0,0), (0,HEIGHT-600), (WIDTH,HEIGHT-600), 1)
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render("Level ", 1, (0, 0, 0))
    screen.blit(label, (10, 11))

    # create new spinBox instance called *spinBox1*
    spinBox1 = spinBox((60, 10))
    spinBox1.draw(screen)
    #
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

    # ev = pygame.event.wait()
    #
    # # call spinBox1 if pygame.MOUSEBUTTONDOWN event detected
    # if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
    #     spinBox1(pygame.mouse.get_pos())
    #     spinBox1.draw(screen)

    R = get_height(spinval)
    # if spinval >= 8:
    #     PR = get_total_petal_rad(spinval-8)

    if spinval >= 1: #and spinval <=7:
         len = 600 / R
    # elif spinval > 7:
    #     len = (600 - PR) / (R - PR)

    # if init==False:
    init_component3(screen, WIDTH / 2, HEIGHT, len, math.pi / 2, 1)
        # init = True
    pygame.display.update()


    # pygame.draw.circle(screen, (0, 255, 0), (450, 450), 15, 4)
    # pygame.draw.circle(screen, (255, 0, 0), (435, 450), 7.5, 3)
    # pygame.draw.circle(screen, (255, 0, 0), (450, 435), 7.5, 3)
    # pygame.draw.circle(screen, (0, 0, 0), (465, 450), 7.5, 3)
    # pygame.draw.circle(screen, (0, 0, 0), (450, 465), 7.5, 3)

    # # pygame.draw.circle(screen, (0, 0, 0), (450, 450), 30, 4)
    # pygame.draw.circle(screen, (0,0,0), (450, 450), 15, 4)
    # # pygame.draw.lines(screen, (255,0,0), True, ((450,350),(450,550)), 3)
    # for i in range(1, 7):
    #     x2 = int(450 - (15 * math.cos(math.pi / 3 * i)))
    #     y2 = int(450 - (15 * math.sin(math.pi / 3 * i)))
    #     pygame.draw.circle(screen, (255,0,0), (x2, y2), 7.5, 3)
    # #     # print(f'level {level}, {x}, {y} || {x2}, {y2}')
    #
    # pygame.draw.circle(screen, (249, 163, 203), (550, 550), 15, 4)
    # # pygame.draw.lines(screen, (255,0,0), True, ((450,350),(450,550)), 3)
    # for i in range(1, 7):
    #     x2 = 550 - int((15 * math.cos(math.pi / 3 * i)))
    #     y2 = 550 - int((15 * math.sin(math.pi / 3 * i)))
    #     pygame.draw.circle(screen, (252, 188, 215), (x2, y2), 7.5, 3)
    #     for i in range(1, 7):
    #         x3 = x2 - int((7.5 * math.cos(math.pi / 3 * i)))
    #         y3 = y2 - int((7.5 * math.sin(math.pi / 3 * i)))
    #         pygame.draw.circle(screen, (255, 206, 230), (x3, y3), 3.75, 2)
    # #     # print(f'level {level}, {x}, {y} || {x2}, {y2}')

    pygame.display.update()
    pygame.display.flip()
# pygame.quit()


