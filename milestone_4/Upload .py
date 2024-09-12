from typing import List, Tuple
#функція find_sum приймає два аргумени:
#    target з типом int ( target : int)
#    li з типом список int (li : List[int])
# і повертає значення кортеж з двох int (-> Tuple[int, int])
def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    # йдемо від 1го елементу списку "li" до кінця, індекс заносимо в змінну "i"
    for i in range(1, len(li)):
        # йдемо від 0го елементу списку "li" до "i" не включно з "i", індекс заносимо в змінну "j"
        for j in range(0, i):
            # якщо елементи дають в сумі "target" вовертаємо їх
            if li[i] + li[j] == target:
                return sorted([i, j])

# O(n^2)
myList = input()
myList = myList.split()
myList = [int(x) for x in myList]
target = input()
target = int(target)
print("1",find_sum(target, myList))

#функція find_sum приймає два аргумени:
#    target з типом int ( target : int)
#    li з типом список int (li : List[int])
# і повертає значення кортеж з двох int (-> Tuple[int, int])
def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    # сортуємо список "li" і записуємо відсортований список в зміну "sort_li"
    # O(n log n )
    sort_li = sorted(li)
    # ідемо здвох сторін по відсортованому списку, якщо сума елементів більша
    # за "target" зменшуємо праву межу "j" щоб зменшить суму sort_li[i] + sort_li[j]
    # якщо ж сума менше за задане число таргет, треба збільшить ліву межу щоб сума
    # збільшилась , так як sort_li відсортований
    i = 0
    j = len(sort_li)-1
    # O(n)
    while sort_li[i] + sort_li[j] != target:
        if sort_li[i] + sort_li[j] > target:
            j = j-1
        else:
            i = i+1
    result = []

    # шукаємо індекси знайдених нами елементів в початковому списку і повертаємо їх 
    # шукаємо елементи з протележних сторін списку "li" щоб уникнути ситуаціє,
    # якщо елементи які шукаємо рівні щоб не повертався той самий індекс  
    # O(n)
    for k1 in range(0, len(li)):
        if li[k1] == sort_li[i]:
            result.append(k1)
            break
    # O(n)
    for k2 in range(len(li)-1, -1, -1):
        if li[k2] == sort_li[j]:
            result.append(k2)
            break
    return sorted(result) 
print("2",find_sum_fast(target, myList))

#O(n log n)+ O(n) + O(n) + O(n)
