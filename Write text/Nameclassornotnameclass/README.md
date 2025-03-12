16/01/2024
 
Write in Portuguese,English and Spanish.


![image](https://github.com/user-attachments/assets/958db988-0923-41e2-8d9d-ff16045a2b7c)

 
# Português 

# Diferença entre Cobol e Python

-No mercado contemos separação de dois grupos sobre linguagens de programação de nível baixo como o Cobol e de nível alto o Python.


# Principais diferenças 

## Cobol

-Lançamento em 1959;

-O recurso principal é orientação a objeto;

-Contém divisões de ambiente,dados e procedimento.

## Python

-Lançamento em 1991;

-O recurso principal é análise de dados;

-Contém biblioteca padrão,tratamento de exceções e programação funcional.


# Exemplos


-Abaixo contém o exemplo  das duas linguagens de programação sobre a realização de uma multiplicação que o usuário solicita os números.



## Cobol 

```markdown
#

IDENTIFICATION DIVISION.
PROGRAM-ID. OPERATIONS.
DATA  DIVISION.2024/01/16
FILE SECTION.
WORKING-STORAGE SECTION.
01 NUM1 PIC 9(4).
01 NUM2 PIC 9(4).
01 RESULTADO PIC 9(5).
PROCEDURE DIVISION.
MAIN-PROCEDURE.
DISPLAY "One number".
ACCEPT NUM1.
DISPLAY "Two number".
ACCEPT NUM2.
MULTIPLY NUM1 BY NUM2 GIVING RESULT.
DISPLAY "The result"RESULT.
STOP RUN.
END  PROGRAM  OPERATIONS.

#

```

## Python 

```markdown
#

onenum = int(input("One number\n"))
twonum = int(input("Two number\n"))

multi = onenum * twonum

print("The result")
print(multi)

#

```


Muito obrigada esse é um pequeno texto rápido dos principais pontos.Até a próxima!


--------------------------------------------------------------------------------------------------------------------------------
