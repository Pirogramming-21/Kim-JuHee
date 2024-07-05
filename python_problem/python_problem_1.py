import random

def brGame():
    num = 0
    turn = 'computer'  

    while num < 31:
        if turn == 'player':
            while True:
                try:
                    n = int(input(f"{turn}, 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
                    if n in [1, 2, 3]:
                        break
                    else:
                        print("1,2,3 중 하나를 입력하세요")
                except ValueError:
                    print("정수를 입력하세요")
        else:
            n = random.randint(1, 3)
            print(f"computer 부른 숫자의 개수: {n}")
        
        for i in range(n):
            num += 1
            print(f"{turn} : {num}")
        
        if num >= 31:
            if turn == 'player':
                winner = 'computer'
            else:
                winner = 'player'
            print(f"{winner} win!")
            break
        
        if turn == 'player':
            turn = 'computer'
        else:
            turn = 'player'

brGame()
