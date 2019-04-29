import Tkinter as tk
import tkMessageBox
import ttk

LARGE_FONT = ("Verdana", 40)
BUTTON_FONT = ("Verdana", 20)
RADIO_FONT = ('Verdana', 18)




class StartPage(tk.Frame):



    def __init__(self, parent, controller):
        from effortCalculate import Effort_Page
        from FP_Converter import LOC_Page
        from functionPointCalculate import FP_Page_1
        tk.Frame.__init__(self,parent)
        self.controller=controller        
        heading = tk.Label(self, text="COCOMO 2 Simulator", font=LARGE_FONT)
        heading.place(x=600, y=80)
        button1 = tk.Button(self, wraplength=320, justify=tk.CENTER,text="Function Point Calculator", font=BUTTON_FONT, command=lambda: controller.show_frame(FP_Page_1),      background='white')
        button1.config(height=10, width=14)
        button1.place(x=200, y=350)
    
        button2 = tk.Button(self, wraplength=320, justify=tk.CENTER,text="Funtion Point to SLOC Converter", font=BUTTON_FONT, command=lambda: controller.show_frame(LOC_Page),
background='white')
        button2.config(height=10, width=14)
        button2.place(x=700, y=350)

        button3 = tk.Button(self, wraplength=320, justify=tk.CENTER,text="Effort                Calculator", font=BUTTON_FONT, command=lambda: controller.show_frame(Effort_Page),
background='white')
        button3.config(height=10, width=14)
        button3.place(x=1200, y=350)

        help_button = tk.Button(self, text="Help", font=BUTTON_FONT, command=lambda: controller.show_frame(StartPage), background='white')
        help_button.config(width=14)
        help_button.place(x=700, y=800)
