#from tkinter import *
import math
#import parser
#import tkinter.messagebox

'''
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

# FOr Power Function
def power(x, y):
    return math.pow(x, y)
    
# ---------------------------------------------		End		----------------------------------------------------





