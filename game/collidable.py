#collidable.py

import pyglet,aabb

class Collidable(pyglet.sprite.Sprite):

    def __init__(self,img,*args,**kwargs):
        super(Collidable,self).__init__(img,*args,**kwargs)
        self.dead=False
        self.is_avatar=False
        self.is_enemy=False
        self.is_pwrup=False
        self.insubstantial=False
        self.event_handlers=[]


    def update(self,dt):
        pass
        
        
    def collides_with(self,other):

        return self.bounding_box.collides_with(other.bounding_box) or\
               other.bounding_box.collides_with(self.bounding_box)

    def handle_collision_with(self,other):
        pass

    

   
