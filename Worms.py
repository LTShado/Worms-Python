import pygame
import Pwayer
import time
import math
import random

#test 2

res = (640, 480)

pygame.init()

clock = pygame.time.Clock()

#création de la fenetre + changement de nom de la fenetre
pygame.display.set_caption("Worms")
surface = pygame.display.set_mode(res)
print(pygame.display.Info())

ground = list()
ground_color = (155,118,53)

colide = pygame.Rect(0,440,300,40)
pygame.draw.rect(surface,ground_color,colide)
ground.append(colide)

colide = pygame.Rect(301,440,640,40)
pygame.draw.rect(surface,ground_color,colide)
ground.append(colide)

colision = dict()

#initialisation des differents sons et images, et modification du volume pour certain
sound = pygame.mixer.Sound("musique/wormstheme.mp3")
sound.set_volume(0.10)
sound.play()
rocket = pygame.mixer.Sound("musique/rocketlauncher.mp3")
grenade = pygame.mixer.Sound("musique/grenade.mp3")
explosion = pygame.mixer.Sound("musique/explosion.mp3")
explosion.set_volume(0.30)
menu_img = pygame.image.load("images/menu.jpg")
menu_img = pygame.transform.scale(menu_img,(640,480))
menu_img.convert()

#création de differente taille de texte pour divers truc, avec la police arial
menu_font = pygame.font.SysFont("arial",50)
arial_font = pygame.font.SysFont("arial",10)
death_font = pygame.font.SysFont("arial",50)
player_font = pygame.font.SysFont("arial",15)

#initialisation couleur
fps_color = (26,7,109)
traj_color = (109,7,26)
bullet_color = (109,7,26)

#initialisation de variables
g = 9.81
AB = 0 #distance AB, distance entre le y du joueur et le y de la souris
AC = 0 #distance AC, distance entre le x du joueur et le x de la souris
angle_radian = 0
angle_degree = 0
vitesse = 0
#position du x et y de la souris
x_souris = 0
y_souris = 0

weapon = 0
player = 1
debug_mode = 0
wind_speed = 0.5

colision["ground"] = ground

#initialisation de la pos des players, et changements de couleur pour le player 2
playerOne = Pwayer.Player(random.randint(0,620), 60, 20, surface, ground)
playerTwo = Pwayer.Player(random.randint(0,620), 60, 20, surface, ground)
playerTwo.color=(7,109,26)

#variable pour la fleche pour savoir le tour de quel joueur
player_turn_x = 0
player_turn_y = 0

#le joueur ayant gagner
winner = 0

#initialisation de la position de la bullet en fonction du joueur qui joue de meme pour la traj
if player == 1:
    bullet = pygame.Rect(playerOne.body.x,playerOne.body.y,20,19.5)
    traj_bullet = pygame.Rect(playerOne.body.x,playerOne.body.y,10,10)
elif player==2:
    bullet = pygame.Rect(playerTwo.body.x, playerTwo.body.y, 20, 19.5)
    traj_bullet = pygame.Rect(playerTwo.body.x, playerTwo.body.y, 10, 10)

#status de trajectoire pour l'afficher ou non
traj_status = 0

#status death pour savoir si un joueur est mort
status_death = 0


def keyDownAction():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player==1:
            playerOne.MovePlayer("Left")
        elif player==2:
            playerTwo.MovePlayer("Left")
    if keys[pygame.K_RIGHT]:
        if player == 1:
            playerOne.MovePlayer("Right")
        elif player == 2:
            playerTwo.MovePlayer("Right")
    if keys[pygame.K_SPACE] and playerOne.isGrounded() and playerTwo.isGrounded():
        if player==1:
            playerOne.Jump()
        elif player==2:
            playerTwo.Jump()



ciel = (30, 144, 255)

#initialisation d'une variable timers pour le timer de 30 sec
timers = time.time()
launched = True

