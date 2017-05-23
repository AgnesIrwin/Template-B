#spawn_enemies.py

import random,horizontal_pacer

#fill this list with tuples (x,y), where each tuple is a viable spawn location
#possible_enemy_locations=[(100,500),(200,400),(800,200),(100,100)]

#this list will store references to your enemy sprites, it will be appended to game objects
#in the topfile



def spawn_horizontal_pacers(n,level):

    #n is the number of enemies to spawn
    #args are (init x,init y,min_x,max_x)
    possible_enemy_locations={1:[(610,50,610,1000),(610,550,610,1000)],
                              2:[(250,500,250,600),(225,255,225,700),(325,350,325,650),(350,50,350,675),(135,550,100,600),(65,375,75,300),(525,50,475,850)],
                              3:[(1000,350,875,1025),(50,400,65,175)]}
    if n<=len(possible_enemy_locations[level]):
                          
        enemies=[]

        for i in range(n):
            location=random.choice(possible_enemy_locations[level])
            possible_enemy_locations[level].remove(location)
            x=location[0]
            y=location[1]
            min_x=location[2]
            max_x=location[3]
            new_enemy=horizontal_pacer.HorizontalPacer()
            new_enemy.x=x
            new_enemy.y=y
            new_enemy.min_x=min_x
            new_enemy.max_x=max_x
            enemies.append(new_enemy)
            
        return enemies
    else:
        print 'not enough locations provided to spawn %i mobs'%(n)
