import tkinter as tk
from tkcalendar import Calendar, DateEntry


# Class Definition

class Tkinter_Example:

 

    # class constructor

    def __init__(self):

        # Instantiate Tkinter Window

        window = tk.Tk()

        # Adds TCU Athletics logo
        photo = tk.PhotoImage(file=r'TCU_logo.gif') # specify the path to your file; the r prefix stands for "raw" string
        tk.Label(window, image=photo).grid(row = 1, column = 1, sticky = tk.W)

        # Sets window color
    
        window.geometry("400x200")
        window.configure(bg='purple')

        # Class Members
        self.User_ID_Var = tk.StringVar()
        self.Select_Sport_Var = tk.StringVar()
        self.Event_Date_Var = tk.StringVar()
        self.Expected_Weather_Var = tk.StringVar()
        self.Opponent_Var = tk.StringVar()
        self.Student_Attendance_Var = tk.StringVar()
        self.Non_Student_Attendance_Var = tk.StringVar()
 
        # reference these values to display computations
        self.Hot_Dogs_Var = tk.StringVar()
        self.Nachos_Var = tk.StringVar()
        self.Pretzels_Var = tk.StringVar()
        self.Burgers_Var = tk.StringVar()
        self.Water_Var = tk.StringVar()
        self.Beer_Var = tk.StringVar()
        self.Soda_Var = tk.StringVar()
        self.Staffing_Var = tk.StringVar()

        # Set title of the window
        window.title("SportTrak")

        # Create labels for user input values
        tk.Label(window, text = "User ID: ").grid(row = 5, column = 1, sticky = tk.W)
        tk.Label(window, text = "Select Sport: ").grid(row = 6, column = 1, sticky = tk.W)
        tk.Label(window, text = "Event Date: ").grid(row = 7, column = 1, sticky = tk.W)
        tk.Label(window, text = "Expected Weather").grid(row = 8, column = 1, sticky = tk.W)
        tk.Label(window, text = "Big 12 Opponent: ").grid(row = 9, column = 1, sticky = tk.W)
        tk.Label(window, text = "Expected Student Attendence: ").grid(row = 10, column = 1, sticky = tk.W)
        tk.Label(window, text = "Expected Non-Student Attendence: ").grid(row = 11, column = 1, sticky = tk.W)
       
        # Create labels for the program outout values
        tk.Label(window, text = "Hot Dogs: ").grid(row = 5, column = 5, sticky = tk.E)
        tk.Label(window, text = "Nachos: ").grid(row = 6, column = 5, sticky = tk.W)
        tk.Label(window, text = "Pretzels: ").grid(row = 7, column = 5, sticky = tk.W)
        tk.Label(window, text = "Burgers: ").grid(row = 8, column = 5, sticky = tk.W)
        tk.Label(window, text = "Water: ").grid(row = 9, column = 5, sticky = tk.W)
        tk.Label(window, text = "Beer: ").grid(row = 10, column = 5, sticky = tk.W)
        tk.Label(window, text = "Soda: ").grid(row = 11, column = 5, sticky = tk.W)
        tk.Label(window, text = "Staffing: ").grid(row = 12, column = 5, sticky = tk.W)
 
        #list for option menu
        sport_list = ["Football", "Womens Soccer", "Baseball", "Basketball"]
        
        # Create input boxes for users to pass values through Entry control (IS THIS WHERE I ADD CONDITIONS LIKE PASSOWRD LENGTH?)
        userId_selection = tk.Entry(window, textvariable = self.User_ID_Var, justify = tk.RIGHT).grid(row = 5, column = 2) #lengths
        self.User_ID_Var.set(userId_selection)
       

        #tk.OptionMenu(window, textvariable = self.Select_Sport_Var, *sport_list,justify =tk.RIGHT).grid(row = 3, column = 2) #four sports
        sport_selection = tk.OptionMenu(window, self.Select_Sport_Var,*sport_list).grid(row = 6, column = 2)
        self.Select_Sport_Var.set(sport_selection)

        date_selection = DateEntry(window).grid(row = 7, column = 2) #date format only
        self.Event_Date_Var.set(date_selection)

        weather_selection = tk.Entry(window, textvariable = self.Expected_Weather_Var, justify =tk.RIGHT).grid(row = 8, column = 2) #two integers
        self.Expected_Weather_Var.set(weather_selection)

        opponent_selection = tk.OptionMenu(window, self.Opponent_Var,"Yes","No").grid(row = 9, column = 2) #how to make computation work for drop down value
        self.Opponent_Var.set(opponent_selection)

        student_attendance_selection= tk.Entry(window, textvariable = self.Student_Attendance_Var, justify =tk.RIGHT).grid(row = 10, column = 2) #integer
        self.Student_Attendance_Var.set(student_attendance_selection)
        
        non_studentattendance_selection = tk.Entry(window, textvariable = self.Non_Student_Attendance_Var, justify =tk.RIGHT).grid(row = 11, column = 2) #integer
        self.Non_Student_Attendance_Var.set((non_studentattendance_selection))
       
        #For each of the eight outputs, self. a String variable and output each to a Label in the Window
        tk.Label(window, textvariable = self.Hot_Dogs_Var).grid(row = 5, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.Nachos_Var).grid(row = 6, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.Pretzels_Var).grid(row = 7, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.Burgers_Var).grid(row = 8, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.Water_Var).grid(row = 9, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.Beer_Var).grid(row = 10, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.Soda_Var).grid(row = 11, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.Staffing_Var).grid(row = 12, column = 8, sticky = tk.E)

 
        # This button runs the computations defined below in the program_computations funciton
        tk.Button(window, text = "Compute", command = self.program_computations).grid(row = 15, column = 2, sticky = tk.E)

        # This loops the window
        window.mainloop()

    # This combines the computations to interact with one another when executing the compute button
    def program_computations(self):

        # Use these variables to get the values from the entries for calculations below
        userId= self.User_ID_Var.get()
        sport = self.Select_Sport_Var.get()
        date = self.Event_Date_Var.get()
        weather = self.Expected_Weather_Var.get()
        opponent = self.Opponent_Var.get()
        students = self.Student_Attendance_Var.get()
        nonStudents = self.Non_Student_Attendance_Var.get()
        
        # Call all computation functions here!!!!
        self.compute_weather(int(weather),int(self.compute_attendance()))
        self.compute_opponent
        self.compute_attendance

    def compute_attendance(self):
        students = self.Student_Attendance_Var.get()
        nonStudents = self.Non_Student_Attendance_Var.get()
        total_attendance = students + nonStudents
   
    def compute_weather(self,weather,attendance):
        if weather > 90:
            mult = attendance * 0.8
        elif weather < 50:
            mult = attendance * 0.6
        else:
            mult = attendance * 1
        print(mult)
        return mult

    def compute_opponent(self,opponent,attendance):
        attendance = attendance
        if opponent == 'Yes': # Need to account for drop down input
            attendance *= 1.5
        else:
            attendance = attendance


# PROGRAM WILL START HERE AND WORK DOWNWARDS 
tkinter_app = Tkinter_Example()