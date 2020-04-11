import tkinter
from tkinter import messagebox
from game import launchGame


class GameMenuApp:
    def __init__(self, master):
        self.title = tkinter.Label(master, text="Getting", fg="black", font=("Verdana", 48, "bold italic"), bg="white")
        self.subtitle = tkinter.Label(master, text="Hotter", fg="red", font=("Verdana", 38, "italic"), bg="white")
        self.diffVar = tkinter.StringVar(master)
        self.diffVar.set("Choose Your Difficulty")
        self.howTo = tkinter.Label(master,
                                   text="Have you ever play hot and cold, \nor whatever you called it? \nIt is precisely that! \nThere is an object you can't see. \nBut, you are hinted \nby temperatures where it is, \nhot means closer, and vice versa.",
                                   bg="white", font=("Verdana", 12, "italic"),
                                   pady=25
                                   )
        self.difficulty = tkinter.OptionMenu(master, self.diffVar,
                                             "Easy (250x250)", "Medium (500x500)",
                                             "Hard (750x750)", "Crazy (1000x1000)",
                                             )
        self.lnchBtn = tkinter.Button(master, text="Launch Game", bg="white", command=self.launch)

        self.title.pack()
        self.subtitle.pack()
        self.howTo.pack()
        self.difficulty.pack(side=tkinter.TOP)
        self.lnchBtn.pack()

    def launch(self):
        if self.diffVar.get() == "Choose Your Difficulty":
            messagebox.showerror("Invalid Difficulty", "You must choose a difficulty for the game!")
            return
        wid = 100

        if self.diffVar.get().split(" ")[0] == "Easy":
            wid = 250
        elif self.diffVar.get().split(" ")[0] == "Medium":
            wid = 500
        elif self.diffVar.get().split(" ")[0] == "Hard":
            wid = 750
        elif self.diffVar.get().split(" ")[0] == "Crazy":
            wid = 1000

        launchGame(wid)


root = tkinter.Tk()
root.config(bg="white")
root.resizable(False, False)
root.geometry("300x400")
root.title("Getting Hotter: Menus")
menu = GameMenuApp(root)
root.mainloop()
