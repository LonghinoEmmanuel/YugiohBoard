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
    ExamplesCard(board.zones)
def draw():
    background(0)
    stroke(255)
    for i in range(len(board.zones)):
        if board.zones[i].content==None:
            board.zones[i].displayZones()
        else:
            board.zones[i].displayCard()
        
class Zone(object):
    def __init__(self,n,o,p):
        self.name=n
        self.state="empty"
        self.content=None
        self.owner=o
        self.extra=False
        self.pos=p
    
    def displayZones(self):
        textAlign(CENTER, CENTER)
        fill(255)
        text(self.name,self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])
        noFill()
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
    
    def displayCard(self):
        if self.content.state==1 or self.content.state==2:
            col=self.content.type.backcolour
            fill(col[0],col[1],col[2])
            stroke(255)
            if self.content.state==1:
               rect(self.pos[0]+(cell-cardSize[1])/2,self.pos[1]+(cell-cardSize[0])/2,cardSize[1],cardSize[0])
            else:
               rect(self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])  
        else:    
            col=self.content.type.colour
            fill(col[0],col[1],col[2])
            stroke(255)
            if self.content.state==3:
                rect(self.pos[0]+(cell-cardSize[1])/2,self.pos[1]+(cell-cardSize[0])/2,cardSize[1],cardSize[0])
            else:
                rect(self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])
            if self.content.special!=None:
                self.drawSpe()
            textAlign(CENTER, CENTER)
            self.printText()
            
    def printText(self):
        if self.content.type.id<2:
            fill(0)
            text(self.content.name,self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])
        elif self.content.type.id==7:
            fill(255)
            monsterText=self.content.name+" Rank:"+str(self.content.stats[0])+" Atk:"+str(self.content.stats[1])+" Def:"+str(self.content.stats[2])
            text(monsterText,self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])
        elif self.content.type.id==8:
            fill(0)
            monsterText=self.content.name+" Link-"+str(self.content.stats[0])+" Atk:"+str(self.content.stats[1])
            text(monsterText,self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])
        else:
            fill(0)
            monsterText=self.content.name+' Level:'+str(self.content.stats[0])+' Atk:'+str(self.content.stats[1])+" Def:"+str(self.content.stats[2])
            text(monsterText,self.pos[0]+(cell-cardSize[0])/2,self.pos[1]+(cell-cardSize[1])/2,cardSize[0],cardSize[1])
    
    def drawSpe(self):
        if self.content.type.pendulumFlag:
            fill(51,142,107)
            noStroke()
            if self.content.state==3:
               rect(self.pos[0]+70,self.pos[1]+26,int(cardSize[1]/2)-1,cardSize[0]-2)
               fill(0)
               text(str(self.content.special),self.pos[0]+120,self.pos[1]+35)
            else:
               rect(self.pos[0]+26,self.pos[1]+70,cardSize[0]-2,int(cardSize[1]/2)-1)
               fill(0)
               text(str(self.content.special),self.pos[0]+35,self.pos[1]+120)
            stroke(255)
        else:
            fill(128,0,0)
            if self.content.special[0]==1:
                rect(self.pos[0]+25,self.pos[1]+5,9,9)
            if self.content.special[1]==1:
                rect(self.pos[0]+65,self.pos[1]+5,9,9)
            if self.content.special[2]==1:
                rect(self.pos[0]+105,self.pos[1]+5,9,9)
            if self.content.special[3]==1:
                rect(self.pos[0]+25,self.pos[1]+65,9,9)
            if self.content.special[4]==1:
                rect(self.pos[0]+105,self.pos[1]+65,9,9)
            if self.content.special[5]==1:
                rect(self.pos[0]+25,self.pos[1]+125,9,9)
            if self.content.special[6]==1:
                rect(self.pos[0]+65,self.pos[1]+125,9,9)
            if self.content.special[7]==1:
                rect(self.pos[0]+105,self.pos[1]+125,9,9)
                
            
            
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

class TypeCard(object):
    def __init__(self):
        self.backcolour=(70,12,0)

class TCtrap(TypeCard):
    def __init__(self):
        super(TCtrap,self).__init__()
        self.id=0
        self.monsterTag=False
        self.colour=(141,11,107)

