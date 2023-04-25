import sys, pygame

pygame.init()

clk = pygame.time.Clock()

if pygame.joystick.get_count() == 0: raise IOError("No joystick detectes")
joy = pygame.joystick.Joystick(0)
joy.init()


def buttonX(boton):
    if boton==0: return 693
    elif boton==1: return 817
    elif boton==8: return 382
    elif boton==9: return 532

def buttonY(boton):
    if boton==1: return 296
    elif boton==0: return 296
    elif boton==8: return 296
    elif boton==9: return 296

size = width, height = 960, 440
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image =pygame.image.load('control.png').convert()

crosshair = pygame.surface.Surface((20, 20))
pygame.draw.circle(crosshair, pygame.Color("black"), (5,5), 5, 0)

crosshairb = pygame.surface.Surface((20, 20))
pygame.draw.circle(crosshairb,pygame.Color("red"), (10,10), 10, 0)

buttons = {}
for b in range(joy.get_numbuttons()):
    buttons[b] = [ crosshair , (buttonX(b), buttonY(b))]

while True:

    pygame.event.pump()

    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill([255,255,255])
    screen.blit(background_image, (0, 0))

    x = joy.get_axis(0)
    y = joy.get_axis(1)

    screen.blit(crosshairb, ((x*70)+168, (y*70)+262))

    for b in range(joy.get_numbuttons()):
        if joy.get_button(b):
            screen.blit(buttons[b][0], buttons[b][1])

    pygame.display.flip()

    clk.tick(40)