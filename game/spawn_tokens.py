#spawn_tokens.py

import random,token

#fill this list with tuples (x,y), where each tuple is a viable spawn location
#possible_token_locations=[(100,500),(200,500),(300,500),(400,500)]

#this list will store references to your enemy sprites, it will be appended to game objects
#in the topfile



def spawn_tokens(n,level):

    #n is the number of enemies to spawn
    possible_token_locations={1:[(100,500),(200,500),(300,500),(400,500)],
                              2:[(200,200),(600,100),(400,200),(500,300)],
                              3:[(300,300),(100,200),(400,100),(200,400)]}


    if n<=len(possible_token_locations[level]):
                          
        tokens=[]

        for i in range(n):
            location=random.choice(possible_token_locations[level])
            possible_token_locations[level].remove(location)
            x=location[0]
            y=location[1]
            new_token=token.Token(level=level)
            new_token.x=x
            new_token.y=y
            new_token.update_bounding_box()
            tokens.append(new_token)

  
        return tokens
    else:
        print 'not enough locations provided to spawn %i mobs'%(n)
