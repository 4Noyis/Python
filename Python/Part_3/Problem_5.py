#Problem 5
#1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

while True:
    for i in range(1,101):
        if(i % 3 ==0):
            print(i)
        else:
            continue
    break                