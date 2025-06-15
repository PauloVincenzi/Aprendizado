"""
Estruturas condicionais
if, else, elif
"""

idade = int(input('Qual sua idade? '))

"""
# Estrutura condicionais if, else em C:

if (idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
   printf("Tem 18 anos");
}else{
   printf("Maior de idade");
}
"""

"""
# Estrutura condicionais if, else em Java:

if (idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
   System.out.println("Tem 18 anos");
}else{
   System.out.println("Maior de idade");
}
"""

# Em Python:
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')

# Em C e em Java, não existe elif. Para isso, utiliza-se 'else if'.