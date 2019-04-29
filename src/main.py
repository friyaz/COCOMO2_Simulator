import Tkinter as tk
import tkMessageBox
import ttk

LARGE_FONT = ("Verdana", 40)
BUTTON_FONT = ("Verdana", 20)
RADIO_FONT = ('Verdana', 18)


from effortCalculate import Effort_Page, Modify_Scale_Drivers, Modify_Cost_Drivers
from startPage import StartPage
from functionPointCalculate import FP_Page_1, FP_Page_2
from FP_Converter import LOC_Page

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("COCOMO2 Simulator") 
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.configure(background='black')

        self.frames = {}

        for F in (StartPage, FP_Page_1, FP_Page_2, Effort_Page, LOC_Page, Modify_Scale_Drivers, Modify_Cost_Drivers):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]

    def validate_input(self, number, message):
        if number < 0:
            tkMessageBox.showerror("Error", message)
            return False
        return True

    def close(self):
        self.destroy()
        
if __name__ == "__main__":
        
    Simulator = App()
    Simulator.geometry("2000x1600")
    Simulator.mainloop()
