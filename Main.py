from CreateObjects import CreateObjects
import tkinter as tk
from GUI import Application

createObjects = CreateObjects()
root = tk.Tk()
app = Application(createObjects.createRoom(1, 1, 1, 2, 1, "test"), master=root)
app.mainloop()



