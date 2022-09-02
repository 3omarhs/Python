import os

import io
from PIL import Image
import threading

import random, math, pygame
from pygame.locals import *
import PySimpleGUIWeb as sg


#constants
WINSIZE = [640, 480]
WINCENTER = [320, 240]
NUMSTARS = 150


def init_star():
    "creates new star values"
    dir = random.randrange(100000)
    velmult = random.random()*.6+.4
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    return vel, WINCENTER[:]


def initialize_stars():
    "creates a new starfield"
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        vel, pos = star
        steps = random.randint(0, WINCENTER[0])
        pos[0] = pos[0] + (vel[0] * steps)
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * .09)
        vel[1] = vel[1] * (steps * .09)
        stars.append(star)
    move_stars(stars)
    return stars


def draw_stars(surface, stars, color):
    "used to draw (and clear) the stars"
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)


def move_stars(stars):
    "animate the star values"
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            vel[:], pos[:] = init_star()
        else:
            vel[0] = vel[0] * 1.05
            vel[1] = vel[1] * 1.05


class PILImageViewverWidget():
    def __init__(self, image_elem=None, pil_image=None, **kwargs):
        self._buf = None
        self.index = 0
        self.render_done = True
        self.image_elem = image_elem        # type: sg.Image
        self.image_widget = image_elem.Widget # type: sg.SuperImage

    def set_image(self, pil_image):
        if not self.render_done:
            return
        self.render_done = False
        self._buf = io.BytesIO()
        pil_image.save(self._buf, format='png')
        self.refresh()

    def refresh(self):
        self.image_widget.attributes['src'] = "/%s/get_image_data?update_index=%d" % (id(self.image_widget), self.index)
        self.index = self.index+1
        self.image_widget.style['background-image'] = "url('/%s/get_image_data?update_index=%d')" % (id(self.image_widget), self.index)

    def get_image_data(self, update_index):
        if self._buf is None:
            return None
        self.render_done = True
        self._buf.seek(0)
        headers = {'Content-type': 'image/png'}
        return [self._buf.read(), headers]


def pygame_main():
    "This is the starfield code"
    #create our starfield
    random.seed()
    stars = initialize_stars()
    clock = pygame.time.Clock()
    #initialize and prepare screen

    # --------------------- PySimpleGUI window layout and creation --------------------
    layout = [[sg.T('Test of PySimpleGUI with PyGame')],
              [sg.Image(filename=r'C:\Python\PycharmProjects\GooeyGUI\logo200.png', size=(640, 480), background_color='lightblue', key='_IMAGE_')],
              [sg.B('Draw'), sg.Exit()]]

    window = sg.Window('PySimpleGUI + PyGame', layout).Finalize()
    image_elem = window.Element('_IMAGE_')
    pil_image_viewer = PILImageViewverWidget(image_elem)

    # -------------- Magic code to integrate PyGame with tkinter -------
    os.environ['SDL_WINDOWID'] = str(1)
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    # pygame.init()

    screen = pygame.display.set_mode(WINSIZE)
    screen.fill(pygame.Color(255, 255, 255))

    pygame.display.init()
    pygame.display.update()

    pygame.display.set_caption('pygame Stars Example')
    white = 255, 240, 200
    black = 20, 20, 40
    # screen.fill(black)
    #main game loop
    done = 0
    count = 0
    while not done:
        event, values = window.Read(timeout=10)
        print(event, values) if event != sg.TIMEOUT_KEY else None
        if event in (None, 'Exit'):
            break
        draw_stars(screen, stars, black)
        move_stars(stars)
        draw_stars(screen, stars, white)
        pygame.display.update()
        for e in pygame.event.get():
            print(f'Event = {e}')
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                print('**** FOUND  A KEY PRESS!')
                done = 1
                break
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                print('**** FOUND  A MOUSE PRESS!')
                WINCENTER[:] = list(e.pos)
        clock.tick(50)

        #>>>>>>>>> here the pygame window gets shown in the REMI widget <<<<<<<<<
        surf = pygame.display.get_surface()
        data = pygame.image.tostring(surf, 'RGBA')
        img = Image.frombytes('RGBA', surf.get_size(), data)
        # with update_lock: #thread sync
        pil_image_viewer.set_image(img)
        # pil_image_viewer.get_image_data(count)
        count +=1
    window.Close()

if __name__ == "__main__":
    pygame_main()
    # t = threading.Thread(target=pygame_main)
    # t.start()