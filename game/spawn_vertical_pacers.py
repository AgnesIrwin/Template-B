#spawn_vertical_enemies.py

import random,enemy,vertical_pacer

#fill this list with tuples (x,y), where each tuple is a viable spawn location
#possible_enemy_locations=[(100,500),(200,400),(800,200),(100,100)]

#this list will store references to your enemy sprites, it will be appended to game objects
#in the topfile



def spawn_vertical_pacers(n,level):

    #n is the number of enemies to spawn
    #args are (init x,init y,min_x,max_x)
    possible_enemy_locations={1:[(433,550,250,550),(50,550,175,550),(1025,475,125,475)],
                              2:[(950,547,50,547),(875,50,50,547),(215,50,50,274),(415,275,50,272),(130,300,300,555),(675,250,250,455)],
                              3:[(300,200,185,475),(725,200,185,475),(430,530,250,540)]}
                              

    if n<=len(possible_enemy_locations[level]):
                          
        enemies=[]

        for i in range(n):
            location=random.choice(possible_enemy_locations[level])
            possible_enemy_locations[level].remove(location)
            x=location[0]
            y=location[1]
            min_y=location[2]
            max_y=location[3]
            new_enemy=vertical_pacers.VerticalPacer()
            new_enemy.x=x
            new_enemy.y=y
            new_enemy.min_y=min_y
            new_enemy.max_y=max_y
            enemies.append(new_enemy)
        

        return enemies
    else:
        print 'not enough locations provided to spawn %i mobs'%(n)

