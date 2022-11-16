from model import *
from ui import *


while True:
    operNum = menu()
    
    match operNum:
        case 0: break
        
        case 1: # добавление контакта
            name = userInput("Введите имя контакта: ", lambda uInput: uInput != "")
            if not bool(len(findContacts(name, strong=True))):
                phone = userInput("Введите телефон контакта: ", lambda uInput: isPhone(uInput))
                addContact(name, phone)
            else: userPrint("Такой контакт уже существует.")

        case 2: # удаление контактов
            indList = findContacts(userInput("Введите имя контакта (Enter для всех): "))
            if bool(len(indList)):
                contList = getContList(indList)
                showContacts(contList)
                if userBinChoice("Вы действительно хотите удалить эти контакты?"):
                    delContacts(contList)
            else: userPrint("Нет подходящих контактов для удаления.")
                
        case 3: # редактирование контакта
            userPrint("==ed==")

        case 4: # просмотр контактов
            indList = findContacts(userInput("Введите имя контакта (Enter для всех): "))
            if bool(len(indList)):
                contList = getContList(indList)
                showContacts(contList)
            else: userPrint("Контакты не найдены.")

        case 5: # экспорт контактов
            formatId = inputFormat()
            contList = findContacts(userInput("Введите имя контакта (Enter для всех): "))
            if bool(len(contList)):
                fileName = userInput("Введите имя файла для экспорта: ")
                if fileName[-4:] != "." + formatId: fileName += "." + formatId
                expList = EXP_FUNCS[formatId](contList)
                writeFile(expList, fileName)
            else: userPrint("Нет контактов для экспорта.")

        case 6: # импорт контактов
            fileName = userInput("Введите имя файла для импорта: ")
            impList = readFile(fileName)
            if len(impList) > 0:
                formatId = fileName[-3:]
                if formatId in [el[0] for el in IMP_FUNCS.items()]:
                    if bool(IMP_FUNCS[formatId](impList)):
                        userPrint("Некорректный формат импорта. Не все данные были загружены.")
                else: userPrint("Неизвестный формат импорта.")
            else: userPrint("Не удалось загрузить данные из файла.")


