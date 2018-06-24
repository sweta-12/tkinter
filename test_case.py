from tkinter import *

class TestCase(Toplevel):
	def __init__(self,master,**params):
		self.testcase_master = Toplevel(master)
		self.x1 = params['x1']
		self.y1 = params['y1']
		self.x2 = params['x2']
		self.y2 = params['y2']
		# self.canvas = master
		self.canvas = Canvas(self.testcase_master, width = 700, height = 400)
		self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="green")
		self.canvas.after(5000, self.hide_ball)
		self.canvas.pack()

	def hide_ball(self):
		self.canvas.destroy()


