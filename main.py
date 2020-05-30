# Imports everything
import gi
import time
from pynput.mouse import Button, Controller
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

mouse = Controller()

# Puts window in a class
class MyWindow(Gtk.Window):
	def __init__(self):
		global button1
		global entry1
		global entry2

		# Sets title and window
		Gtk.Window.__init__(self, title="Auto Clicker")

		# Adds the grid
		grid = Gtk.Grid()
		self.add(grid)

		# Defines the labels
		label1 = Gtk.Label(label="Auto Clicker (By Daniel Pavela)")

		label2 = Gtk.Label(label="Enter time (seconds):")

		label3 = Gtk.Label(label="Enter delay between clicks (seconds):")

		# Defines a text Entry
		entry1 = Gtk.Entry()
		entry1.set_text("10")

		entry2 = Gtk.Entry()
		entry2.set_text("0.1")

		# Defines a button
		button1 = Gtk.Button(label="Start clicking!")
		# Connects button, when pressed calls function
		button1.connect("clicked", self.on_button_clicked)

		# Adds each component to the grid
		grid.attach(label1, 1, 1, 3, 1)
		grid.attach(label2, 1, 2, 3, 1)
		grid.attach(entry1, 1, 3, 3, 1)

		grid.attach(label3, 1, 4, 3, 1)
		grid.attach(entry2, 1, 5, 3, 1)

		grid.attach(button1, 1, 6, 3, 1)


	def on_button_clicked(self, widget):
		global button1
		global entry1
		global entry2

		print("---Clicking in 3 seconds!---")
		time.sleep(3)

		# When button is pressed
		clickingTime = entry1.get_text()
		clickingDelay = entry2.get_text()

		t_end = time.time() + int(clickingTime)
		while time.time() < t_end:
			mouse.click(Button.left)
			time.sleep(float(clickingDelay))


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
