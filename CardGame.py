#git push -u origin main
#git add --all
#git commit -m "nombre del cambio"
from tkinter import *
from PIL import ImageTk, Image
import random
import time
import tkinter as tk

root = Tk()
root.attributes('-fullscreen', True)


screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
print(screenWidth)
print(screenHeight)

canva = Canvas(root, width=screenWidth, height=screenHeight)
canva.pack(fill="both", expand=True)

panelImage = Image.open("Grass.png")
panelFinal = panelImage.resize((screenWidth,screenHeight))
panel_Tk = ImageTk.PhotoImage(panelFinal)

canva.create_image(0,0, anchor="nw", image=panel_Tk)

#cards

cards_clubs = []
cards_diamonds = []
cards_hearts = []
cards_spades = []
positionx = [160,290,420,550,680,810,940]
positiony = [200,240,280,320,360,400,440,480,520,560,600,640,680,720,40]

#movement
Coords = [0]*2

def start_drag(event):
    global dragging_label
    dragging_label = event.widget
    dragging_label.start_x = event.x
    dragging_label.start_y = event.y
    
def on_drag(event):
    if dragging_label is not None:
        x = dragging_label.winfo_x() - dragging_label.start_x + event.x
        y = dragging_label.winfo_y() - dragging_label.start_y + event.y
        dragging_label.place(x=x, y=y)
        Coords[0]=x
        Coords[1]=y

def stop_drag(event):
    global dragging_label
    dragging_label = None
    Coords[0]=None
    Coords[1]=None


def follow_mouse(event):
    x = event.x_root - root.winfo_rootx()
    y = event.y_root - root.winfo_rooty()
    blankBox.place(x=x, y=y)

#back


cardBack = Image.open("Back.png")
cardBackFinal = cardBack.resize((100,141))
cardBack_Tk = ImageTk.PhotoImage(cardBackFinal)

for index in range(1,14,1):
    card = Image.open(str(index)+"_of_clubs.png")
    cardFinal = card.resize((100,141))
    card_Tk = ImageTk.PhotoImage(cardFinal)
    cards_clubs.append(card_Tk)
    
for index in range(1,14,1):
    card = Image.open(str(index)+"_of_diamonds.png")
    cardFinal = card.resize((100,141))
    card_Tk = ImageTk.PhotoImage(cardFinal)
    cards_diamonds.append(card_Tk)
    
for index in range(1,14,1):
    card = Image.open(str(index)+"_of_hearts.png")
    cardFinal = card.resize((100,141))
    card_Tk = ImageTk.PhotoImage(cardFinal)
    cards_hearts.append(card_Tk)
    
for index in range(1,14,1):
    card = Image.open(str(index)+"_of_spades.png")
    cardFinal = card.resize((100,141))
    card_Tk = ImageTk.PhotoImage(cardFinal)
    cards_spades.append(card_Tk)
    
allCards = []

for index in range(0,52,1):
    if(index<13):
        allCards.append(cards_clubs[index])
    elif(index<26 and index>=13):
        allCards.append(cards_hearts[index-13])
    elif(index<39 and index>=26):
        allCards.append(cards_spades[index-26])
    elif(index<52 and index>=39):
        allCards.append(cards_diamonds[index-39])

xcor = []
ycor = []

row1 = [None]
row2 = [None]*2
row3 = [None]*3
row4 = [None]*4
row5 = [None]*5
row6 = [None]*6
row7 = [None]*7

rowValues1 = [None]
rowValues2 = [None]*2
rowValues3 = [None]*3
rowValues4 = [None]*4
rowValues5 = [None]*5
rowValues6 = [None]*6
rowValues7 = [None]*7

randomNums = random.sample(range(0,52),52)
randomlyChosenCards = []
cardsValues = []

for index in range (0,52,1):
    cardsValues.append(randomNums[index])
    randomlyChosenCards.append(allCards[randomNums[index]])

row1[0] = randomlyChosenCards[0]

label = Label(root, image=randomlyChosenCards[0])
label.place(x=positionx[0],y=positiony[0])
label.bind("<ButtonPress-1>", start_drag)
label.bind("<B1-Motion>", on_drag)
row1[0] = label