#variable start pour savoir si le jeu est lancer ou non
start = 0
while launched:
    #ecran du menu
    if start == 0:
        #text et image qui vont être afficher sur l'écran du menu
        Start_text = menu_font.render(f"Press ENTER to Start", True, (255, 0, 0))
        surface.blit(menu_img, [0, 0])
        start_fill = pygame.Rect(125, 200, 400, 60)
        pygame.draw.rect(surface, (0, 0, 0), start_fill)
        surface.blit(Start_text, [125, 200])
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
                print("exit")

            #appuie sur ENTRER pour lancer le jeu donc passer start à 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("start")
                    start = 1
    #ecran jeu
    elif start==1:
        if status_death == 0:
            #regler le jeu à 60 fps
            clock.tick(60)
            #remplir l'ecran de la couleur ciel
            surface.fill(ciel)

            #difference de temps entre timers et time.time arrondie pour l'affichage
            dt = round(time.time()-timers)
            #le timer de 30 secondes qui descend grace dt
            timer = 30-dt
            #si le timer arrive à 0 change de joueur et on remet le timer à 30s
            if timer <=0 :
                timers = time.time()
                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1

            #création des differents text qui vont être affichés
            text_fps = arial_font.render(f"{clock.get_fps():.2f} FPS", True, fps_color)
            angle_number = arial_font.render(f"{angle_degree} °", True, fps_color)
            AB_number = arial_font.render(f"AB = {AB}", True, traj_color)
            AC_number = arial_font.render(f"AC = {AC}", True, traj_color)
            vitesse_number = arial_font.render(f"vitesse = {vitesse}", True, traj_color)
            player_number_render = arial_font.render(f"Player n° : {player}", True, traj_color)
            player_turn_render_1 = player_font.render(f"Player 1",True, (0,0,0))
            player_turn_render_2 = player_font.render(f"Player 2", True, (0, 0, 0))
            timer_render = death_font.render(f"{timer}",True, (0,0,0))

            #text pour l'arme choisie
            if weapon==0:
                weapon_name="grenade"
            elif weapon==1:
                weapon_name="rocket"

            #text pour l'arme et le vent
            weapon_render = arial_font.render(f"Weapon : {weapon_name}", True,traj_color)
            wind_render = arial_font.render(f"Wind speed : {wind_speed}", True,traj_color)

            #refresh des valeurs tant que le jeu est lancer
            if player==1:
                AB = math.sqrt(((x_souris - (playerOne.body.centerx)) ** 2) + ((y_souris - (playerOne.body.centery)) ** 2))
                AC = x_souris - (playerOne.body.centerx)
                player_turn_x = playerOne.body.x
                player_turn_y = playerOne.body.y
                player_turn_center_x = playerOne.body.centerx
                pygame.draw.line(surface, bullet_color, [playerOne.body.centerx, playerOne.body.centery], [x_souris, y_souris])#la ligne pour avoir une direction

            elif player==2:
                AB = math.sqrt(((x_souris - (playerTwo.body.centerx)) ** 2) + ((y_souris - (playerTwo.body.centery)) ** 2))
                AC = x_souris - (playerTwo.body.centerx)
                player_turn_x = playerTwo.body.x
                player_turn_y = playerTwo.body.y
                player_turn_center_x = playerTwo.body.centerx
                pygame.draw.line(surface, bullet_color, [playerTwo.body.centerx, playerTwo.body.centery], [x_souris, y_souris])

            #avoir un speed max de 100
            if round(AB / 2, 0) > 100:
                vitesse = 100

            else:
                vitesse = round(AB / 2, 0)

            #pour empecher d'avoir une division par 0
            if AB == 0:
                AB == 1
            else:
                angle_radian = round(math.acos(AC / AB), 4)#avoir l'angle grace au 2 longueur
                #pour avoir un angle de 360°
                if player == 1:
                    if y_souris > playerOne.body.y:
                        angle_degree = round(360 - (angle_radian * 180 / math.pi), 0)
                    else:
                        angle_degree = round(angle_radian * 180 / math.pi, 0)
                elif player == 2:
                    if y_souris > playerTwo.body.y:
                        angle_degree = round(360 - (angle_radian * 180 / math.pi), 0)
                    else:
                        angle_degree = round(angle_radian * 180 / math.pi, 0)

            #fleche de tour
            turn_form = [(player_turn_center_x, player_turn_y - 20),(player_turn_x, player_turn_y - 30),(player_turn_x+20, player_turn_y - 30)]
            pygame.draw.polygon(surface,bullet_color, turn_form)

            #text au dessus de joueur "Joueur 1" ou 2
            surface.blit(player_turn_render_1, [playerOne.body.x-10, playerOne.body.y - 20])
            surface.blit(player_turn_render_2, [playerTwo.body.x - 10, playerTwo.body.y - 20])

            #affichage à l'écran du timer
            surface.blit(timer_render, [290, 0])

            #mode debug
            if debug_mode == 1:
                #affichage de toute les variables
                surface.blit(text_fps, [10, 10])
                surface.blit(angle_number, [500, 10])
                surface.blit(AB_number, [500, 20])
                surface.blit(AC_number, [500, 30])
                surface.blit(vitesse_number, [500, 40])
                surface.blit(weapon_render, [500, 50])
                surface.blit(wind_render, [500, 60])
                surface.blit(player_number_render, [500, 70])

            #pour savoir le x0 ou y0 dans le calcul de trajectoire en fonction de quel joueur joue
            if player == 1:
                x0 = playerOne.body.centerx
                y0 = playerOne.body.centery
            elif player == 2:
                x0 = playerTwo.body.centerx
                y0 = playerTwo.body.centery

            #angle de 360 et aussi vue de l'origin se trouve en haut à gauche modif la valeur de langle pour quelle soit dans le bon sens
            if player == 1:
                if (y_souris > playerOne.body.y):
                    angle = angle_radian
                else:
                    angle = -angle_radian
            elif player == 2:
                if (y_souris > playerTwo.body.y):
                    angle = angle_radian
                else:
                    angle = -angle_radian

            #initialisation des variables v0 et w0
            v0 = vitesse * math.cos(angle)
            w0 = vitesse * math.sin(angle)

            #trajectoire en fonction de l'arme choisie
            for i in range(0, 20):
                if weapon == 0:
                    traj_bullet_x = x0 + v0 * (i * 0.5)
                    traj_bullet_y = 0.5 * g * ((i * 0.5) ** 2) + w0 * (i * 0.5) + y0
                elif weapon == 1:
                    if AC < 0:
                        traj_bullet_x = x0 + ((v0 / -wind_speed) * (1 - math.exp(wind_speed * i)))
                        traj_bullet_y = y0 + (((w0 / -wind_speed) - (g / (-wind_speed ** 2))) * (1 - math.exp(wind_speed * i))) + ((g * i) / -wind_speed)

                    elif AC > 0:
                        traj_bullet_x = x0 + ((v0 / wind_speed) * (1 - math.exp(-wind_speed * i)))
                        traj_bullet_y = y0 + (((w0 / wind_speed) - (g / (wind_speed ** 2))) * (1 - math.exp(-wind_speed * i))) + ((g * i) / wind_speed)

                #affichage de la traj si traj_status vaut 1
                if traj_status == 1:
                    pygame.draw.circle(surface, traj_color, [traj_bullet_x,traj_bullet_y],3)

            #dessiner le sol
            for collide in ground:
                pygame.draw.rect(surface, ground_color, collide)

            #gravité sur les joueurs
            playerOne.fall(g)
            playerTwo.fall(g)

            #dessiner les joueurs
            playerOne.draw()
            playerTwo.draw()
            pygame.display.flip()

            keyDownAction()

            for event in pygame.event.get():
                #exit si appuie sur la croix
                if event.type == pygame.QUIT:
                    launched = False
                    print("exit")

                elif event.type == pygame.KEYDOWN:
                    #change la valeur de traj_status en appyant sur r
                    if event.key == pygame.K_r:
                        if traj_status == 0:
                            traj_status = 1
                        elif traj_status == 1:
                            traj_status = 0

                    #changement d'arme avec tab
                    elif event.key == pygame.K_TAB:
                        if weapon==0:
                            weapon=1
                        elif weapon==1:
                            weapon=0

                    #passer en mode debug avec F3
                    elif event.key == pygame.K_F3:
                        if debug_mode==0:
                            debug_mode=1
                        elif debug_mode==1:
                            debug_mode=0

                    #ptit changement de joueur direct, debug
                    elif event.key == pygame.K_c:
                        if player == 1:
                            player = 2
                        elif player == 2:
                            player = 1

                #la souris bouge
                elif event.type == pygame.MOUSEMOTION:
                    #print("{}".format(event.pos))

                    surface.fill(ciel)
                    #redessiner la fleche de tour
                    pygame.draw.polygon(surface, bullet_color, turn_form)

                    surface.blit(player_turn_render_1, [playerOne.body.x - 10, playerOne.body.y - 20])
                    surface.blit(player_turn_render_2, [playerTwo.body.x - 10, playerTwo.body.y - 20])

                    surface.blit(timer_render, [290, 0])

                    x_souris = event.pos[0]
                    y_souris = event.pos[1]

                    playerOne.draw()
                    playerTwo.draw()

                    for collide in ground:
                        pygame.draw.rect(surface, ground_color, collide)

                    if debug_mode == 1:
                        surface.blit(text_fps, [10, 10])
                        surface.blit(AB_number, [500, 20])
                        surface.blit(AC_number, [500, 30])
                        surface.blit(vitesse_number, [500, 40])
                        surface.blit(angle_number, [500, 10])
                        surface.blit(weapon_render, [500, 50])
                        surface.blit(wind_render, [500, 60])
                        surface.blit(player_number_render, [500, 70])

                    if player == 1:
                        pygame.draw.line(surface, bullet_color, [playerOne.body.centerx, playerOne.body.centery],[x_souris, y_souris])
                        x0 = playerOne.body.centerx
                        y0 = playerOne.body.centery
                    elif player == 2:
                        pygame.draw.line(surface, bullet_color, [playerTwo.body.centerx, playerTwo.body.centery],[x_souris, y_souris])
                        x0 = playerTwo.body.centerx
                        y0 = playerTwo.body.centery

                    if player == 1:
                        if (y_souris > playerOne.body.y):
                            angle = angle_radian
                        else:
                            angle = -angle_radian
                    elif player == 2:
                        if (y_souris > playerTwo.body.y):
                            angle = angle_radian
                        else:
                            angle = -angle_radian

                    v0 = vitesse * math.cos(angle)
                    w0 = vitesse * math.sin(angle)

                    for i in range(0, 20):
                        if weapon == 0:
                            traj_bullet_x = x0 + v0 * (i*0.5)
                            traj_bullet_y = 0.5 * g * ((i*0.5) ** 2) + w0 * (i*0.5) + y0
                        elif weapon == 1:
                            if AC < 0:
                                traj_bullet_x = x0 + ((v0 / -wind_speed) * (1 - math.exp(wind_speed * i)))
                                traj_bullet_y = y0 + (((w0 / -wind_speed) - (g / (-wind_speed ** 2))) * (1 - math.exp(wind_speed * i))) + ((g * i) / -wind_speed)

                            elif AC > 0:
                                traj_bullet_x = x0 + ((v0 / wind_speed) * (1 - math.exp(-wind_speed * i)))
                                traj_bullet_y = y0 + (((w0 / wind_speed) - (g / (wind_speed ** 2))) * (1 - math.exp(-wind_speed * i))) + ((g * i) / wind_speed)

                        if traj_status == 1:
                            pygame.draw.circle(surface, traj_color, [traj_bullet_x,traj_bullet_y],3)

                    clock.tick(60)

                    pygame.display.flip()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # grenade.play()

                    #affectation de valeur à la variable bullet.x ou bullet.y pour avoir sont point de départ, x0 et y0 point de départ pour les calculs
                    if player == 1:
                        bullet.x = playerOne.body.x
                        bullet.y = playerOne.body.y
                        x0 = playerOne.body.x
                        y0 = playerOne.body.y
                    elif player == 2:
                        bullet.x = playerTwo.body.x
                        bullet.y = playerTwo.body.y
                        x0 = playerTwo.body.x
                        y0 = playerTwo.body.y

                    t = 0

                    #jouer un sons en fonction de l'arme choisie
                    """if weapon == 0:
                        grenade.play()
                    elif weapon ==1 :
                        rocket.play()"""

                    #boucle pour le calcul de trajectoire avec un collision de la bullet avec le sol et l'écran
                    while not bullet.collidelistall(ground) and bullet.x < 640 and bullet.y < 480 and bullet.x>0 and bullet.y>0:
                        time.sleep(.05)
                        surface.fill(ciel)

                        t += 0.5
                        if player == 1:
                            if (y_souris > playerOne.body.y):
                                angle = angle_radian
                            else:
                                angle = -angle_radian
                        elif player == 2:
                            if (y_souris > playerTwo.body.y):
                                angle = angle_radian
                            else:
                                angle = -angle_radian

                        v0 = vitesse * math.cos(angle)
                        w0 = vitesse * math.sin(angle)

                        #calcul des trajectoirs en fonction de l'arme, bullet[1] un peu différent de ce que vue en cours car techiquement on se trouve dans un y négatif dans la réalité avec un origin en bas à gauche
                        if weapon == 0:
                            bullet[0] = x0 + v0 * t
                            bullet[1] = 0.5 * g * (t ** 2) + w0 * t + y0

                        elif weapon == 1:
                            if AC < 0:
                                bullet[0] = x0 + ((v0 /-wind_speed) * (1 - math.exp(wind_speed * t)))
                                bullet[1] = y0 + (((w0 /-wind_speed) - (g / (-wind_speed ** 2))) * (1 - math.exp(wind_speed * t))) + ((g * t) / -wind_speed)

                            elif AC > 0:
                                bullet[0] = x0 + ((v0 / wind_speed) * (1 - math.exp(-wind_speed * t)))
                                bullet[1] = y0 + (((w0 / wind_speed) - (g / (wind_speed ** 2))) * (1 - math.exp(-wind_speed * t))) + ((g * t) / wind_speed)

                        #redessiner la bullet tant quelle n'a pas touché
                        pygame.draw.rect(surface, bullet_color, bullet)
                        playerOne.draw()
                        playerTwo.draw()
                        for collide in ground:
                            pygame.draw.rect(surface, ground_color, collide)

                        pygame.display.flip()

                        #i = 0.5 * g * (t ** 2) + w0 * t + y0

                    #lancement du sons de l'explosion à l'impact
                    explosion.play()

                    j=0
                    #affichage d'un effet d'explosion avec un rayon qui augmente
                    while j<=10:
                        time.sleep(.05)
                        surface.fill(ciel)

                        pygame.draw.circle(surface, traj_color, [bullet[0], bullet[1]], 40+j)
                        playerOne.draw()
                        playerTwo.draw()
                        for collide in ground:
                            pygame.draw.rect(surface, ground_color, collide)
                        pygame.display.flip()

                        j = j+1

                    #si le bullet touche un personnage donc ya une mort meme si on se touche soit meme
                    if bullet[0]+50 >= playerOne.body.x and bullet[0]-50 <= playerOne.body.x and bullet[1]+50>= playerOne.body.y:
                        status_death=1
                        if player == 1:
                            winner = 2
                        elif player == 2:
                            winner = 2

                    if bullet[0]+50 >= playerTwo.body.x and bullet[0]-50 <= playerTwo.body.x and bullet[1]+50>= playerTwo.body.y:
                        status_death=1
                        if player == 2:
                            winner = 1
                        elif player == 1:
                            winner = 1

                    #personne n'est mort donc reset timer et on change de personnage
                    else :
                        timers = time.time()
                        if player == 1 :
                            player = 2
                        elif player == 2:
                            player = 1

        #écran pour afficher le winner et dire que ya une mort et un restart avec enter
        elif status_death == 1:
            surface.fill(ciel)
            death_render = death_font.render(f"Player {winner} win", True, traj_color)
            surface.blit(death_render, [230, 200])
            Return_text = death_font.render(f"Press ENTER to Restart", True, (0, 0, 0))
            surface.blit(Return_text, [100, 270])
            pygame.display.flip()

            keyDownAction()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
                    print("exit")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        status_death=0
                        timers = time.time()
                        playerOne.body.x = random.randint(0,620)
                        playerTwo.body.x = random.randint(0, 620)