class TCspell(TypeCard):
    def __init__(self):
        super(TCspell,self).__init__()
        self.id=1
        self.monsterTag=False
        self.colour=(51,142,107)

class TClink(TypeCard):
    def __init__(self):
        super(TClink,self).__init__()
        self.id=8
        self.monsterTag=True
        self.pendulumFlag=False
        self.colour=(3,79,154)
        self.linkrating=0
        self.linkarrows=(0,0,0,0,0,0,0,0)
        
class TCmonster(TypeCard):
    def __init__(self):
        super(TCmonster,self).__init__()
        self.monsterTag=True
        self.pendulumFlag=False

class TCnormal(TCmonster):
    def __init__(self):
        super(TCnormal,self).__init__()
        self.id=2
        self.colour=(177,142,78)
        
class TCeffect(TCmonster):
    def __init__(self):
        super(TCeffect,self).__init__()
        self.id=3
        self.colour=(194,109,28)
        
class TCfusion(TCmonster):
    def __init__(self):
        super(TCfusion,self).__init__()
        self.id=4
        self.colour=(132,83,164)

class TCritual(TCmonster):
    def __init__(self):
        super(TCritual,self).__init__()
        self.id=5
        self.colour=(62,109,165)

class TCsynchro(TCmonster):
    def __init__(self):
        super(TCsynchro,self).__init__()
        self.id=6
        self.colour=(232,228,227)    
        
class TCxyz(TCmonster):
    def __init__(self):
        super(TCxyz,self).__init__()
        self.id=7
        self.colour=(42,46,45)

class TCtoken(TCmonster):
    def __init__(self):
        super(TCtoken,self).__init__()
        self.id=9
        self.colour=(128,128,128)

class Card(object):
    def __init__(self,n,id,stats,pos,spe,s):
        self.name=n
        self.pos=pos
        self.stats=stats
        self.state=s#the state of the card, 0=invisible, 1=down h, 2=down v, 3=up h, 4=up v
        if id==0:
            self.type=TCtrap()
            self.special=None   
        elif id==1:
            self.type=TCspell()
            self.special=None   
        elif id==2:
            self.type=TCnormal()
            if spe!=None:
                self.type.pendulumFlag=True
                self.special=spe
            else:
                self.special=None
        elif id==3:
            self.type=TCeffect()
            if spe!=None:
                self.type.pendulumFlag=True
                self.special=spe
            else:
                self.special=None
        elif id==4:
            self.type=TCfusion()
            if spe!=None:
                self.type.pendulumFlag=True
                self.special=spe
            else:
                self.special=None
        elif id==5:
            self.type=TCritual()
            if spe!=None:
                self.type.pendulumFlag=True
                self.special=spe
            else:
                self.special=None
        elif id==6:
            self.type=TCsynchro()
            if spe!=None:
                self.type.pendulumFlag=True
                self.special=spe
            else:
                self.special=None
        elif id==7:
            self.type=TCxyz()
            if spe!=None:
                self.type.pendulumFlag=True
                self.special=spe
            else:
                self.special=None
        elif id==8:
            self.type=TClink()
            self.special=spe
        elif id==9:
            self.type=TCtoken()    
            self.special=None       

def ExamplesCard(board):
    board[7].content=Card("E-hero FlameWingman",4,(6,2100,1200),7,None,4)
    board[20].content=Card("Relinquished",5,(1,0,0),20,None,3)
    board[21].content=Card("Dark Magician",2,(7,2500,2000),21,None,4)
    board[22].content=Card("Cyber Dragon",3,(5,2100,1600),22,None,4)
    board[23].content=Card("Number 39: Utopia",7,(4,2500,2000),23,None,4)
    board[24].content=Card("Goat Token",9,(1,0,0),24,None,4)
    board[25].content=Card("Odd Eyes Pendulum Dragon",3,(7,2500,2000),25,4,4)
    board[26].content=Card("Pot of Greed",1,None,26,None,4)
    board[27].content=Card("Mirror Force",0,None,27,None,4)
    board[28].content=Card("Magic Cylinder",1,None,28,None,2)
    board[30].content=Card("Stardust Dragon",6,(8,2500,2000),30,None,4)
    board[31].content=Card("Decode Talker",8,(3,2300,None),31,(0,1,0,0,0,1,0,1),4)
