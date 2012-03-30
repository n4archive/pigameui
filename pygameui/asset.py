import os
import weakref
import pygame

import theme


fonts = weakref.WeakValueDictionary()
images = weakref.WeakValueDictionary()
sounds = weakref.WeakValueDictionary()


default_font = None
default_bold_font = None


root = os.path.join('..', 'assets')


def init():
    global default_font, default_bold_font
    default_font = get_font()
    default_bold_font = get_font(usebold=True)


def get_font(size=theme.font_size, usebold=False):
    regular_path = os.path.join(root, 'fonts', 'regular.ttf')
    bold_path = os.path.join(root, 'fonts', 'bold.ttf')

    path = regular_path
    if usebold:
        path = bold_path

    key = '%s - %d' % (path, size)
    try:
        font = fonts[key]
    except KeyError:
        try:
            font = pygame.font.Font(path, size)
            fonts[key] = font
        except:
            print 'WARNING: failed to load font', path
            font = pygame.font.SysFont('helvetica,arial', size, usebold)
    return font


def get_image(name):
    path = os.path.join(root, 'images', '%s.png' % name)
    try:
        img = images[path]
    except KeyError:
        img = pygame.image.load(path)
        if not img:
            print 'WARNING: failed to load image', path
        img = img.convert_alpha()
        images[path] = img
    return img


def scale_image(image, size):
    return pygame.transform.smoothscale(image, size)


def get_sound(name):
    class NoSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoSound()

    path = os.path.join(root, 'sounds', '%s.wav' % name)

    try:
        sound = sounds[path]
    except KeyError:
        if os.path.exists(path):
            sound = pygame.mixer.Sound(path)
            sounds[path] = sound
        else:
            print 'WARNING: failed to load sound', path
            sound = NoSound()
    return sound
