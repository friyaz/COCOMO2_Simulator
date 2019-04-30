import Tkinter as tk
import tkMessageBox
import ttk

LARGE_FONT = ("Verdana", 30)
BUTTON_FONT = ("Verdana", 20)
RADIO_FONT = ('Verdana', 18)

from startPage import StartPage


class Effort_Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        back_button = tk.Button(self, text="Back", font=BUTTON_FONT, command=lambda: controller.show_frame(StartPage))
        back_button.place(x=150, y=950)
        
        Scale_Driver_button = tk.Button(self,  wraplength=300, justify=tk.CENTER,text="Modify Scale Drivers",
                                         font=RADIO_FONT, background='white', command=lambda: controller.show_frame(Modify_Scale_Drivers))
        Scale_Driver_button.config(height=5)
        Scale_Driver_button.place(x=800, y=330)
        tk.Label(self, text="Default set to Nominal",background='white', font=("Verdana", 11)).place(x=850, y=460) 

        Cost_Driver_button = tk.Button(self,  wraplength=300, justify=tk.CENTER,text="Modify Cost   Drivers",
                                         font=RADIO_FONT, background='white' ,command=lambda: controller.show_frame(Modify_Cost_Drivers))
        Cost_Driver_button.config(height=5)
        Cost_Driver_button.place(x=400, y=330)
        tk.Label(self, text="Default set to Nominal",background='white', font=("Verdana", 11)).place(x=450, y=460)
        
        SLOC_Label = tk.Label(self, text="Kilo Lines of Code", font=RADIO_FONT)
        SLOC_Label.place(x=170, y=200)
        self.SLOC_Entry = tk.Entry(self)
        self.SLOC_Entry.place(x=470, y=200)
        self.SLOC_Entry.config(font=RADIO_FONT, width=12)    

        Labour_Rate_Label = tk.Label(self, text="Labour Rate    $", font=RADIO_FONT)
        Labour_Rate_Label.place(x=900, y=200)
        self.LR_Entry = tk.Entry(self)
        self.LR_Entry.place(x=1130, y=200)
        self.LR_Entry.config(font=RADIO_FONT, width=12)

        Effort_Label = tk.Label(self, text="Effort (Person Months)", font=RADIO_FONT)
        Effort_Label.place(x=150, y=660)
        Dev_Time_Label = tk.Label(self, text="Development Time", font=RADIO_FONT)
        Dev_Time_Label.place(x=150, y=730)
        Cost_Label = tk.Label(self, text="Total Cost                 $", font=RADIO_FONT)
        Cost_Label.place(x=150, y=800)





        self.Effort_display = tk.Text(self, height=1, width=12, font=RADIO_FONT)
        self.Effort_display.place(x=470, y = 660)

        self.Dev_Time_display = tk.Text(self, height=1, width=12, font=RADIO_FONT)
        self.Dev_Time_display.place(x=470, y=730)

        self.Cost_display = tk.Text(self, height=1, width=12, font=RADIO_FONT)
        self.Cost_display.place(x=470, y = 800)

        Submit_Button = tk.Button(self, text="Calculate", font=RADIO_FONT, command= self.calculate_Effort)
        Submit_Button.config(width=20)
        Submit_Button.place(x=600, y=560)

        Label_A = tk.Label(self, text = "A", font=RADIO_FONT)
        Label_A.place(x=1320, y=330)
        self.A_Entry = A_Entry = tk.Entry(self)
        A_Entry.place(x=1400, y=330)
        A_Entry.insert('end',2.94)
        A_Entry.config(font=RADIO_FONT, width=6)    
        Label_B = tk.Label(self, text = "B", font=RADIO_FONT)
        Label_B.place(x=1320, y=410)
        self.B_Entry = B_Entry = tk.Entry(self)
        B_Entry.place(x=1400, y=410)
        B_Entry.insert('end',0.91)
        B_Entry.config(font=RADIO_FONT, width=6)    
        Label_C = tk.Label(self, text = "C", font=RADIO_FONT)
        Label_C.place(x=1320, y=490)
        self.C_Entry = C_Entry = tk.Entry(self)
        C_Entry.place(x=1400, y=490)
        C_Entry.insert('end',3.67)
        C_Entry.config(font=RADIO_FONT, width=6)    
        Label_D = tk.Label(self, text = "D", font=RADIO_FONT)
        Label_D.place(x=1320, y=570)
        self.D_Entry = D_Entry = tk.Entry(self)
        D_Entry.place(x=1400, y=570)
        D_Entry.insert('end',0.28)
        D_Entry.config(font=RADIO_FONT, width=6)    

    def calculate_Effort(self):
        
        SD_Frame =  self.controller.get_page(Modify_Scale_Drivers)
        CD_Frame =  self.controller.get_page(Modify_Cost_Drivers)
        SD_Frame.set_scaleDrivers()
        CD_Frame.set_costDrivers()

        SLOC = float(self.SLOC_Entry.get())

        if not self.controller.validate_input(SLOC, "SLOC must be non-negative"):
            return        

        pi_Cost_Drivers = 1
        for i in range(17):
            selected = CD_Frame.var[i].get()
            pi_Cost_Drivers = pi_Cost_Drivers * CD_Frame.costDrivers[ selected ][i]

        sum_Scale_Drivers = 0
        for i in range(5):
            selected = SD_Frame.var[i].get()
            sum_Scale_Drivers = sum_Scale_Drivers + SD_Frame.scaleDrivers[selected][i]

        self.A = A = float(self.A_Entry.get())
        self.B = B = float(self.B_Entry.get())
        self.C = C = float(self.C_Entry.get())
        self.D = D = float(self.D_Entry.get()) 

        if( not self.controller.validate_input(A, "Wrong Input")):
            return
        if( not self.controller.validate_input(B, "Wrong Input")):
            return
        if( not self.controller.validate_input(C, "Wrong Input")):
            return
        if( not self.controller.validate_input(D, "Wrong Input")):
            return

        self.E = E = B + 0.01 * sum_Scale_Drivers
         
        
        self.effort = effort = A * SLOC**(E) * pi_Cost_Drivers  
        
        self.F = F = (E - B)*0.2 + D
        self.Dev_Time = Dev_Time = C * effort**F  
        Labour_Rate = int(self.LR_Entry.get())

        if not self.controller.validate_input(Labour_Rate, "Labour Rate must be non-negative"):
            return        

        self.Dev_Cost = Dev_Cost = Labour_Rate * effort

        self.Effort_display.delete('1.0', tk.END)
        self.Effort_display.insert('end',"%.2f"%self.effort)

        self.Dev_Time_display.delete('1.0', tk.END)
        self.Dev_Time_display.insert('end',"%.2f"%self.Dev_Time)

        self.Cost_display.delete('1.0', tk.END)
        self.Cost_display.insert('end',"%.2f"%self.Dev_Cost)


