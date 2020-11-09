import os
import sys
# import user

def file_open():
    file_name = open(file_name, 'r')
    return file_name.read_lines()
def name():
    """
    connects to the login and brings in user_name from login naem e.g KBintcli
    """
    # This needs to be completed with the user login name.
    user_name = input("Who are you? ")
    # if user_name.lower() == 'voldemort':
    #     print("We welcome you, our Dark Lord.")
    # else:
    #     print("Welcome " + user_name + "!")
    print("Welcome " + user_name + "!")
    return user_name
def patient_or_volenteer(user_name, command):
    """
    Determins if the patient is a volenteer. This should be in another function as both user_interface and volenteer_interface use it.
    """
    what_is_user = 'patient'
    user_input = input("Are you a user or volunteer? ")
    if user_input.lower() == "patient":
        # needs access to user_interface
        patient(user_name)
    elif user_input.lower() == 'volunteer':
        what_is_user = 'volenteer'
        user_help(user_name, command)
        # volenteer(user_name, command)
    else:
        print("Sorry I cant do that.")
        patient_or_volenteer(user_name, command)
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
        volenteer(user_name, command)
    elif user_input.lower() == 'cancel':
        command = 'cancel'
        volenteer(user_name, command)
    elif user_input.lower() == 'check':
        command = 'check'
        volenteer(user_name, command)
    elif user_input.lower() == 'create':
        command = 'create'
        volenteer(user_name, command)
    elif user_input.lower() == 'help':
        command = 'help'
        user_help(user_name, command)
    elif user_input.lower() == 'refresh':
        command = 'refresh'
        refresh(user_name, command)
    else:
        print("Sorry that is an invalid command.")
        validate(user_name, command)
def volunteer(user_name, command):
    """
    This directs a user to the function they want to use.
    """
    # as user_input is never returned it can be used as a variable again and again
    if command == 0:
        validate(user_name, command)
    if command == "create":
        create_slot(user_name, command)
    elif command == "check":
        check_bookings(user_name, command)
    elif command == "cancel":
        cancel_bookings(user_name, command)
    elif command == "book":
        print("Sorry you cant do that as a volunteer.")
        user.validate(user_name, command, user_type, command_list)
def create_slot(user_name, command):
    """
    As patient you can check what slots you have signed up for, as a volenteer you can check what slots you have created.
    """
    proceed = input("Would you like to create a new slot? (y/n) ")
    if proceed == 'y':
        print("The event will be called 'CODE CLINIC VOLUNTEERING'.")
        # These functions are to keep this curretn function from looking to messy.
        location = user_location()
        date = dates()
        time = timing()
        description = user_description()
        print("Thank you for creating a slot. Here are the details")
        print("Title: CODE CLINIC VOLUNTEERING")
        print("Volunteer :" + user_name)
        if location == 'CPT':
            print("Location: Cape Town main campus.")
        else:
            print("Location: Johanesburg campus 3.")
        print("Date: " + date)
        print("Time: " + time)
        print("Description: " + description + ".")
        validate(user_name, command)
    elif proceed == 'n':
        validate(user_name, command)
    else:
        print("Sorry that is invalid.")
        create_slot(user_name, command)
def user_location():
    """
    This helps with sorting out if the review is going to be from CPT OR JHB.
    """
    location = input("Are you from JHB or CPT? ")
    if location.upper() == 'CPT':
        return location.upper()
    elif location.upper == 'JHB':
        return location.upper()
    else:
        print("Sorry that is an invalid location.")
        user_locationing()
