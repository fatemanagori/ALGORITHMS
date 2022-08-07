from collections import deque
class Solution:
  def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
    m = len(maze)
    n = len(maze[0])
    dirs = [0, 1, 0, -1, 0]
    q = deque([(start[0], start[1])])
    seen = {(start[0], start[1])}

    def isValid(x: int, y: int) -> bool:
      return 0 <= x < m and 0 <= y < n and maze[x][y] == 0

    while q:
      i, j = q.popleft()
      for k in range(4):
        x = i
        y = j
        while isValid(x + dirs[k], y + dirs[k + 1]):
          x += dirs[k]
          y += dirs[k + 1]
        if [x, y] == destination:
          return True
        if (x, y) in seen:
          continue
        q.append((x, y))
        seen.add((x, y))

    return False
def main():
    sol=Solution()
    print('Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0], start=[0,4], destination=[4,4]]')
    print("Output: " ,sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4],[4,4]))
    print()
    print('Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0], start=[0,4], destination=[3,2]]')
    print("Output: " ,sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4],[3,2]))
    print()
    print('Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0], start=[0,4], destination=[0,1]]')
    print("Output: " ,sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [4,3],[0,1]))
if __name__=="__main__":
    main()