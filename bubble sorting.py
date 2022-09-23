mas=[9,6,5,4,1,2,10,7]
for j in range(len(mas)-1):
    for i in range(len(mas)-1-j):
        if mas[i]>mas[i+1]:
            mas[i],mas[i+1]=mas[i+1],mas[i]
    print(mas)



