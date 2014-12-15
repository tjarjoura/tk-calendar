import tkinter as tk
import tkinter.font as tkFont
import calendar

week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
year = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

class Application(tk.Frame):
    def __init__(self, master=None, month=11):
        tk.Frame.__init__(self, master) 
        self.grid()
        self.month = month 
   
        self.createWidgets()

    def createWidgets(self):
        self.monthDays = [] # Widgets for days of the month
        self.weekDays = [] # Widgets for days of the week
        
        self.monthLabel = tk.Label(self, font=tkFont.Font(weight="bold", family="Helvetica", size=20), text=year[self.month])
        
        for i in range(7): # Create days of the week
            sq = tk.Label(self, font=tkFont.Font(weight="bold"), text=week[i])
            sq.grid(column=i, row=1)
            self.weekDays.append(sq)
        
        for i in range(6): # Create days of the month
            for j in range(7):
                sq = DateSlot(self, day=i*7 + j)
                sq.grid(column=j, row=i+2, sticky = tk.N + tk.S + tk.W + tk.E)
                sq.grid_propagate(0)
                self.monthDays.append(sq)

class DateSlot(tk.Frame):
    def __init__(self, master, day=0):
        tk.Frame.__init__(self, master, borderwidth=1, width=50, height=50, relief=tk.RIDGE)
        self.grid()

        self.day = tk.Label(self, text=str(day))
        self.day.grid(row=0, column=0)
            
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
