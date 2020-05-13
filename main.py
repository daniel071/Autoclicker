# Imports everything
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Puts window in a class
class MyWindow(Gtk.Window):
	def __init__(self):
		global button1
		global entry1

		# Sets title and window
		Gtk.Window.__init__(self, title="Auto Clicker")

		# Adds the grid
		grid = Gtk.Grid()
		self.add(grid)

		# Defines a label
		label1 = Gtk.Label(label="Auto Clicker (By Daniel Pavela)")

		label2 = Gtk.Label(label="Enter clicking speed:")

		# Defines a text Entry
		entry1 = Gtk.Entry()
		entry1.set_text("10")



		# Defines a button
		button1 = Gtk.Button(label="Start clicking!")
		# Connects button, when pressed calls function
		button1.connect("clicked", self.on_button_clicked)

		# Adds each component to the grid
		grid.attach(label1, 1, 1, 3, 1)
		grid.attach(label2, 1, 2, 3, 1)
		grid.attach(entry1, 1, 3, 3, 1)
		grid.attach(button1, 1, 4, 3, 1)


	def on_button_clicked(self, widget):
		global button1
		global entry1

		# When button is pressed
		clickingSpeed = entry1.get_text()

		# TODO: Implement this!
		print("")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
