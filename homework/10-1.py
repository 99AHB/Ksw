# 진수 변환하기
def A(base,n):
    if n < base:
        print(numberN[n], end=' ')
    else:
        A(base,n // base)
        print(numberN[n%base], end=' ')

numberN = ['0', '1', '2', '3',  '4', '5', '6', '7', '8', '9']
numberN += ['A', 'B', 'C', 'D', 'E', 'F']

number = int(input('10진수 입력-->'))
print('\n 2진수 : ',end=' ')
A(2,number)
print('\n 8진수 : ',end=' ')
A(8,number)
print('\n 16진수 : ',end=' ')
A(16,number)