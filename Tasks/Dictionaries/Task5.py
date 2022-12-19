list = []
list_files = []
number_of_files = int(input())
for i in range(number_of_files):
    paires = input()
    list.append(paires)
    list_files.append(paires.split(' ')[0])

number_of_operations = int(input())
for i in range(number_of_operations):
    operations, filename = input().split()
    operations = operations.upper()
    if operations == 'EXECUTE' or operations == 'WRITE' or operations == 'READ':
        operations = operations[0]
        flag = 0
        for data in list:
            if data.count(filename) and data.count(operations):
                flag = 1
        if flag == 1:
            print('OK')
        else:
            print('Denied')