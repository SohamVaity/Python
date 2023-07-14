from tkinter import *
from webbrowser import *

root = Tk()
root.title("Search On Twitter")
e = Entry(root,font=("Cascadia Mono",25))
e.grid()
def navi():
    print(f"Navigating to = {e.get()} on Twitter")
    query = "https://twitter.com/search?q="+e.get()
    open(query)
b = Button(root,text = "Search Twitter",
           font = ("Cascadia Mono",25),
           command = navi
        )
b.grid()    

root.mainloop()