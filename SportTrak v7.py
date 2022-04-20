'''
Program: SportTrak 
Developers: Alex Herman, Amanda Varni, Noah Skolnick, and William Westhoff
Date: April 20, 2022
Purpose: Team Project
Installation Instructions: Install tkinter and tkcalendar; have TCU_logo.gif in the same folder
'''
# To Do:
# Create entry restrictions and error messages
# Help button that displays help line number
# Get computations functional
# Set larger starting window size
# Change color of labels
#


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
        self.user_IDVar = tk.IntVar()
        self.select_sportVar = tk.StringVar()
        self.eventdateVar = tk.StringVar()
        self.expected_weatherVar = tk.IntVar()
        self.opponentVar = tk.StringVar()
        self.student_attendVar = tk.IntVar()
        self.nonstudent_attendVar = tk.IntVar()
 
        # reference these values to display computations
        self.hot_dogVar = tk.IntVar()
        self.nachosVar = tk.IntVar()
        self.pretzelVar = tk.IntVar()
        self.burgersVar = tk.IntVar()
        self.waterVar = tk.IntVar()
        self.beerVar = tk.IntVar()
        self.sodaVar = tk.IntVar()
        self.staffingVar = tk.IntVar()

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
        tk.Label(window, text = "Waters: ").grid(row = 9, column = 5, sticky = tk.W)
        tk.Label(window, text = "Beers: ").grid(row = 10, column = 5, sticky = tk.W)
        tk.Label(window, text = "Sodas: ").grid(row = 11, column = 5, sticky = tk.W)
        tk.Label(window, text = "Staffing: ").grid(row = 12, column = 5, sticky = tk.W)
 
        #list for option menu
        sport_list = ["Football", "Womens Soccer", "Baseball", "Basketball"]
        
        # Create input boxes for users to pass values through Entry control (IS THIS WHERE I ADD CONDITIONS LIKE PASSOWRD LENGTH?)
        userId_selection = tk.Entry(window, textvariable = self.user_IDVar, justify = tk.RIGHT).grid(row = 5, column = 2) #lengths
        self.user_IDVar.set(userId_selection)
       
        #tk.OptionMenu(window, textvariable = self.Select_Sport_Var, *sport_list,justify =tk.RIGHT).grid(row = 3, column = 2) #four sports
        sport_selection = tk.OptionMenu(window, self.select_sportVar,*sport_list).grid(row = 6, column = 2)
        self.select_sportVar.set(sport_selection)

        date_selection = DateEntry(window).grid(row = 7, column = 2) #date format only
        self.eventdateVar.set(date_selection)

        weather_selection = tk.Entry(window, textvariable = self.expected_weatherVar, justify =tk.RIGHT).grid(row = 8, column = 2) #two integers
        self.expected_weatherVar.set(weather_selection)

        opponent_selection = tk.OptionMenu(window, self.opponentVar,"Yes","No").grid(row = 9, column = 2) #how to make computation work for drop down value
        self.opponentVar.set(opponent_selection)

        student_attendance_selection= tk.Entry(window, textvariable = self.student_attendVar, justify =tk.RIGHT).grid(row = 10, column = 2) #integer
        self.student_attendVar.set(student_attendance_selection)
        
        non_studentattendance_selection = tk.Entry(window, textvariable = self.nonstudent_attendVar, justify =tk.RIGHT).grid(row = 11, column = 2) #integer
        self.nonstudent_attendVar.set((non_studentattendance_selection))
       
        #For each of the eight outputs, self. a String variable and output each to a Label in the Window
        tk.Label(window, textvariable = self.hot_dogVar).grid(row = 5, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.nachosVar).grid(row = 6, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.pretzelVar).grid(row = 7, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.burgersVar).grid(row = 8, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.waterVar).grid(row = 9, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.beerVar).grid(row = 10, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.sodaVar).grid(row = 11, column = 8, sticky = tk.E)
        tk.Label(window, textvariable = self.staffingVar).grid(row = 12, column = 8, sticky = tk.E)

 
        # This button runs the computations defined below in the program_computations funciton
        tk.Button(window, text = "Compute", command = self.program_computations).grid(row = 15, column = 2, sticky = tk.E)

        # This loops the window
        window.mainloop()
        
    def compute_weather(self):
        base_attend = self.get_base_attend
        weather = self.expected_weatherVar.get()
        if weather >= 90:
            b1A = base_attend * 0.2
        elif weather <= 89 and weather >= 51:
            b1A = 0
        elif weather <= 50:
            b1A = base_attend * 0.3
        else:
            b1A = base_attend
        return b1A

    def compute_opponent(self):
        base_attend = self.get_base_attend
        opponent = self.opponentVar.get()
        if opponent == "Yes":
            b2A = base_attend * 0.5
        else:
            b2A = base_attend
        return b2A

    def get_base_attend(self):
        student_attend = self.student_attendVar.get()
        nonstudent_attend = self.nonstudent_attendVar.get()
        base_attend = student_attend + nonstudent_attend
        return base_attend

    def get_total_attend(self):
        total_attend = (self.get_base_attend - self.compute_weather) + self.compute_opponent 
        return total_attend

    def program_computations(self):
        total_attend = self.get_total_attend
        hot_dog = total_attend * 0.2
        self.hot_dogVar.set(hot_dog)
        nachos = total_attend * 0.2
        self.nachosVar.set(nachos)
        pretzel = total_attend * 0.2
        self.pretzelVar.set(pretzel)
        burger = total_attend * 0.2
        self.burgersVar.set(burger)
        water = total_attend * 0.4
        self.waterVar.set(water)
        beer = total_attend * 0.3
        self.beerVar.set(beer)
        soda = total_attend * 0.2
        self.sodaVar.set(soda)
        staffing = total_attend * 0.5
        self.staffingVar.set(staffing)
        
# PROGRAM WILL START HERE AND WORK DOWNWARDS 
tkinter_app = Tkinter_Example()