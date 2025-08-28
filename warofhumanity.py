import pygame,pyautogui,random
pygame.init()
WIDTH,HEIGHT=pyautogui.size()

warzone=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("war of humanity")

#ship dimensions
sw,sh=WIDTH/16,HEIGHT/9

#images
bg=pygame.transform.scale(pygame.image.load("spacebg.jpg"),(WIDTH,HEIGHT))
sp1=pygame.transform.scale(pygame.image.load("protector.png"),(sw,sh))
sp1=pygame.transform.rotate(sp1,90)
sp2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("invader.png"),(sw,sh)),-90)
BORDER=pygame.Rect(WIDTH/2-10,0,20,HEIGHT)
def red_movement(key_pressed,red):
    if key_pressed[pygame.K_a] and red.x>0:
        red.x-=5
    if key_pressed[pygame.K_d] and red.x+red.width<BORDER.x:
        red.x+=5
    if key_pressed[pygame.K_w] and red.y>0:
        red.y-=5
    if key_pressed[pygame.K_s] and red.y+red.height<HEIGHT:
        red.y+=5
    

def yellow_movement(key_pressed,yellow):
    if key_pressed[pygame.K_j] and yellow.x>BORDER.x+BORDER.width:
        yellow.x-=5
    if key_pressed[pygame.K_l] and yellow.x<WIDTH-yellow.width:
        yellow.x+=5
    if key_pressed[pygame.K_i] and yellow.y>0:
        yellow.y-=5
    if key_pressed[pygame.K_k] and yellow.y+yellow.height<HEIGHT:
        yellow.y+=5
#display
def display_window(red,yellow):
    warzone.blit(bg,(0,0))
    warzone.blit(sp1,(red.x,red.y))
    warzone.blit(sp2,(yellow.x,yellow.y))
    pygame.draw.rect(warzone,"red",BORDER)
    #pygame.draw.rect(warzone,"blue",red)
    #pygame.draw.rect(warzone,"yellow",yellow)

    pygame.display.update()
    #print(sp1)


#main execution
def main():
    red=pygame.Rect(100,HEIGHT/2,sw,sh)
    yellow=pygame.Rect(WIDTH-100,HEIGHT/2,sw,sh)
    red_bullets=[]
    yellow_bullets=[]
    red_health=10
    yellow_health=10
    gameover=False
    while not gameover:
        for e in pygame.event.get():
            print(e)
            if e.type==pygame.QUIT:
                pygame.quit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_e:
                    bullet=pygame.Rect(red.x+red.width,red.y+red.height/2,10,2)
                    red_bullets.append(bullet)

        key_pressed=pygame.key.get_pressed()
        
        red_movement(key_pressed,red)
        yellow_movement(key_pressed,yellow)

        display_window(red,yellow)
main()

