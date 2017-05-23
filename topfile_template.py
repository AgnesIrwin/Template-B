#topfile_template.py

import pyglet, random
from game import viewport,world,avatar,hud,spawn_enemies,spawn_tokens,background
from game import token, hidden_token, util, instructions, sound_fx
from game import power_up, extra_life

#this function initializes global variables and kicks off the instructions 
def init():

    global inst, event_stack_size, level, score, player_lives, bg

    event_stack_size=0 #do not change
    score=0

    #edit these while testing to try later levels without needing to clear
    #early levels or to give yourself more lives if you need more
    level=1
    player_lives=3

    #don't change any of these
    bg=background.Background(level=1,batch=bg_batch)
    hud.lives_label.text="Lives:%i"%(player_lives)
    inst=instructions.Instructions_display()
    inst.batch=inst_batch
    viewport.window.push_handlers(inst.key_handler)
    pyglet.clock.schedule_interval(inst.update,1/120.0)

#this function waits for the instructions object to register as complete
#and then loads level 1
def check_instructions(dt):
    media_player.play()
    if inst.complete:
        pyglet.clock.unschedule(inst.update)
        pyglet.clock.unschedule(check_instructions)
        load_level(level)
    
#this function wipes all game objects from the game objects list    
def clear_level():

    global game_objects

    if game_objects:
        for obj in game_objects:
            obj.delete()
        game_objects=[]
            
#this function is responsible for loading all elements of each level
def load_level(level):

    global game_objects, hidden, player, event_stack_size
    global tokens_collected, max_tokens, bg

    while event_stack_size>0:
        viewport.window.pop_handlers()
        event_stack_size-=1

    event_stack_size=0

    
    game_objects=[]
    reload(world)
    world.generate_world(level)

    bg=background.Background(level=level,batch=bg_batch)


    player=avatar.Avatar(batch=main_batch)
    player.affected_by_gravity=False #Don't change this
    game_objects.append(player)

    if level==1:

        hidden_locations=[(250,500),(250,250),(750,250),(500,250)]
        loc=random.choice(hidden_locations)
        hidden=hidden_token.Hidden_token(batch=main_batch)
        hidden.x=loc[0]
        hidden.y=loc[1]
        hidden.update_bounding_box()
        game_objects.append(hidden)

        enemies=spawn_enemies.spawn_enemies(5,level)
        for enemy in enemies:
            enemy.batch=main_batch
        game_objects+=enemies

        collectibles=spawn_tokens.spawn_tokens(4,level)
        for collectible in collectibles:
            collectible.batch=main_batch
        game_objects+=collectibles

        hud.d.x=50
        hud.d.y=50

        tokens_collected=0
        max_tokens=4
        
    elif level==2:

        player.x=50
        player.y=50
        
        pwr_up=power_up.Power_up(batch=main_batch)
        pwr_up.x=650
        pwr_up.y=450
        pwr_up.make_armed=True
        pwr_up.update_bounding_box()
        game_objects.append(pwr_up)

        enemies=spawn_enemies.spawn_enemies(6,level)
        for enemy in enemies:
            enemy.batch=main_batch
        game_objects+=enemies

        collectibles=spawn_tokens.spawn_tokens(4,level)
        for collectible in collectibles:
            collectible.batch=main_batch
        game_objects+=collectibles

        hud.d.x=1050
        hud.d.y=50
        
        tokens_collected=0
        max_tokens=4
        
    elif level==3:
        enemies=spawn_enemies.spawn_enemies(8,level)
        for enemy in enemies:
            enemy.batch=main_batch
        game_objects+=enemies

        collectibles=spawn_tokens.spawn_tokens(4,level)
        for collectible in collectibles:
            collectible.batch=main_batch
        game_objects+=collectibles

        life_up=extra_life.Extra_life(batch=main_batch)
        life_up.x=650
        life_up.y=150
        life_up.update_bounding_box()
        game_objects.append(life_up)

        hud.d.x=1050
        hud.d.y=400
        
        tokens_collected=0
        max_tokens=4

    
    viewport.window.push_handlers(player.key_handler)

    pyglet.clock.schedule_interval(update,1.0/120.0)


