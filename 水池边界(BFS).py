def check_pool(pool):
    n = len(pool)
    m = len(pool[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    ans = 0
    queue = []
    for i in range(n):
        for j in range(m):
            while queue != []:
                current = queue.pop(0)
                # check 4 direction
                x, y = current[0], current[1]
                if x-1 >= 0 and pool[x-1][y] == "S" and not visited[x-1][y]:
                    queue.append((x-1, y))
                    visited[x-1][y] = True
                if x+1 < n and pool[x+1][y] == "S" and not visited[x+1][y]:
                    queue.append((x+1, y))
                    visited[x+1][y] = True
                if y-1 >= 0 and pool[x][y-1] == "S" and not visited[x][y-1]:
                    queue.append((x, y-1))
                    visited[x][y-1] = True
                if y+1 < m and pool[x][y+1] == "S" and not visited[x][y+1]:
                    queue.append((x, y+1))
                    visited[x][y+1] = True
            if not visited[i][j] and pool[i][j] == "S":
                # a new pool
                ans += 1
                queue.append((i, j))
    return ans





if __name__ == "__main__":
    n_m = input()
    array = n_m.split(',')
    n, m = array[0], array[1]
    rows = []
    for i in range(int(n)):
        rows.append(input())

    print(check_pool(rows))