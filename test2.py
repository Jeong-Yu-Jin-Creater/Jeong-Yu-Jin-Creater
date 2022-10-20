#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

from platform import java_ver


result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

#while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

#*
#**
#***
#****
#*****
i = 0
while i < 5:
    i = i + 1
    print(i * "*")
    

#for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for i in range(1,101):
    print(i)

######################################################################
print("-------------------------------------------------")
#A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#for문을 사용하여 A 학급의 평균 점수를 구해 보자.

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for num in score:
    total += num
average = total / len(score)
print(average)
    
        
    

