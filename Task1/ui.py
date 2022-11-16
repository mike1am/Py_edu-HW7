from model import phonebookData


# chkFunc - функция, осуществляющая проверку ввода, если возвращает False - ввод некорректен
# возвращает введённую строку
def userInput (prompt, chkFunc=lambda _: True):
    while True:
        try:
            uInput = input(prompt)
            if not chkFunc(uInput): raise ValueError
        except ValueError:
            print("Некорректный ввод.")
        else:
            return uInput


def userPrint (outStr):
    print(outStr)


def menu ():
    MENU_ITEMS = {
        0: "Выход",
        1: "Добавить контакт",
        2: "Удалить контакты",
        3: "Редактировать контакт",
        4: "Просмотр контактов",
        5: "Экспортировать контакты",
        6: "Импортировать контакты",
    }

    print()    
    for operNum, operDesc in MENU_ITEMS.items(): 
        print(f"{operNum}. {operDesc}")

    return int(userInput("Введите требуемое действие: ", lambda uImp: 0 <= int(uImp) <= len(MENU_ITEMS)))


def showContacts (contList):
    for contInd in contList:
        print(f"\nИмя: {phonebookData[contInd]['name']}\nТелефон: {phonebookData[contInd]['phone']}")


def userBinChoice (prompt):
    uAnswer = userInput(prompt + " [Y/N] ", lambda uInput: len(uInput) == 1 and uInput in "YNynДНдн")
    return uAnswer in "YyДд"


def writeFile (expList, fName):
    try:
        with open(fName, "a") as file:
            for fileStr in expList:
                file.write(fileStr + "\n")
    except IOError:
        print("Ошибка записи в файл.")


def readFile (fName):
    readList = []
    try:
        with open(fName, "r") as file:
            for fileStr in file:
                readList.append(fileStr)
    except IOError:
        print("Ошибка чтения из файла.")
    finally:
        return readList


FORMATS = {
    "txt": "Текстовый (одно значение на строке)",
    "cvs": "Значения, разделённые запятыми",
    "json": "JavaScript Object Notation",
}

def inputFormat ():
    print()
    for id, desc in FORMATS.items(): 
        print(f"{id} - {desc}")

    return userInput("Введите идентификатор формата для экспорта: ", \
            lambda uImp: uImp in [el[0] for el in FORMATS.items()])
