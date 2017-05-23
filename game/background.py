#background.py

import pyglet,viewport
#background_batch=pyglet.graphics.Batch()

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

background1_image=pyglet.resource.image('ocean_floor_background.png')
background2_image=pyglet.resource.image('jungle_background.jpg')
background3_image=pyglet.resource.image('space_background.jpg')

bg_map={1:background1_image,
        2:background2_image,
        3:background3_image}

class Background(pyglet.sprite.Sprite):
        def __init__(self,level,*args,**kwargs):
                super(Background,self).__init__(bg_map[level],*args,**kwargs)
                      

                #self.scale=.999
                
 
