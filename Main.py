from CreateObjects import CreateObjects
import tkinter as tk
from GUI import Application

#create random data for stuff
createObjects = CreateObjects()
#initial tkinter
root = tk.Tk()

#begin gui
app = Application(createObjects.createRoom(1, 1, 1, 2, 1, 'Living Room'), master=root)
app.mainloop()



