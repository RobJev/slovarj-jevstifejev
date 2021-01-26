def read_fail(f): #читает txt файл
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def save_fail(f,text): #сохраняет изменения в txt файле
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=read_fail(f)
    return mas

def new_words(): #добавление новых слов
        rus_sona=input("Введи слово на русском:")
        eng_sona=input("Write a word in english:")
        rus_list=save_fail("rus.txt",rus_sona)
        eng_list=save_fail("eng.txt",eng_sona)
        print(rus_list)
        print(eng_list)
        return rus_list,eng_list

def mistake_cor(rus_list,eng_list):
        pass

def tolkimine(rus_list,eng_list): #перевод слов
    slovo=input("Введи слово для перевода:")
    if slovo in rus_list:
         ind=rus_list.index(slovo)
         print(f"{slovo}-{eng_list[ind]}")
    elif slovo in eng_list:
         ind=eng_list.index(slovo)
         print(f"{slovo}-{rus_list[ind]}")
    else:
         print(f"{slovo.upper()} отсутствует в словаре")
         v=input("Желаете добавить это слово в словарь?")
         if v.lower()=="да": new_words()
rus_list=read_fail("rus.txt")
eng_list=read_fail("eng.txt")
print(rus_list)
print(eng_list)


while True:
    ot=input("1-Перевод слов\n2-Добавить слово\n3-Исправить ошибку\n4-Проверка знаний\nВыбери цифру:")
    if ot=="1":
         tolkimine(rus_list,eng_list) 
    elif ot=="2":
         rus_list,eng_list=new_words()
    elif ot=="3":
         pass
         