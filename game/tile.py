#tile.py

import pyglet,collidable,util,viewport


pyglet.resource.path.append('./images')
pyglet.resource.reindex()


rose_bush=pyglet.resource.image('rose_bush.png')
util.set_tile_anchor(rose_bush)
water=pyglet.resource.image('water_tile.png')
util.set_tile_anchor(water)
stone=pyglet.resource.image('stone.png')
util.set_tile_anchor(stone)
sand=pyglet.resource.image('sand_tile.jpg')
util.set_tile_anchor(sand)


tile_mapping={1:water,
              2:stone,
              3:rose_bush,
              4:sand}


solid_tile_types=[1,2]

class Tile(collidable.Collidable):
    

    def __init__(self, *args, **kwargs):

        super(Tile, self).__init__(*args, **kwargs)
        

   

##import pyglet,collidable,util,viewport
##
##
##pyglet.resource.path.append('./images')
##pyglet.resource.reindex()
##
##tilesheet_image=pyglet.resource.image('tiles.jpg')
##
##wood_image=tilesheet_image.texture.get_region(0,0,50,50)
##util.set_tile_anchor(wood_image)
##bamboo_image=tilesheet_image.texture.get_region(50,0,50,50)
##util.set_tile_anchor(bamboo_image)
##grass_image=tilesheet_image.texture.get_region(100,0,50,50)
##util.set_tile_anchor(grass_image)
##
##tile_mapping={1:wood_image,
##              2:bamboo_image,
##              3:grass_image}
##
##solid_tile_types=[1,2]
##
##class Tile(collidable.Collidable):
##    
##
##    def __init__(self, *args, **kwargs):
##
##        super(Tile, self).__init__(*args, **kwargs)
##        
##
##   
##
       
        
        
