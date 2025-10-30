# 1부터 100까지 숫자를 출력
# 단, 2의 배수이거나 5의 배수일 경우 "x의 배수입니다" 출력

for i in range(1, 101):
    if i % 2 == 0 or i % 5 == 0:
        print(f"{i}는 x의 배수입니다")
    else:
        print(i)
