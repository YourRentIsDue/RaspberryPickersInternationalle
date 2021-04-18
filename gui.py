import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.minsize(400,600)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.roomList = []
        self.checkButtons = []

        self.title = tk.Label(self,text="Title")
        self.title.pack(side="top")
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.testButton
        self.hi_there.pack(side="top")
    
        self.roomFrame = tk.Frame(self, bg="blue", height=20, width=50, bd=2)
        self.roomFrame.pack(padx=20,pady=20)

        for i in range(1,5):
            self.addRoom()

    def addRoom(self, roomName = "test"):
        roomButton = tk.Button(self.roomFrame, text=roomName)
        roomButton.pack(side="top")
        self.roomList.append(roomButton)


    def testButton(self):
        test = tk.Checkbutton(self.roomFrame, text="abc")
        test.pack(side="top")
        self.checkButtons.append(test)

root = tk.Tk()
app = Application(master=root)
app.mainloop()