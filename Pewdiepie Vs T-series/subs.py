import urllib.request,json,pygame,sys


key = " "#INSERT GOOGLE API KEY HERE

def displayText():

        black = (0,0,0 )
        pygame.init()
        pygame.display.set_caption("Pewdiepie VS T-series")
        screen_width = 800
        screen_height = 300
        screen = pygame.display.set_mode([screen_width,screen_height])

        font = pygame.font.Font("roboto/Roboto-Regular.ttf", 50)

        count_pos = [100,20]
        count1_pos = [100, 80]
        difference_pos = [20,160]
        pew_logo = pygame.image.load('pew_logo.png')
        t_logo = pygame.image.load('t_logo.png')
        while True:#MAIN LOOP
                pewdiepie = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
                t_series = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+key).read()
                subs_pew = json.loads(pewdiepie)["items"][0]["statistics"]["subscriberCount"]
                subs_pew = int(subs_pew)
                subs_t = json.loads(t_series)["items"][0]["statistics"]["subscriberCount"]
                subs_t = int(subs_t)
                count = str("Pewdiepie: "+" "*5+ "{:,d}".format(int(subs_pew)) + " subs")
                count1 = str("T-series: " + " "*9+"{:,d}".format(int(subs_t)) + " subs")

                difference = str(" "*15+"difference:"+" "*10+"{:,d}".format(int(max(subs_t, subs_pew) - min(subs_t, subs_pew))))

                difference_render = font.render(difference,1,(255,255,255))

                count_render = font.render(count, 1, (255, 255, 255))
                count1_render = font.render(count1,1,(255,255,255))
                for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                                sys.exit()

                screen.fill(black)
                screen.blit(count_render,count_pos)
                screen.blit(count1_render,count1_pos)
                screen.blit(difference_render,difference_pos)
                screen.blit(pew_logo,[20,19])
                screen.blit(t_logo,[25,90])
                pygame.display.update()
                pygame.time.wait(2500)# slows down the iteration of the loop

displayText()