import tkinter
from tkinter import messagebox
from random import randint

# Text Hex Codes
hot = "#FF5733"
vhot = "#E32800"
cold = "#269AFB"
vcold = "#007BE2"


class GameApp:
    def __init__(self, master, wid, hei):
        self.master = master
        self.run = True
        self.targetX = randint(0, wid - 20)
        self.targetY = randint(0, hei - 20)
        self.gameCanv = tkinter.Canvas(master, width=wid, height=hei, bg="black")
        self.gameCanv.focus_set()
        self.gameCanv.bind("<Key>", self.handle_keys)
        self.gameCanv.bind("<Button-1>", lambda arg: self.gameCanv.focus_set())
        self.wid = wid
        self.hei = hei
        self.pastX = randint(0, wid - 5)
        self.pastY = randint(0, hei - 5)
        self.plrX = self.pastX
        self.plrY = self.pastY
        self.temp = "Very Cold"
        self.tempFg = vcold
        self.gameCanv.pack()

    def handle_keys(self, event):
        if 0 <= self.plrX <= self.wid - 5 and 0 <= self.plrY <= self.hei - 5:
            key = event.char
            if key == "w":
                self.plrY -= 5
            elif key == "a":
                self.plrX -= 5
            elif key == "s":
                self.plrY += 5
            elif key == "d":
                self.plrX += 5
        else:
            self.plrX = self.pastX
            self.plrY = self.pastY

    def draw(self):
        self.gameCanv.delete("all")
        if abs(self.targetX - self.plrX) <= self.wid / 20 and abs(self.targetY - self.plrY) <= self.wid / 20:
            # Win
            messagebox.showinfo("Win", "Yes, you've won!")
            self.run = False
            self.master.destroy()

        magnitude = (abs(self.targetX - self.plrX) ** 2 + abs(self.targetY - self.plrY) ** 2) ** 0.5  # ^ 1/2

        if 0 <= magnitude <= self.wid / 8:  # 1/8 region
            self.temp = "Very Hot"
            self.tempFg = vhot
        elif self.wid / 8 < magnitude <= self.wid / 8 * 3:  # 2/8 region
            self.temp = "Hot"
            self.tempFg = hot
        elif self.wid / 8 * 3 < magnitude <= self.wid / 8 * 5:  # 2/8 region
            self.temp = "Cold"
            self.tempFg = cold
        elif self.wid / 8 * 5 < magnitude <= self.wid:  # 3/8 region
            self.temp = "Very Cold"
            self.tempFg = vcold
        else:
            self.temp = "Very Cold"
            self.tempFg = vcold

        #self.gameCanv.create_rectangle(self.targetX, self.targetY, self.targetX + 5, self.targetY + 5,
                                       #fill=vhot)  # Only for debug purposes
        self.gameCanv.create_rectangle(self.plrX, self.plrY, self.plrX + 5, self.plrY + 5, fill="white")
        self.gameCanv.create_text(15, 30, text=self.temp, fill=self.tempFg, font=("Verdana", 12, "bold"), anchor=tkinter.SW)


def launchGame(wid):
    root = tkinter.Tk()
    root.config(bg="white")
    root.resizable(False, False)
    root.geometry(f"{wid}x{wid}")
    root.title("Getting Hotter: Game")
    game = GameApp(root, wid, wid)

    while game.run:
        try:
            root.update()
            game.draw()
        except:
            break
