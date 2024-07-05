num = 0
turn = 'A'

while num < 31:
    while True:
        try:
            n = int(input(f"player{turn}, 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if n in [1, 2, 3]:
                break
            else:
                print("1,2,3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")
    
    for i in range(n):
        num += 1
        print(f"player{turn} : {num}")
    
    if num >= 31:
        print(f"player{turn} win!")
        break
    
    if turn == 'A':
        turn = 'B'
    else:
        turn = 'A'
