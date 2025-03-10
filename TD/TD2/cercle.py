import tkinter as tk 
racine=tk.Tk()
canva=tk.Canvas(racine, height=600, width=600, bg='black')
canva.grid()
x=300
y=300
canva.create_oval(x+290, y+290, x-290, y-290, fill='blue')

racine.mainloop()