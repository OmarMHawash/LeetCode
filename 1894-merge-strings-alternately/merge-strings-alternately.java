class Solution {
    public String mergeAlternately(String word1, String word2) {
        int size1 = word1.length();
        int size2 = word2.length();
        int minLen = Math.min(size1, size2);
        
        StringBuilder result = new StringBuilder(size1 + size2);
        
        for (int i=0; i<minLen; i++){
            result.append(word1.charAt(i)).append(word2.charAt(i));
        }

         if (size1 > size2) {
            result.append(word1, minLen, size1);
        } else {
            result.append(word2, minLen, size2);
        }

        return result.toString();
    }
}