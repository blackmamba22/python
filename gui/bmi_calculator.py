#!/usr/bin/env python

"""
Project: BMI Calculator
Date Started: Sept. 17, 2014
Author: Gawaine O'Gilvie
"""

import Tkinter

class bmi_calc(Tkinter.Tk):

	def __init__(self, parent):
		
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		
		self.grid()
		self.geometry('300x250')
		#self.label_standard_vs_metric
		self.label_height = Tkinter.Label(self, text="Your Height (centimeters):")
		self.label_height.grid(column=0,row=1, pady=5, padx=5)

		self.label_weight = Tkinter.Label(self, text="Your Weight (kilograms):")
		self.label_weight.grid(column=0,row=2, pady=5, padx=5)

		self.label_bmi = Tkinter.Label(self, text="Your BMI:")
		self.label_bmi.grid(column=0,row=10, pady=5, padx=5)

		self.entry_height = Tkinter.Entry(self)
		self.entry_height.grid(column=2,row=1,pady=5, padx=5)

		self.entry_weight = Tkinter.Entry(self)
		self.entry_weight.grid(column=2,row=2,pady=5, padx=5)

		self.entry_bmi = Tkinter.Entry(self)
		self.entry_bmi.grid(column=2,row=10, pady=5, padx=5)




if __name__ == "__main__":
	app = bmi_calc(None)
	app.title('BMI Calculator')
	app.mainloop()