import os
import sys
# def file_open():
#     file_name = open(file_name, 'r')
#     return file_name.read_lines()
def name():
    """
    connects to the login and brings in user_name from login name e.g KBintcli
    """
    # This needs to be completed with the user login name.
    user_name = input("What is your username? ")
    if user_name.lower() == 'voldermort':
        print("We welcome you, our Dark Lord.")
    else:
        print("Welcome " + user_name + "!")
    return user_name
def patient_or_volunteer(user_name, command):
    """
    Determins if the patient is a volunteer. This should be in another 
    function as both user_interface and volunteer_interface use it.
    """
    #what_is_user = 'volunteer'
    user_input = input("Are you a patient or volunteer? ")
    if user_input.lower() == "patient":     # needs access to user_interface
        user_help(user_name, command)       #patient(user_name) #what_is_user = 'patient'
    elif user_input.lower() == 'volunteer':
        user_help(user_name, command)
        # patient(user_name, command)
    else:
        print("Sorry I cant do that.")
        patient_or_volunteer(user_name, command)
def validate(user_name, command):
    """
    Checks if the command is valid.
    """
    user_input = input("What would you like to do? ")
    command = 0
    if user_input.lower() == 'off':
        print("This session has ended...")
        return False
    elif user_input.lower() == 'book':
        # only with the user interface
        command = 'book'
        patient(user_name, command)
    elif user_input.lower() == 'cancel':
        command = 'cancel'
        patient(user_name, command)
    elif user_input.lower() == 'check':
        command = 'check'
        patient(user_name, command)
    elif user_input.lower() == 'help':
        command = 'help'
        user_help(user_name, command)
    elif user_input.lower() == 'submit':
        command = 'submit'
        patient(user_name, command)
    else:
        print("Sorry that is an invalid command.")
        validate(user_name, command)
def patient(user_name, command):
    """
    This allows for the function to be used depending on the command.
    """
    if command == 0:
        validate(user_name, command)
    if command == "book":
        create_booking(user_name, command)
    elif command == "check":
        check_bookings(user_name, command)
    elif command == "cancel":
        cancel_bookings(user_name, command)
    elif command == "submit":
        submit_booking(user_name, command)
    # elif command == "book":
    #     print("Sorry you cant do that as a volunteer.")
        validate(user_name, command)
def create_booking(user_name, command):
    """
    This function allows the patient to book a slot
    """
    proceed = input("Would you like to book a new slot? (y/n) ")
    if proceed == 'y':
        print("The event will be called 'CODE CLINIC PATIENT'.")
        location = user_location(user_name, command)                                  #stores user location
        date = dates()                                              #stores the date the user has chosed
        time = timing()                                             #stores the time the user has set
        description = user_description()                            #stores the user description
        print("Thank you for booking a slot. Here are the details")
        print("Title: CODE CLINIC PATIENT")
        if location == 'CPT':
            print("Location: Cape Town main campus.")
        else:
            print("Location: Johanesburg campus 3 is not allowed.")
        print("Date: " + date)
        print("Time: " + time)
        print("Description: " + description + ".")
        validate(user_name, command)
    elif proceed == 'n':
        validate(user_name, command)
    else:
        print("Sorry that is invalid.")
        create_booking(user_name, command)
def user_location(user_name, command):
    """
    This function checks whether the user is from cpt or jhb.
    if user = jhb the program exits 
    """
    location = input("Are you from JHB or CPT? ")
    if location.upper() == 'CPT':
        return location.upper()
    elif location.upper == 'JHB':
        print("The session will end now. Bye.")
        exit()
    else:
        print("That is an invalid location. Please try again.")
        validate(user_name, command)
def dates():
    """
    This function creates the date for when the user wants to book a slot
    """
    days_31 = ('JAN', 'MAR', 'MAY', 'JUL', 'AUG', 'OCT', 'DEC') #months which have 31 days
    days_30 = ('APR', 'JUN', 'SEP', 'NOV')                      #months with 30 days 
    exception_days = ('FEB')                                    #month with 28 days
    date_str = " "                                               
    date = input("What day do you want to book a slot?" 
" [(e.g 27 DEC) You can only plan 30 days in advance.] : " )
    date = date.split(' ')
    if len(date) == 2:
        if date[1].upper() in days_31:
            if int(date[0]) <= 31 and int(date[0]) > 0:
                date_str = date_str.join(date)
                return date_str.upper()
            else:
                print("Please choose a valid day within the given month.")
        if date[1].upper() in days_30:
            if int(date[0]) <= 30 and int(date[0]) > 0:
                date_str = date_str.join(date)
                return date_str.upper()
            else:
                print("Please choose a valid day within the given month.")
        if date[1].upper() in exception_days:
            if int(date[0]) <= 28 and int(date[0]) > 0:
                date_str = date_str.join(date)
                return date_str.upper()
            else:
                print("Please choose a valid day in the given month.")
        else:
            print("Please choose a valid month.")
    else: 
        print("Please formulate the date properly.")
        dates()
def timing():
    """
    This function sets a time for when the user wants to book a slot.
    """
    time = input("""These are the times available to book a slot on this day:"
 09:30 
 12:00 
 16:00 
 What time do you want to book a slot? (24H time): """)
    time_hour = ''
    time_min = ""
    time_str = " "
    semi_colons = ':'
    time = time.split(':')
    if int(time[1]) >= 0 and (24 >= int(time[0]) > 0):
        if int(time[1]) > 60:
            time_min = int(time[1]) - 60
            time_hour = int(time[0]) + 1
            time_str = time_hour + semi_colons + time_min
            return time_str
        else:
            time_hour = time[0]
            time_min = time[1] 
            time_str = time_hour + semi_colons + time_min
            return time_str
    else:
        print("Please choose a valid time.")
        timing()  
def user_description():
    """
    This function asks the user what help they need to receive.
    """
    description = input("Please give a description of the help you need: ")
    return description
def cancel_bookings(user_name, command):
    """
    Enables the patient to cancel a booking they've created.
    """
    ask_user = input("Are you sure you want to cancel the booking? (y/n): ")
    if ask_user == "y":
        print("Your booking has been canceled.")
    else:
        ask_user == "n"
        print("You have been redirected.")
    validate(user_name, command)
def submit_booking(user_name, command):
    """
    At this point this funtion just prints out request submitted
    """
    prompt_user = input("Are you sure you want to submit this request? (y/n): ")
    if prompt_user == "y":
        print("Your request has been submitted. Please keep an eye on your email.")
    else:
        prompt_user == "n"
        print("You have been redirected.")
    validate(user_name, command)
def check_bookings(user_name, command):
    """
    A patient can check which slots they've booked
    """
    print("checking the bookings you have made..")
    print("loading..  ")
    print("This is a list of bookings you've made so far:")
    print("You dont have any bookings saved yet. This is just a trial.")
    validate(user_name, command)
def user_help(user_name, command):
    """
    This function prints out all the available commands in the terminal
    """
    print("These are a list of your valid commands:")
    print(" > Book - As a patient you can book a slot.")
    print(" > Cancel - As a patient you can cancel a slot you have booked.")
    print(" > Check - As patient you can check what slots you have signed up for.")
    print(" > Submit - allows you to submit the request you've made.")
    print(" > Off - Ends the Code Clinic session")
    validate(user_name, command)
def start():
    #command_list = ['book', 'cancel', 'check', 'create', 'help', 'off', 'submit']
    command = 0
    user_name = name()
    patient_or_volunteer(user_name, command)
if __name__ == "__main__":
    start()