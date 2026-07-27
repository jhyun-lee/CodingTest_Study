import sys
# DFS 탐색 시 파이썬 기본 재귀 깊이 제한(1000)에 걸리는 것을 방지하기 위해 한도를 늘립니다.
sys.setrecursionlimit(10000)

def solution(board):
    answer = 987654321
    
    R_len = len(board)
    C_len = len(board[0])
    
    # 방문 여부를 체크하는 맵 (최소 이동 횟수 갱신을 위해 무한대 값으로 초기화)
    # 단순 0, 1로만 체크하면 빙빙 돌아간 최악의 경로가 먼저 도달했을 때 
    # 더 빠른 경로가 진입하지 못하는 DFS의 고질적 문제를 방지하기 위함입니다.
    Board_Map = [[987654321 for _ in range(C_len)] for _ in range(R_len)]
    
    StartPoint = []
    EndPoint = []
    
    # 1. 미끄러지는 이동 로직 수정
    def MoveCheck(i, j, Dir):
        AddPoint_y = [1, -1, 0, 0] # 아래, 위, 오른, 왼
        AddPoint_x = [0, 0, 1, -1]
        
        # [수정] 인덱스 범위(보드 경계선) 검사와 "D" 검사를 동시에 진행
        # 다음 칸이 보드 안쪽이고 장애물이 아니라면 계속 미끄러짐
        while 0 <= i + AddPoint_y[Dir] < R_len and 0 <= j + AddPoint_x[Dir] < C_len:
            if board[i + AddPoint_y[Dir]][j + AddPoint_x[Dir]] == "D":
                break
            # [수정] 리스트 더하기 오류 해결 -> [Dir] 인덱스를 명시해서 더함
            i += AddPoint_y[Dir]
            j += AddPoint_x[Dir]
            
        return [i, j]
            
    def FindWay(R, G, Count):
        # [수정] 바깥에 있는 answer 변수를 수정하기 위해 nonlocal 선언
        nonlocal answer
        
        # [수정] 강제로 Count = 0 하던 코드 삭제!
        
        # 가지치기 1: 이미 현재까지 찾은 최소 이동 횟수(answer)보다 더 많이 이동했다면 탐색 중단
        if Count >= answer:
            return
        
        # 가지치기 2: 기존에 이 칸에 도달했던 횟수보다 더 효율적이지 않다면 탐색 중단
        if Board_Map[R[0]][R[1]] <= Count:
            return
            
        # 현재 칸에 도달한 최소 비용(Count) 기록
        Board_Map[R[0]][R[1]] = Count
        
        for i in range(4):
            # [수정] 고정 숫자 4 대신 반복문 변수 i를 전달
            Arrive = MoveCheck(R[0], R[1], i)
            
            # 이동했는데 위치가 그대로라면(벽이나 장애물 바로 앞이라 못 움직임) 스킵
            if Arrive == R:
                continue
            
            if Arrive == G:
                answer = min(answer, Count + 1)
                return
            
            # [수정] 다음 재귀 호출 시 R이 아니라 새로 도착한 위치(Arrive)를 넘기고, Count + 1 전달
            FindWay(Arrive, G, Count + 1)
            
    # 시작점과 도착점 찾기
    for i in range(R_len):
        for j in range(C_len):
            if board[i][j] == "R":
                StartPoint = [i, j]
            elif board[i][j] == "G":
                EndPoint = [i, j]
                
    FindWay(StartPoint, EndPoint, 0)
    
    # 목표 지점에 도달하지 못해 answer가 갱신되지 않았다면 -1 반환
    if answer == 987654321:
        return -1
        
    return answer