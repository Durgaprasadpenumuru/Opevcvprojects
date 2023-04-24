import tkinter as tk
from tkinter import filedialog
import pyarrow.parquet as pq
import pandas as pd
#from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="File Converter", bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def parquet():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pq.read_table(source=import_file_path).to_pandas()

browse_png = tk.Button(text="Select parquet  file", command=parquet, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browse_png)

def convert():
    global df
    export_file_path = filedialog.asksaveasfilename(defaultextension ="csv")
    df.to_csv(export_file_path)
    #df.save(export_file_path)

saveasbutton = tk.Button(text="Convert parquet to csv", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)
root.mainloop()