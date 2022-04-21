'''
Program: SportTrak
Developers: Alex Herman, Amanda Varni, Noah Skolnick, and William Westhoff
Date: April 20, 2022
Purpose: Team Project
Installation Instructions: Install tkinter and tkcalendar; have TCU_logo.gif in the same folder
Accepted User IDs (Admin): "tcu_football", "tcu_soccer", "tcu_baseball", "tcu_basketball"
'''
# Imports used
import tkinter as tk
import tkinter.messagebox as message
from tkcalendar import Calendar, DateEntry
 
# Class definition
class SportTrak:
 
    # class constructor
    def __init__(self):
 
        # Instantiate Tkinter Window
        window = tk.Tk()
 
        # Adds TCU Athletics logo
        photo = tk.PhotoImage(file=r'TCU_logo.gif')
        tk.Label(window, image=photo).grid(row = 1, column = 1, sticky = tk.W)
 
        # Sets window color
        window.geometry("550x400")
        window.configure(bg='white')
 
        # Lock Computations if user is not admin
        self.lock = True               
        
        # Class Members
        self.userIdVar = tk.StringVar()
        self.select_sportVar = tk.StringVar()
        self.eventdateVar = tk.StringVar()
        self.expected_weatherVar = tk.IntVar()
        self.opponentVar = tk.StringVar()
        self.student_attendVar = tk.IntVar()
        self.nonstudent_attendVar = tk.IntVar()
 
        # Values are referenced to display computations
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
        tk.Label(window, text = "Nachos: ").grid(row = 6, column = 5, sticky = tk.E)
        tk.Label(window, text = "Pretzels: ").grid(row = 7, column = 5, sticky = tk.E)
        tk.Label(window, text = "Burgers: ").grid(row = 8, column = 5, sticky = tk.E)
        tk.Label(window, text = "Waters: ").grid(row = 9, column = 5, sticky = tk.E)
        tk.Label(window, text = "Beers: ").grid(row = 10, column = 5, sticky = tk.E)
        tk.Label(window, text = "Sodas: ").grid(row = 11, column = 5, sticky = tk.E)
        tk.Label(window, text = "Staffing: ").grid(row = 12, column = 5, sticky = tk.E)
 
        #list for option menu
        sport_list = ["Football", "Womens Soccer", "Baseball", "Basketball"]
 
        # Create input boxes for users to pass values through Entry control (IS THIS WHERE I ADD CONDITIONS LIKE PASSOWRD LENGTH?)
        userid_selection = tk.Entry(window, textvariable = self.userIdVar, justify = tk.RIGHT).grid(row = 5, column = 2)
        self.userIdVar.set(userid_selection)
 
        sport_selection = tk.OptionMenu(window, self.select_sportVar,*sport_list).grid(row = 6, column = 2, sticky = tk.E)
        self.select_sportVar.set(sport_selection)
 
        date_selection = DateEntry(window).grid(row = 7, column = 2, sticky = tk.E)
        self.eventdateVar.set(date_selection)
 
        weather_selection = tk.Entry(window, textvariable = self.expected_weatherVar, justify =tk.RIGHT).grid(row = 8, column = 2)
        self.expected_weatherVar.set(weather_selection)
 
        opponent_selection = tk.OptionMenu(window, self.opponentVar,"Yes","No").grid(row = 9, column = 2, sticky = tk.E)
        self.opponentVar.set(opponent_selection)
 
        student_attendance_selection= tk.Entry(window, textvariable = self.student_attendVar, justify =tk.RIGHT).grid(row = 10, column = 2)
        self.student_attendVar.set(student_attendance_selection)
 
        non_studentattendance_selection = tk.Entry(window, textvariable = self.nonstudent_attendVar, justify =tk.RIGHT).grid(row = 11, column = 2)
        self.nonstudent_attendVar.set((non_studentattendance_selection))
 
        # For each of the eight outputs, self. a String variable and output each to a Label in the Window
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
 
    # These defs calculate the the total attendance for the final calculations
    def compute_weather(self) -> float:
        base_attend = self.get_base_attend()
        weather = self.expected_weatherVar.get()
        b1A = 1
        if weather >= 90:
            b1A = base_attend * 0.15
        elif weather <= 89 and weather >= 51:
            b1A = 0
        elif weather <= 50:
            b1A = base_attend * 0.2
        else:
            b1A = base_attend
        return b1A
 
    def compute_opponent(self) -> float:
        base_attend = self.get_base_attend()
        opponent = self.opponentVar.get()
        b2A = 1
        if opponent == "Yes": 
            b2A = base_attend
        else:
            base_attend *= 0.25
            b2A = base_attend
        return b2A
 
    def get_base_attend(self) -> float:
        student_attend = self.student_attendVar.get()
        nonstudent_attend = self.nonstudent_attendVar.get()
        base_attend = student_attend + nonstudent_attend
        return base_attend
 
    def get_total_attend(self):
        total_attend = self.get_base_attend() - self.compute_weather() + self.compute_opponent()
        return total_attend

    def program_computations(self):
        total_attend = self.get_total_attend()
 
        # Admin users
        userIDs = ["tcu_football", "tcu_soccer", "tcu_baseball", "tcu_basketball"]
        user_value = self.userIdVar.get()
        
        # For-in loop
        for x in userIDs:     
 
            # User ID passed is admin user       
            if x == user_value:
                print("UNLOCKING PROGRAM")
                self.lock = False
                break
 
            # User ID passed is NOT an admin users: LOCK program
            else:
                print(f"LOCKING PROGRAM {user_value}")
                self.lock = True
                
        
        # Program functionality is locked here if not admin user
        if(not self.lock): 
            hot_dog = int(total_attend * 0.2)
            nachos = int(total_attend * 0.2)
            pretzel = int(total_attend * 0.2)
            burger = int(total_attend * 0.2)
            water = int(total_attend * 0.4)
            beer = int(total_attend * 0.3)
            soda = int(total_attend * 0.2)
            staffing = int(total_attend * 0.05)
 
            self.hot_dogVar.set(hot_dog)
            self.nachosVar.set(nachos)
            self.pretzelVar.set(pretzel)
            self.burgersVar.set(burger)
            self.waterVar.set(water)
            self.beerVar.set(beer)
            self.sodaVar.set(soda)
            self.staffingVar.set(staffing)

        # Displays error message for non admin user
        else:
            message.showerror(title="ERROR", message="Unpermitted Access to Program")

# PROGRAM WILL START HERE AND WORK DOWNWARDS
tkinter_app = SportTrak()