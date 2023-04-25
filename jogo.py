print("Heroic Side\nDigite 'start' para começar")
start = str(input())
difI = False
difH = False
while start != 'start':
    start = str(input())
if start == 'start':
    print('Carregando...')
    nome = str(input("Digite seu nome de herói: "))
    print("Seu nome de herói é",nome,", deseja alterá-lo ?")
    altnome= str(input("S para sim e N para não."))
    while altnome == "S" or altnome == "s":
        nome = str(input("Digite seu nome de herói: "))
        print("Seu nome de herói é",nome,", deseja alterá-lo ?")
        altnome= str(input("S para sim e N para não."))
    dificuldade = str(input("Definido o nome do herói.\nAgora escolha a dificuldade (I)para Iniciante e (H) para Heróico: "))
    while dificuldade != 'i' and dificuldade != 'I' and dificuldade != 'h' and dificuldade != 'H':
        dificuldade = str(input("Digite novamente: "))
    if dificuldade == 'i' or dificuldade == 'I':
        dificuldade = "Iniciante"
        difI = True
    elif dificuldade == 'h' or dificuldade == 'H':
        dificuldade = "Heróico"
        difH = True
    print("Você escolheu a dificuldade",dificuldade)
    if difI == True:
        vida = 5
        enemyhealth1 = 3
        enemyhealth2 = 5
        bosshealth = 10
    if difH == True:
        vida = 3
        enemyhealth1 = 5
        enemyhealth2 = 10
        bosshealth = 15
    print('___Heroic Side___')
    print(f'Na escola de heróis Heroic Side(HS), localizada em Tóquio no Japão, estudava um aluno chamado {nome}, um aluno exemplar e de alto escalão.')
    print('A vida era normal e calma, as vezes apareciam alguns vilões e esses eram derrotados como forma de teste para os alunos, porém um dia essa calma foi encerrada.')
    print("No dia do teste final dos alunos a organização Villan's District armou uma enboscada para os todos os heróis e a maioria foi derrotado, por conta disso algo fora do comum aconteceu, foi necessário pedir reforços para os heróis do Estados Unidos.")
    print(f'Após a chegada deles foram formadas equipes e o {nome} foi designado para uma, com o héroi Exterminator. Para facilitar a comunicação foi necessário utilizar o inglês, você consegue derrotar os vilões e salvar Tóquio?')
    print(vida,enemyhealth1,bosshealth)