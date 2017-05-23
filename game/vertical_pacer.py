#vertical_pacer.py

import mob, pyglet, util, random, viewport
from pyglet.window import key


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

enemy_image=pyglet.resource.image('polar_bear.png')
util.center_image(enemy_image)

class VerticalPacer(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(VerticalPacer,self).__init__(enemy_image, *args,**kwargs)
        #self.scale=0.08
        self.spd=200
        self.x=0
        self.y=0
        self.vel_y=200
        self.is_enemy=True
        
            
    def update(self,dt):

        dx=0
        dy=self.vel_y*dt
        
        super(VerticalPacer,self).update(dx,dy,dt)

    def change_velocity(self,dt):
        if self.y<=self.min_y :
            self.y=self.min_y
            self.vel_y*=-1
        if self.y>=self.max_y:
            self.y=self.max_y
            self.vel_y*=-1

    def check_bounds(self):
        if self.y<=self.min_y :
            self.y=self.min_y
            self.vel_y*=-1
        if self.y>=self.max_y:
            self.y=self.max_y
            self.vel_y*=-1
      

    def handle_collision_with(self,other):
        pass
