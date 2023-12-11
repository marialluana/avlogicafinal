#primeiro eu peço o valor do salario pro usuario
s = float(input("Digite o valor do seu salário [COLOQUE 2 CASAS DECIMAIS]: "))

#se "s" for igual ou menor que 2000, o usuario está isento de impostos 
if s <= 2000.00:
    #se a condição for verdadeira, o "print" é ultilizado
    print("Você está ISENTO de impostos!")

#se "s" for igual ou maior que 2000 ou
#menor ou igual a 3000, o usuario irá pagar 8% de imposto
elif s >= 2000.01 and s <= 3000.00:
    #a variavel "i" de IMPOSTO é criada
    i = s * 8 /100
    #mostro o valor do imposto que será pago
    print(f"Você deve pagar R$ {i} de imposto!")

#faço o mesmo que no código anterior, porém com valores diferentes
elif s >= 3000.01 and s <= 4500.00:
    i = s * 18 /100
    print(f"Você deve pagar R$ {i} de imposto!")

#agora precisa apenas de uma comparação, pois a partir do 4500.00 o valor do imposto
#será sempre 28%
elif s > 4500.00:
    i = s * 28 /100
    print(f"Você deve pagar R$ {i} de imposto!")