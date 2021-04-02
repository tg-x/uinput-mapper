from uinputmapper.cinput import *

"""
Configuration for a 3DConnexion SpaceNavigator as pointer device
"""

counter = { }

def every_nth (ev, n, val):
    if ev not in counter:
        counter[ev] = 0
    else:
        counter[ev] = counter[ev] + 1
    if counter[ev] % n: return val
    else: return 0

config = {
    (0, EV_KEY) : {
        BTN_0: {
            'type': (0, EV_KEY),
            'code': BTN_LEFT,
            'value' : None
        },
        BTN_1: {
            'type': (0, EV_KEY),
            'code': BTN_RIGHT,
            'value' : None
        }
    },
    (0, EV_ABS) : {
        ABS_RX : {
            'type': (0, EV_REL),
            'code': REL_Y,
            'value': lambda x: x / 5
        },
        ABS_RY : {
            'type': (0, EV_REL),
            'code': REL_X,
            'value': lambda x: -x / 5
        },
        ABS_RZ : {
            'type': (0, EV_REL),
            'code': REL_WHEEL,
            'value': lambda x: every_nth (REL_WHEEL, 5, x / 100 if x > 0 else x / 300)
        }
    }
}

names = {
    0 : '3Dconnexion SpaceNavigator remapped'
}

def config_merge(c, n):
    c.clear()
    n.update(names)
    c.update(config)
