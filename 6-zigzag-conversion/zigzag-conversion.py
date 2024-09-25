class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = 0; zig = False
        i = 0
        M = [[] for _ in range(numRows)]

        while(len(s) > i):
            M[row].append(s[i])
            if row < numRows-1 and zig == False:
                row+=1
            if row > 0 and zig == True:
                row -= 1
            if row == 0 or row == numRows-1:
                zig = not zig
            i+=1

        return ''.join(''.join(c) for c in M)