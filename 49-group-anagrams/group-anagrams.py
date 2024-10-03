class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        for i in range(len(strs)):
            asc_val = ''.join(sorted(strs[i]))
            if asc_val not in D.keys():
                D[asc_val] = [strs[i]]
            else:
                D[asc_val].append(strs[i])
        print(D)
        return reversed([reversed(vals) for vals in D.values()])