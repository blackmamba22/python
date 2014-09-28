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
		self.geometry('400x300')

		#self.label_standard_vs_metric
		# unit = self.IntVar()
		# unit.set(2)

		self.standard_unit = Tkinter.Radiobutton(self, text="Standard (US):", value=1)
		self.standard_unit.grid(column=0, row=0, pady=5, padx=5, sticky="W")

		self.metric_unit = Tkinter.Radiobutton(self, text="Metric",value=2)
		self.metric_unit.grid(column=2, row=0, pady=5, padx=5, sticky="W")


		self.label_height = Tkinter.Label(self, text="Your Height (meters):")
		self.label_height.grid(column=0,row=1, pady=5, padx=5, sticky="W")

		self.label_weight = Tkinter.Label(self, text="Your Weight (kilograms):")
		self.label_weight.grid(column=0,row=2, pady=5, padx=5, sticky="W")

		self.label_bmi = Tkinter.Label(self, text="Your BMI:")
		self.label_bmi.grid(column=0,row=10, pady=5, padx=5, sticky="W")

		self.entry_height = Tkinter.Entry(self)
		self.entry_height.grid(column=2,row=1,pady=5, padx=5, sticky="W")

		self.entry_weight = Tkinter.Entry(self)
		self.entry_weight.grid(column=2,row=2, pady=5, padx=5, sticky="W")

		self.compute_bmi = Tkinter.Button(self, text="Calculate BMI", command=self.calcBMI)
		self.compute_bmi.grid(column=2, row=4, pady=5, padx=5)
		#self.compute_bmi.bind("<Button-1>", self.calcBMI)

		self.entryVariable = Tkinter.StringVar()

		self.entry_bmi = Tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry_bmi.grid(column=2,row=10, pady=5, padx=5, sticky="W")
		self.entry_bmi.bind("<Button-1>", self.calcBMI)
		self.entryVariable.set(u"Your BMI is here.")
		

		#prevent the main window from resizing
		self.resizable(False, False)

	def calcBMI(self):

		bmi = float(self.entry_weight.get())/(float(self.entry_height.get()) ** 2)

		if bmi < 18.5:
			self.entryVariable.set("BMI = %d = Underweight" % (bmi))
		elif bmi >= 18.5 and bmi <= 24.9:
			self.entryVariable.set("BMI = %d = Normal weight" % (bmi))
		elif bmi >= 25 and bmi <= 29.9:
			self.entryVariable.set("BMI = %d = Overweight" % (bmi))
		else:
			self.entryVariable.set("BMI = %d = Obesity" % (bmi))




if __name__ == "__main__":
	app = bmi_calc(None)
	app.title('BMI Calculator')
	app.mainloop()