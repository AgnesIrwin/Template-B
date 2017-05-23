#power_up.py

import collidable, util, pyglet, aabb

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

pwrup_image=pyglet.resource.image('explosion.png')
util.center_image(pwrup_image)


class Power_up(collidable.Collidable):
    
    def __init__(self, *args, **kwargs):
        super(Power_up,self).__init__(pwrup_image,*args,**kwargs)
        self.scale=0.3
        self.is_pwrup=True
        self.speed_up=False
        self.make_invincible=False
        self.make_armed=False
        self.make_insubstantial=False

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    def update(self,dt):
        pass


    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    


    
    def handle_collision_with(self,other):

        if other.is_avatar:
            self.dead=True
           