#this is the global update method
#it is scheduled to run 60x each second
#it continually checks for certain game events on each level
#it looks for and processes all collisions between game objects
#it checks the type of all dead objects to trigger necessary events
def update(dt):

    global tokens_collected, max_tokens, level, score, player_lives

    player_dead=False
    victory=False

    if level==1:
        if hidden in game_objects:
            if util.distance((player.x,player.y),(hidden.x,hidden.y))<=150:
                hidden.found=True
    elif level==2:
        pass
    elif level==3:
        pass

    #look for collisions
    for i in xrange(len(game_objects)):
        for j in xrange(i+1,len(game_objects)):

            obj_1=game_objects[i]
            obj_2=game_objects[j]

            #make sure objects are not dead

            if not obj_1.dead and not obj_2.dead:
                if obj_1.__class__ is not obj_2.__class__:
                    if obj_1.collides_with(obj_2) or obj_2.collides_with(obj_1):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)


    #call the update method of every game object
    for obj in game_objects:
        obj.update(dt)


    #get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:

        #remove the object from the batch and the game_objects list
        to_remove.delete()
        game_objects.remove(to_remove)


        if to_remove==player:
            player_dead=True
        
        
        #Adjust the score if the dead item was worth points
        if isinstance(to_remove,token.Token):
            tokens_collected+=1
            sound_fx.pop_sound.play()
            score+=10
            hud.score_label.text='Score:'+str(score)
            #if tokens_collected==max_tokens:
            #    victory=True
            #    sound_fx.level_clear_sound.play()
        

        
        
        #Adjust the score if the dead item was worth points
        if isinstance(to_remove,power_up.Power_up):
            player.process_power_up(to_remove)
##            score+=to_remove.pt_value
##            hud.score_label.text='Score:'+str(score)
##            sound_fx.power_up_sound.play()

        #Adjust the score if the dead item was worth points
        if isinstance(to_remove,extra_life.Extra_life):
            player_lives+=1
            hud.lives_label.text="Lives: %i"%(player_lives)
##            score+=to_remove.pt_value
##            hud.score_label.text='Score:'+str(score)
##            sound_fx.power_up_sound.play()



##        #Adjust the score if the dead item was worth points
##        if isinstance(to_remove,enemy.Enemy):
##            sound_fx.pop_sound.play()
##            score+=to_remove.pt_value
##            score_label.text='Score:'+str(score)
    
        
        
        
    #check for win/lose conditions

    if tokens_collected==max_tokens and\
       util.distance((player.x,player.y),(hud.d.x,hud.d.y))<=25:
        victory=True
        
    if player_dead:
        player_lives-=1
        hud.lives_label.text="Lives:%i"%(player_lives)
        pyglet.clock.unschedule(update)
        pyglet.clock.unschedule(player.revert)
        if player_lives>0:
            clear_level()
            load_level(level)
        else:
            hud.game_over_label.y=viewport.v_ctr

    elif victory:
        if level<3:
            level+=1
            pyglet.clock.unschedule(player.revert)
            pyglet.clock.unschedule(update)
            clear_level()
            load_level(level)
        else:
            hud.win_label.y=viewport.v_ctr
            pyglet.clock.unschedule(update)

        
        


#this handler is in charge of drawing objects to the window from back to front       
@viewport.window.event
def on_draw():
    global bg
    
    viewport.window.clear()
    #bg_batch.draw()
    if not inst.complete:
        inst_batch.draw()
    else:
        world.tile_batch.draw()
        main_batch.draw()
        hud.hud_batch.draw()

@viewport.window.event
def on_close():
    viewport.window.close()
    quit()


#main
if __name__=='__main__':

    pyglet.gl.glClearColor(0.24,0.42,0.65,1.0)
    inst_batch=pyglet.graphics.Batch()
    main_batch=pyglet.graphics.Batch()
    bg_batch=pyglet.graphics.Batch()
    
    media_player=pyglet.media.Player()
    media_player.queue(sound_fx.theme_music)
    media_player.eos_action=media_player.EOS_LOOP


    init()
    pyglet.clock.schedule_interval(check_instructions,1/120.0)
    
    pyglet.app.run()
