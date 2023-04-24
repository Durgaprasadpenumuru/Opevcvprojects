import tkinter as tk
from tkinter import filedialog
#mport pandas as pd
import pandas as pd
#from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="ETL Data testing", bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def csvfirst():
    global df1
    import_file_path = filedialog.askopenfilename()
    df1 = pd.read_csv(import_file_path)

browse_fileone = tk.Button(text="Select first  file", command=csvfirst, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=browse_fileone)

def csvsecond():
    global df2
    import_file_path = filedialog.askopenfilename()
    df2 = pd.read_csv(import_file_path)

browse_filetwo = tk.Button(text="Select second file", command=csvsecond, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 140, window=browse_filetwo)

def compare():
    global df
    #df=df1.equals(df2)
    df=df1.compare(df2, align_axis=1, keep_shape=False, keep_equal=False)

    export_file_path = filedialog.asksaveasfilename(defaultextension ="csv")
    df.to_csv(export_file_path)
    #df.save(export_file_path)

saveasbutton = tk.Button(text="Get comparison", command=compare, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)
root.mainloop()