#token.py

import collidable, util, pyglet, aabb

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

token1_image=pyglet.resource.image('fireball.png')
util.center_image(token1_image)

token2_image=pyglet.resource.image('marble.png')
util.center_image(token2_image)

token3_image=pyglet.resource.image('candy.png')
util.center_image(token3_image)

token_map={1:token1_image,
           2:token2_image,
           3:token3_image}


class Token(collidable.Collidable):
    
    def __init__(self, level,*args, **kwargs):
        super(Token,self).__init__(token_map[level],*args,**kwargs)
        #self.scale=0.3

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
           
