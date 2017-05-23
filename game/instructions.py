#instructions.py

import pyglet,util
from pyglet.window import key

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

inst_1_img=pyglet.resource.image('inst_1.png')
inst_2_img=pyglet.resource.image('inst_2.png')
inst_3_img=pyglet.resource.image('inst_3.png')


class Instructions_display(pyglet.sprite.Sprite):

    def __init__(self,*args,**kwargs):
        super(Instructions_display,self).__init__(inst_1_img,*args,**kwargs)
        self.key_handler=key.KeyStateHandler()
        self.counter=1
        self.keypress_delay=1
        self.complete=False

    def update(self,dt):

        self.keypress_delay-=dt

        if self.keypress_delay<=0:

            if self.key_handler[key.SPACE]:
                self.counter+=1
                if self.counter==2:
                    self.image=inst_2_img
                elif self.counter==3:
                    self.image=inst_3_img
                else:
                    self.complete=True

                    
                self.keypress_delay=0.5
            


        

    
                

    

        
