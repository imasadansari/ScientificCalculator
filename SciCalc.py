from tkinter import *
import math
import parser
import tkinter.messagebox

# print("All Goood with imports")
'''
root = Tk()
root.title("Scientific Calculator")
root.configure(background = "#566666")
root.resizable(width = False, height= False)
root.geometry("600x568+50+50") # +0+0 means it starts from left top corner

calc = Frame(root)
calc.grid()



class Calc():
	def __init__(self):
		self.total = 0
		self.current = ""
		self.input_value = True
		self.check_sum = False
		self.op = ""
		self.result = False
		
	# For numberss
	def numberEnter(self,num):
		self.result = False
		firstnum = txtDisplay.get()
		secondnum = str(num)
		flag = False
		if self.input_value:
			self.current = secondnum
			self.input_value = False
		else:
			if secondnum == '.':
				flag = True
				if secondnum in firstnum:
					return
			self.current = firstnum + secondnum
			if (float(self.current) == 0.0) and (not flag): # TO solve 0.0001 problem
				self.current = 0
		self.display(self.current)
	
	# Function for equals
	def sum_of_total(self):
		self.result = True
		self.current = float(self.current)
		if self.check_sum == True:
			self.valid_function()
		else:
			self.total = float(txtDisplay.get())
	
	# For Display
	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)
	
	# FOr Arithmatic Functions
	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			# To prevent operations like (-1 * 0 == -0.0)
			if(self.total == 0 or self.current == 0):
				self.total = 0.0
				print("Negative Zero result from multiplication prevented")
			else:
				self.total *= self.current
		if self.op == "divide":
			if self.current == 0:
				self.current = self.total
				self.display(self.current)
				print("U cannot devide by 0")
				
			# To Prevent negative Zero result of operations like (0 / -1) = (-0.0)
			elif self.total == 0 and self.current < 0:
				self.total = 0
				print("Negative Zero result of division prevented")
			
			else:
				self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
			
		if self.op == "power":
			self.total = math.pow(self.total, self.current)
		self.input_value = True
		self.check_sum = False
		self.display(self.total)
		
		
	# For operators
	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result :
			self.total = self.current
			self.input_value = True
		self.check_sum = True
		self.op = op
		self.result = False
	
	# Clear
	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value = True
	
	# For all clear
	def all_Clear_Entry(self):
		self.Clear_Entry()
		self.total = 0
	
	# For Plus Minus
	def mathsPM(self):
		self.result = False
		temp = float(txtDisplay.get())
		# TO prevent negative zero
		if temp != 0: 
			self.current = -1 * temp
			self.display(self.current)
		else:
			print("Cannot negate zero")
			self.current = temp
			self.display(self.current)
			
	# Squre root
	def square_root(self):
		self.result = False
		temp = float(txtDisplay.get())
		# GEtting Exception in case of taking sqare root of Negative numbers
		if temp >= 0:
			self.current = math.sqrt(float(txtDisplay.get()))
			self.display(self.current)
		else:
			# Prevent Exception : ValueError: math domain error
			# Occured due to taking sqare root of negative numeber
			self.current = temp
			self.display(self.current)
			print("Cannot calculate Sqaure root of Negative numbers")
		return self.current
	
	# Trigonometric functions
	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	
	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))
		self.display(self.current)


	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	
	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	
	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtDisplay.get())))
		self.display(self.current)
	
	# For natural log
	def log(self):
		self.result = False
		temp = float(txtDisplay.get())
		
		if(temp > 0):
			self.current = math.log(float(txtDisplay.get()))
			self.display(self.current)
		else:
			print("Cannot take calculate natural log of negative number or Zero")
			self.current = 0
			self.total = 0
			self.display(0)
	
	# for exponential
	def exp(self):
		self.result = False		
		self.current = math.exp(float(txtDisplay.get()))
		self.display(self.current)
	
	# pi
	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)
		
	# pi * 2
	def pi2(self):
		self.result = False
		self.current = math.tau
		self.display(self.current)
	
	# e
	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)
	
	# Factorial Function
	def factorial(self):
		self.result = False
		temp = float(txtDisplay.get())
		# TO prevent ValueError: factorial() not defined for negative values EXCEPTION
		if temp >= 0:
			# print(temp, "    ", round(temp))
			if temp == float(round(temp)):
				self.current = math.factorial(float(txtDisplay.get()))
			else:
				self.current = round(temp)
				print("Cannot take Factorial of Decimal Numbers, SO we converted It to INT")		
		else: 
			self.current = 0.0
			print("Factorial of negative number cannot be taken")
		self.display(self.current)
	
	
	def acosh(self):
		self.result = False
		self.current = math.acosh(float(txtDisplay.get()))
		self.display(self.current)
	
	
		
	def acosh(self):
		self.result = False
		self.current = math.acosh(float(txtDisplay.get()))
		self.display(self.current)
	
	
	def asinh(self):
		self.result = False
		self.current = math.acosh(float(txtDisplay.get()))
		self.display(self.current)
	
	
	def expm1(self):
		self.result = False
		self.current = math.expm1(float(txtDisplay.get()))
		self.display(self.current)
	
	
	def lgamma(self):
		self.result = False
		self.current = math.lgamma(float(txtDisplay.get()))
		self.display(self.current)
	
	
	def degrees(self):
		self.result = False
		self.current = math.degrees(float(txtDisplay.get()))
		self.display(self.current)
	
	def log2(self):
		self.result = False
		temp = float(txtDisplay.get())
		
		if(temp > 0):
			self.current = math.log2(float(txtDisplay.get()))
			self.display(self.current)
		else:
			self.current = 0
			self.total = 0
			self.display(0)
	
	
	def log10(self):
		self.result = False
		temp = float(txtDisplay.get())
		
		if(temp > 0):
			self.current = math.log10(float(txtDisplay.get()))
			self.display(self.current)
		else:
			self.current = 0
			self.total = 0
			self.display(0)
	
	
	def log1p(self):
		self.result = False
		temp = float(txtDisplay.get())
		
		if(temp > 0):
			self.current = math.log1p(float(txtDisplay.get()))
			self.display(self.current)
		else:
			self.current = 0
			self.total = 0
			self.display(0)
	
	
	
	
added_value = Calc()



txtDisplay = Entry(calc, font=('ariel', 20, 'bold'), bg = "powder blue", bd = 30, width=28, justify = RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
	for k in range(3):
		btn.append(Button(calc, width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,  text = numberpad[i]))
		btn[i].grid(row = j, column = k, pady = 1)
		btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
		i+= 1

# ---------------------Butttons area--------------------------------------

# C
btnClear = Button(calc, text= "C", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.Clear_Entry).grid(row = 1, column = 0, pady = 1)

# CE or AC
btnAllClear = Button(calc, text= "CE", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.all_Clear_Entry).grid(row = 1, column = 1, pady = 1)

# sqare root
btnSq = Button(calc, text= "√", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = added_value.square_root).grid(row = 1, column = 2, pady = 1)

# Plus or add
btnAdd = Button(calc, text= "+", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = lambda: added_value.operation("add")).grid(row = 1, column = 3, pady = 1)


# Subtraction Minus
btnSub = Button(calc, text= "-", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = lambda: added_value.operation("sub")).grid(row = 2, column = 3, pady = 1)

# Multiply
btnMult = Button(calc, text= "*", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = lambda: added_value.operation("multi")).grid(row = 3, column = 3, pady = 1)

# Divide
btnDiv = Button(calc, text= chr(247), width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = lambda: added_value.operation("divide")).grid(row = 4, column = 3, pady = 1)


# Zero
btnZero = Button(calc, text= "0", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = lambda: added_value.numberEnter(0)).grid(row = 5, column = 0, pady = 1)



# Decimal or Dot
btnDot = Button(calc, text= ".", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = lambda: added_value.numberEnter(".")).grid(row = 5, column = 1, pady = 1)

# PM
btnPM = Button(calc, text= chr(177), width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = added_value.mathsPM ).grid(row = 5, column = 2, pady = 1)

# Evaluate or equals
btnEquals = Button(calc, text= "=", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "black",  bg = "red", command = added_value.sum_of_total).grid(row = 5, column = 3, pady = 1)

#-------------------------------- Scientific Calci----------------------------

# ======================     Row 1	======================================
# Pi - π
btnPi = Button(calc, text= "π", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.pi).grid(row = 1, column = 4, pady = 1)

# deg
btnDeg = Button(calc, text= "deg", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "orange",  bg = "#566666", command = added_value.degrees).grid(row = 1, column = 5, pady = 1)

# ACosh
#btnACosh = Button(calc, text= "acosh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.acosh).grid(row = 4, column = 6, pady = 1)

# Power
btnPow = Button(calc, text= "x^y", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "orange",  bg = "#566666", command = lambda: added_value.operation("power")).grid(row = 1, column = 6, pady = 1)


# asinh
#btnASinh = Button(calc, text= "asinh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.asinh).grid(row = 4, column = 7, pady = 1)

# Factorial of x
btnFactorial = Button(calc, text= "x!", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "orange",  bg = "#566666", command = added_value.factorial).grid(row = 1, column = 7, pady = 1)

# =======================	Row 2	===============================
# 2 pi
btn2Pi = Button(calc, text= "2π", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = added_value.pi2).grid(row = 2, column = 4, pady = 1)


# Cos 
btnCos = Button(calc, text= "cos", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.cos).grid(row = 2, column = 5, pady = 1)

# tan
btnTan = Button(calc, text= "tan", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = added_value.tan).grid(row = 2, column = 6, pady = 1)


# Sin
btnSin = Button(calc, text= "sin", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.sin).grid(row = 2, column = 7, pady = 1)


# =======================	Row 3	===============================

# log
btnLog = Button(calc, text= "log", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = added_value.log).grid(row = 3, column = 4, pady = 1)

# exponential Exp
btnExp = Button(calc, text= "Exp", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666",command = added_value.exp).grid(row = 3, column = 5, pady = 1)

# Mod
btnMod = Button(calc, text= "Mod", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = lambda: added_value.operation("mod")).grid(row = 3, column = 6, pady = 1)

# E - e
btnE = Button(calc, text= "e", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.e).grid(row = 3, column = 7, pady = 1)


# =======================	Row 4	===============================
# log2
btnLog2 = Button(calc, text= "log2", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = added_value.log2).grid(row = 4, column = 4, pady = 1)


# Cosh
btnCosh = Button(calc, text= "cosh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.cosh).grid(row = 4, column = 5, pady = 1)

# Tamh
btnTanh = Button(calc, text= "tanh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.tanh).grid(row = 4, column = 6, pady = 1)


# Sinh
btnSinh = Button(calc, text= "sinh", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4,fg = "white",  bg = "#566666", command = added_value.sinh).grid(row = 4, column = 7, pady = 1)



# =======================	Row 5	===============================
# log base 10
btnLog10 = Button(calc, text= "log10", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.log10).grid(row = 5, column = 4, pady = 1)

# Log1p
btnLog1p = Button(calc, text= "log1p", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.log1p).grid(row = 5, column = 5, pady = 1)

# Expm1
btnExpm1 = Button(calc, text= "expm1", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.expm1).grid(row = 5, column = 6, pady = 1)


# gamma
btnLgamma = Button(calc, text= "lgamma", width = 6, height = 2, font=('ariel', 20, 'bold'), bd = 4, fg = "white",  bg = "#566666", command = added_value.lgamma).grid(row = 5, column = 7, pady = 1)

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
	root.geometry("1200x568+50+50")
	
	
def Standard():
	root.resizable(width=False, height=False)
	root.geometry("600x568+50+50")
	

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
root.destroy()
#root.mainloop()
'''

# ----------------------------------------------------	Testing Functions	----------------------------------


def square_root(x):
	# GEtting Exception in case of taking sqare root of Negative numbers
	if x >= 0:
		x = math.sqrt(x)
		return x
	else:
		# Prevent Exception : ValueError: math domain error
		# Occured due to taking sqare root of negative numeber
		# x = x
		print("Cannot calculate Sqaure root of Negative numbers")
		return float(x)


def factorial(x):
	
	temp = float(x)
	# TO prevent ValueError: factorial() not defined for negative values EXCEPTION
	if temp >= 0:
		# print(temp, "    ", round(temp))
		if temp == float(round(temp)):
			temp = math.factorial(float(temp))
		else:
			temp = round(temp)
			print("Cannot take Factorial of Decimal Numbers, SO we converted It to INT")		
	else: 
		temp = 0.0
		print("Factorial of negative number cannot be taken")
	return temp


# For natural log
def log(x):
	temp = float(x)
	
	if(temp > 0):
		temp = math.log(float(temp))
		#return temp
	else:
		temp = 0
	return temp	

def power(x, y):
    return math.pow(x, y)
    
# ---------------------------------------------		End		----------------------------------------------------





