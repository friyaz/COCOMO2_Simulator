import Tkinter as tk
import tkMessageBox
import ttk

LARGE_FONT = ("Verdana", 40)
BUTTON_FONT = ("Verdana", 20)
RADIO_FONT = ('Verdana', 18)

from startPage import StartPage
from effortCalculate import Effort_Page

class FP_Page_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller      
        self.set_FunctionPoint()  
        label = tk.Label(self, text="Function Point Calculator", font=LARGE_FONT)
        label.place(x=650, y=30)
        back_button = tk.Button(self, text="Back", font=BUTTON_FONT, command=lambda: controller.show_frame(StartPage))
        back_button.place(x=150, y=950)

        next_button = tk.Button(self, text="Next", font=BUTTON_FONT, command=lambda: controller.show_frame(FP_Page_2))
        next_button.place(x=1600, y=950)



        label_ILF = tk.Label(self, text="Internal Logical File", font=RADIO_FONT)
        label_ILF.place(x=150, y=300+40)
        label_ELF = tk.Label(self, text="External Logical File", font=RADIO_FONT)
        label_ELF.place(x=150, y=400+40)
        label_EI = tk.Label(self, text="External Input", font=RADIO_FONT)
        label_EI.place(x=150, y=500+40)
        label_EO = tk.Label(self, text="External Output", font=RADIO_FONT)
        label_EO.place(x=150, y=600+40)
        label_EIn = tk.Label(self, text="External Inquiry", font=RADIO_FONT)
        label_EIn.place(x=150, y=700+40)

        Headings = ['Simple', 'Average', 'Complex']
        Head_Label_1 = tk.Label(self, text='Simple', font=BUTTON_FONT)
        Head_Label_1.place(x=580, y=280)
        Head_Label_2 = tk.Label(self, text='Average', font=BUTTON_FONT)
        Head_Label_2.place(x=930, y=280)
        Head_Label_3 = tk.Label(self, text='Complex', font=BUTTON_FONT)
        Head_Label_3.place(x=1280, y=280)

        self.Entry_Widgets_simple = Entry_Widgets_simple= []
        h = 0
        for i in range(5):
            Entry_Widgets_simple.append(tk.Entry(self))
            Entry_Widgets_simple[i].place(x=550, y=340 + h)
            Entry_Widgets_simple[i].config(font=RADIO_FONT, width=12)
            h = h + 100
            Entry_Widgets_simple[i].insert('end',0)

        self.Entry_Widgets_average = Entry_Widgets_average = []
        h = 0
        for i in range(5):
            Entry_Widgets_average.append(tk.Entry(self))
            Entry_Widgets_average[i].place(x=900, y=340 + h)
            Entry_Widgets_average[i].config(font=RADIO_FONT, width=12)
            h = h + 100
            Entry_Widgets_average[i].insert('end',0)

        self.Entry_Widgets_complex = Entry_Widgets_complex = []
        h = 0
        for i in range(5):
            Entry_Widgets_complex.append(tk.Entry(self))
            Entry_Widgets_complex[i].place(x=1250, y=340 + h)
            Entry_Widgets_complex[i].config(font=RADIO_FONT, width=12)
            h = h + 100
            Entry_Widgets_complex[i].insert('end',0)






    def set_FunctionPoint(self):
        self.FP_dict = {}
        self.FP_dict['Average'] = [10, 7, 4, 5, 4]
        self.FP_dict['Simple'] = [7, 5, 3, 4, 3]
        self.FP_dict['Complex'] = [15, 10, 6, 7, 6]

class FP_Page_2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent)
        complexity_factors_heading = tk.Label(self, text="Complexity Factors", font=BUTTON_FONT)
        complexity_factors_heading.place(x=70, y=120)
        back_button = tk.Button(self, text="Back", font=RADIO_FONT, command=lambda: controller.show_frame(FP_Page_1))
        back_button.place(x=150, y=950)
        next_button = tk.Button(self, text="Calculate Effort", font=RADIO_FONT, command=lambda: self.controller.show_frame(Effort_Page))
        next_button.place(x=1500, y=950)
        calculate_button = tk.Button(self, text="Calculate", font=BUTTON_FONT, command=self.calculate_FP)
        calculate_button.config(width=14)        
        calculate_button.place(x=800, y=800)
        Result_Label = tk.Label(self, text='Function Point', font=BUTTON_FONT)
        Result_Label.place(x=550, y=900)
        self.Result_Entry = tk.Entry(self)
        self.Result_Entry.config(width=17, font=RADIO_FONT)
        self.Result_Entry.place(x=800, y =900)
        arr = []
        self.var = []
        dropdowns = []
        TF_Labels = []
        values = ['No Influence', 'Incidental', 'Moderate', 'Average', 'Significant', 'Essential']
        Technical_Factors = ['Data communication', 'Distributed data processing', 'Performance criteria',
                            'Heavily utilized software', 'High transaction rate', 'Online data entry',
                            'End-user efficiency', 'Online updating', 'Complex computations', 'Reusability',
                            'Ease of installation', 'Ease of operation', 'Portability', 'Maintainability']
        h = 0

        for i in range(7):
            self.var.append(tk.StringVar()) 
            self.var[i].set('Average')  
            dropdowns.append(tk.OptionMenu(self, self.var[i], *values))
            dropdowns[i].config(width=15, font=RADIO_FONT)
            dropdowns[i]['menu'].config(font=RADIO_FONT)
            dropdowns[i].place(x=510, y=220 + h )
            TF_Labels.append(tk.Label(self, text=Technical_Factors[i], font=RADIO_FONT))
            TF_Labels[i].place(x=70, y=220 + h)
            h = h + 80  

        h = 0

        for i in range(7, 14):
            self.var.append(tk.StringVar()) 
            self.var[i].set('Average')  
            dropdowns.append(tk.OptionMenu(self, self.var[i], *values))
            dropdowns[i].config(width=15, font=RADIO_FONT)
            dropdowns[i]['menu'].config(font=RADIO_FONT)
            dropdowns[i].place(x=1380, y=220 + h )
            TF_Labels.append(tk.Label(self, text=Technical_Factors[i], font=RADIO_FONT))
            TF_Labels[i].place(x=1000, y=220 + h)
            h = h + 80  

    def calculate_FP(self):
        pg_1 = self.controller.get_page(FP_Page_1)
        d = dict()
        d['No Influence'] = 0
        d['Incidental'] = 1
        d['Moderate'] = 2
        d['Average'] = 3
        d['Significant'] = 4
        d['Essential']= 5

        self.UFP = UFP = 0
        for i in range(5):
            value = int(pg_1.Entry_Widgets_simple[i].get())

            if not self.controller.validate_input(value, "Values can not be negative"):
                return

            UFP = UFP + value * pg_1.FP_dict['Simple'][i]
        for i in range(5):
            value = int(pg_1.Entry_Widgets_average[i].get())

            if not self.controller.validate_input(value, "Values can not be negative"):
                return

            UFP = UFP + value * pg_1.FP_dict['Average'][i]

        for i in range(5):
            value = int(pg_1.Entry_Widgets_complex[i].get())

            if not self.controller.validate_input(value, "Values can not be negative"):
                return

            UFP = UFP + value * pg_1.FP_dict['Complex'][i]

        DI = 0
        for i in range(14):
            selected = self.var[i].get()
            DI = DI + d[selected]

        self.CAF = CAF = 0.65 + 0.01 * DI

        self.FP = FP = UFP * CAF
                                  
        self.Result_Entry.delete('0', tk.END)
        self.Result_Entry.insert('end',"%.2f"%self.FP)
