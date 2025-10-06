# https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return 0
        else:
            queue = deque([(0, 0)])

        visited, max_val = set(), 0
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))

            lowest = None
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    val = grid[x][y]
                    max_val = val if val > max_val else max_val
                    if lowest is None:
                        lowest = (x, y, val)
                    else:
                        lowest = (x, y, val) if val <= lowest[2] else lowest
            if lowest is not None:
                queue.append((lowest[0], lowest[1]))

        return max_val
