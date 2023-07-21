
def sumTuples(tup1,tup2):
    list_result=[]
    for i in range(len(tup1)):
        list_result.append(tup1[i]+tup2[i])

    tup_result=tuple(list_result)
    return tup_result

def exportJson(dictionary,file_name):
        with open(file_name, 'w') as file:
            file.write('{\n')
            for key, value in dictionary.items():
                file.write('  "' + key + '": ')
                if isinstance(value, str):
                    file.write('"' + value + '"')
                    file.write(',\n')
                elif isinstance(value, int):
                    file.write(str(value))
                    file.write(',\n')
                elif isinstance(value, list):
                    file.write('[')
                    for i in range(len(value)):
                        if i < len(value)-1:
                            file.write('"' + value[i] + '",')
                        else:
                            file.write('"' + value[i] + '"')
                    file.write(']\n')
            file.write('}')

def importJson(file_name):
        data = []

        with open(file_name, 'r') as file:
            json_string = file.read()
            print(json_string)

            json_string = json_string.strip()
            print(json_string)

            json_content = json_string[1:-1]
            print(json_content)

            key_value_pairs = json_content.split(',')


            lst=[]
            for item in key_value_pairs:
                lst.append(item.split(':'))

            print(lst)



        return data

def show_menu(menu):

    if menu == 1:
        tup_length = int(input('Enter length of tuples: '))
        lst1=input('Enter integers :').split()[:tup_length]
        if all(i.isdigit() for i in lst1):
            int_lst1=list(map(int,lst1))
            tup1=tuple(int_lst1)
            lst2 = input('Enter integers :').split()[:tup_length]
            if all(i.isdigit() for i in lst2):
                int_lst2 = list(map(int, lst2))
                tup2=tuple(int_lst2)
                print(sumTuples(tup1,tup2))


    elif menu == 2:
        dictionary = {'name': 'Ola', 'age': 25, 'city': 'Beirut', 'siblings': ['Mohammed', 'Aya']}
        file_name = 'output.json'
        exportJson(dictionary,file_name)
        with open(file_name, 'r') as file:
            json_data = file.read()
            print(json_data)




    elif menu == 3:
        file_name = 'output.json'
        result = importJson(file_name)
        print(result)



    elif menu == 4:
        exit()

    ques = int(input('would you like to choose again? (yes=1/no=2)'))
    if ques == 1:
        menu = int(input('''1. Sum Tuples
2. Export JSON
3. Import JSON
4. Exit
- - - - - - - - - - - - - - -
Enter a choice: '''))

        show_menu(menu)

menu = int(input('''1. Sum Tuples
2. Export JSON
3. Import JSON
4. Exit
- - - - - - - - - - - - - - -
Enter a choice: '''))

show_menu(menu)