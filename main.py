import pygame, random, copy
w, h = 500, 500
cellsize = 10
cells = []
pygame.init()
clock = pygame.time.Clock()
width, height = (w // cellsize), (h // cellsize)
drag=False
width = int(width)
height = int(height)
pygame.display.set_caption("Space to begin/pause")
dis = pygame.display.set_mode((w, h))
dis.fill((0, 0, 0))

randomBool = []


def start():
  cellPc = 0.2
  for y in range(height + 1):
      randomBool.append([])
      for x in range(width + 1):
          if random.random() < cellPc:
              randomBool[y].append(True)
          else:
              randomBool[y].append(False)


#sojipo ajs;koojihhasuiio h;asjioasddfoiaidhoiiosaiof


            
def die():
    global randomBool
    global height
    global width
    temp = copy.deepcopy(randomBool)
    for y in range(height):
        for x in range(width):
            count = 0
            if randomBool[y - 1][x - 1] == True:
                count += 1
              
            if randomBool[y - 1][x] == True:
                count += 1
     
            if randomBool[y - 1][x + 1] == True:
                count += 1

            if randomBool[y + 1][x - 1] == True:
                count += 1
            
            if randomBool[y + 1][x] == True:
                count += 1
             
            if randomBool[y + 1][x + 1] == True:
                count += 1
              
            if randomBool[y][x - 1] == True:
                count += 1
               
            if randomBool[y][x + 1] == True:
                count += 1
            if randomBool[y][x] and count == 2:
                    temp[y][x] = True
            elif count == 3:
                    temp[y][x] = True
            else:
                    temp[y][x] = False
              
            
    randomBool = temp




def addcell():
  global randomBool
  global width
  global height
  (x,y)=pygame.mouse.get_pos()
  (x,y)=(x//cellsize,y//cellsize)
  try:
    randomBool[y].append([x])
    randomBool[y][x]=True
  except:
    print("error")
  




def draw():
  dis.fill((0, 0, 0))
  for y in range(height):
        for x in range(width):
            if randomBool[y][x] == True:
                pygame.draw.rect(dis, (255, 0, 0),(((x * cellsize),(y * cellsize), cellsize, cellsize)))
  for x in range(0, w, cellsize):
        pygame.draw.line(dis, (0, 25, 0), (x, 0), (x, h))
  for y in range(0, h, cellsize):
        pygame.draw.line(dis, (0, 25, 0), (0, y), (w, y))

running = True
running2=True

start()
while running:
  if running2 == True:
    die()
  clock.tick(10)
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
        if event.type==pygame.MOUSEMOTION and drag==True:
            addcell()
        if event.type==pygame.MOUSEBUTTONUP:
            drag=False
            addcell()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
            if running2 == True:
              running2 = False
            else:
              running2 = True
  draw()
  pygame.display.update()
