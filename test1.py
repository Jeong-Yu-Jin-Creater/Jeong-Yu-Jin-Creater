#홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
#과목	점수
#국어	80
#영어	75
#수학	55

a = 80
b = 75
c = 55
print((a+b+c)/3)

#자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.

a=13
b=2
rest = a % b
if rest == 1:
    print("%d는 홀수입니다." % a)
else:
    print("%d는 짝수입니다." % a)

#홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
#※ 문자열 슬라이싱 기법을 사용해 보자.

a = "19"
pin = "881120-1068234"
print(a + pin[0:6], end=' ')
print(pin[7:])

#주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
#>>> pin = "881120-1068234"

pin = "881120-1068324"
print(pin[7])

#다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
#>>> a = "a:b:c:d"

a= "a:b:c:d"
print(a.replace(":", "#"))

#[1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.

a = ['Life', 'is', 'too', 'short']
print(a[0], a[1], a[2], a[3])

#(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.

a = (1, 2, 3)
b = (4,)
print(a+b)

#딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
#>>> a = {'A':90, 'B':80, 'C':70}

a = {'A':90, 'B':80, 'C':70}
print(a['B'])

#a 리스트에서 중복 숫자를 제거해 보자.
#>>> a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
result1 = dict.fromkeys(a)
print(result1)

result2 = list(result1)
print(result2)