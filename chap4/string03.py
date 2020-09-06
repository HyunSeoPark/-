# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결

# 문자열.join(문자열로 구성된 리스트) // join() 함수는 리스트의 요소를 문자열로 연결
 
# 변수 선언
number = int(input("정수 입력> "))

# if 조건문으로 홀수 짝수 구분
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
        ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다." 
    ]).format(number, number))