import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0,0};

        int degree = 1;
        int count = 0;
        Map<String, Boolean> result = new HashMap<>();
        String before = "";
        for (String word : words) {
            count++;
            if (
                    result.containsKey(word)
                            || (!(count == 1 && degree == 1) && before.charAt(before.length() - 1) != word.charAt(0))) {
                answer[0] = count;
                answer[1] = degree;
                break;
            }
            result.put(word, true);
            before = word;
            if (count == n) {
                count = 0;
                degree++;
            }
        }
        return answer;
    }
}
