import Tkinter as tk
import tkMessageBox
import ttk

LARGE_FONT = ("Verdana", 35)
BUTTON_FONT = ("Verdana", 20)
RADIO_FONT = ('Verdana', 18)
      

from startPage import StartPage

class LOC_Page(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.set_Language_Factor()
        label = tk.Label(self, text="Function Point to LOC Converter", font=LARGE_FONT)
        label.place(x=500, y=70)

        label2 = tk.Label(self, text="Function Point", font=BUTTON_FONT)
        label2.place(x=150, y=300)

        label3 = tk.Label(self, text="Language", font=BUTTON_FONT)
        label3.place(x=150, y=400)

        label4 = tk.Label(self, text="Lines of Code", font=BUTTON_FONT)
        label4.place(x=150, y=700)

        self.textBox = tk.Entry(self)
        self.textBox.place(x=390, y = 300)
        self.textBox.config(font=BUTTON_FONT, width=20)
        
        buttonCommit=tk.Button(self, height=1, width=19, text="Calculate", font=BUTTON_FONT, command=self.calculate_FP)
        buttonCommit.place(x=390, y=600)

        self.output = tk.Text(self, font=BUTTON_FONT, width=20, height=1)
        self.output.place(x=390, y=700)

        lst1 = ['Ada', 'Assembly', 'Basic', 'C','C++','Java', 'HTML 3.0', 'Pascal', 'Perl', 'Python', 'Spreadsheet', 'Oracle']
        self.var1 = tk.StringVar()
        self.var1.set('Java')
        drop = tk.OptionMenu(self, self.var1, *lst1)
        drop.config(width=15, font=BUTTON_FONT)
        drop['menu'].config(font=BUTTON_FONT)
        drop.place(x=390, y=400)


        back_button = tk.Button(self, text="Back", font=BUTTON_FONT, command=lambda: controller.show_frame(StartPage))
        back_button.place(x=150, y=950)

    def set_Language_Factor(self):
        self.languageFactor = dict()
        self.languageFactor["Ada"] = 71
        self.languageFactor["Assembly"] = 320
        self.languageFactor["Basic"] = 64
        self.languageFactor["C"] = 128     
        self.languageFactor["C++"] = 53
        self.languageFactor["Java"] = 53
        self.languageFactor["HTML 3.0"] = 15
        self.languageFactor["Pascal"] = 91
        self.languageFactor["Perl"] = 27
        self.languageFactor["Spreadsheet"] = 6
        self.languageFactor["Oracle"] = 40
 

    def calculate_FP(self):
        
        FP = self.textBox.get()

        if not self.controller.validate_input(int(FP), "Function Points can not be negative"):
            return

        self.output.delete('1.0', tk.END)
        selected = self.var1.get()
        SLOC = int(FP) * self.languageFactor[selected]
        self.output.insert('end', "%.2f"%str(SLOC) + "\n")
