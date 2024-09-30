class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows
        rows = [''] * numRows
        row = 0
        direction = -1  # Direction control
        
        for char in s:
            rows[row] += char
            
            # Change direction when at the top or bottom row
            if row == 0 or row == numRows - 1:
                direction *= -1
            
            row += direction
        
        # Combine all rows into one string
        return ''.join(rows)
