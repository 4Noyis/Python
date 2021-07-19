# 1,1,2,3,5,8


a=1
b=1

fibonacci=[a,b]

for i in range(10):
    print(a,b)
    a,b=b,a+b

    fibonacci.append(b)
print(fibonacci)    
