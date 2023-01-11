from typing import List
def until_one(n,k):
    cnt = 0
    while n>1:
        if n % k == 0:
            cnt += 1
            n /= k
        else:
            n -= 1
    
    return cnt

print(until_one(26,5))


def muzi_mukbang(food_times, k):
    if sum(food_times) <= k:
        return -1
    n = len(food_times)
    arg2 = list(range(n))
    arg = sorted(arg2, key=lambda x: food_times[x])
    cnt = 0
    
    for minimum in arg:
        if k - (food_times[minimum] - cnt) * n < 0:
            break
        k -= (food_times[minimum] - cnt) * n
        arg2.remove(minimum)
        n -= 1
        cnt += food_times[minimum] - cnt
            
    
    
    return arg2[k % n] + 1

import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    n = len(food_times)
    food_times = list(zip(food_times,range(1,n+1)))
    heapq.heapify(food_times)
    
    cnt = 0
    while k - (food_times[0][0] - cnt) * n >= 0:
        k -= (food_times[0][0] - cnt) * n
        cnt += food_times[0][0] - cnt
        heapq.heappop(food_times)
        n -= 1
        
    food_times.sort(key=lambda x: x[1])
    return food_times[k % n][1]
        
# 다른사람의풀이
def solution(ft, k):
    answer = 0

    while k > 0 :
        a = k // (len(ft) - ft.count(0) )
        b = k % (len(ft) - ft.count(0) )

        for i, j in zip(ft, range(len(ft))):
            if ft[j] != 0:
                ft[j] = i - a
                if ft[j] < 0:
                    b = b + abs(ft[j])
                    ft[j] = 0
            k = b

        if len(ft) - ft.count(0) ==0:
            return -1

        if k+1 <= len(ft) - ft.count(0):
            for i in ft:
                answer += 1
                if i !=0 :
                    k -= 1
                if k == -1:
                    return answer

