import tkinter as tk
from tkinter import font as tkfont
import matplotlib as plt
from matplotlib import style
import datetime
from datetime import datetime

class OvertimeApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family = 'Helvetic', size=10, weight='bold')
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
        label = tk.Label(self, text='This is the home page', font=controller.title_font)
        label.grid(row=1, column=2)
       
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.timelabel = tk.Label(self, text=self.time, font=controller.title_font)
        self.timelabel.grid(row=2, column=2)
        self.update_time()
        
        button1 = tk.Button(self, text='Page One',
                             command = lambda: controller.show_frame('PageOne'))
                             
        button2 = tk.Button(self, text='Page Two',
                             command = lambda: controller.show_frame('PageTwo'))
                             
        button3 = tk.Button(self, text='Settings',
                             command = lambda: controller.show_frame('Settings'))    
                              
        
        cibutton = tk.Button(self, text='Check In')
        cobutton = tk.Button(self, text='Check Out')
        rsbutton = tk.Button(self, text='Reset')        
        
        cibutton.grid(row=3, column=1,columnspan=2,sticky='W',padx=1,pady=1)                      
        cobutton.grid(row=4, column=1,columnspan=2,sticky='W',padx=1,pady=1)
        rsbutton.grid(row=5, column=1,columnspan=2,sticky='W',padx=1,pady=1)                  
        button1.grid(row=10, column=1,sticky='SW',padx=2,pady=2)
        button2.grid(row=10, column=2,sticky='S',padx=2,pady=2)
        button3.grid(row=10, column=3,sticky='SE',padx=2,pady=2)
        
        
    def update_time(self):
        timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time = timenow
        self.timelabel.config(text=self.time)
        self.timelabel.after(1000, self.update_time)        

   
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
        label.pack(side='top', fill='x', pady=10)
        
        button = tk.Button(self, text='Home',
                           command = lambda: controller.show_frame('HomePage'))
        button.pack()
                
if __name__ == '__main__':
    app = OvertimeApp()
    app.mainloop()
    