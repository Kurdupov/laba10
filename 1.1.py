#1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
#натурального числа n.
#Курдупов Олексій 122Г
import timeit #імпорт таймера
def fact_iter(z):#ітераційне рішення.
    count=1
    for i in range(1, z+1):
        count*=i
    return count

def fac_rekur(x):#рекурсивне рішення.
    if x==0 or x==1:
        return 1
    else:
        return fac_rekur(x-1)*x
z=int(input('введіть число, для знаходження факторіалу: '))# введеня даних
print('Ітераційне рішення факторалу: ')
print(fact_iter(z))
t=timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)# таймер
print('Час виконання програми: ', t)

x=int(input('Введіть число, для знаходження факторіалу: '))#введеня даних
print('Рекурсивне рішення факторіалу: ')
print(fac_rekur(x))
t1=timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)# таймер
print('Час виконання програми : ', t1)

