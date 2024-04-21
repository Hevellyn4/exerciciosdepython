a = input("Informe um valor para a variável A: ")
b = input("Informe um valor para a variável B: ")

if (a>b):
    aux=a;
    a=b;
    b=aux;
print("O valor da variável A agora é: ", a);
print("O valor da variável B agora é: ", b);