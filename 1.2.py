#2. Сформувати функцію для обчислення цифрового кореню натурального числа.
#Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
#числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
#сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
#числа.
#Курдупов Олексій 122Г
import timeit#імпорт таймера
def Summa(z):#рекурсивне рішення.
    if z<10:
        return z
    else:
        return z%10+Summa(z//10)
def Digital_sqrt(z):
    if z<10:
        return z
    else:
        return Digital_sqrt(Summa(z))
y=int(input('введіть число, корінь якого потрібно знайти: '))# введеня даних
print("Рекурсивний розв'язок:")
print(Digital_sqrt(y))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)# таймер
print("Час виконання рекурсивного розв'язку: ", t)
def digit_sqrt(z):#ітераційне рішення.
    digit=0#щотчик
    count=0#ЩОТЧИК
    for i in range(len(z)):
        digit+=int(z[i-1])
    if int(digit)>9:
        digit=str(digit)
        for j in range(len(digit)):
            count+=int(digit[j-1])
        return count
    else:
        return digit
x=input('Введіть число, цифровий корінь якого потрібно знайти: ')# введеня даних
print("Ітераційний розв'язок:")
print(digit_sqrt(x))
t1= timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)# таймер
print("Час виконання ітераційного розв'язку: ", t1)

