#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

input1 = input("자연수를 입력하세요:" )
num = int(input1) % 2
if num == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def avr_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result / len(args)

result = avr_many(1, 2, 3)
print(result)

#filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

a = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x:x>0, a)))

