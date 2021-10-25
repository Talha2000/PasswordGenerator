import tkinter as tk
from ExpenseTracker import GUI, main
# from BudgetCalculator.GUI import app2


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.bt = tk.Button(self, width = 50)
        self.bt["text"] = "Expense Tracker"
        self.bt["command"] = Application.createNewWindow_expense
        self.bt.pack(side="left")        
        self.bt = tk.Button(self, width = 50)
        self.bt["text"] = "Budget Calculator"
        self.bt.pack(side="right")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                    command=self.master.destroy)
        self.quit.pack(side="bottom")

    # def select_widget(self):
    #     # if self.bt["text"] == "Expense Tracker":
    #     #     self.bt["command"] = self.createNewWindow_expense

    # After clicking the Expense Tracker button
    # Open a new or clear existing window with new window.
    def createNewWindow_expense():
        root = tk.Tk()
        app = GUI.ExpenseApp(master=root)
        app.master.title("Expense Manager")
        app.master.geometry("1000x400")
        app.master.configure(bg='black')
        app.configure(bg='gray')
        app.mainloop()

root = tk.Tk()
app = Application(master=root)
app.master.title("Expense Man")
app.master.geometry("1000x400")
app.master.configure(bg='black')
app.configure(bg='gray')
app.mainloop()