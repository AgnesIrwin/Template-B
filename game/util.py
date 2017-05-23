#util.py
import math

def center_image(image):
    image.anchor_x=image.width//2
    image.anchor_y=image.height//2
    

def set_tile_anchor(image):
    image.anchor_y=image.height

def distance(a,b):

    return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)



