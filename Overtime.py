import tkinter as tk          
from tkinter import font  as tkfont

import matplotlib as plt
from matplotlib import style
import datetime 
from datetime import timedelta

       
class OvertimeApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Helvetica', size=12, weight="bold")
        self.sub_title_font = tkfont.Font(family='Helvetica', size=8, weight="bold")
        self.title('Overtime')
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (HomePage, PageOne, PageTwo, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame('HomePage')
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()     
     
      
class HomePage(tk.Frame):   

          
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Home Page', font=controller.title_font)
        label.grid(row=1, column=2)
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.timelabel = tk.Label(self, text=self.time, font=controller.sub_title_font)
        self.timelabel.grid(row=2, column=2)
        self.update_time()
        self.onsite = False
        
        button1 = tk.Button(self, text='Page One',
                             command = lambda: controller.show_frame('PageOne'))
                             
        button2 = tk.Button(self, text='Page Two',
                             command = lambda: controller.show_frame('PageTwo'))
                             
        button3 = tk.Button(self, text='Settings',
                             command = lambda: controller.show_frame('Settings'))    
                              
        cibutton = tk.Button(self, text='Check In',
                             command = self.check_in_time)
        cobutton = tk.Button(self, text='Check Out',
                             command = self.check_out_time)
        rsbutton = tk.Button(self, text='Reset',
                             command = self.check_in_reset)        
        
        self.citime_text = ''
        self.cilabel = tk.Label(self, text=self.citime_text)
        self.cilabel.grid(row=3, column=2)
        self.cotime_text = ''
        self.colabel = tk.Label(self, text= self.cotime_text)
        self.colabel.grid(row=4, column=2)
        self.ottext = ''      
        self.otlabel = tk.Label(self, text = self.ottext)
        self.otlabel.grid(row=5, column=2)
        
        cibutton.grid(row=3, column=1,columnspan=2,sticky='W',padx=1,pady=1)                      
        cobutton.grid(row=4, column=1,columnspan=2,sticky='W',padx=1,pady=1)
        rsbutton.grid(row=5, column=1,columnspan=2,sticky='W',padx=1,pady=1)                  
        button1.grid(row=10, column=1,sticky='SW',padx=2,pady=2)
        button2.grid(row=10, column=2,sticky='S',padx=2,pady=2)
        button3.grid(row=10, column=3,sticky='SE',padx=2,pady=2)
             
    def update_time(self):
        timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time = timenow
        self.timelabel.config(text=self.time)
        self.timelabel.after(200, self.update_time)  
     
    def check_in_time(self):
        
        if self.onsite == False:
            self.onsite = True
            self.citime = datetime.datetime.now()
            self.citime_text = datetime.datetime.now().strftime(' %H:%M ')
            self.update_label()

    def check_out_time(self):
        if self.onsite == True:
            self.cotime = datetime.datetime.now()
            self.cotime_text = self.cotime.strftime(' %H:%M ')
            self.update_label()
            self.overtime_calc()

    def check_in_reset(self):
        self.onsite = False
        self.cotime_text = ''
        self.citime_text = ''
        self.ottext = ''
        self.update_label()  
        
    def update_label(self):
       self.cilabel.config(text=self.citime_text)
       self.colabel.config(text=self.cotime_text)
       self.otlabel.config(text=self.ottext)
    
    def overtime_calc(self):
     
       inputshiftpatten = 'Enginnering Day Shift'
       #dayoftheweek = datetime.datetime.today().weekday()
       dayoftheweek = 5
       shift_patten = {'Enginnering Day Shift':[[7,55,16,40,30,1,1.5],[7,55,16,40,30,1,1.5],[7,55,16,40,30,1,1.5],[7,55,16,40,30,1,1.5],[7,55,14,25,30,1,1.5],[0,0,0,0,0,1,1.5],[0,0,0,0,0,1,2]]}
       
       contracthours = shift_patten[inputshiftpatten]
      
       stimehours = contracthours[dayoftheweek][0]
       stimemins = contracthours[dayoftheweek][1]
       ftimehours = contracthours[dayoftheweek][2]
       ftimemins = contracthours[dayoftheweek][3]
       ltimemins = contracthours[dayoftheweek][4]
       shiftmulti = contracthours[dayoftheweek][5]
       otmulti = contracthours[dayoftheweek][6]
      
       stime = timedelta(hours=stimehours, minutes=stimemins)
       ftime = timedelta(hours=ftimehours, minutes=ftimemins)
       ltime = timedelta(minutes=ltimemins)
       conthours = ftime - stime - ltime
       hoursin = self.cotime - self.citime
      
       if hoursin > conthours:
           overtime = hoursin - conthours
           overtime_text = ':'.join(str(overtime).split(':')[:2])
           
       else: 
           overtime = timedelta(hours=0)
           overtime_text='0:00'
           
       self.ottext = "Overtime: " + str(overtime_text)    
       self.update_label()  
   
   
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='This is page one', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        
        button = tk.Button(self, text='Home',
                           command = lambda: controller.show_frame('HomePage'))
        button.pack()
  
         
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='This is page two', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        
        button = tk.Button(self, text='Home',
                           command = lambda: controller.show_frame('HomePage'))
        button.pack()


class Settings(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Settings', font=controller.title_font)
        label.grid(row=1, column=2, padx=2, pady=2)
        
        button = tk.Button(self, text='Home',
                           command = lambda: controller.show_frame('HomePage'))
                           
        button.grid(row=10, column=1,sticky='SW',padx=2,pady=2)

        self.shiftpatten = ['','1','2','3','4']        
     
        e1label = tk.Label(self, text='Start Time')
        e1label.grid(row=3,column=1)
        e2label = tk.Label(self, text='Start Time')
        e2label.grid(row=4,column=1)
        e3label = tk.Label(self, text='Start Time')
        e3label.grid(row=3,column=3)
        e4label = tk.Label(self, text='Start Time')
        e4label.grid(row=4,column=3)
        
        e1 = tk.Entry(self, width=10)
        e1.grid(row=3, column=2)
        e2 = tk.Entry(self, width=10)
        e2.grid(row=4, column=2)
        e3 = tk.Entry(self, width=10)
        e3.grid(row=5, column=2)
        e4 = tk.Entry(self, width=10)
        e4.grid(row=6, column=2)
        e5 = tk.Entry(self, width=10)
        e5.grid(row=3, column=4)
        e6 = tk.Entry(self, width=10)
        e6.grid(row=4, column=4)
        e7 = tk.Entry(self, width=10)
        e7.grid(row=5, column=4)
        e8 = tk.Entry(self, width=10)
        e8.grid(row=6, column=4)
        
if __name__ == '__main__':
    app = OvertimeApp()
    app.mainloop()
    