#horizontal_pacer.py

import mob, pyglet, util, random, viewport
from pyglet.window import key


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

enemy_image=pyglet.resource.image('polar_bear.png')
util.center_image(enemy_image)

class HorizontalPacer(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(HorizontalPacer,self).__init__(enemy_image,*args,**kwargs)
        #self.scale=0.08
        self.spd=200
        self.x=0
        self.y=0
        self.is_enemy=True
        self.vel_x=0
        self.vel_y=0
        
        pyglet.clock.schedule_interval(self.change_velocity,3)
   
    def update(self,dt):

        dx=self.vel_x*dt
        dy=self.vel_y*dt
        
##        if self.affected_by_gravity:
##            if not self.supported:
##                self.vel_y-=self.acc*dt
##                dy=self.vel_y*dt

        
        super(HorizontalPacer,self).update(dx,dy,dt)

    def change_velocity(self,dt):

        if self.x<=self.min_x:
            self.x=self.min_x
            self.vel_x*=-1
        if self.x>=self.max_x:
            self.x=self.max_x
            self.vel_x*=-1
            
    def check_bounds(self):

        if self.x<=self.min_x :
            self.x=self.min_x
            self.vel_x*=-1
        if self.x>=self.max_x:
            self.x=self.max_x
            self.vel_x*=-1


    def handle_collision_with(self,other):
        pass


   
