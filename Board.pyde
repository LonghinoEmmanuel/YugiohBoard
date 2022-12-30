class Board(object):
    def __init__(self):
        self.zones=[]      
        
cell=139
cardSize=(89,129)
board=Board()

def setup():    
    size(cell*7,cell*5)
    fill(255, 204)
    noStroke()
    CreateBoard(board.zones)

def draw():
    background(0)
    stroke(255)
    for i in range(len(board.zones)):
        board.zones[i].display()
        
class Zone(object):
    def __init__(self,n,o,p):
        self.name=n
        self.state="empty"
        self.content=None
        self.owner=o
        self.extra=False
        self.pos=p
    
    def display(self):
        noFill()
        #print("entre")
        textAlign(CENTER, CENTER)
        text(self.name,self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])
        if self.name=="Main Monster Zone":
            stroke(128)
            rect(self.pos[0]+(cell-cardSize[1])/2,self.pos[1]+(cell-cardSize[0])/2,cardSize[1],cardSize[0])
            stroke(255)
            rect(self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])    
        elif self.name=="Banished Zone":
            stroke(128)
            rect(self.pos[0]+(cell-cardSize[1])/2,self.pos[1]+(cell-cardSize[0])/2,cardSize[1],cardSize[0])
        else:
            rect(self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])

def CreateBoard(board):
    board.append(Zone("Main Deck Zone",1,(cell*0,cell*0)))
    board.append(Zone("Extra Deck Zone",1,(cell*6,cell*0)))
    board.append(Zone("Graveyard Zone",1,(cell*0,cell*1)))
    board.append(Zone("Field Card Zone",1,(cell*6,cell*1)))
    board.append(Zone("Banished Zone",1,(cell*0,cell*2)))
    board.append(Zone("Main Monster Zone",1,(cell*1,cell*1)))
    board.append(Zone("Main Monster Zone",1,(cell*2,cell*1)))
    board.append(Zone("Main Monster Zone",1,(cell*3,cell*1)))
    board.append(Zone("Main Monster Zone",1,(cell*4,cell*1)))
    board.append(Zone("Main Monster Zone",1,(cell*5,cell*1)))
    board.append(Zone("Spell and Trap Zone",1,(cell*1,cell*0)))
    board.append(Zone("Spell and Trap Zone",1,(cell*2,cell*0)))
    board.append(Zone("Spell and Trap Zone",1,(cell*3,cell*0)))
    board.append(Zone("Spell and Trap Zone",1,(cell*4,cell*0)))
    board.append(Zone("Spell and Trap Zone",1,(cell*5,cell*0)))
    board.append(Zone("Main Deck Zone",2,(cell*6,cell*4)))
    board.append(Zone("Extra Deck Zone",2,(cell*0,cell*4)))
    board.append(Zone("Graveyard Zone",2,(cell*6,cell*3)))
    board.append(Zone("Field Card Zone",2,(cell*0,cell*3)))
    board.append(Zone("Banished Zone",2,(cell*6,cell*2)))
    board.append(Zone("Main Monster Zone",2,(cell*5,cell*3)))
    board.append(Zone("Main Monster Zone",2,(cell*4,cell*3)))
    board.append(Zone("Main Monster Zone",2,(cell*3,cell*3)))
    board.append(Zone("Main Monster Zone",2,(cell*2,cell*3)))
    board.append(Zone("Main Monster Zone",2,(cell*1,cell*3)))
    board.append(Zone("Spell and Trap Zone",2,(cell*5,cell*4)))
    board.append(Zone("Spell and Trap Zone",2,(cell*4,cell*4)))
    board.append(Zone("Spell and Trap Zone",2,(cell*3,cell*4)))
    board.append(Zone("Spell and Trap Zone",2,(cell*2,cell*4)))
    board.append(Zone("Spell and Trap Zone",2,(cell*1,cell*4)))
    board.append(Zone("Extra Monster Zone",2,(cell*2,cell*2)))
    board.append(Zone("Extra Monster Zone",2,(cell*4,cell*2)))
