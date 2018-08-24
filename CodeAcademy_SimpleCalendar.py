# простенький календарь в консоли
from time import sleep, strftime

us_name = "Alex"
calendar = {}


def welcome():
    print ("Hello, dear %s" % us_name)
    print ("Calendar is launching")
    sleep(1)
    print ("Today is: " + strftime("%A, %B, %d, %Y"))
    print ("Current time is: " + strftime("%H:%M:%S"))
    sleep(1)
    print ("What would you like to do? ")


def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print ("Calendar is empty:(")
            else:
                print (calendar)
        elif user_choice == "U":
            date = input("What date? ")
            update = input("Enter the update: ")
            calendar[date] = update
            print ("Upd. successful")
            print (calendar)
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print ("Wrong date!")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper
                if try_again == "Y":
                    continue  # перезапустит текущий цикл элиф
                else:
                    start = False
            else:
                calendar[date] = event
                print ("Upd. successful")
                print (calendar)
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print ("Calendar is empty:(")
            else:
                event = input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print ("Event was successfully deleted")
                        print (calendar)
                    else:
                        print ("Incorrect event was specified.")
        elif user_choice == "X":
            start = False
        else:
            print ("Invalid command was entered")


start_calendar()