class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        w1_counts = Counter(word1)
        w2_counts = Counter(word2)

        if set(w1_counts.keys()) != set(w2_counts.keys()): return False

        return sorted(w1_counts.values()) == sorted(w2_counts.values())
