from pickle import *
list_in =[]
find_word="19"
paste_word="20"
#  Поиск и замена слов в содержимом текстового файла
with open("qwest_1.txt", mode="r+",encoding="utf8") as f1:
    list_in=f1.readlines() 
    # writer=f1.writelines() 
    # find_word=input( "Enter word for f&z ")
    # print(list1,len(list1),paste_word)
    for el in list_in:
        list_out.apppend[list_in[el].split(" ")]
        [el]= 
        print(list1,len(list1))
        print
    #     if list1[el]==find_word:
    #         # f1.write.paste_word
    #         print(list1[el],paste_word)

#    Подсчет количества слов в содержимом текстового файла, которые не являются числами
def find_list_int(list_int):
    find_el=int(input("Введите число для поиска в списке "))
    for el in range(0,len(list_int)):
        if int(list_int[el])==find_el:
            print("Число ",find_el,"найдено в списке и имеет индекс ",el)
    return 
find_list_int(list_int)
#    Вывести слова содержимого файла  в обратном порядке
def revers(list_int):
    i=(len(list_int)/2)
    for el in range(0,int(i)):
        list_int[el],list_int[int(len(list_int)-el-1)]=list_int[int(len(list_int)-el-1)],list_int[el]
    print("Перевернутый список: ",list_int)
revers(list_int)

#    Удаление заданной  по номеру строки из файла