class Modify_Scale_Drivers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        label = tk.Label(self, text="Scale Drivers", font=LARGE_FONT)
        label.place(x=655, y=45)
        back_button = tk.Button(self, text="Back", font=RADIO_FONT, command=lambda: controller.show_frame(Effort_Page))
        back_button.place(x=150, y=950)

        values = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High']
        headings = ["Precentedness", "Development Flexibility", "Architecture", "Team Cohesion", "Process Maturity"]
        self.var = []
        dropdowns = []
        SF_Labels = []





        h = 0
        for i in range(5):
            self.var.append(tk.StringVar())
            self.var[i].set('Nominal')
            dropdowns.append(tk.OptionMenu(self, self.var[i], *values))
            dropdowns[i].config(width=15, font=RADIO_FONT)
            dropdowns[i]['menu'].config(font=RADIO_FONT)
            dropdowns[i].place(x=600, y=300 + h)
            SF_Labels.append(tk.Label(self, text=headings[i], font=RADIO_FONT))
            SF_Labels[i].place(x=150, y=300 + h)
            h = h + 100

    def set_scaleDrivers(self): 
        self.scaleDrivers = dict()
        self.scaleDrivers["Very Low"] = [4.05, 4.07, 6.07, 4.22, 4.94, 4.54]
        self.scaleDrivers["Low"] = [3.24, 4.86, 3.38, 3.95, 3.64]
        self.scaleDrivers["Nominal"] = [2.43, 3.64, 2.53, 2.97, 2.73]
        self.scaleDrivers["High"] = [1.62, 2.43, 1.69, 1.98, 1.82]
        self.scaleDrivers["Very High"] = [0.81, 1.21, 0.84, 0.99, 0.91]
        self.scaleDrivers["Extra High"] = [0, 0, 0, 0, 0]

