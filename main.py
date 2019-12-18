# Сделать словарем, с добавлением параметров к каждому сотруднику. +
# Отдел, должность, имя и отчество, год принятия на работу, оклад +
# Читать и Выводить в csv
# Сделать через ООП
mass = []
import webbrowser
# функция заведения нового сотрудника
def input_sotr (mass):
    key = True
    while key:
        sotr = []
        a = input('введите сотрудника или ввердите [0] для завершения ввода \n ')
        if (a == '0'):
            key = False
            break
        else:
            sotr.append(a)
            sotr.append(input('введите инициалы сотрудника \n '))
            sotr.append(input('введите отдел сотрудника \n '))
            sotr.append(input('введите должность сотрудника \n '))
            sotr.append(input('введите год принятия на работу сотрудника \n '))
            sotr.append(input('введите оклад сотрудника \n '))
            mass.append(sotr)

# функция удаления сотрудника
def remove_sotr (fam, mass):
    for i in mass:
        if (i[0]==fam):
            mass.remove(i)

input_sotr(mass)
print (mass)

# Выводим меню
key=True
while key:
    a= input('Что вы хотите сделать со списком?\n '
             '[1] - Вывести список\n '
             '[2] - Отсортировать по возрастанию\n '
             '[3] - Отсортировать по убыванию\n '
             '[4] - Добавить сотрудника\n '
             '[5] - Удалить сотрудника\n '
             '[6] - Записать в файл\n '
              '[7] - Вывести в html\n '
             '[0] - завершить программу\n')

# Обрабатываем ввод
    if (a=='1'):
        for i in mass:
            for j in i:
                print (j)
            print('\n')

    elif (a=='2'):
        mass.sort()

    elif (a=='3'):
        mass.sort(reverse=True)

    elif (a=='4'):
        input_sotr(mass)

    elif (a=='5'):
        remove_sotr (input('Введите имя сотрудинка:\n'), mass)

    elif (a == '6'):
        fname = input('Введите имя файла [по умолчанию default.txt`]')
        if (fname == ''):
            fname = 'default'
        f = open(fname + '.txt', 'w')
        for m in mass:
            for n in m:
                f.write(n+'\n')
            f.write('\n')

    elif (a=='7'):
        h = 1
        httxt = '''
<!DOCTYPE html>
<html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf8">
    <title>Сотрудники</title>
    </head>
    <body>
    <div align=center>
      <h2>Список сотрудников</h2>
      <br>
    <table border="1" cellpadding="7">
        <tr>
            <td><b>Номер</b></td>
            <td><b>Фамилия</b></td>
            <td><b>Инициалы</b></td>
            <td><b>Отдел</b></td>
            <td><b>Должность</b></td>
            <td><b>Год</b></td>
            <td><b>Оклад</b></td>
        </tr>
      '''
        for i in mass:
            httxt = httxt+'\n <tr> \n <td>' + str(h) + '</td>'
            h = h + 1
            for j in i:
                httxt = httxt + '\n <td>'+ j + '</td>'
            httxt = httxt + '\n </tr> \n'

        httxt = httxt+'''
                </table>
                </div>
                </body>
            
            </html>
        '''
        fname = input('Введите имя файла [по умолчанию default.html`]')
        if (fname == ''):
            fname = 'default'
        f = open(fname + '.html', 'w')
        f.write(httxt)
        f.close()
        webbrowser.open_new('file://'+'/Users/sergejgulin/PycharmProjects/firstproj/'+fname+'.html')
        break

    elif (a=='0'):
        key = False
        break




