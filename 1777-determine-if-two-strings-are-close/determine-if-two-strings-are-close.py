class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        w1_counts = Counter(list(word1))
        w2_counts = Counter(list(word2))

        word1 = ''.join(sorted(word1))
        word2 = ''.join(sorted(word2))

        if word1 == word2: return True
        if sorted(w1_counts.values()) == sorted(w2_counts.values()) and sorted(w1_counts.keys()) == sorted(w2_counts.keys()): return True
        return False