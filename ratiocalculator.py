# Import Module
from tkinter import *

# Create Object
root = Tk()

# Set height and width
width = 600
height = 250

# Set Geometry and min, max size
root.geometry(f"{width}x{height}")
root.maxsize(width, height)
root.minsize(width, height)

# Create Label
Label(root, text="Ratio Calculator", font=(
	"Helvetica", 18, "bold"), fg="blue").pack()


# Function will calculate the value of x
def ratio_calculator():
		# Get the value of spinbox using get() method
	s11 = int(s1.get())
	s22 = int(s2.get())
	s33 = int(s3.get())

	# Formula Used
	value = (s33*s22)/s11

	# change the text of label using config method
	value_of_x.config(text=value)


# Create Frame
frame = Frame(root)
frame.pack()

# Create Spin Boxes
s1 = Spinbox(frame, from_=0, to=10000000, width=10,
			font=("Helvetica", 14, "bold"))
s1.pack(side=LEFT, padx=10, pady=10)
s2 = Spinbox(frame, from_=0, to=10000000, width=10,
			font=("Helvetica", 14, "bold"))
s2.pack(side=LEFT, padx=10, pady=10)
s3 = Spinbox(frame, from_=0, to=10000000, width=10,
			font=("Helvetica", 14, "bold"))
s3.pack(side=LEFT, padx=10, pady=10)

# Add Another Label
Label(frame, text="X", width=10, font=("Helvetica",
									14, "bold"),
	borderwidth=1, relief="solid").pack(side=LEFT,
										padx=10,
										pady=10)

# Add Another Frame
frame1 = Frame(root)
frame1.pack()

x_value = Label(frame1, text="Value of x:",
				font=("Helvetica", 18, "bold"))
x_value.pack(side=LEFT)

value_of_x = Label(frame1, text="",
				font=("Helvetica", 18, "bold"))
value_of_x.pack(side=LEFT)

# Create Button
Button(root, text="Calculate", borderwidth=2, width=15,
	font=("Helvetica", 14, "bold"),
	command=ratio_calculator, fg="red",
	bg="black").pack(pady=20)

# Execute Tkinter
root.mainloop()
