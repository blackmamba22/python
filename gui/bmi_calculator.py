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
		self.geometry('350x250')

		self.unit = Tkinter.IntVar()
		self.unit.set(2)			#default value set to Metric System

		self.standard_unit = Tkinter.Radiobutton(self, text="Standard (US):", variable=self.unit, value=1, command=self.useStandard)
		self.standard_unit.grid(column=0, row=0, pady=5, padx=5, sticky="W")
		self.standard_unit.bind("<Button-1>", self.useStandard())

		self.metric_unit = Tkinter.Radiobutton(self, text="Metric", variable=self.unit, value=2, command=self.useMetric)
		self.metric_unit.grid(column=2, row=0, pady=5, padx=5, sticky="W")
		self.metric_unit.bind("<Button-1>", self.useMetric())


		self.compute_bmi = Tkinter.Button(self, text="Calculate BMI", command=self.calcBMI)
		self.compute_bmi.grid(column=2, row=4, pady=5, padx=5)

		self.entryVariable = Tkinter.StringVar()

		self.entry_bmi = Tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry_bmi.grid(columnspan=2, column=2,row=10, pady=5, padx=5, sticky="W")
		self.entry_bmi.bind("<Button-1>", self.calcBMI)
		self.entryVariable.set(u"Your BMI is here.")

		self.quit_app = Tkinter.Button(self, text="Quit", command=self.quit)
		self.quit_app.grid(column=2, row=12, pady=5, padx=5, sticky="W")

		
		#prevent the main window from resizing
		self.resizable(False, False)

	def useMetric(self):

		#self.hideStandardLabel()

		self.label_height_metric = Tkinter.Label(self, text="Your Height (meters):")
		self.label_height_metric.grid(column=0,row=1, pady=5, padx=5, sticky="W")

		self.label_weight_metric = Tkinter.Label(self, text="Your Weight (kilograms):")
		self.label_weight_metric.grid(column=0,row=2, pady=5, padx=5, sticky="W")

		self.label_bmi = Tkinter.Label(self, text="Your BMI:")
		self.label_bmi.grid(column=0,row=10, pady=5, padx=5, sticky="W")

		self.entry_height = Tkinter.Entry(self)
		self.entry_height.grid(column=2,row=1,pady=5, padx=5, sticky="W")

		self.entry_weight = Tkinter.Entry(self)
		self.entry_weight.grid(column=2,row=2, pady=5, padx=5, sticky="W")

	def useStandard(self):

		#self.hideMetricLabel()

		self.label_height_standard = Tkinter.Label(self, text="Your Height (inches):")
		self.label_height_standard.grid(column=0,row=1, pady=5, padx=5, sticky="W")

		self.label_weight_standard = Tkinter.Label(self, text="Your Weight (pounds):")
		self.label_weight_standard.grid(column=0,row=2, pady=5, padx=5, sticky="W")

		self.label_bmi = Tkinter.Label(self, text="Your BMI:")
		self.label_bmi.grid(column=0,row=10, pady=5, padx=5, sticky="W")

		self.entry_height = Tkinter.Entry(self)
		self.entry_height.grid(column=2,row=1,pady=5, padx=5, sticky="W")

		self.entry_weight = Tkinter.Entry(self)
		self.entry_weight.grid(column=2,row=2, pady=5, padx=5, sticky="W")

	def hideMetricLabel(self):

		self.label_height_metric.pack_forget()
		self.label_weight_metric.pack_forget()

	def hideStandardLabel(self):

		self.label_height_standard.pack_forget()
		self.label_weight_standard.pack_forget()

	def calcBMI(self):

		bmi = None

		if self.unit.get() == 1:
			try:
				bmi = float(self.entry_weight.get())/(float(self.entry_height.get()) ** 2) * 703
			except ValueError:
				self.entryVariable.set("Invalid Input")
				return
		elif self.unit.get() == 2:
			try:
				bmi = float(self.entry_weight.get())/(float(self.entry_height.get()) ** 2)
			except ValueError:
				self.entryVariable.set("Invalid Input")
				return 

		#bmi = float(self.entry_weight.get())/(float(self.entry_height.get()) ** 2)

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