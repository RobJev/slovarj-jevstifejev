def read_fail(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def save_fail(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=read_fail(f)
    return mas
def tolkimine():
    pass

rus_list=read_fail("rus.txt")
eng_list=read_fail("eng.txt")
print(rus_list)
print(eng_list)


while True:
    ot=input("1-Перевод слов\n2-Добавить слово\n3-Исправить ошибку\n4-Проверка знаний\nВыбери цифру:")
    if ot=="1":
         tolkimine() 
    elif ot=="2":
         rus_sona=input("Введи слово на русском:")
         eng_sona=input("Write a word in english:")
         rus_list=save_fail("rus.txt",rus_sona)
         eng_list=save_fail("eng.txt",eng_sona)
         print(rus_list)
         print(eng_list)