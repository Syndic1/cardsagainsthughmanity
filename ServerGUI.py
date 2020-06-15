

from tkinter import * 

top = Tk()


top.minsize(800,600)

top.title("Cards Against Hughmanity Server")


lservername = Label(text="Server Name")
lservername.grid(column = 0, row = 0,padx=10)
eservername = Entry(top)
eservername.grid(column = 1, row = 0, pady=10)

lserverpassword = Label(text="Server Password")
eserverpassword = Entry(top)
lserverpassword.grid(column = 0, row = 1,padx=10)
eserverpassword.grid(column = 1, row = 1,padx=10)

lserverdeck = Label(text="Select Deck")
oserverdeck = OptionMenu(top, "Jon's Tiny Deck", "Jon is Great")
oserverdeck.config(width=30)
lserverdeck.grid(column = 3, row = 0,padx=10)
oserverdeck.grid(column = 3, row = 1,padx=10)

lplayerlist = Label(text="Connected Players")
playerlist = Listbox(top)
lplayerlist.grid(column=4,row=4, columnspan=2)
playerlist.grid(column=4,row=5, columnspan=2)



startserverbutton = Button(top,text="Start Server", width=20, height=2)
startserverbutton.grid(column=5, row=1)


top.mainloop()


