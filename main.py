from myGUI import Application
import tkinter as tk
root = tk.Tk()
app = Application(master=root)
app.mainloop()
print(type(app.frame1))