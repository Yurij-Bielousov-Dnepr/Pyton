metrics=[]
def bubblesort(sorting_list: list,metrics):
    list_сopy=sorting_list.copy()
    for i in range(len(list_сopy)):
        for j in range(len(list_сopy)-1-i):
            metrics[0] += 1
            if list_сopy[j] > list_сopy[j+1]:
                list_сopy[j], list_сopy[j+1] = list_сopy[j+1], list_сopy[j]
                metrics[1]+= 1
    return list_сopy
def SortInsert(sorting_list, metrics, start = 1):
    sorting_list_tmp=sorting_list.copy()
    for i in range(start,len(sorting_list_tmp)):
        for j in range(i,0,-1):
            metrics[0] += 1
            if sorting_list_tmp[j] < sorting_list_tmp[j-1]:
                metrics[1]+= 1
                sorting_list_tmp[j], sorting_list_tmp[j-1] = sorting_list_tmp[j-1], sorting_list_tmp[j]
            else:
                break
        return sorting_list_tmp

def SortShell(sorting_list, metrics):
    sorting_list_tmp=sorting_list.copy()
    step = len(sorting_list_tmp) // 2
    while step > 0:
        for i in range(0,step):
            for j in range(i+step,len(sorting_list_tmp),step):
                for k in range(j,0,-step):
                    metrics[0] += 1
                    if sorting_list_tmp[j] < sorting_list_tmp[j-step]:
                        metrics[1]+= 1
                        sorting_list_tmp[j], sorting_list_tmp[j-step] = sorting_list_tmp[j-step], sorting_list_tmp[j]
                    else:
                        break
        step //= 2  
    return sorting_list_tmp

def SortMerge(sorting_list, metrics):
    sorting_list_tmp=sorting_list.copy()
    if len(sorting_list_tmp) > 1:
        metrics[0]+=1
        nn = len(sorting_list_tmp) // 2
        leftPart = sorting_list_tmp[:nn]
        rightPart = sorting_list_tmp[nn:]
        SortMerge(leftPart, metrics)
        SortMerge(rightPart, metrics)
        i = j = k = 0
        while i < len(leftPart) and j < len(rightPart):
            if leftPart[i] < rightPart[j]:
                sorting_list_tmp[k] = leftPart[i]
                i+=1
            else:
                sorting_list_tmp[k] = rightPart[j]
                j+=1
            metrics[1]+=1
            k+=1
        while i < len(leftPart):
            sorting_list_tmp[k] = leftPart[i]
            i+=1
            metrics[1]+=1
            k+=1
        while j < len(rightPart):
            sorting_list_tmp[k] = rightPart[j]
            j+=1
            metrics[1]+=1
            k+=1
    return sorting_list_tmp

# К пройденным методам добавить метрики кол-ва перестановок и циклов
# Применить эти методы к спискам из одинаковых элементов, но разной 
# последовательности (среднии, лучший и худший случай)
# По полученым метрикам сделать выводы о производительности методов 
# сортировки относительно друг друга.  

list_best = [-2,0,1,2,3,4,5]
list_bad = [5,4,3,2,1,0,-2]
list_normal =[-2,0,4,2,3,5,1] 
metrics=[]
metrics.append([0,0])
print("Сортировка Пузырьками, лучший случай")
print("Исходные данные       ",list_best)
print("Отсортированные данные",bubblesort(list_best,metrics[0]))
print("При сортировке сделано ",metrics[0][0],"проходов и замена сделана",metrics[0][1],"раз")

metrics.append([0,0])
print("Сортировка Пузырьками, худший случай")
print("Исходные данные       ",list_bad)
print("Отсортированные данные",bubblesort(list_bad,metrics[1]))
print("При сортировке сделано ",metrics[1][0],"проходов и замена сделана",metrics[1][1],"раз")

metrics.append([0,0])
print("Сортировка Пузырьками, средний случай")
print("Исходные данные       ",list_normal)
print("Отсортированные данные",bubblesort(list_normal, metrics[2]))
print("При сортировке сделано ",metrics[2][0],"проходов и замена сделана",metrics[2][1],"раз")

metrics.append([0,0])
print("Сортировка вставками, лучший случай")
print("Исходные данные       ",list_best)
print("Отсортированные данные",SortInsert(list_best, metrics[3]))
print("При сортировке сделано ",metrics[3][0],"проходов и замена сделана",metrics[3][1],"раз")

metrics.append([0,0])
print("Сортировка вставками, худший случай")
print("Исходные данные       ",list_bad)
print("Отсортированные данные",SortInsert(list_bad, metrics[4]))
print("При сортировке сделано ",metrics[4][0],"проходов и замена сделана",metrics[4][1],"раз")

metrics.append([0,0])
print("Сортировка вставками, средний случай")
print("Исходные данные       ",list_normal)
print("Отсортированные данные",SortInsert(list_normal, metrics[5]))
print("При сортировке сделано ",metrics[5][0],"проходов и замена сделана",metrics[5][1],"раз")

metrics.append([0,0])
print("Сортировка методом Шелла, лучший случай")
print("Исходные данные       ",list_best)
print("Отсортированные данные",SortShell(list_best, metrics[6]))
print("При сортировке сделано ",metrics[6][0],"проходов и замена сделана",metrics[6][1],"раз")

