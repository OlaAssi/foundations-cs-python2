def countDigits(n):
    if n == 0:
        return 0
    else:
        return 1 + countDigits(abs(n) // 10)


def findMax(lst):
    if len(lst) == 0 :
        return 0
    else :
        max_value = lst[0]
        max2 = findMax(lst[1:])
        if max2>max_value:
            max_value= max2
    return max_value


def countTags(html,tag):
    if tag not in html :
        return 0
    else:
        return 1 + countTags(html.replace(tag,'',1),tag)


def show_menu(menu):

    if menu == 1:
        n=input('Enter integer :')
        if n.lstrip('-').isdigit():
            n=int(n)
            print(countDigits(n))


    elif menu == 2:
        length_list = int(input('Enter number of elements in list: '))
        lst=[]
        for i in range(length_list):
            n=input('Enter number: ')
            if n.lstrip('-').isdigit():
                n=int(n)
                lst.append(n)
        print(findMax(lst))


    elif menu == 3:
        html = ''' <html>
        <head>
        <title>My Website</title>
        </head>
        <body>
        <h1>Welcome to my website!</h1>
        <p>Here you'll find information about me and my hobbies.</p>
        <h2>Hobbies</h2>
        <ul>
        <li>Playing guitar</li>
        <li>Reading books</li>
        <li>Traveling</li>
        <li>Writing cool h1 tags</li>
        </ul>
        </body>
        </html> '''

        initial = input('Enter tag: ')
        tag = '<' + initial +'>'
        print(countTags(html,tag))


    elif menu == 4:
        exit()

    ques = int(input('would you like to choose again? (yes=1/no=2)'))
    if ques == 1:
        menu = int(input('''1. Count Digits
2. Find Max
3. Count Tags
4. Exit
- - - - - - - - - - - - - - -
Enter a choice: '''))

        show_menu(menu)

menu = int(input('''1. Count Digits
2. Find Max
3. Count Tags
4. Exit
- - - - - - - - - - - - - - -
Enter a choice: '''))

show_menu(menu)