def draw_board():
    a=['0','1','2','3','4','5','6','7','8','9']
    print("\n\n\n TIC TAC TOE \n\n")
    print("player 1 [X]  - player 2 [O]")
    print("    |    |    ")
    print(" {}  | {}  | {}".format(a[1], a[2], a[3]))
    print("____|____|____")
    print("    |    |    ")
    print(" {}  | {}  | {}".format(a[4], a[5], a[6]))
    print("____|____|____")
    print("    |    |    ")
    print(" {}  | {}  | {}".format(a[7], a[8], a[9]))
    print("    |    |    ")

def check_win(a):
    if (a[1]==a[2] and a[2]==a[3]):
        return 0
    elif (a[4]==a[5] and a[5]==a[6]):
        return 0
    elif (a[7]==a[8] and a[8]==a[9]):
        return 0
    elif (a[1]==a[4] and a[4]==a[7]):
        return 0
    elif (a[2]==a[5] and a[5]==a[8]):
        return 0
    elif (a[3]==a[6] and a[6]==a[9]):
        return 0
    elif (a[1]==a[5] and a[5]==a[9]):
        return 0
    elif (a[3]==a[5] and a[5]==a[7]):
        return 0
    elif(all(a[i]!=str(a[i])for i in range(1, 10))):
        return 1
    else:
        return -1


def play():
    player=1
    status=-1
    while(status==-1):
        draw_board()
        player=1 if player%2!=0 else 2
        print("Player{} give your choice: ".format(player))
        try:
            d=int(input())
            mark = 'x' if player==1 else 'o'
            if d>=1 and d<=9 and a[d]==str(d):
                a[d] = mark
            else:
                print("Invalid move. Try again.")
                time.sleep(1)
                continue
        except ValueError:
            print(" Invalid Input")
            time.sleep(1)
            continue
        status = check_win(a)
        current_player = 'X' if player == 1 else 'O'
    
draw_board():
    result = check_win(a)
        if result == 0:
            print(f"Player {player} wins!")
            break
        elif result == 1:
            print("It's a draw!")
            break
        
        player += 1