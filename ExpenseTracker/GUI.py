from ExpenseTracker import main
import tkinter as tk


class ExpenseApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.bt = tk.Button(self, width=10)
        self.bt["text"] = "View"
        self.bt["command"] = self.view
        self.bt.pack(side="left")
        self.bt = tk.Button(self, width=10)
        self.bt["text"] = "log"
        self.bt["command"] = self.log
        self.bt.pack(side="right")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def view(self):
        print(main.view())
    
    def log(self):
        amount, category = input("Enter the amount and category").split(",")
        print(main.log(amount,category))

    # def run_expense(self, tk):
    #     root = tk.Tk()
    #     app = ExpenseApp(master=root)
    #     app.master.title("Expense Manager")
    #     app.master.geometry("1000x400")
    #     app.master.configure(bg='black')
    #     app.configure(bg='gray')
    #     app.mainloop()