# Сделать словарем, с добавлением параметров к каждому сотруднику.
# Отдел, должность, имя и отчество, год принятия на работу, оклад
# Читать и Выводить в svc
# Сделать через ООП


key = True
mass = []
while key:
    a = input('введите сотрудника или ввердите [0] для завершения ввода \n ')
    if (a=='0'):
        key=False
        break
    else:
        mass.append(a)
print (mass)
key=True
while key:
    a= input('Что вы хотите сделать со списком?\n '
             '[1] - Вывести список\n '
             '[2] - Отсортировать по возрастанию\n '
             '[3] - Отсортировать по убыванию\n '
             '[4] - Добавить сотрудника\n '
             '[5] - Удалить сотрудника\n '
             '[6] - Записать в файл\n'
             '[0] - завершить программу\n')
    if (a=='1'):
        for i in mass:
            print (i)
    elif (a=='2'):
        mass.sort()
    elif (a=='3'):
        mass.sort(reverse=True)
    elif (a=='4'):
        mass.append(input('Введите имя сотрудника: \n'))
    elif (a=='5'):
        mass.remove(input('Введите имя сотрудинка:\n'))
    elif (a=='6'):
        fname=input('Введите имя файла [по умолчанию default.txt`]')
        if (fname == '' ):
            fname='default'
        f=open(fname+'.txt', 'w')
        for m in mass:
            f.write(m+'\n')
    elif (a=='0'):
        key = False
        break




