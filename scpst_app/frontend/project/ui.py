import tkinter as tk
from PIL import Image, ImageTk
from picamera2 import Picamera2
import subprocess

picam2 = Picamera2()

root = tk.Tk()
root.title('SCPS GUI')
root.geometry('700x500+50+50')
root.columnconfigure(0, weight=1)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

capture_bt = tk.Button(button_frame, text='Capture')
capture_bt.grid(column=0, row=0, stick=tk.EW, padx=10)

display_bt = tk.Button(button_frame, text='Display')
display_bt.grid(column=1, row=0, stick=tk.EW, padx=10)

button_frame.grid(column=0, row=0)

label = tk.Label(root, text='This is a label')
label.grid(column=0, row=2, sticky=tk.NS, pady=50)

image = Image.open('utah.jpeg')
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image)
image_label.grid(column=0, row=2, sticky=tk.NS, pady=50)

def capture_click():
	
	picam2.start_and_capture_file("testing.jpg")
	picam2.stop_preview()
	
	new_image = Image.open('testing.jpg')
	new_image = new_image.resize((650, 450), Image.Resampling.LANCZOS)
	new_image = ImageTk.PhotoImage(new_image)
	image_label.config(image=new_image)
	image_label.image = new_image
	
def display_click():
	subprocess.run(['./run_proj.sh'])
	
capture_bt.config(command=capture_click)
display_bt.config(command=display_click)

root.mainloop()
