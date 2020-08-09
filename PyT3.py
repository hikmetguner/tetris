import copy,random,pygame,sys
from time import sleep


#GLOBAL VAR
table = [[1 for i in range(13)] if j == 0 or j == 21 else [1 if i == 0 or i == 12 else 0 for i in range(13)] for j in range(22)]
score = 0

class Rect:

    global table

    def __init__(self,x,y,side,color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self):
        object = self

        difference = object.side // 12.5

        pygame.draw.rect(screen, color["light_"+object.color], (object.x,object.y,object.side,object.side))
        pygame.draw.polygon(screen, color["dark_"+object.color], ((object.x+object.side,object.y),(object.x,object.y+object.side),(object.x+object.side,object.y+object.side)))
        pygame.draw.rect(screen, color[object.color], (object.x+difference,object.y+difference,object.side-(difference*2),object.side-(difference*2)))



color_dict = {
    
    1: "gray",

    2: "blue",
    21: "tblue",

    3: "red",
    31: "tred",

    4: "magenta",
    41: "tmagenta",

    5: "cyan",
    51: "tcyan",

    6: "yellow",
    61: "tyellow",

    7: "green",
    71: "tgreen",

    8: "orange",
    81: "torange",

    
    }

color = {
    "black": (0,0,0),
    "white": (255,255,255),

    "gray": (128,128,128),
    "light_gray": (160,160,160),
    "dark_gray": (96,96,96),
    
    "blue": (0,0,204),
    "light_blue": (0,0,255),
    "dark_blue": (0,0,153),

    "tblue": (0,0,0),
    "light_tblue": (0,0,255),
    "dark_tblue": (0,0,153),

    "red": (204,0,0),
    "light_red": (255,0,0),
    "dark_red": (153,0,0),

    "tred": (0,0,0),
    "light_tred": (255,0,0,255),
    "dark_tred": (153,0,0,255),

    "magenta": (204,0,204),
    "light_magenta": (255,0,255),
    "dark_magenta": (153,0,153),

    "tmagenta": (0,0,0),
    "light_tmagenta": (255,0,255),
    "dark_tmagenta": (153,0,153),

    "cyan": (0,204,204),
    "light_cyan": (0,255,255),
    "dark_cyan": (0,153,153),

    "tcyan": (0,0,0),
    "light_tcyan": (0,255,255),
    "dark_tcyan": (0,153,153),

    "yellow": (204,204,0),
    "light_yellow": (255,255,0),
    "dark_yellow": (153,153,0),

    "tyellow": (0,0,0),
    "light_tyellow": (255,255,0),
    "dark_tyellow": (153,153,0),

    "green": (0,204,0),
    "light_green":(0,255,0),
    "dark_green":(0,153,0),

    "tgreen": (0,0,0),
    "light_tgreen":(0,255,0),
    "dark_tgreen":(0,153,0),

    "orange": (255,128,0),
    "light_orange": (255,153,51),
    "dark_orange": (204,102,0),

    "torange": (0,0,0),
    "light_torange": (255,153,51),
    "dark_torange": (204,102,0),
}

#SHAPE CLASSES

