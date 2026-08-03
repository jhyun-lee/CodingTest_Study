def solution(key, lock):
    N = len(lock)
    M = len(key)
    
    def rotate_matrix(a):
        n = len(a)
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[j][n - 1 - i] = a[i][j]
        return result

    Lock_Lota = [lock] 
    for _ in range(3): 
        Lock_Lota.append(rotate_matrix(Lock_Lota[-1]))
        
        
    def check(board):
        for i in range(N, N * 2):
            for j in range(N, N * 2):
                if board[i][j] != 1:
                    return False
        return True

    for current_lock in Lock_Lota:
        board = [[0] * (N * 3) for _ in range(N * 3)]
        
        for i in range(N):
            for j in range(N):
                board[i + N][j + N] = current_lock[i][j]
                
        for x in range(N * 2):
            for y in range(N * 2):
                
                
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] += key[i][j]
                        
                if check(board):
                    return True
                    
                for i in range(M):
                    for j in range(M):
                        board[x + i][y + j] -= key[i][j]


    return False