#hidden_token.py

import collidable, util, pyglet, aabb

pyglet.resource.path.append('./images')
pyglet.resource.reindex()

hidden_token_image=pyglet.resource.image('key.jpeg')
util.center_image(hidden_token_image)


class Hidden_token(collidable.Collidable):
    
    def __init__(self, *args, **kwargs):
        super(Hidden_token,self).__init__(hidden_token_image,*args,**kwargs)
        self.scale=0.5
        
        self.visible=False
        self.found=False

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

        
        
    def update(self,dt):
        super(Hidden_token,self).update(dt)
        if self.found:self.visible=True

    def update_bounding_box(self):
        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

    
    def handle_collision_with(self,other):
        if other.is_avatar:self.dead=True


    

    
    
