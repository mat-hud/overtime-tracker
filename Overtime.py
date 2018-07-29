import tkinter as tk
from tkinter import font as tkfont
import matplotlib as plt
from matplotlib import style
import datetime
from datetime import datetime

class OvertimeApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family = 'Helvetic', size=18, weight='bold')
        
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame('StartPage')
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='This is the start page', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timelabel = tk.Label(self, text=timenow, font=controller.title_font)
        timelabel.pack(side='top', fill='x', pady=10)
    
    def update_time(self):
        self.label.configure(timelabel)
        self.root.after(1000, self.update_time)
        
    
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='This is page one', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        
   
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='This is page two', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
            
        
if __name__ == '__main__':
    app = OvertimeApp()
    app.mainloop()
    