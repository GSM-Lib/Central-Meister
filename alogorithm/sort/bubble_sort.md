# Bubble sort

![image](https://user-images.githubusercontent.com/81360154/210468724-e954b608-66fa-4fad-bce2-f93576a859b3.png)

가장 큰수를 뒤로 밀어내며 정렬한다.

1. 배열안의 이웃하는 두 값을 고른다.
2. 둘이 swap해야하는 경우(오름차순 기준 왼쪽이 더 클 경우) swap한다.
3. else continue
4. 한바퀴 돌면 마지막 값은 가장 큰 값이 되기 떄문에 (전체 배열의 크기 - 현재까지 반복한 바퀴수)만큼 비교한다. 즉 한바퀴마다 비교하는 경우가 하나씩 줄어든다.

## O(n^2)
best, worst상관없이 비교를 n-1,n-2,..,1번 하므로 시간복잡도는 O(n^2)이다