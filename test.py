# Read the text file line by line then using lstrip() we removed the spaces that were present at the beginning
# of the elements in the list. then used strip() to remove the empty spaces (\n) and i used split(',') to turn
# the elements that are separated by commas into a list.

dictionary = {}
lst = []
with open('tickets.txt') as file:
    for item in file:
        new_item = [i.lstrip() for i in item.strip().split(',')]
        lst.append(new_item)
# convert the list into a dictionary
for ticket in lst:
    dictionary[ticket[0]] = ticket[1:]
# the last ticket id is for the incrementation when booking a ticket
last_ticket_id = lst[-1:][0][0]


# function ticketId takes the last ticket id found in the file and increments it by 1
def ticketId(last_ticket_id):
    # I used slicing in order to extract the numbers from the ticket id (ex: tick114 becomes 114)
    ticket_num = int(last_ticket_id[4:])
    new_ticket_num = ticket_num + 1
    # added back 'tick' to the id number
    new_ticket = 'tick' + str(new_ticket_num)
    return new_ticket


# This function below is for sorting the tickets according to the priorities in descending order
# I used merge sort algorithm to sort the dictionary in the optimal time complexity for sorting o(nlogn)
def mergeSortPriority(lstofdict):
    # this is the base case so that when we recursively split the list we have in half
    # we stop when we no longer can split in half, this happens when the length becomes 1
    if len(lstofdict) > 1:
        mid = len(lstofdict) // 2
        left = lstofdict[:mid]
        right = lstofdict[mid:]
        # recursive call for the function of the smaller lists we are creating
        mergeSortPriority(left)
        mergeSortPriority(right)
        # i is the index for the left list
        # j is the index for the right list
        # k is the index of the main list
        i = 0
        j = 0
        k = 0
        # the while loop here is used to stop comparing when one of the lists
        # left or right no longer has elements to compare
        while i < len(left) and j < len(right):
            # i used int inorder to be able to compare since originally these values are strings
            # [i][1][3] refers to the priority in the ticket
            # if the priority in the left list is larger or equal to the right list we append the ticket which is
            # left[i] to the main list, if its smaller we append the right list instead
            if int(left[i][1][3]) >= int(right[j][1][3]):
                lstofdict[k] = left[i]
                i += 1
            else:
                lstofdict[k] = right[j]
                j += 1
            k += 1
        # this while loop ensures that when one of the lists ends in the previous loop and the loop exists,
        # the remaining elements in either the left or right will also be added to the main list
        while i < len(left):
            lstofdict[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lstofdict[k] = right[j]
            j += 1
            k += 1
        # I convert the resulting list into a dictionary and return it
        new_dictionary = dict(lstofdict)
        return new_dictionary


# This function below is for sorting the tickets according to the dates first then the id in ascending order
# I used merge sort algorithm to sort the dictionary in the optimal time complexity for sorting o(nlogn)
def mergeSortDateId(lst_dict):
    # this is the base case so that when we recursively split the list we have in half
    # we stop when we no longer can split in half, this happens when the length becomes 1
    if len(lst_dict) > 1:
        mid = len(lst_dict) // 2
        left = lst_dict[:mid]
        right = lst_dict[mid:]
        # recursive call for the function of the smaller lists we are creating
        mergeSortDateId(left)
        mergeSortDateId(right)

        # i is the index for the left list
        # j is the index for the right list
        # k is the index of the main list
        i = 0
        j = 0
        k = 0
        # the while loop here is used to stop comparing when one of the lists
        # left or right no longer has elements to compare
        while i < len(left) and j < len(right):
            # I used int inorder to be able to compare since originally these values are strings.
            # 2 conditions apply, first if left[i][1][2] which is the date is smaller than that of the right list
            # then the left ticket is appended first. and in the case of when the dates are equal in the left and
            # right lists and the left[i][1][0][2:] which is the id(sliced inorder to compare numbers) is smaller than
            # that of the right, then the left ticket will also be appended first.
            # if the date on the right ticket was smaller than that of the left, the right will be appended first.
            if int(left[i][1][2]) < int(right[j][1][2]) or (
                    int(left[i][1][2]) == int(right[j][1][2]) and int(left[i][1][0][2:]) < int(right[j][1][0][2:])):
                lst_dict[k] = left[i]
                i += 1
            else:
                lst_dict[k] = right[j]
                j += 1
            k += 1
        # this while loop ensures that when one of the lists ends in the previous loop and the loop exists,
        # the remaining elements in either the left or right will also be added to the main list
        while i < len(left):
            lst_dict[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_dict[k] = right[j]
            j += 1
            k += 1
    # I convert the resulting list into a dictionary and return it
    new_dictionary = dict(lst_dict)
    return new_dictionary


# after the username and password are entered correctly if the user was an admin I use this function to prompt
# the admin to choose from the admin menu
def displayAdminOption():
    # check if user input is a valid choice and call each function accordingly
    # if not, prompt the user to choose again until a valid choice is entered
    # I call the function recursively so that the user can choose continuously until he or she exists the program
    option = input('Enter choice: ')
    if option == '1':
        displayStatistics()
        displayAdminOption()

    elif option == '2':
        bookTicket()
        displayAdminOption()

    elif option == '3':
        displayTickets()
        displayAdminOption()

    elif option == '4':
        changePriority()
        displayAdminOption()

    elif option == '5':
        disableTicket()
        displayAdminOption()

    elif option == '6':
        runEvents()
        displayAdminOption()

    elif option == '7':
        exit()

    else:
        print('Invalid option')
        displayAdminOption()


# after the username and password are entered correctly if the user was not an admin I use this function to prompt
# the user to choose from the user menu
def displayUserOption():
    # check if user input is a valid choice and call the function accordingly
    # if not, prompt the user to choose again until a valid choice is entered
    # I call the function recursively so that the user can book again until he or she exists the program
    option = input('Enter choice: ')
    if option == '1':
        bookTicketUser()
        displayUserOption()
    elif option == '2':
        exit()

    else:
        print('Invalid option')
        displayUserOption()


# This is the main function that ties the program together. In this function I let the user enter the username
# and password and check whether they are valid
def displayMenu():
    print('hello, please enter username and password.')
    i = 0
    # this while loop lets the user try to log in 5 times.
    while i < 5:
        # the username here is set as global because I will need to access the content of this variable when a user
        # wants to book a ticket without asking for his or her input again.
        global username
        username = input('Username: ')
        password = input('Password: ')
        # If the username and password are entered correctly, the admin menu is displayed and the displayAdminOption()
        # is called and the loop breaks.
        if username == 'admin' and password == 'admin123123':
            admin_menu = '''1. Display Statistics
2. Book a Ticket
3. Display all Tickets
4. Change Ticket’s Priority
5. Disable Ticket
6. Run Events
7. Exit '''
            print(admin_menu)
            displayAdminOption()
            break
        # If the username and password are entered correctly, the user menu is displayed and the displayUserOption()
        # is called and the loop breaks.
        elif username != 'admin' and password == '':
            print('''1. Book a ticket
2. Exit''')
            displayUserOption()
            break
        # if username and password aren't correct a message will appear stating that the input was
        # incorrect and the user will have 5 attempts.
        else:
            i += 1
            print('Incorrect Username and/or Password')


# In this function, I showed the event ID with the highest number of tickets
def displayStatistics():
    # I created a list of all the event IDs in the tickets
    lst2 = []
    for i in dictionary:
        lst2.append(dictionary[i][0])
    # I set count to zero and iterated over the elements of lst2, using the count operator I compared the count
    # to the count variable and everytime I found a greater count I would set the count variable equal to the count of
    # the element in the list. And I set that greatest count i found to variable element.
    count = 0
    element = ''
    for i in lst2:
        if lst2.count(i) > count:
            count = lst2.count(i)
            element = i

    print(element)


# when the admin or user want to book a ticket they are asked to enter a date for the event
# this function turns the input into a valid date format before it is added to the ticket
def eventDate():
    # inorder to book a ticket to an event, the date of the event cannot be in the past.
    # using datetime we are able to access the date from the computer inorder to compare the date entered by the user
    # to the date of when the user is booking the ticket
    from datetime import datetime
    print('Date of event:')
    year = input('Enter year of event: ')
    # I used isnumeric() before using int() to make sure the input are numbers
    if year.isnumeric():
        year = int(year)
        # if the year entered is in the past then a message will appear and the function is called again
        # to start over
        if year < datetime.now().year:
            print('invalid year')
            eventDate()
    # The same concept is applied for the month, but we check if the year entered earlier is equal to the current year
    # then we check if the month has already passed
    month = input('Enter month in (M): ')
    if month.isnumeric():
        month = int(month)
        # month has to be between 1 and 12
        if month in range(1, 13):
            if year == datetime.now().year and month < datetime.now().month:
                print('invalid month')
                eventDate()
        else:
            print('invalid month/format')
            eventDate()
    # the same concept is applied here the date is checked if it's in the past.
    # and according to the month entered by the user earlier we check if the date is greater than 30
    # for certain months or 31 for others
    # february is 28 days only
    day = input('Enter day in (D): ')
    if day.isnumeric():
        day = int(day)
        if year == datetime.now().year and month == datetime.now().month and day < datetime.now().day:
            print('invalid day')
            eventDate()
        if month in [4, 6, 9, 11] and day > 30:
            print('invalid day')
            eventDate()
        if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            print('invalid day')
            eventDate()
        if month == 2 and day > 28:
            print('invalid day')
            eventDate()
    # I concatenate the year and month and day after converting them to strings
    date_str = str(year) + str(month) + str(day)
    # using strptime I convert the date string to a date format YYYYMMDD
    date = datetime.strptime(date_str, "%Y%m%d")
    output_date = date.strftime("%Y%m%d")

    return output_date


# This function prompts the admin to enter details of ticket he or she wishes to book
def bookTicket():
    user_name = input('Enter username: ')
    event_id = input('Enter event id (ex:ev002): ')
    priority = input('Enter priority: ')
    # I call the eventdate() function to get the date from the user in the correct format
    date = eventDate()
    # Check that priority entered is an integer, if not then i recursively call the function
    if not priority.isnumeric() or priority == '':
        print('incorrect priority input')
        bookTicket()
    else:
        # once I have all the details I concatenate them into a variable ticket separating them using commas
        # I call ticketID and pass the last ticket id in the file to increment it by 1 everytime a ticket is booked
        ticket = ticketId(last_ticket_id) + ',' + event_id + ',' + user_name + ',' + date + ',' + priority
        # I open the file using 'a' to append to the end of the file
        f = open('tickets.txt', 'a')
        # I write the ticket to the file following with \n so that the next time i append to the file it
        # gets appended to the end
        f.write(ticket + '\n')
        f.close()
        print(ticket, 'is now booked')


# This function is called when a user wishes to book a ticket
def bookTicketUser():
    event_id = input('Enter event id (ex:ev002): ')
    # I call eventdate() function to get the proper date format from the user input
    date = eventDate()
    # I call ticketID and pass the last ticket id in the file to increment it by 1 everytime a ticket is booked
    # the username is taken from the global variable username entered by the user ad the beginning of the program
    ticket = ticketId(last_ticket_id) + ',' + event_id + ',' + username + ',' + date + ',' + '0'
    # I write the ticket to the file following with \n so that the next time i append to the file it
    # gets appended to the end
    f = open('tickets.txt', 'a')
    f.write(ticket + '\n')
    f.close()
    print(ticket, 'is now booked')


# This function is called when the admin asks the program to show all tickets registered in the system, ordered by
# event’s date and event ID
def displayTickets():
    # First using today's date like earlier explained, I created a new dictionary excluding the tickets that are no
    # longer valid (before today)
    from datetime import date
    today = date.today().strftime('%Y%m%d')
    new_dict = {}
    # If v[2] which is the element at index 2 of the values which is the date, is bigger than today or equal
    # the ticket is added to the new dictionary
    for k, v in dictionary.items():
        if v[2] >= today:
            new_dict[k] = v
    # The function mergeSortDateId() is called and since we cannot pass the dictionary into it
    # instead we convert it to list using the following method then we passed it into the function
    sorted_dic = mergeSortDateId(list(new_dict.items()))
    print(sorted_dic)


# This function is called when the admin chooses to change a ticket's priority
def changePriority():
    # I did this inorder to get the number then add the 'tick' to it myself to make sure it's in the correct format
    ticket_id = input('Enter ticket id number: ')
    if ticket_id.isnumeric():
        ticket_id = 'tick' + ticket_id
        priority = input('Enter new priority: ')
        # check if priority is a valid integer
        if priority.isnumeric():
            # check if the ticket specified by the admin actually exists
            if ticket_id in dictionary:
                # if it exists we assign the new priority to the index at which the previous priority existed
                dictionary[ticket_id][3] = priority
                print(dictionary[ticket_id])
            else:
                # if the ticket wasn't found a proper message is displayed and the function gets called recursively
                # for the admin to try another ticketid
                print('ticket id does not exist')
                changePriority()
        else:
            # if the priority entered is invalid then a message is displayed and the function gets called recursively
            print('invalid priority input')
            changePriority()


# This function is called when the admin chooses to disable a ticket
def disableTicket():
    # I did this inorder to get the number then add the 'tick' to it myself to make sure it's in the correct format
    ticket_id = input('Enter ticket Id number: ')
    if ticket_id.isnumeric():
        ticket_id = 'tick' + ticket_id
    # check if ticket id exists then delete it
    if ticket_id in dictionary:
        del dictionary[ticket_id]
        print('Ticket removed')
    else:
        # if id provided by admin doesn't exist the function gets called recursively
        print('ticket id does not exist')
        disableTicket()


# This function displays tickets for today's date ordered by priority
def runEvents():
    # I created a new dictionary and added to it the tickets that includes today's date only
    from datetime import date
    # today's date from computer
    today = date.today().strftime('%Y%m%d')
    dictionary2 = {}
    for k, v in dictionary.items():
        if today == v[2]:
            dictionary2[k] = v
    # If no tickets hold today's date then the dictionary will be empty thus ' no events today '
    if not dictionary2:
        print('No events today')
    else:
        # if it's not empty, then I call the function mergeSortPriority() and pass to it the dictionary I created
        # containing todays' tickets casted into a list using the following method
        print(mergeSortPriority(list(dictionary2.items())))


# some details were necessary for me to look up in order to complete my program
# here are the links to where I got the information I needed
# References:
# https://www.w3schools.com/python/ref_string_isnumeric.asp#:~:text=The%20isnumeric()%20method%20returns,%2C%20and%20the%20%2D%20and%20the%20.
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://discuss.codecademy.com/t/stripping-white-space-from-a-list-within-a-list/468944
# https://sparkbyexamples.com/python/count-occurrences-of-element-in-python-list/?expand_article=1
# https://www.geeksforgeeks.org/python-ways-to-remove-a-key-from-dictionary/
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://thispointer.com/python-check-if-a-value-exists-in-the-dictionary-3-ways/
# https://www.askpython.com/python/examples/obtain-current-year-and-month#:~:text=In%20Python%2C%20you%20can%20obtain,function%20to%20format%20the%20output.
# https://www.datacamp.com/tutorial/converting-strings-datetime-objects
# https://www.geeksforgeeks.org/python-append-to-a-file/
# https://stackoverflow.com/questions/4706499/how-do-i-append-to-a-file
# https://stackoverflow.com/questions/11941817/how-can-i-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
# https://www.tutorialspoint.com/How-to-convert-Python-Dictionary-to-a-list

# call the main function for the program to start
displayMenu()