row2[0] = randomlyChosenCards[1]
row2[1] = randomlyChosenCards[2]
row3[0] = randomlyChosenCards[3]
row3[1] = randomlyChosenCards[4]
row3[2] = randomlyChosenCards[5]
row4[0] = randomlyChosenCards[6]
row4[1] = randomlyChosenCards[7]
row4[2] = randomlyChosenCards[8]
row4[3] = randomlyChosenCards[9]
row5[0] = randomlyChosenCards[10]
row5[1] = randomlyChosenCards[11]
row5[2] = randomlyChosenCards[12]
row5[3] = randomlyChosenCards[13]
row5[4] = randomlyChosenCards[14]
row6[0] = randomlyChosenCards[15]
row6[1] = randomlyChosenCards[16]
row6[2] = randomlyChosenCards[17]
row6[3] = randomlyChosenCards[18]
row6[4] = randomlyChosenCards[19]
row6[5] = randomlyChosenCards[20]
row7[0] = randomlyChosenCards[21]
row7[1] = randomlyChosenCards[22]
row7[2] = randomlyChosenCards[23]
row7[3] = randomlyChosenCards[24]
row7[4] = randomlyChosenCards[25]
row7[5] = randomlyChosenCards[26]
row7[6] = randomlyChosenCards[27]

rowValues1[0] = randomNums[0]
rowValues2[0] = randomNums[1]
rowValues2[1] = randomNums[2]
rowValues3[0] = randomNums[3]
rowValues3[1] = randomNums[4]
rowValues3[2] = randomNums[5]
rowValues4[0] = randomNums[6]
rowValues4[1] = randomNums[7]
rowValues4[2] = randomNums[8]
rowValues4[3] = randomNums[9]
rowValues5[0] = randomNums[10]
rowValues5[1] = randomNums[11]
rowValues5[2] = randomNums[12]
rowValues5[3] = randomNums[13]
rowValues5[4] = randomNums[14]
rowValues6[0] = randomNums[15]
rowValues6[1] = randomNums[16]
rowValues6[2] = randomNums[17]
rowValues6[3] = randomNums[18]
rowValues6[4] = randomNums[19]
rowValues6[5] = randomNums[20]
rowValues7[0] = randomNums[21]
rowValues7[1] = randomNums[22]
rowValues7[2] = randomNums[23]
rowValues7[3] = randomNums[24]
rowValues7[4] = randomNums[25]
rowValues7[5] = randomNums[26]
rowValues7[6] = randomNums[27]

def createRow(row,ind,Sum):
    for index in range (0,len(row),1):
        label = Label(root, image=randomlyChosenCards[index+Sum])
        label.place(x=positionx[ind],y=positiony[index])
        row[index] = label
        if index == len(row)-1:
            row[index].bind("<ButtonPress-1>", start_drag)
            row[index].bind("<B1-Motion>", on_drag)
            row[index].bind("<ButtonRelease-1>",stop_drag)
        else:
            row[index].pack_forget()
            backLabel = Label(root, image=cardBack_Tk)
            backLabel.place(x=positionx[ind],y=positiony[index])

createRow(row2,1,1)
createRow(row3,2,3)
createRow(row4,3,6)
createRow(row5,4,10)
createRow(row6,5,15)
createRow(row7,6,21)

blankBox = Label()

def coordsInfo():
    text="x="+str(Coords[0])+"    y="+str(Coords[1])+"   Condition"+str(val)
    blankBox = Label(root, text=text)
    blankBox.place(x=0,y=0)
    root.after(60,coordsInfo)

val = False

BobMarley = Label()

def coordsValue():
    text="x="+str(row2[-1].winfo_x())+"   y="+str(row2[-1].winfo_y())
    BobMarley = Label(root, text=text)
    BobMarley.place(x=0,y=50)
    root.after(60,coordsValue)

val = False

