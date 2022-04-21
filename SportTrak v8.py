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
 
 
 
import tkinter as tk
from tkcalendar import Calendar, DateEntry
 
# Class Definition
class SportTrak:
 
    # class constructor
    def __init__(self):
 
        # Instantiate Tkinter Window
        window = tk.Tk()
 
        # Adds TCU Athletics logo
        photo = tk.PhotoImage(file=r'TCU_logo.gif') # specify the path to your file; the r prefix stands for "raw" string
        tk.Label(window, image=photo).grid(row = 1, column = 1, sticky = tk.W)
 
        # Sets window color
 
        window.geometry("550x400")
        window.configure(bg='black')
 
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
        userid_selection = tk.Entry(window, textvariable = self.user_IDVar, justify = tk.RIGHT).grid(row = 5, column = 2) #lengths
 
        self.user_IDVar.set(userid_selection)
 
        #tk.OptionMenu(window, textvariable = self.Select_Sport_Var, *sport_list,justify =tk.RIGHT).grid(row = 3, column = 2) #four sports
        sport_selection = tk.OptionMenu(window, self.select_sportVar,*sport_list).grid(row = 6, column = 2, sticky = tk.E)
        self.select_sportVar.set(sport_selection)
 
        date_selection = DateEntry(window).grid(row = 7, column = 2, sticky = tk.E) #date format only
        self.eventdateVar.set(date_selection)
 
        weather_selection = tk.Entry(window, textvariable = self.expected_weatherVar, justify =tk.RIGHT).grid(row = 8, column = 2) #two integers
        self.expected_weatherVar.set(weather_selection)
 
        opponent_selection = tk.OptionMenu(window, self.opponentVar,"Yes","No").grid(row = 9, column = 2, sticky = tk.E) #how to make computation work for drop down value
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
 
    def compute_weather(self) -> float:
        base_attend = self.get_base_attend()
        weather = self.expected_weatherVar.get()
        b1A = 1
        if weather >= 90:
            b1A = base_attend * 0.2
        elif weather <= 89 and weather >= 51:
            b1A = 0
        elif weather <= 50:
            b1A = base_attend * 0.3
        else:
            b1A = base_attend
        return b1A
 
    def compute_opponent(self) -> float:
        base_attend = self.get_base_attend()
        opponent = self.opponentVar.get()
 
        # MAKE SURE YOU INITALIZE VARIABLES ON THE SAME INDENTATION
        # LEVEL YOU WILL BE ACCESSING THEM
        # THIS IS CALLED THE SCOPE OF A VARIABLE
        # IF I INITIALIZE IT INSIDE AN IF STATEMENT, WHEN WE
        # COME OUT OF THE IF STATEMENT, THE VARIABLE IS 
        # POPPED OFF THE STACK AND IT IS NO LONGER REFERENCEABLE
 
        # I WOULD JUST USE base_attend, you can reuse it, no need for 
        # another variable
        b2A = 1
        if opponent == "Yes":
 
            # you can do it like this:
            base_attend *= 0.5 # this means multiple the value stored in base_attend by 0.5
            b2A = base_attend * 0.5
        else:
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
 
 
    # I HAVE IMPLEMENTED ROUNDING ON THE FLOATS WITH round(number, digits)
    # where number is the number to found and digits is the number of digits we are keeping
    # IF YOU WANT ALL OF THESE VALUES TO BE INTEGERS... cast it to int i.e. no decimals
    # like so:   int(number_to_round)
    def program_computations(self):
        total_attend = self.get_total_attend()
 
        # example of casting to an int here 
        hot_dog = int(total_attend * 0.2) # hot dogs will be an integer
        nachos = round(total_attend * 0.2,3)
        pretzel = round(total_attend * 0.2,3)
        burger = round(total_attend * 0.2,3)
        water = round(total_attend * 0.4,3)
        beer = round(total_attend * 0.3,3)
        soda = round(total_attend * 0.2,3)
        staffing = round(total_attend * 0.5,3)
 
 
        self.hot_dogVar.set(hot_dog)
        self.nachosVar.set(nachos)
        self.pretzelVar.set(pretzel)
        self.burgersVar.set(burger)
        self.waterVar.set(water)
        self.beerVar.set(beer)
        self.sodaVar.set(soda)
        self.staffingVar.set(staffing)
 
# PROGRAM WILL START HERE AND WORK DOWNWARDS
tkinter_app = SportTrak()
 
 
# Here is a cool example of how you can have your text Entry objects have defualt text
# as well as erase all the default text as soon as the user clicks into the box!!!
 
# i have commended this out here because I could not get it to work perfectly, and I 
# don't want to spend anymore time, i need to go to bed lol
 
# the fuction basicallly erases the text, you bind the textbox fucntionlity to the button
# so that on click it erases the text
 
# the other code just creates the default text and inserts it into the Entry object
 
# userid_selection = tk.Entry(window, justify = tk.RIGHT)
# userid_selection.grid(row = 5, column = 2) #lengths
# userid_selection.insert(tk.END, "Enter user ID Here")
# userid_selection.bind("<Button-1>", self.on_click)
 
# def on_click(self,event):
#     event.widget.delete(0, tk.END)
 
 
# I've determined that the issue comes from removing: 
# textvariable = self.user_IDVar
# 
# which shouldn't be needed at all because you can use the set function
# right below it to set the data... im not sure whats happening
# if you can figure it out I think it will put a really nice finishing touch on the project
# it will kinda look cool
#
# that line needs to be removed from the Entry paramer for some reason because it like
# overrides the inert text with !entry1 for some reason. not sure what it does mean do or why tf
 
# i hope you and you team do well!