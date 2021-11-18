total = 0 # tota을 0으로 초기화
Answer = 'yes' # Answer을 yes로 초기화
while Answer == 'yes': # Answer이 yes면 반복문 조건 성립
    total += int(input('입력 : ')) # total에 입력받은 값을 누적해서 더해나감
    print(total) # total 출력
    Answer = input('계속? (yes/no)') # Answer값을 다시 입력받음