def validateRow(rowValues,row):

    if(rowValues[-1]>38):
        rowValues[-1]-=26
        
    elif(rowValues[-1]<13):
        rowValues[-1]+=26
        
    if (rowValues != rowValues1 and (rowValues[-1] == rowValues1[-1]-14 or rowValues[-1] == rowValues1[-1]+12) and (Coords[0]+50>=positionx[0] and Coords[0]-50<=positionx[0]) and (Coords[1]+72>=positiony[len(row1)-1] and Coords[1]-72<=positiony[len(row1)-1])):
        rowValues1.append(rowValues[-1])
        print(Coords[0])
        del rowValues[-1]
        row1.append(row[-1])
        del row[-1]
        row1[-1].place(x=positionx[0],y=positiony[len(row1)])
        val = True
        
    elif (rowValues != rowValues2 and (rowValues[-1] == rowValues2[-1]-14 or rowValues[-1] == rowValues2[-1]+12) and (Coords[0]+50>=positionx[1] and Coords[0]-50<=positionx[1]) and (Coords[1]+72>=positiony[len(row2)-1] and Coords[1]-72<=positiony[len(row2)-1])):
        rowValues2.append(rowValues[-1])
        print(Coords[0])
        del rowValues[-1]
        row2.append(row[-1])
        del row[-1]
        row2[-1].place(x=positionx[1],y=positiony[len(row2)])
        val = True
        
    elif (rowValues != rowValues3 and (rowValues[-1] == rowValues3[-1]-14 or rowValues[-1] == rowValues3[-1]+12) and (Coords[0]+50>=positionx[2] and Coords[0]-50<=positionx[2]) and (Coords[1]+72>=positiony[len(row3)-1] and Coords[1]-72<=positiony[len(row3)-1])):
        rowValues1.append(rowValues[-1])
        print(Coords[0])
        del rowValues[-1]
        row3.append(row[-1])
        del row[-1]
        row3[-1].place(x=positionx[2],y=positiony[len(row3)])
        val = True
        
    elif (rowValues != rowValues4 and (rowValues[-1] == rowValues4[-1]-14 or rowValues[-1] == rowValues4[-1]+12) and (Coords[0]+50>=positionx[3] and Coords[0]-50<=positionx[3]) and (Coords[1]+72>=positiony[len(row4)-1] and Coords[1]-72<=positiony[len(row4)-1])):
        rowValues1.append(rowValues[-1])
        print(Coords[0])
        del rowValues[-1]
        row4.append(row[-1])
        del row[-1]
        row4[-1].place(x=positionx[3],y=positiony[len(row4)])
        val = True
        
    elif (rowValues != rowValues5 and (rowValues[-1] == rowValues5[-1]-14 or rowValues[-1] == rowValues5[-1]+12) and (Coords[0]+50>=positionx[4] and Coords[0]-50<=positionx[4]) and (Coords[1]+72>=positiony[len(row5)-1] and Coords[1]-72<=positiony[len(row5)-1])):
        rowValues1.append(rowValues[-1])
        print(Coords[0])
        del rowValues[-1]
        row5.append(row[-1])
        del row[-1]
        row5[-1].place(x=positionx[4],y=positiony[len(row5)])
        val = True
        
    elif (rowValues != rowValues6 and (rowValues[-1] == rowValues6[-1]-14 or rowValues[-1] == rowValues6[-1]+12) and (Coords[0]+50>=positionx[5] and Coords[0]-50<=positionx[5]) and (Coords[1]+72>=positiony[len(row6)-1] and Coords[1]-72<=positiony[len(row6)-1])):
        rowValues6.append(rowValues[-1])
        print(Coords[0])
        del rowValues[-1]
        row6.append(row[-1])
        del row[-1]
        row6[-1].place(x=positionx[5],y=positiony[len(row6)])
        val = True
        
    elif (rowValues != rowValues7 and (rowValues[-1] == rowValues7[-1]-14 or rowValues[-1] == rowValues7[-1]+12) and (Coords[0]+50>=positionx[6] and Coords[0]-50<=positionx[6]) and (Coords[1]+72>=positiony[len(row7)-1] and Coords[1]-72<=positiony[len(row7)-1])):
        rowValues7.append(rowValues[-1])
        print(Coords[0])
        del rowValues[-1]
        row7.append(row[-1])
        del row[-1]
        row7[-1].place(x=positionx[6],y=positiony[len(row7)])
        val = True
        
    else:
        row[-1].place(x=row[-1].winfo_x(),y=row[-1].winfo_y())
        val = False
    root.after(30,validateRow)
    
coordsValue()
validateRow(rowValues1,row1)
validateRow(rowValues2,row2)
validateRow(rowValues3,row3)
validateRow(rowValues4,row4)
validateRow(rowValues5,row5)
validateRow(rowValues6,row6)
validateRow(rowValues7,row7)

row_clubs=[]
row_diamonds=[]
row_hearts=[]
row_spades=[]

for index in range (0,25,1):
    label = tk.Label(root, image=randomlyChosenCards[index+27])
    label.place(x=positionx[0],y=positiony[-1])

coordsInfo()

root.mainloop()


