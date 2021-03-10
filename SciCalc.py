from tkinter import *
import math
import parser
import tkinter.messagebox

#print("All Goood with imports")

root = Tk()
root.title("Scientific Calculator")
root.configure(background = "powder blue")
root.resizable(width = False, height= False)
root.geometry("600x568+0+0") # +0+0 means it starts from left top corner

calc = Frame(root)
calc.grid()


txtDisplay = Entry(calc, font=('ariel', 20, 'bold'), bg = "powder blue", bd = 30, width=28, justify = RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
	for k in range(3):
		btn.append(Button(calc, width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, text = numberpad[i]))
		btn[i].grid(row = j, column = k, pady = 1)

		i+= 1

# ---------------------Butttons area--------------------------------------

# C
btnClear = Button(calc, text= "C", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 0, pady = 1)

# CE or AC
btnAllClear = Button(calc, text= "CE", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 1, pady = 1)

# sqare root
btnSq = Button(calc, text= "√", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 2, pady = 1)

# Plus or add
btnAdd = Button(calc, text= "+", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 3, pady = 1)


# Subtraction Minus
btnSub = Button(calc, text= "-", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 2, column = 3, pady = 1)

# Multiply
btnMult = Button(calc, text= "*", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 3, column = 3, pady = 1)

# Divide
btnDiv = Button(calc, text= chr(247), width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 4, column = 3, pady = 1)


# Zero
btnZero = Button(calc, text= "0", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 0, pady = 1)


# Decimal or Dot
btnDot = Button(calc, text= ".", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 1, pady = 1)

# PM
btnPM = Button(calc, text= chr(177), width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 2, pady = 1)

# Evaluate or equals
btnEquals = Button(calc, text= "=", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 3, pady = 1)

#-------------------------------- Scientific Calci----------------------------

# ======================     Row 1	======================================
# Pi - π
btnPi = Button(calc, text= "π", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 4, pady = 1)

# Cos 
btnSq = Button(calc, text= "cos", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 5, pady = 1)

# tan
btnAdd = Button(calc, text= "tan", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 6, pady = 1)


# Sin
btnSub = Button(calc, text= "sin", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 1, column = 7, pady = 1)

# =======================	Row 2	===============================
# 2 pi
btn2Pi = Button(calc, text= "2π", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 2, column = 4, pady = 1)

# Cosh
btnCosh = Button(calc, text= "cosh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 2, column = 5, pady = 1)

# Tamh
btnTanh = Button(calc, text= "tanh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 2, column = 6, pady = 1)


# Sinh
btnSinh = Button(calc, text= "sinh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 2, column = 7, pady = 1)



# =======================	Row 3	===============================

# 2 log
btnLog = Button(calc, text= "log", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 3, column = 4, pady = 1)

# exponential Exp
btnExp = Button(calc, text= "Exp", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 3, column = 5, pady = 1)

# Mod
btnMod = Button(calc, text= "Mod", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 3, column = 6, pady = 1)

# E - e
btnE = Button(calc, text= "e", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 3, column = 7, pady = 1)


# =======================	Row 4	===============================
# log2
btnLog2 = Button(calc, text= "log2", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 4, column = 4, pady = 1)

# deg
btnDeg = Button(calc, text= "deg", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 4, column = 5, pady = 1)

# Cosh
btnCosh = Button(calc, text= "acosh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 4, column = 6, pady = 1)


# asinh
btnASinh = Button(calc, text= "asinh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4).grid(row = 4, column = 7, pady = 1)


# =======================	Row 5	===============================
# log base 10
btnLog10 = Button(calc, text= "log10", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 4, pady = 1)

# Log1p
btnLog1p = Button(calc, text= "log1p", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 5, pady = 1)

# Expm1
btnExpm1 = Button(calc, text= "expm1", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 6, pady = 1)


# gamma
btnLgamma = Button(calc, text= "lgamma", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, bg = "powder blue").grid(row = 5, column = 7, pady = 1)

# label display extend for scientific
lblDisplay = Label(calc, text="Scientific Calculator", font=('ariel', 30, 'bold'), justify = CENTER)
lblDisplay.grid(row = 0, column = 4, columnspan = 4)


# ---------------------Menu & Functions--------------------------------------

def iExit():
	iExit = tkinter.messagebox.askyesno("Scientific Calculator") 
	if iExit > 0:
		root.destroy()
		return
	

def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("1200x568+0+0")
	
	
def Standard():
	root.resizable(width=False, height=False)
	root.geometry("600x568+0+0")
	

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)



editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")



helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Take Help!", menu=helpmenu)
helpmenu.add_command(label = "Here is help!")



root.config(menu=menubar)
root.mainloop()


