class Solution {
    public String mergeAlternately(String word1, String word2) {
        // define size, interators, result
        int size1 = word1.length();
        int size2 = word2.length();
        int totalLen = size1 + size2;
        StringBuilder result = new StringBuilder(totalLen);
        int w1count = 0;
        int w2count = 0;
        
        // add alternately:
        while (w1count < size1 || w2count < size2){
            if (w1count < size1){
                result.append(word1.charAt(w1count));
                w1count++;
            }
            if (w2count < size2){
                result.append(word2.charAt(w2count));
                w2count++;
            } 
        }

        return result.toString();
    }
}