metrics.append([0,0])
print("Сортировка методом Шелла, худший случай")
print("Исходные данные       ",list_bad)
print("Отсортированные данные",SortShell(list_bad, metrics[7]))
print("При сортировке сделано ",metrics[7][0],"проходов и замена сделана",metrics[7][1],"раз")

metrics.append([0,0])
print("Сортировка методом Шелла, средний случай")
print("Исходные данные       ",list_normal)
print("Отсортированные данные",SortShell(list_normal, metrics[8]))
print("При сортировке сделано ",metrics[8][0],"проходов и замена сделана",metrics[8][1],"раз")

metrics.append([0,0])
print("Сортировка объединением, лучший случай")
print("Исходные данные       ",list_best)
print("Отсортированные данные",SortMerge(list_best, metrics[9]))
print("При сортировке сделано ",metrics[9][0],"проходов и замена сделана",metrics[9][1],"раз")

metrics.append([0,0])
print("Сортировка объединением, худший случай")
print("Исходные данные       ",list_bad)
print("Отсортированные данные",SortMerge(list_bad, metrics[10]))
print("При сортировке сделано ",metrics[10][0],"проходов и замена сделана",metrics[10][1],"раз")

metrics.append([0,0])
print("Сортировка объединением, средний случай")
print("Исходные данные       ",list_normal)
print("Отсортированные данные",SortMerge(list_normal, metrics[11]))
print("При сортировке сделано ",metrics[11][0],"проходов и замена сделана",metrics[11][1],"раз")

print("Список отсортирован как лучший ",list_best," среднии ",list_normal, " и худший случай ",list_bad)
print("Пузырьки лучший случай n=",metrics[0][0],"p=",metrics[0][1],"Bad n=",metrics[1][0],"p=",metrics[1][1],"средний случай n=",metrics[2][0],"p=",metrics[2][1])
print("Вставками лучший случай n=",metrics[3][0],"p=",metrics[3][1],"Bad n=",metrics[4][0],"p=",metrics[4][1],"средний случайn=",metrics[5][0],"p=",metrics[5][1])
print("Шелла лучший случай n=",metrics[6][0],"p=",metrics[6][1],"Bad n=",metrics[7][0],"p=",metrics[7][1],"средний случай n=",metrics[8][0],"p=",metrics[8][1])
print("Обьединением лучший случай n=",metrics[9][0],"p=",metrics[9][1],"Bad n=",metrics[10][0],"p=",metrics[10][1],"средний случай n=",metrics[11][0],"p=",metrics[11][1])
print("Проводим анализ данных:")
print("Чем меньше значение метрик Проходов и Замен, тем эффективнее метод сортировки.")
print("Изменение метрик при использовании метода, зависит от отсортированности исходного списка.")
print("Отсортируем метрики и найдем наиболее эффективный метод для каждого из списков:")
# import collections библиотека для сортировок
# from collections import Counter
dict_sort_n_best = dict(zip(["Пузырьки ","Вставками ","Шелла ","Обьединением "], [(metrics[0][0]), (metrics[3][0]),(metrics[6][0]), (metrics[9][0])]))
dict_sort_n_bad = dict(zip(["Пузырьки ","Вставками ","Шелла ","Обьединением "], [(metrics[1][0]), (metrics[4][0]),(metrics[7][0]), (metrics[10][0])]))
dict_sort_n_norm = dict(zip(["Пузырьки ","Вставками ","Шелла ","Обьединением "], [(metrics[2][0]), (metrics[5][0]),(metrics[8][0]), (metrics[11][0])]))
dict_sort_p_best = dict(zip(["Пузырьки ","Вставками ","Шелла ","Обьединением "], [(metrics[0][1]), (metrics[3][1]),(metrics[6][1]), (metrics[9][1])]))
dict_sort_p_bad = dict(zip(["Пузырьки ","Вставками ","Шелла ","Обьединением "], [(metrics[1][1]), (metrics[4][1]),(metrics[7][1]), (metrics[10][1])]))
dict_sort_p_norm = dict(zip(["Пузырьки ","Вставками ","Шелла ","Обьединением "], [(metrics[2][1]), (metrics[5][1]),(metrics[8][1]), (metrics[11][1])]))
sort_n_best = dict(sorted(dict_sort_n_best.items(), key=lambda x: x[1]))
sort_n_bad = dict(sorted(dict_sort_n_bad.items(), key=lambda x: x[1]))
sort_n_norm = dict(sorted(dict_sort_n_norm.items(), key=lambda x: x[1]))
sort_p_best = dict(sorted(dict_sort_p_best.items(), key=lambda x: x[1]))
sort_p_bad = dict(sorted(dict_sort_p_bad.items(), key=lambda x: x[1]))
sort_p_norm = dict(sorted(dict_sort_p_norm.items(), key=lambda x: x[1]))
# sort_p_norm = dict(sorted(dict_sort_p_norm.items(), key=lambda x: x[1], reverse=True)) для обращения сортировки 

print("По количеству Проходов, лучший случай ",sort_n_best)
print("По количеству Замен, лучший случай ",sort_p_best)
print("По количеству Проходов, худший случай ",sort_n_bad)
print("По количеству Замен, худший случай ",sort_p_bad)
print("По количеству Проходов, средний случай ",sort_n_norm)
print("По количеству Замен, средний случай ",sort_p_norm)
print("Эффективность метода зависит от длинны списка и его предварительной сортировки. ")