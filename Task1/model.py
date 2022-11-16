# Список словарей контактов. Каждый словарь содержит ключи, соответствующие полям контакта (name и phone) и соотв. значения
phonebookData = []

# Формирование списка строк для экспорта в текстовом формате
# cList - список индексов в phonebookData
def txtExp (cList):
    expList = []
    for cInd in cList:
        expList.append(phonebookData[cInd]["name"])
        expList.append(phonebookData[cInd]["phone"])
        expList.append("")
    
    return expList


def csvExp (cList):
    # ...
    return []


def jsonExp (cList):
    # ...
    return []


# Импорт из списка строк в текстовом формате: имена и тел. на отдельных строках, между контактами пустая строка
def txtImp (sList):
    # ...
    return


def csvImp (sList):
    # ...
    return


def jsonImp (sList):
    # ...
    return


EXP_FUNCS = {
    "txt": txtExp,
    "csv": csvExp,
    "json": jsonExp,
}


IMP_FUNCS = {
    "txt": txtImp,
    "csv": csvImp,
    "json": jsonImp,
}


# Определяет, является ли строка номером телефона
def isPhone(phoneStr):
    return not bool(len(list(filter(lambda ch: ch not in "+() 0123456789", phoneStr))))


# Формирует список индексов контактов в phonebookData, на основе строки, в которой должно содержаться имя или часть имени контакта
# strong - булевый флаг, True - ищет только полное соответствие в именах, False - вхождение
def findContacts (nameStr, strong=False):
    resList = []
    for ind, contact in enumerate(phonebookData):
        if not strong and nameStr in contact["name"] or strong and nameStr == contact["name"]:
            resList.append(ind)

    return resList


def addContact (cName, cPhone):
    global phonebookData
    phonebookData.append({"name": cName, "phone": cPhone})


def delContacts (cList):
    global phonebookData
    for i in range(len(cList)):
        phonebookData.pop(cList[i] - i)