class Shape:

    def __init__(self,x,y,n):
        self.x = x
        self.y = y
        self.n = n
        self.t = n*10 + 1

    def move(self):

        canNotMove = False
        for i in [self.node1,self.node2,self.node3,self.node4]:
            if table[i[0]+1][i[1]] in range(1,10) and [i[0]+1,i[1]] not in [self.node1,self.node2,self.node3,self.node4]:
                canNotMove = True
                break
        if not canNotMove:
            for i in [self.node1,self.node2,self.node3,self.node4]:
                table[i[0]][i[1]] = 0
                i[0] += 1

            for i in [self.node1,self.node2,self.node3,self.node4]:
                table[i[0]][i[1]] = self.n

        return canNotMove

    def moveRight(self):

        canNotMove = False
        for i in [self.node1,self.node2,self.node3,self.node4]:
            if table[i[0]][i[1]+1] in range(1,10) and [i[0],i[1]+1] not in [self.node1,self.node2,self.node3,self.node4]:
                canNotMove = True
                break
        if not canNotMove:
            for i in [self.node1,self.node2,self.node3,self.node4]:
                table[i[0]][i[1]] = 0
                i[1] += 1

            for i in [self.node1,self.node2,self.node3,self.node4]:
                table[i[0]][i[1]] = self.n

    def moveLeft(self):

        canNotMove = False
        for i in [self.node1,self.node2,self.node3,self.node4]:
            if table[i[0]][i[1]-1] in range(1,10) and [i[0],i[1]-1] not in [self.node1,self.node2,self.node3,self.node4]:
                canNotMove = True
                break
        if not canNotMove:
            for i in [self.node1,self.node2,self.node3,self.node4]:
                table[i[0]][i[1]] = 0
                i[1] -= 1

            for i in [self.node1,self.node2,self.node3,self.node4]:
                table[i[0]][i[1]] = self.n

    def appear(self):

        canNotAppear = False
        for i in [self.node1,self.node2,self.node3,self.node4]:
            if table[i[0]][i[1]] in range(1,10):
                canNotAppear = True
                continue
            table[i[0]][i[1]] = self.n

        return canNotAppear

    def turn(self):

        nod1 = [self.node3[0] - (self.node1[1]-self.node3[1]) , self.node3[1] + (self.node1[0]-self.node3[0])]
        nod2 = [self.node3[0] - (self.node2[1]-self.node3[1]) , self.node3[1] + (self.node2[0]-self.node3[0])]
        nod4 = [self.node3[0] - (self.node4[1]-self.node3[1]) , self.node3[1] + (self.node4[0]-self.node3[0])]

        for i in [nod1,nod2,nod4]:
            try:
                if table[i[0]][i[1]] in [i if i != self.n else 1 for i in range(1,10)]:
                    return False
            except IndexError:
                return False

        for i in [self.node1,self.node2,self.node3,self.node4]:
            table[i[0]][i[1]] = 0

        self.node1,self.node2,self.node4 = nod1,nod2,nod4

        for i in [self.node1,self.node2,self.node3,self.node4]:
            table[i[0]][i[1]] = self.n

    def slam(self,shadow):
        for i in [self.node1,self.node2,self.node3,self.node4]:
            table[i[0]][i[1]] = 0
        self.node1,self.node2,self.node3,self.node4 = shadow.node1,shadow.node2,shadow.node3,shadow.node4
        self.appear()




#Inverse T
class Shape1(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x],[self.y+1,self.x+1],[self.y+1,self.x],[self.y+1,self.x-1]


#Long
class Shape2(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x+2],[self.y,self.x+1],[self.y,self.x],[self.y,self.x-1]


#Square
class Shape3(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x],[self.y+1,self.x+1],[self.y+1,self.x],[self.y,self.x+1]


#Inverse L starting right
class Shape4(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x],[self.y,self.x-1],[self.y+1,self.x],[self.y+2,self.x]

#inverse L starting left
class Shape5(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x],[self.y,self.x+1],[self.y+1,self.x],[self.y+2,self.x]

#Tetris shape 1
class Shape6(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x],[self.y+1,self.x],[self.y+1,self.x+1],[self.y+2,self.x+1]

#Tetris shape 2
class Shape7(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x],[self.y+1,self.x],[self.y+1,self.x-1],[self.y+2,self.x-1]

class DebugShape(Shape):

    global table

    def __init__(self,x,y,n):
        super().__init__(x,y,n)
        self.node1,self.node2,self.node3,self.node4 = [self.y,self.x],[self.y+1,self.x],[self.y+2,self.x],[self.y+3,self.x]

    def shadow(self):
        shadow = Shadow(self.x,self.y,self.n*10+1)
        canNotMove = False
        while not canNotMove:
            canNotMove = shadow.move(self)

class Shadow():

    global table

    def __init__(self,shape):
        self.shape = copy.deepcopy(shape)
        self.n = self.shape.n*10+1
        self.node1,self.node2,self.node3,self.node4 = self.shape.node1,self.shape.node2,self.shape.node3,self.shape.node4

    def move(self):

        canNotMove = False
        for i in [self.node1,self.node2,self.node3,self.node4]:
            if table[i[0]+1][i[1]] in range(1,10) and [i[0]+1,i[1]] not in [self.shape.node1,self.shape.node2,self.shape.node3,self.shape.node4]:
                canNotMove = True
                break
        if not canNotMove:
            for i in [self.node1,self.node2,self.node3,self.node4]:
                i[0] += 1

        return canNotMove   
    
    def disappear(self):
        for i in [self.node1,self.node2,self.node3,self.node4]:
            if table[i[0]][i[1]] != self.shape.n:
                table[i[0]][i[1]] = 0

    def appear(self):
        for i in [self.node1,self.node2,self.node3,self.node4]:
            if table[i[0]][i[1]] != self.shape.n:
                table[i[0]][i[1]] = self.n

    def showShadow(self):

        canNotMove = False
        while not canNotMove:
            canNotMove = self.move()
        self.appear()





