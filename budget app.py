from tkinter import*
import Categories

root=Tk()
root.geometry("900x900")

Appname=Label(root,text="Daily Life Budget")

def displayBudget():
  if sumTotal()==True:

def displayActual():

def addFoodItem():

def takeData():

def seeBudget():

def enterActual():

def createBudget():
#push new budgets to budgets window
    budgetCreated=Button(CrtdBudgeFrame,text="",  command=seeBudget)
    budgetCreated.pack()
    actualBudget=Button(actualSpentFrame, text="", command=enterActual)
    actualBudget.pack()

NewButton=Button(root,text="Create New Budget +" command=displayNew)
NewButton.pack(side=LEFT)

BudgetButton=Button(root,text="Budgets",command=displayBudget)
BudgetButton.pack(side=RIGHT)

ActualBudgetButton=Button(root,text="Actual Spent", command=displayActual)
ActualBudgetButton.pack(side=RIGHT)

#the new budget window
BudgetLabelFrame=Labelframe(root,text=New Budget)
BudgetLabelFrame.pack()

FoodLabel=Label(BudgetLabelFrame,text="Food")
FoodLabel.pack()
FoodItem=Entry(BudgetLabelFrame,"item")
FoodItem.pack(side=LEFT)
FoodItemAmount=Entry(BudgetLabelFrame,bd=2)
FoodItemAmount.pack(side=RIGHT)
NewItemButton=Button(BudgetLabelFrame,text="+", command=addFoodItem)
NewItemButton.pack()

ClothsLabel=Label(BudgetLabelFrame,text="Clothes")
ClothsLabel.pack()
ClothItem=Entry(BudgetLabelFrame,"item")
ClothItem.pack(side=LEFT)
ClothItemAmount=Entry(BudgetLabelFrame,bd=2)
ClothItemAmount.pack(side=RIGHT)
NewItemButton=Button(BudgetLabelFrame,text="+", command=addFoodItem)
NewItemButton.pack()

AutoLabel=Label(BudgetLabelFrame,text="Auto")
AutoLabel.pack()
AutoItem=Entry(BudgetLabelFrame,"item")
AutoItem.pack(side=LEFT)
AutoItemAmount=Entry(BudgetLabelFrame,"item amount")
AutoItemAmount.pack(side=RIGHT)
NewItemButton=Button(BudgetLabelFrame,text="+", command=addFoodItem)
NewItemButton.pack()

HouseLabel=Label(BudgetLabelFrame,text="House Expenses")
HouseLabel .pack()
HouseItem=Entry(BudgetLabelFrame,"item")
HouseItem.pack(side=LEFT)
HouseItemAmount=Entry(BudgetLabelFrame,"item amount")
HouseItemAmount.pack(side=RIGHT)
NewItemButton=Button(BudgetLabelFrame,text="+", command=addFoodItem)
NewItemButton.pack()

MiscLabel=Label(BudgetLabelFrame,text="Miscellaneous")
MiscLabel.pack()
MiscItem=Entry(BudgetLabelFrame,"item")
MiscItem.pack(side=LEFT)
MiscItemAmount=Entry(BudgetLabelFrame,"item amount")
MiscItemAmount.pack(side=RIGHT)
NewItemButton=Button(BudgetLabelFrame,text="+", command=addFoodItem)
NewItemButton.pack()

Totalabel=Label(BudgetLabelFrame,text="Total" )
Totalabel.pack()
Total=Entry(BudgetLabelFrame, bd=0)
Total.pack()

CreateBudget=Button(BudgetLabelFrame, text="Create Budget", bg="blue", fg="white", command=createBudget)
CreateBudget.pack(side=BOTTOM)

#the budgets created window

CrtdBudgeFrame=LabelFrame(root,text="Budgets Created")
CrtdBudgeFrame.pack()
EmptyBudget=Text(CrtdBudgeFrame, "No budgets yet")
EmptyBudget.pack()

#the actual spent window
actualSpentFrame=LabelFrame(root,text="Actual")
actualSpentFrame.pack()
EmptyBudget.pack()

root.mainloop()