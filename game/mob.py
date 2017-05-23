#mob.py

import collidable,world,viewport,aabb,util

class Mob(collidable.Collidable):

    def __init__(self,img,*args,**kwargs):
        super(Mob,self).__init__(img,*args,**kwargs)
        
        self.affected_by_gravity=False
        self.supported=False
        self.acc=self.height*2

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

        self.is_enemy=False
        self.is_avatar=False


    def can_move_there(self,x,y):

        lower_bound=((x-self.width//2),(y-self.height//2))
        upper_bound=((x+self.width//2),(y+self.height//2))

        new_box=aabb.AABB(lower_bound,upper_bound)
        no_collision=True
        
        for occ_tile_pt in self.get_occupied_tiles(x,y):
            if occ_tile_pt in world.grid_solid_tile_mapping.keys():
                occ_tile=world.grid_solid_tile_mapping[occ_tile_pt]
                if occ_tile.bounding_box.collides_with(new_box) or \
                   new_box.collides_with(occ_tile.bounding_box):
                    no_collision=False
                    if self.is_enemy:
                        self.change_velocity(0)
                    dx=abs(self.x-occ_tile.x)
                    dy=abs(self.y-occ_tile.y)
                    if self.y>=occ_tile.y+self.height//2:
                        self.supported=True
                    
        return no_collision or self.insubstantial
         
                

    def update(self,dx,dy,dt):

        next_x=self.x+dx
        next_y=self.y+dy
        
        if dx or dy:   
            if self.can_move_there(next_x,next_y):
                self.x=next_x
                self.y=next_y
                self.supported=False
                                     

        self.lower_bound=((self.x-self.width//2),(self.y-self.height//2))
        self.upper_bound=((self.x+self.width//2),(self.y+self.height//2))
        self.bounding_box=aabb.AABB(self.lower_bound,self.upper_bound)

        self.check_bounds()




    def get_occupied_tiles(self,x,y):

        min_horiz=int((x-self.width//2)/world.col_width)
        max_horiz=int((x+self.width//2)/world.col_width)
        min_vert=int((y-self.height//2)/world.col_height)
        max_vert=int((y+self.height//2)/world.col_height)
       
        #convert min and max values into all or outer tile pts
        occupied_tiles=[]
        for i in range(min_horiz,(max_horiz+1)):
            for j in range(min_vert,(max_vert+1)):
                occupied_tiles.append((i,j))

        return occupied_tiles

 
    def check_bounds(self):
 
        min_x=self.width//2
        max_x=viewport.window.width-(self.width//2)
        min_y=self.height//2
        max_y=viewport.window.height-(self.height//2)

        if self.x<min_x:self.x=min_x
        if self.x>max_x:self.x=max_x
        if self.y<min_y:self.y=min_y
        if self.y>max_y:self.y=max_y
        