shape_dict = {
    
    1: Shape1(6,1,2),
    2: Shape2(6,1,3),
    3: Shape3(6,1,4),
    4: Shape4(6,1,5),
    5: Shape5(6,1,6),
    6: Shape6(6,1,7),
    7: Shape7(6,1,8),
    "d": DebugShape(6,1,5),
    
    }

#PYGAME

pygame.init()

screen_heigth = screen_width = 600
screen = pygame.display.set_mode((screen_width,screen_heigth))
font = pygame.font.SysFont("Consolas",30)
pygame.display.set_caption("PyTetris v1.2")
screen.fill(color["black"])

#DRAWING STUFF WITH PYGAME

def draw(t):
    global screen_heigth

    table = t

    dif = screen_heigth // 24

    for i in range(len(table)):
        for j in range(len(table[-1])):
            if table[i][j] == 0:
                continue
            temp = Rect((j+1)*dif,(i+1)*dif,dif,color_dict[table[i][j]])
            temp.draw()
    pygame.display.update()

#TILE SPAWN

last = []
def spawn():

    global last
    
    while len(last) < 2:
        number = random.randrange(1,8,1)
        if number in last:
            while number in last:
                number = random.randrange(1,8,1)
        last.append(number)


    #ENABLE TO DEBUG

    #last = ["d","d"]

    return copy.deepcopy(shape_dict[last.pop(0)])


#CHECK BLOCK
def checkWin():
    global table,score

    toDel = []

    for i in range(22):
        if i == 0 or i == 21:
            continue
        if 0 not in table[i]:
            toDel.append(i)

    for i in toDel:
        table[i] = [1 if i == 0 or i == 12 else 0 for i in range(13)]


    if toDel != []:
        score += 100000 *(1 + 0.25 * len(toDel))
        moveDown()
        checkWin()

    return toDel != []

