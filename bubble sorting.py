
#сортировка ПУЗЫРЬКОМ
'''def mas(mas):
    for i in range(len(mas)):
        mas[i]=int(mas[i])
    for i in range(len(mas)-1):
        for j in range(len(mas)-1-j):
            if mas[i]>mas[i+1]:
                mas[i],mas[i+1]=mas[i+1],mas[i]
    return mas
massiv=input("Введи числа в строку через запятую: ").split(",")
print(*mas(massiv))
'''



def mas(mas):
    for i in range(len(mas)):
        mas[i]=int(mas[i])
    for i in range(len(mas)-1):
        minn=mas[i]
        index=i
        for j in range(i+1,len(mas)):   
            if minn>mas[j]:
                minn=mas[j]
                index=j
        if index!=i:
            x=mas[i]
            mas[i]=mas[index]
            mas[index]=x
    return mas
massiv=input("Введи числа в строку через запятую: ").split(",")
print(*mas(massiv), end=" ")
