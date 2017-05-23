#avatar.py

import mob, pyglet, util
from pyglet.window import key


pyglet.resource.path.append('./images')
pyglet.resource.reindex()

avatar_image=pyglet.resource.image('frodo.png')
util.center_image(avatar_image)

avatar_pwrup_image=pyglet.resource.image('bat.png')
util.center_image(avatar_pwrup_image)


class Avatar(mob.Mob):

    def __init__(self,*args,**kwargs):
        super(Avatar,self).__init__(avatar_image,x=1000,y=450,*args,**kwargs)
        self.key_handler=key.KeyStateHandler()
        self.scale=0.1
        self.vel_y=0
        self.is_avatar=True
        self.death_timer=0
        
        self.spd=200
        self.invincible=False
        self.armed=False
        self.insubstantial=False
   
    def update(self,dt):

        
        self.death_timer-=dt

        dx=0
        dy=0

#new code to prevent sticking
        if self.affected_by_gravity:
            if self.key_handler[key.RIGHT]:
                dx=self.spd*dt
    
            if self.key_handler[key.LEFT]:
                dx=-1*self.spd*dt

            if self.supported:
                if self.key_handler[key.SPACE]:
                    self.jump()
                    
            else:
                self.vel_y-=self.acc*dt
                dy=self.vel_y*dt

        else:
            
            if self.key_handler[key.RIGHT]:
                dx=self.spd*dt
    
            if self.key_handler[key.LEFT]:
                dx=-1*self.spd*dt

            if self.key_handler[key.UP]:
                dy=self.spd*dt

            if self.key_handler[key.DOWN]:
                dy=-1*self.spd*dt

        super(Avatar,self).update(dx,dy,dt)
        
    
#original code
##        if self.key_handler[key.RIGHT]:
##            dx=self.spd*dt
##    
##            
##        if self.key_handler[key.LEFT]:
##            dx=-1*self.spd*dt
##
##
##        if not self.affected_by_gravity:
##           
##
##            if self.key_handler[key.UP]:
##                dy=self.spd*dt
##                
##
##            if self.key_handler[key.DOWN]:
##                dy=-1*self.spd*dt
##
##                
##        if self.affected_by_gravity:
##            if not self.supported:
##                self.vel_y-=self.acc*dt
##                dy=self.vel_y*dt
##
##        if self.supported:
##            if self.key_handler[key.SPACE]:
##                self.jump()
##                
##
##        super(Avatar,self).update(dx,dy,dt)


    def handle_collision_with(self,other):
        if self.death_timer<=0:
            if other.is_enemy:
                if self.armed:
                    other.dead=True
                elif not self.invincible:
                    self.dead=True         #change  to False for invincibilty
                    self.death_timer=2
        
    def process_power_up(self,other):
        self.image=avatar_pwrup_image
        self.scale=0.5
        if other.speed_up:
            self.spd=400
        elif other.make_invincible:
            self.invincible=True
        elif other.make_armed:
            self.armed=True
        elif other.make_insubstantial:
            self.insubstantial=True
            self.invincible=True
            
        pyglet.clock.schedule_once(self.revert,50)

    def revert(self,dt):
        self.image=avatar_image
        self.scale=0.1
        self.spd=200
        self.invincible=False
        self.armed=False
        self.insubstantial=False

    def jump(self):
        self.supported=False
        self.vel_y=600
