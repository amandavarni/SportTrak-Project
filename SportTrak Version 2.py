'''
Program: SportTrak Application
Date: April 12, 2022
Purpose: Estimate resources required for TCU sporting events
Installation Instructions: Install this file and the accompanying GWlogo.gif in the same folder 
'''

from tkinter import * # Import tkinter; do not need to install it

class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window instance
        window.title("SportTrak") # Set title of the window
        
        # First, create labels in the window for each input value.
        Label(window, text = "User ID: ").grid(row = 2, column = 1, sticky = W) # if proper ID is not entered
        Label(window, text = "Select Sport: ").grid(row = 3, column = 1, sticky = W) # Drop down input selection
        Label(window, text = "Event Date: ").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Expected Weather").grid(row = 5, column = 1, sticky = W) # Drop down input selection
        Label(window, text = "Opponent: ").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Expected Student Attendence: ").grid(row = 7, column = 1, sticky = W)
        Label(window, text = "Expected Non-Student Attendence: ").grid(row = 8, column = 1, sticky = W)
        
        # Next, create labels in the window for each output value.
        Label(window, text = "Hot Dogs: ").grid(row = 2, column = 3, sticky = W)
        Label(window, text = "Nachos: ").grid(row = 3, column = 3, sticky = W)
        Label(window, text = "Pretzels: ").grid(row = 4, column = 3, sticky = W)
        Label(window, text = "Burgers: ").grid(row = 5, column = 3, sticky = W)
        Label(window, text = "Water: ").grid(row = 6, column = 3, sticky = W)
        Label(window, text = "Beer: ").grid(row = 7, column = 3, sticky = W)
        Label(window, text = "Soda: ").grid(row = 8, column = 3, sticky = W)
        Label(window, text = "Staffing: ").grid(row = 9, column = 3, sticky = W)

        #For each of the seven inputs, create string variable and get their values through Entry control
        self.User_ID_Var = StringVar()
        Entry(window, textvariable = self.User_ID_Var, justify = RIGHT).grid(row = 2, column = 2)
        self.Select_Sport_Var = StringVar()
        Entry(window, textvariable = self.Select_Sport_Var, justify = RIGHT).grid(row = 3, column = 2)
        self.Event_Date_Var = StringVar()
        Entry(window, textvariable = self.Event_Date_Var, justify = RIGHT).grid(row = 4, column = 2)
        self.Expected_Weather_Var = StringVar()
        Entry(window, textvariable = self.Expected_Weather_Var, justify = RIGHT).grid(row = 5, column = 2)
        self.Opponent_Var = StringVar()
        Entry(window, textvariable = self.Opponent_Var, justify = RIGHT).grid(row = 6, column = 2)
        self.Student_Attendance_Var = StringVar()
        Entry(window, textvariable = self.Student_Attendance_Var, justify = RIGHT).grid(row = 7, column = 2)
        self.Non_Student_Attendance_Var = StringVar()
        Entry(window, textvariable = self.Non_Student_Attendance_Var, justify = RIGHT).grid(row = 8, column = 2)
        
        #For each of the eight outputs, crete a String variable and output each to a Label in the Window
        self.Hot_Dogs_Var = StringVar()
        Label(window, textvariable = self.Hot_Dogs_Var).grid(row = 2, column = 3, sticky = E)
        self.Nachos_Var = StringVar()
        Label(window, textvariable = self.Nachos_Var).grid(row = 3, column = 3, sticky = E)
        self.Pretzels_Var = StringVar()
        Label(window, textvariable = self.Pretzels_Var).grid(row = 4, column = 3, sticky = E)
        self.Burgers_Var = StringVar()
        Label(window, textvariable = self.Burgers_Var).grid(row = 5, column = 3, sticky = E)
        self.Water_Var = StringVar()
        Label(window, textvariable = self.Water_Var).grid(row = 6, column = 3, sticky = E)
        self.Beer_Var = StringVar()
        Label(window, textvariable = self.Beer_Var).grid(row = 7, column = 3, sticky = E)
        self.Soda_Var = StringVar()
        Label(window, textvariable = self.Soda_Var).grid(row = 8, column = 3, sticky = E)
        self.Staffing_Var = StringVar()
        Label(window, textvariable = self.Staffing_Var).grid(row = 9, column = 3, sticky = E)
        
        #Create a Compute Payment button to call the computePayment function
        Button(window, text = "Compute", command = self.Compute).grid(row = 9, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop
        

def Weather(self):
    weather_forecast = self.Expected_Weather_Var(
        int(self.Expected_Weather_Var.get()))
    return weather_forecast
def Opponent(self):
    opponent = self.Opponent_Var(
        self.Opponent_Var.get())
    return opponent
def Students(self):
    students_attendance = self.Student_Attendance_Var(
        int(self.Student_Attendance_Var.get()))
    return students_attendance
def Non_Students(self):
    non_students = self.Non_Student_Attendance_Var(
        int(self.Non_Student_Attendance_Var.get()))
    return non_students
    
weather = Weather()
students = Students()
non_students = Non_Students()

attendance = students + non_students

def Compute_Weather(weather,attendance):
    attendance = attendance
    if weather >80:
        attendance = attendance*0.9
    elif weather <50:
        attendance = attendance*0.8
    else:
        attendance = attendance*1.1
    return attendance
    
attendance = Compute_Weather()

def Compute_Opponent(opponent,attendance):
    attendance = attendance
    if opponent == 'Yes':
        attendance = attendance*1.2
    else:
        attendance = attendance
    return attendance

final_attendance = Compute_Opponent()