#SHOW NEXT BLOCK
def showNextBlock(shape):
    global screen_heigth

    nextShape = copy.deepcopy(shape)

    next = [[0 for i in range(6)] for j in range(6)]
    main = nextShape.node3

    y = 2-main[0]
    x = 2-main[1]
    for i in [nextShape.node1,nextShape.node2,nextShape.node3,nextShape.node4]:
        i[0] += y
        i[1] += x

    for i in [nextShape.node1,nextShape.node2,nextShape.node3,nextShape.node4]:
        next[i[0]][i[1]] = nextShape.n

    table = next

    dif = screen_heigth // 24

    text("Next:",(screen_heigth//100 * 3),dif*15-10,dif*4,"white")

    for i in range(len(table)):
        for j in range(len(table[-1])):
            if table[i][j] == 0:
                continue
            temp = Rect((j+1)*dif+dif*15,(i+3)*dif,dif,color_dict[table[i][j]])
            temp.draw()

#MOVE EVERYTHING DOWN
def moveDown():

    global table

    toMove = []

    for i in range(20,1,-1):
        if table[i+1] == [1 if i == 0 or i == 12 else 0 for i in range(13)] and table[i] != [1 if i == 0 or i == 12 else 0 for i in range(13)]:
            toMove.append(i)

    for i in toMove:
        table[i+1] = table[i]
        table[i] = [1 if i == 0 or i == 12 else 0 for i in range(13)]

    if toMove != []:
        moveDown()

#CREATE TEXT ON SCREEN
def text(string,size,x,y,c):

    global screen,color

    f = pygame.font.SysFont("Consolas",size)
    l = f.render(string,1,color[c])
    screen.blit(l,(x,y))




#START MENU
def startMenu():

    global table,score

    table = [[1 for i in range(13)] if j == 0 or j == 21 else [1 if i == 0 or i == 12 else 0 for i in range(13)] for j in range(22)]
    score = 0

    string = """0 0 0 0 0 0 0 5 5 5 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 0 0 5 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 0 0 5 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 5 5 0 0 6 0 6 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 0 0 0 0 6 0 6 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 0 0 0 0 0 6 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 5 0 0 0 6 6 0 0 0 0 0 0 0 0 0
3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0 0 6 0 0 0 0
0 0 3 0 0 0 0 0 0 0 7 0 0 0 0 0 0 0 0 0 0 0
0 0 3 0 0 4 4 4 0 7 7 7 0 8 8 8 0 6 0 3 3 3
0 0 3 0 0 4 0 4 0 0 7 0 0 8 0 0 0 6 0 3 0 0
0 0 3 0 0 4 4 4 0 0 7 0 0 8 0 0 0 6 0 3 3 3
0 0 3 0 0 4 0 0 0 0 7 0 0 8 0 0 0 6 0 0 0 3
0 0 3 0 0 4 4 4 0 0 7 7 0 8 0 0 0 6 0 3 3 3"""

    start_table = [[int(j) for j in i.split(" ")] for i in string.split("\n")]
    t = 1/60
    selection = 1
    while True:


        if selection == 2:
            text(">",(screen_heigth//100 * 4),(screen_heigth//100 * 42),(screen_heigth//100 * 80),"white")
        else:
            text(">",(screen_heigth//100 * 4),(screen_heigth//100 * 42),(screen_heigth//100 * 70),"white")

        text("Play",(screen_heigth//100 * 4),(screen_heigth//100 * 45),(screen_heigth//100 * 70),"white")
        text("Exit",(screen_heigth//100 * 4),(screen_heigth//100 * 45),(screen_heigth//100 * 80),"white")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selection == 1:
                        game()
                    else:
                        pygame.quit()
                        sys.exit(0)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    if selection == 1:
                        selection = 2
                    elif selection == 2:
                        selection = 1

        draw(start_table)
        sleep(t)
        screen.fill(color["black"])



#LOSE SCREEN


def loseScreen():
    string = """0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 1 0 1 1 1 1 0 1 0 0 1 0 0 0
0 0 0 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 0 0
0 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 1 0 0 0
0 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 1 0 0 0
0 0 0 1 1 1 1 0 1 1 1 1 0 1 1 1 1 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
0 1 0 0 0 0 1 1 1 1 0 1 1 1 1 0 1 1 1 0
0 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 0
0 1 0 0 0 0 1 0 0 1 0 1 1 1 1 0 0 1 0 0
0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0
0 1 1 1 1 0 1 1 1 1 0 1 1 1 1 0 0 1 1 0"""

    lose_table = [[int(j) for j in i.split(" ")] for i in string.split("\n")]

    t = 1/60
    selection = 1

    while True:
        
        if selection == 2:
            text(">",(screen_heigth//100 * 3),(screen_heigth//100 * 37),(screen_heigth//100 * 85),"white")
        else:
            text(">",(screen_heigth//100 * 3),(screen_heigth//100 * 37),(screen_heigth//100 * 80),"white")

        text(f"Score : {int(score)}",(screen_heigth//100 * 3),(screen_heigth//100 * 35),(screen_heigth//100 * 70),"white")
        text("Replay",(screen_heigth//100 * 3),(screen_heigth//100 * 40),(screen_heigth//100 * 80),"white")
        text("Exit",(screen_heigth//100 * 3),(screen_heigth//100 * 40),(screen_heigth//100 * 85),"white")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selection == 1:
                        startMenu()
                    else:
                        pygame.quit()
                        sys.exit(0)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    if selection == 1:
                        selection = 2
                    elif selection == 2:
                        selection = 1

        draw(lose_table)
        sleep(t)
        screen.fill(color["black"])


game_difficulty = 30
def game():

    global game_difficulty,table,score,screen_heigth,last

    current = None
    turn = 0
    playing = True
    t = 1/60
    difficulty = game_difficulty

    while playing:
        if current == None:
            current = spawn()
            if current.appear():
                playing = False
                break
            continue

        showNextBlock(shape_dict[last[-1]])

        text(f"Score: {int(score)}",(screen_heigth//100 * 3),screen_heigth//100 * 70, screen_heigth//100 * 50,"white")
        text(f"Made by Hikmet Güner",(screen_heigth//100 * 3),screen_heigth//100 * 62, screen_heigth//100 * 80,"white")

        shadow = Shadow(current)
        shadow.showShadow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif current == None:
                continue
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    current.moveRight()
                elif event.key == pygame.K_UP:
                    current.turn()
                elif event.key == pygame.K_SPACE:
                    current.slam(shadow)
                    checkWin()
                    current = None
                    continue
                elif event.key == pygame.K_DOWN:
                    difficulty = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    difficulty = game_difficulty

        if current == None:
            continue

        if turn % difficulty == 0:
            if current.move():
                if turn == 30:
                    playing = False
                current = None
                turn = 0
                checkWin()
                continue

        draw(table)
        shadow.disappear()

        turn += 1
        sleep(t)

        screen.fill(color["black"])

    loseScreen()
    return playing
      
startMenu()
