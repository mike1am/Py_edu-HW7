from model import *
from ui import *


# Функция предназначена как для редактирования сущ., так ввода новых данных взамен пустых значений
# contInd - индекс в списке контактов phonebookData
def inputContact (contInd):
    contact = getContList([contInd])[0] 
    if contInd > 0: showContacts([contact]) # для ввода нового контакта: поля пустые и отображение не требуется
    FIELDS = {
        "name": "имя",
        "phone": "телефон",
    }
    
    for fieldKey, fieldDesc in FIELDS.items():
        promptExt = ": " if contact[fieldKey] == "" else ". Enter - оставить без изменения: "
        newVal = userInput(f"Введите {fieldDesc} контакта{promptExt}", \
                lambda uInp: (uInp != "" or contact[fieldKey] != "") and (fieldKey != "phone" or isPhone(uInp))) # если поле было пустое (новый контакт), то пустой ввод недопустим, также проверка, если тел. то корректный формат
        if newVal != "" and newVal != contact[fieldKey]: # если введено непустое значение (т.е. требуется изменение) и оно не равно прежнему
            if fieldKey == "name" and len(findContacts(newVal)) > 0: # если это поле имени (ключевое) и оно уже занято др. контактом
                userPrint("Такой контакт уже существует.")
                return
            contact[fieldKey] = newVal
    
    sortContacts()
    return

# Загрузка контактов при запуске программы
impList = readFile("phonebook.bd")
if len(impList) > 0:
    csvImp(impList)

while True:
    operNum = menu()
    
    match operNum:
        case 0: 
            writeFile(csvExp(findContacts("")), "phonebook.bd") # выгрузка контактов при выходе из программы
            break
        
        case 1: # добавление контакта
            addContact()
            inputContact(-1)

        case 2: # удаление контактов
            indList = findContacts(userInput("Введите имя контакта (Enter для всех): "))
            if bool(len(indList)):
                contList = getContList(indList)
                showContacts(contList)
                if userBinChoice("Вы действительно хотите удалить эти контакты?"):
                    delContacts(indList)
            else: userPrint("Нет подходящих контактов для удаления.")

        case 3: # редактирование контакта
            indList = findContacts(userInput("Введите имя контакта: "))
            if bool(len(indList)):
                inputContact(indList[0])
            else:
                userPrint("Контакт не найден.")

        case 4: # просмотр контактов
            indList = findContacts(userInput("Введите имя контакта (Enter для всех): "))
            if bool(len(indList)):
                showContacts(getContList(indList))
            else: userPrint("Контакты не найдены.")

        case 5: # экспорт контактов
            indList = findContacts(userInput("Введите имя контакта (Enter для всех): "))
            if bool(len(indList)):
                formatId = inputFormat()
                fileName = userInput("Введите имя файла для экспорта: ")
                if fileName[fileName.rfind(".")] != "." + formatId: fileName += "." + formatId # если не задано расширение, оно автоматически добавляется
                expList = EXP_FUNCS[formatId](indList)
                writeFile(expList, fileName)
            else: userPrint("Нет контактов для экспорта.")

        case 6: # импорт контактов
            fileName = userInput("Введите имя файла для импорта: ")
            impList = readFile(fileName)
            if len(impList) > 0:
                formatId = fileName[fileName.rfind(".") + 1:] # определение формата по расширению файла
                if formatId in [el[0] for el in IMP_FUNCS.items()]:
                    if bool(IMP_FUNCS[formatId](impList)):
                        userPrint("Некорректный формат импорта. Не все данные были загружены.")
                    else: sortContacts()
                else: userPrint("Неизвестный формат импорта.")
            else: userPrint("Не удалось загрузить данные из файла.")
