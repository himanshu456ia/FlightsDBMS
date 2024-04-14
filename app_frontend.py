import tkinter as tk
from tkinter import messagebox

def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()

class Starting_window:
    def __init__(self, master=None):
        # Constructor for the greeting window
        self.root = master
        self.root.title("Flight Database")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f"{window_width//4}x{window_height//3}")
        self.root.resizable(width=False, height=False)
        
        # Frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill='both', expand=True)

        title_frame = tk.Frame(main_frame, bg='gray')
        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0,weight=1)
        title_frame.pack(fill='both', expand=True, padx=10, pady=5)

        query_frame = tk.Frame(main_frame)
        query_frame.columnconfigure(0, weight=1)
        query_frame.columnconfigure(1, weight=1)
        query_frame.rowconfigure(0, weight=1)
        query_frame.rowconfigure(1, weight=2)
        query_frame.pack(fill='both', expand=True, padx=40, pady=10)

        action_frame = tk.Frame(main_frame)
        # action_frame.columnconfigure(0, weight=5)
        # action_frame.columnconfigure(1, weight=1)
        # action_frame.columnconfigure(2, weight=1)
        action_frame.pack(side='bottom', fill='x', padx=10, pady=5)

        # Labels
        self.lbl_title = tk.Label(title_frame, text="Flight Enquiry System", font='Arial 20 bold')
        self.lbl_title.grid(row=0, column=0, sticky='nwes', padx=10, pady=5)

        self.query_title = tk.Label(query_frame, text="What would you like to enquire about?", font='Arial 12')
        self.query_title.grid(row=0, columnspan=2, sticky='nsew')
        
        # Radiobutton to choose DB
        self.v = tk.StringVar(query_frame, 'None')
        self.rdiobtn_flight = tk.Radiobutton(query_frame, text="Flights", value='F', variable=self.v)
        self.rdiobtn_flight.grid(row=1, column=0, sticky='nsew')
        self.rdiobtn_passengers = tk.Radiobutton(query_frame, text="Passengers", value='P', variable=self.v)
        self.rdiobtn_passengers.grid(row=1, column=1, sticky='nsew')        

        # Buttons
        self.btn_exit = tk.Button(action_frame, text='Quit', font='Arial 12', command=self.on_closing)
        self.btn_exit.pack(side='right', fill='y')
        self.btn_done = tk.Button(action_frame, text='Next', font='Arial 12', command=self.on_done)
        self.btn_done.pack(side='right', fill='y')

        # Protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # Function handling the closing window
        if messagebox.askyesno(title="Quit?", message="Do you want to quit?"):
            self.root.destroy()

    def on_done(self):
        # Function handling actions after pressing done
        if self.v.get()=='None':
            messagebox.showinfo(title="Help", message="Choose one of the options!")
        elif self.v.get()=='F':
            clear_frame(self.root)
            flight_window = Flight_window(self)
        elif self.v.get()=='P':
            clear_frame(self.root)
            passenger_window = Passenger_window(self)

class Flight_window(Starting_window):
    def __init__(self, starting_window):
        self.root = starting_window.root
        self.root.title("Flights Enquiry Database")
        self.root.geometry("1260x720")

class Passenger_window(Starting_window):
    def __init__(self, starting_window):
        self.root = starting_window.root
        self.root.title("Passengers Enquiry Database")
        self.root.geometry("1260x720")


if __name__ == "__main__":
    root = tk.Tk()
    window = Starting_window(root)
    root.mainloop()

