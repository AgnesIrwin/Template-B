#door.py

import collidable, pyglet, util

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

door_image=pyglet.resource.image('door.png')
util.center_image(door_image)


class Door(collidable.Collidable):
    
    def __init__(self, *args, **kwargs):
        super(Door,self).__init__(door_image,*args,**kwargs)
        self.scale=2
    
        
    def update(self,dt):
        pass


    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)
    


    
