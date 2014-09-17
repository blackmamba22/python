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
		#self.label_standard_vs_metric
		self.label_height = Tkinter.Label(self, text="Your Height:")
		self.label_height.grid(column=0,row=1, pady=8)

		self.label_weight = Tkinter.Label(self, text="Your Weight:")
		self.label_weight.grid(column=0,row=2, pady=8)

		self.entry_height = Tkinter.Entry(self)
		self.entry_height.grid(column=2,row=1,pady=8)

		self.entry_weight = Tkinter.Entry(self)
		self.entry_weight.grid(column=2,row=2,pady=8)


if __name__ == "__main__":
	app = bmi_calc(None)
	app.title('BMI Calculator')
	app.mainloop()