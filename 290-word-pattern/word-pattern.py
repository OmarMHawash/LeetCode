class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_arr = list(pattern)
        s_arr = s.split(' ')

        if len(p_arr) != len(s_arr): return False
        if len(set(p_arr)) != len(set(s_arr)): return False

        D = {}
        for i in range(len(p_arr)):
            if p_arr[i] not in D:
                D[p_arr[i]] = s_arr[i]
            else:
                if D[p_arr[i]] != s_arr[i]:
                    return False
        return True