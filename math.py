import random
import matplotlib.pyplot as plt

# 주사위를 던지는 횟수
n_trials = 5000  # 예: 100번 주사위를 던짐
dice = int(input())
# 빈 리스트 생성
results = []
x_values=[]
count = 0
# 주사위 던지는 반복문
for i in range(n_trials):
    roll = random.randint(1, 6)  # 1부터 6까지의 랜덤 숫자 생성
    if roll == dice:
        count+=1
        results.append(count/(i+1))
        x_values.append(i+1)
#print(results)
# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(x_values, results, linestyle='-', color='blue')
plt.title('dice')
plt.xlabel('throwing')
plt.ylabel('hawk')
plt.xlim([0,5000])# x축 눈금 설정
plt.ylim([0,1])  # y축 눈금 설정
plt.grid(True)

# 그래프 보여주기
plt.show()