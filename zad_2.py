# ИЗВИНЯЮСЬ ЗА НАЗВАНИЯ ПЕРЕМЕННЫХ, ДЕЛАЛ ЭТУ ЗАДАЧУ ПОСЛЕДНЕЙ. РЕШМЛ НЕ С ПЕРВОГО РАЗА, ПОЭТОМУ ИСПОЛЬЗОВАЛ ЧТО ПЕРВОЕ НА ЯЗЫК ПОПАДЁТ

# ТУТ РЕШИЛ СДЕЛАТЬ ОГРАНИЧЕНИЕ НА МИНИМАЛЬНОЕ ЧИСЛО(ВДРУГ ВСЕ ЧИЛО БУДУТ НА НЕГО ДЕЛИТЬСЯ - 12,36,48), ПОСТАВИЛ ЕГО ВЕРХНЕЙ ГРАНИЦЕЙ И ИСКАЛ ЧИСЛА КОТОРЫЕ
# ДЕЛЯТСЯ НА НЕГО
def poisk(masik):
    mini = min(masik)
    spis =[] # ОСНОВНОЙ СПИСОК НАЙДЕННЫХ ДЕЛИТЕЛЕЙ
    spis_2 = [] # БУДУ ИСПОЛЬЗОВАТЬ ДЛЯ ФИЛЬТРАЦИИ ЗНАЧЕНИЙ КОТОРЫЕ НЕ ДЕЛЯТСЯ НА ДРУГ(-ОЕ/-ИЕ) ЗНАЧЕНИ(-Е/-Я)
    for i in range(1,mini+1):
        if mini % i == 0 and i not in spis:
            spis.append(i)
    for n in masik: # В ЭТОМ ЦИКЛЕ ИСКАЛ ЛИШНИЕ ЗНАЧЕНИЯ В ПЕРВОМ СПИСКЕ
        for el in spis:
            if n % el != 0 and el not in spis_2:
                spis_2.append(el)

    result = set(spis) - set(spis_2) #ЭТА ПЕРЕМЕННАЯ И ЕСТЬ РЕЗУЛЬТАТ ИСКОМЫХ ЗНАЧЕНИЙ
    return list(result)


print(poisk([14,28,46]))
print(poisk([34,85,112]))
print(poisk([50,78,94]))
print(poisk([19,57,148]))
print(poisk([21,48,96]))