def dates():
    """
    This is the date the volunteer wahts to create a new slot.
    """
    # This needs to formualted properly and completed with a 30 day in advnace implmented.
    # The months with 31 days to see if the date is valid
    days_31 = ('JAN', 'MAR', 'MAY', 'JUL', 'AUG', 'OCT', 'DEC')
    # THe months with 30 days to see if the date is valid
    days_30 = ('APR', 'JUN', 'SEP', 'NOV')
    # Seperates feburaruy cause it has 28 days
    exception_days = ('FEB')
    date_str = " "
    date = input("What day are you wanting to create a slot? (e.g 27 DEC) You can only plan 30 days in advance. " )
    date = date.split(' ')
    if len(date) == 2:
        if date[1].upper() in days_31:
            if int(date[0]) <= 31 and int(date[0]) > 0:
                date_str = date_str.join(date)
                return date_str.upper()
            else:
                print("Please choose a valid day within the chosen month.")
        if date[1].upper() in days_30:
            if int(date[0]) <= 30 and int(date[0]) > 0:
                date_str = date_str.join(date)
                return date_str.upper()
            else:
                print("Please choose a valid day within the chosen month.")
        if date[1].upper() in exception_days:
            if int(date[0]) <= 28 and int(date[0]) > 0:
                date_str = date_str.join(date)
                return date_str.upper()
            else:
                print("Please choose a valid day in the chosen month.")
        else:
            print("Please choose an actual month.")
    else:
        print("Please formulate the date properly")
        dates()
def timing():
    """
    This will get the time the volunteer wants to create a slot for.
    """
    time = input("What time do you want to create you slot? (24H time) ")
    time_hour = ""
    time_min = ""
    time_str = " "
    end_time = ""
    end_min = ""
    end_hour = ""
    semi_colons = ':'
    time = time.split(':')
    if (60 > int(time[1]) >= 0) and (24 > int(time[0]) >= 0):
        end_min = int(time[1]) + 30
        if int(time[1]) > 60:
            end_min = int(time[1]) - 60
            end_hour = int(time[0]) + 1
        time_hour = time[0]
        time_min = time[1]
        time_str = time_hour + semi_colons + time_min
        end_time = end_hour + semi_colons + end_min
        return time_str, end_time
    else:
        print("Please choose a valid time.")
        timing()
def user_description():
    """
    This gives a descirption of the type of help the volunteer is willing to give.
    """
    description = input("Give a description of the help you are willing to give. ")
    return description
def cancel_bookings(user_name, command):
    """
    As either a patient or a volenteer you can cancel a slot you have booked or created.
    """
    deleting = input("You can only cancel an empty slot. Are you sure you wish to cancel a slot? (y/n) ")
    if deleting == 'y':
        deleted = input("You have confirmed you want to deleted a slot, what day slot do you want to delete? (if you decide not to delete a slot type 'back') e.g 12:12 2 Dec ")
        print("Thank you for submitting, you have canceled you booking on: " + deleted)
        validate(user_name, command)
    elif deleting =='n':
        print("You have chosen not to delete a slot.")
        validate(user_name, command)
    else:
        print("Sorry you must choose a valid input.")
        cancel_bookings(user_name, command)
def check_bookings(user_name, command):
    """
    As patient you can check what slots you have signed up for, as a volenteer you can check what slots you have created.
    """
    print("You have these slots booked: ")
    print("Here are your booked slots: ")
    print("Here are your empty slots: ")
    validate(user_name, command)
# def user_help(user_name, command):
#     """
#     This prints out all the available commands in the terminal
#     """
#     print("You can:")
#     print(" > Book - As a patient you can book a slot.")
#     print(" > Cancel - As either a patient or a volenteer you can cancel a slot you have booked or created")
#     print(" > Create - As a volenteer you can create a slot.")
#     print(" > Check - As patient you can check what slots you have signed up for, as a volenteer you can check what slots you have created")
#     print(" > Off - Turns of the Code Clinic")
#     validate(user_name, command)
# def start():
#     command_list = ['book', 'cancel', 'check', 'create', 'help', 'off', 'refresh']
#     command = 0
#     user_name = name()
#     patient_or_volenteer(user_name, command)
# if __name__ == "__main__":
#     start()