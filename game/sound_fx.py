#sound_fx.py

import pyglet



try:
    theme_music=pyglet.resource.media('sounds/theme.mp3')
    #theme_music=pyglet.resource.media('sounds/rupaul_theme.mp3')
    pop_sound=pyglet.resource.media('sounds/pop.wav', streaming=False)
except:
    print 'one of your audio files is probably compressed'
