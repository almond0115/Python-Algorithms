# 문제
# 아주 먼 미래에 사람들이 가장 많이 사용하는 대중교통은 하이퍼튜브이다.
# 하이퍼튜브 하나는 역 K개를 서로 연결한다. 1번역에서 N번역으로 가는데 방문하는 최소 역의 수는 몇 개일까?

# 입력
# 첫째 줄에 역의 수 N과 한 하이퍼튜브가 서로 연결하는 역의 개수 K, 하이퍼튜브의 개수 M이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ K, M ≤ 1000)
# 다음 M개 줄에는 하이퍼튜브의 정보가 한 줄에 하나씩 주어진다. 총 K개 숫자가 주어지며, 이 숫자는 그 하이퍼튜브가 서로 연결하는 역의 번호이다.

# 출력
# 첫째 줄에 1번역에서 N번역으로 가는데 방문하는 역의 개수의 최솟값을 출력한다. 만약, 갈 수 없다면 -1을 출력한다.

import sys
from collections import deque
n, k, m = map(int, input().split())
subway = [[] for _ in range(n+m+1)]

for idx in range(1, m+1):
    tube_nums = list(map(int, input().split()))
    subway[n+idx] = tube_nums
    for s in tube_nums:
        subway[s].append(n+idx)

q = deque()
isVisited = [False] * (n+m+1)
q.append((1, isVisited, 1))
isVisited[1] = True

while q:
    station, visited, stage = q.popleft()
    if station == n:
        print('1번역에서 N번역으로 가는데 방문하는 역의 개수의 최솟값 = %d' % stage)
        sys.exit()

    for i in subway[station]:
        if not visited[i]:
            visited[i] = True
            if i > n:
                q.append((i, visited, stage))
            else:
                q.append((i, visited, stage+1))
print(-1)