class Solution:
    def romanToInt(self, s: str) -> int:
        R = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        M = {
            "IV": "IIII", "IX": "VIIII", "XL": "XXXX",
            "XC": "LXXXX", "CD": "CCCC", "CM": "DCCCC"
        }
        for k, v in M.items():
            s = s.replace(k, v)

        return sum(R[c] for c in s)
