maps=list(range(1,10))

def pole(maps):
    print("-"*13)
    for i in range(3):
        print('|',maps[0+i*3],'|',maps[1+i*3],'|',maps[2+i*3],'|')
        print("-"*13)

def board(step,simbol):
    ind=maps.index(step)
    maps[ind]=simbol

def result(maps):
    winner=((0,1,2),(3,4,5),(6,7,8),(1,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for n in winner:
        if maps[n[0]] == maps[n[1]] == maps [n[2]]:
            return maps[n[0]]
    return False

def main(maps):
    game_over= False
    play= True
    counter=0

    while game_over==False:
        if play==True:
            simbol="x"
            step=int(input("Игрок 1, Ваш ход"))

        if  not play:
            simbol="o"
            step=int(input("Игрок 2, Ваш ход"))
        counter+=1
        board(step, simbol)
        win=result(maps)
        if win:
            print(win,'Выиграл ')
            break
        game_over = True
        if counter==9:
            print('Ничья')
            break
        else:
            game_over = False
            play = not(play)
            pole(maps)
main(maps)
input('нажмите Enter для завершения')


