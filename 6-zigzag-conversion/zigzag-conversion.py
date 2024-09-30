class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = 0; direction = -1
        rows = [[] for _ in range(numRows)]

        i = 0
        while(len(s) > i):
            rows[row].append(s[i])
            if row < numRows-1 and direction == -1:
                row+=1
            if row > 0 and direction == 1:
                row -= 1
            if row == 0 or row == numRows-1:
                direction *= -1
            i+=1

        return ''.join(''.join(c) for c in rows)