class Modify_Cost_Drivers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        label = tk.Label(self, text="Cost Drivers", font=LARGE_FONT)
        label.place(x=655, y=42)
        back_button = tk.Button(self, text="Back", font=BUTTON_FONT, command=lambda: controller.show_frame(Effort_Page))
        back_button.place(x=150, y=950)

        values = ['Very Low', 'Low', 'Nominal', 'High', 'Very High', 'Extra High']
        headings = ['Required Software Reliability', 'Data Base Size', 'Product Complexity', 'Developed for Reusability',
                    'Documentation Match', 'Time Constraint', 'Storage Constraint', 'Platform Volatility',
                     'Analyst Capability', 'Programmer Capability', 'Personnel Continuity', 'Application Experience',
                    'Platform Experience', 'Language and Toolset Exp.', 'Use of Software Tools', 
                    'Multisite Development', 'Required Dev. Schedule']
        self.var = []
        dropdowns = []
        SF_Labels = []

        h = 0
        for i in range(9):
            self.var.append(tk.StringVar())
            self.var[i].set('Nominal')
            dropdowns.append(tk.OptionMenu(self, self.var[i], *values))
            dropdowns[i].config(width=15, font=('calibri', 15))
            dropdowns[i]['menu'].config(font=('calibri', 15))
            dropdowns[i].place(x=560, y=270 + h)
            SF_Labels.append(tk.Label(self, text=headings[i], font=RADIO_FONT))
            SF_Labels[i].place(x=90, y=270 + h)
            h = h + 70

        h = 0
        for i in range(9, 17):
            self.var.append(tk.StringVar())
            self.var[i].set('Nominal')
            dropdowns.append(tk.OptionMenu(self, self.var[i], *values))
            dropdowns[i].config(width=15, font=('calibri', 15))
            dropdowns[i]['menu'].config(font=('calibri', 15))
            dropdowns[i].place(x=1440, y=290 + h)
            SF_Labels.append(tk.Label(self, text=headings[i], font=RADIO_FONT))
            SF_Labels[i].place(x=970, y=290 + h)
            h = h + 70

    def set_costDrivers(self):
        
        self.costDrivers = dict()
        self.costDrivers["Very Low"] = [0.75, 1, 0.75, 1, 0.89, 1, 1, 1, 1.50, 1.37, 1.24, 1.22,
                                1.25, 1.22, 1.24, 1.25, 1.29]

        self.costDrivers["Low"] = [0.88, 0.93, 0.88, 0.91, 0.95, 1, 1, 0.87, 1.22, 1.16, 1.10,
                                1.10, 1.12, 1.10, 1.12, 1.10, 1.10]

        self.costDrivers["Nominal"] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.costDrivers["High"] = [1.15, 1.09, 1.15, 1.14, 1.06, 1.11, 1.06, 1.15, 0.83, 0.87,
                                0.92, 0.89, 0.88, 0.91, 0.86, 0.92, 1]

        self.costDrivers["Very High"] = [1.39, 1.19, 1.30, 1.29, 1.13, 1.31, 1.21, 1.30, 0.67,
                                0.74, 0.84, 0.81, 0.81, 0.84, 0.72, 0.84, 1] 

        self.costDrivers["Extra High"] = [1, 1, 1.66, 1.49, 0, 1.67, 1.57, 1, 1, 1, 1, 1, 1, 1, 1,
                                0.78, 1]

  
