'''
Program: SportTrak Application
Date: April 12, 2022
Purpose: Estimate resources required for TCU sporting events
Installation Instructions: Install this file and the accompanying GWlogo.gif in the same folder 
'''

# Code Sections
# Window One: (Displays SportTrak title and TCU Athletics photo) User enters 8 digit User ID to move to next page *help button/next page button*
# Window Two: (Displays TCU Athletics photo) User picks from a drop down menu of 4 sports
# Window Three: (Displays TCU Athletics photo) User enters date, weather, opponent, expected student & non-student attendance *next page button*
# Window Four: (Displays TCU Athletics photo) Returns estimated quantities as well as confirming major inputs 


from tkinter import * # Import tkinter; do not need to install it

class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window instance
        window.title("SportTrak") # Set title of the window

        # Our GUI application has 7 inputs and 15 outputs plus a Compute Button, so we will need 9 rows and 2 columns
        photo = PhotoImage(file=r'GWlogo.gif') # change picture
        Label(window, image=photo).grid(row = 1, column = 1, sticky = W)  #put the image in a label to display it in the window
        
        # First, create labels in the window for each input value.
        Label(window, text = "User ID: ").grid(row = 2, column = 1, sticky = W) # if proper ID is not entered
        Label(window, text = "Select Sport: ").grid(row = 3, column = 1, sticky = W) # Drop down input selection
        Label(window, text = "Event Date: ").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Expected Weather").grid(row = 5, column = 1, sticky = W) # Drop down input selection
        Label(window, text = "Opponent: ").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Expected Student Attendence: ").grid(row = 7, column = 1, sticky = W)
        Label(window, text = "Expected Non-Student Attendence: ").grid(row = 8, column = 1, sticky = W)
        
        # Next, create labels in the window for each output value.
        Label(window, text = "Hot Dogs: ").grid(row = 2, column = 2, sticky = W)
        Label(window, text = "Nachos: ").grid(row = 3, column = 2, sticky = W)
        Label(window, text = "Pretzels: ").grid(row = 4, column = 2, sticky = W)
        Label(window, text = "Burgers: ").grid(row = 5, column = 2, sticky = W)
        Label(window, text = "Water: ").grid(row = 6, column = 2, sticky = W)
        Label(window, text = "Beer: ").grid(row = 7, column = 2, sticky = W)
        Label(window, text = "Soda: ").grid(row = 8, column = 2, sticky = W)
        Label(window, text = "Staffing: ").grid(row = 9, column = 2, sticky = W)

        #For each of the three inputs, create string variable and get their values through Entry control
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 2, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 3, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 4, column = 2)
        
        #For each of the two outputs, crete a String variable and output each to a Label in the Window
        self.monthlyPaymentVar = StringVar()
        Label(window, textvariable = self.monthlyPaymentVar).grid(row = 5, column = 2, sticky = E)
        self.totalPaymentVar = StringVar()
        Label(window, textvariable = self.totalPaymentVar).grid(row = 6, column = 2, sticky = E)
        
        #Create a Compute Payment button to call the computePayment function
        Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 7, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop
        
    def getMonthlyPayment(self,loanAmount, monthlyInterestRate, numberOfYears):
        #this function calculates a monthly payment based on the user data entered and returns the value of the monthly payment
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

    def computePayment(self):
        #this function calls getMonthlyPayment function with the input values entered into the textboxed (Entry controls) and assigned to corresponding variables, 
        # after converting them to numerical values; after the monthly payment is returned, it is assigned to a variable for output in the window and 
        #total payment is calculated and assigned to a variable to output in the window
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))


LoanCalculator()  # Create GUI 