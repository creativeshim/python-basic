#10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
#1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

a = 1;
num = 0;
while a<1000:
    if(a%3 == 0):
        num += a
    elif(a%5 == 0):
        num += a
    a = a + 1
print(num);
