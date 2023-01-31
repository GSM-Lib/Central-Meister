# https://school.programmers.co.kr/learn/courses/30/lessons/60063#
from collections import deque

def solution(board):
    n = len(board)
    q = deque([[[1,1],[1,2],0,False]]) # pos(left,up), pos(right,down), cost, is_vertical
    h_visited = [[False] * (n+2) for _ in range(n+2)]
    v_visited = [[False] * (n+2) for _ in range(n+2)]
    board = [[1] * (n+2)] + [[1]+b+[1] for b in board] + [[1] * (n+2)]
    while q:
        state = q.popleft()
        if state[3]:
            if v_visited[state[0][0]][state[0][1]] and v_visited[state[1][0]][state[1][1]]:
                continue
        else:
            if h_visited[state[0][0]][state[0][1]] and h_visited[state[1][0]][state[1][1]]:
                continue
        print(state)
        if [n,n] in state: return state[2]

        if not state[3]:
            h_visited[state[0][0]][state[0][1]] = True
            h_visited[state[1][0]][state[1][1]] = True
            # left
            if board[state[0][0]][state[0][1]-1] == 0 and not h_visited[state[0][0]][state[0][1]-1]:
                q.append([[state[0][0], state[0][1]-1],state[0], state[2]+1, False])
                
            # right
            if board[state[1][0]][state[1][1]+1] == 0 and not h_visited[state[1][0]][state[1][1]+1]:
                q.append([state[1], [state[1][0],state[1][1]+1], state[2]+1, False])
                
            # up
            if board[state[0][0]-1][state[0][1]] == 0 and board[state[1][0]-1][state[1][1]] == 0 and (not h_visited[state[0][0]-1][state[0][1]] or not h_visited[state[1][0]-1][state[1][1]]):
                q.append([[state[0][0]-1,state[0][1]], [state[1][0]-1,state[1][1]], state[2]+1, False])
                
            # down 
            if board[state[0][0]+1][state[0][1]] == 0 and board[state[1][0]+1][state[1][1]] == 0 and (not h_visited[state[0][0]+1][state[0][1]] or not h_visited[state[1][0]+1][state[1][1]]):
                q.append([[state[0][0]+1,state[0][1]], [state[1][0]+1,state[1][1]], state[2]+1, False])
                
            # right to up
            if board[state[0][0]-1][state[0][1]] == 0 and board[state[1][0]-1][state[1][1]] == 0 and not v_visited[state[0][0]-1][state[0][1]] and not v_visited[state[1][0]-1][state[1][1]]:
                q.append([[state[0][0]-1,state[0][1]], state[0], state[2]+1, True])
                
            # right to down
            if board[state[0][0]+1][state[0][1]] == 0 and board[state[1][0]+1][state[1][1]] == 0 and not v_visited[state[0][0]+1][state[0][1]] and not v_visited[state[1][0]+1][state[1][1]]:
                q.append([state[0], [state[0][0]+1,state[0][1]], state[2]+1, True])
                
            # left to up
            if board[state[0][0]-1][state[0][1]] == 0 and board[state[1][0]-1][state[1][1]] == 0 and not v_visited[state[0][0]-1][state[0][1]] and not v_visited[state[1][0]-1][state[1][1]]:
                q.append([[state[1][0]-1,state[1][1]], state[1], state[2]+1, True])
                
            # left to down
            if board[state[0][0]+1][state[0][1]] == 0 and board[state[1][0]+1][state[1][1]] == 0 and not v_visited[state[0][0]+1][state[0][1]] and not v_visited[state[1][0]+1][state[1][1]]:    
                q.append([state[1], [state[1][0]+1,state[1][1]], state[2]+1, True])
                

        if state[3]:
            v_visited[state[0][0]][state[0][1]] = True
            v_visited[state[1][0]][state[1][1]] = True
            # left
            if board[state[0][0]][state[0][1]-1] == 0 and board[state[1][0]][state[1][1]-1] == 0 and (not v_visited[state[0][0]][state[0][1]-1] or not v_visited[state[1][0]][state[1][1]-1]):
                q.append([[state[0][0],state[0][1]-1], [state[1][0],state[1][1]-1], state[2]+1, True])
                
            # right
            if board[state[0][0]][state[0][1]+1] == 0 and board[state[1][0]][state[1][1]+1] == 0 and (not v_visited[state[0][0]][state[0][1]+1] or not v_visited[state[1][0]][state[1][1]+1]):
                q.append([[state[0][0],state[0][1]+1], [state[1][0],state[1][1]+1], state[2]+1, True])
                
            # up 
            if board[state[0][0]-1][state[0][1]] == 0 and not v_visited[state[0][0]-1][state[0][1]]:
                q.append([[state[0][0]-1, state[0][1]],state[0], state[2]+1, True])
                
            # down
            if board[state[1][0]+1][state[1][1]] == 0 and not v_visited[state[1][0]+1][state[1][1]]:
                q.append([state[1], [state[1][0]+1,state[1][1]], state[2]+1, True])
                
            # down to left
            if board[state[0][0]][state[0][1]-1] == 0 and board[state[1][0]][state[1][1]-1] == 0 and not h_visited[state[0][0]][state[0][1]-1] and not h_visited[state[1][0]][state[1][1]-1]:
                q.append([[state[0][0],state[0][1]-1], state[0], state[2]+1, False])
                
            # down to right
            if board[state[0][0]][state[0][1]+1] == 0 and board[state[1][0]][state[1][1]+1] == 0 and not h_visited[state[0][0]][state[0][1]+1] and not h_visited[state[1][0]][state[1][1]+1]:
                q.append([state[0], [state[0][0],state[0][1]+1], state[2]+1, False])
                
            # up to left
            if board[state[0][0]][state[0][1]-1] == 0 and board[state[1][0]][state[1][1]-1] == 0 and not h_visited[state[0][0]][state[0][1]-1] and not h_visited[state[1][0]][state[1][1]-1]:
                q.append([[state[1][0],state[1][1]-1], state[1], state[2]+1, False])
                
            # up to right
            if board[state[0][0]][state[0][1]+1] == 0 and board[state[1][0]][state[1][1]+1] == 0 and not h_visited[state[0][0]][state[0][1]+1] and not h_visited[state[1][0]][state[1][1]+1]:
                q.append([state[1], [state[1][0],state[1][1]+1], state[2]+1, False])
            