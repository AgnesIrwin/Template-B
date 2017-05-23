#hud.py

import pyglet,viewport,door

hud_batch=pyglet.graphics.Batch()

'''
instantiate all of your labels and or graphic icons here

make sure to set all of their batch attributes to hud_batch

do not draw them in this module

in the topfile, add hud_batch.draw() to the on_draw handler
'''

score_label=pyglet.text.Label(text='Score:0',
                              anchor_x='left',
                              anchor_y='top',
                              x=0,
                              y=viewport.window.height,
                              font_size=32,
                              batch=hud_batch)

lives_label=pyglet.text.Label(text='Lives:',
                              anchor_x='right',
                              anchor_y='top',
                              x=viewport.window.width,
                              y=viewport.window.height,
                              font_size=32,
                              batch=hud_batch)


game_over_label=pyglet.text.Label(text='GAME OVER',
                                  anchor_x='center',
                                  anchor_y='center',
                                  x=viewport.h_ctr,
                                  y=-300,
                                  font_size=72,
                                  batch=hud_batch)

win_label=pyglet.text.Label(text="You Won!!!!",
                                  anchor_x='center',
                                  anchor_y='center',
                                  x=viewport.h_ctr,
                                  y=-300,
                                  font_size=72,
                                  batch=hud_batch)

d=door.Door()
d.batch=hud_batch
