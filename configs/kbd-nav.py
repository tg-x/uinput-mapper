from uinputmapper.cinput import *

"""
Configuration for keyboard navigation layer
"""

mods = {}

def set_mod (mod, x):
    mods[mod] = 1 if x > 0 else 0
    return 0

def mod_map (mod, keys):
    layer = mods[mod] if mod in mods else 0
    return keys[layer]

config = {
    (0, EV_KEY) : {
        KEY_BACKSLASH: {
            'code': KEY_ENTER
        },
        KEY_102ND: {
            'code': KEY_BACKSLASH
        },
        KEY_LEFTMETA: {
            'codes': [KEY_LEFTCTRL, KEY_LEFTALT]
        },
        KEY_CAPSLOCK: {
            'code': KEY_FN,
            'value': lambda x: set_mod('nav', x),
        },
        KEY_RIGHTALT: {
            'code': KEY_FN,
            'value': lambda x: set_mod('nav', x),
        },
        KEY_I: {
            'codes': [KEY_I, KEY_UP],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_J: {
            'codes': [KEY_J, KEY_LEFT],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_K: {
            'codes': [KEY_K, KEY_DOWN],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_L: {
            'codes': [KEY_L, KEY_RIGHT],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_U: {
            'codes': [KEY_U, KEY_BACK],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_O: {
            'codes': [KEY_O, KEY_FORWARD],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_H: {
            'codes': [KEY_H, KEY_BACKSPACE],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_N: {
            'codes': [KEY_N, KEY_DELETE],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_M: {
            'codes': [KEY_M, KEY_HOME],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_DOT: {
            'codes': [KEY_DOT, KEY_END],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_COMMA: {
            'codes': [KEY_COMMA, KEY_INSERT],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_P: {
            'codes': [KEY_P, KEY_PAGEUP],
            'code': lambda codes: mod_map('nav', codes),
        },
        KEY_SEMICOLON: {
            'codes': [KEY_SEMICOLON, KEY_PAGEDOWN],
            'code': lambda codes: mod_map('nav', codes),
        },
    }
}

def config_merge(c, n):
    for k, v in config.iteritems():
        if k in c:
            c[k].update(v)
        else:
            c[k] = v
