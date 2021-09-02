#구현문제 3번째
#왕실 나이트 소요시간 20분 

n = input()

#나이트가 이동할 수 있는 경로 [숫자][알파벳] 
#수직으로 두칸 수평으로 한칸 (+2, +1) , (+2, -1), (-2, +1), (-2, -1)
#수직으로 한칸 수평으로 두칸 (+1, +2) , (+1, -2), (-1, +2), (-1, -2)
#이동 한계 거리 8을 초과할 수 없음 + 1 미만이 될 수 없음
alpha= ['a', 'b','c','d','e','f','g','h']

dx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [2, 2 , -2, -2, 1, 1, -1, -1]

count = 0

x = alpha.index(str(n)[0]) + 1 
y = int(str(n)[1])

for i in range(len(dx)):
    if x + dx[i] > 8 or x + dx[i] < 1 or y +dy[i] > 8  or y + dy[i] < 1:
        continue
    else:
        count += 1

print(count)