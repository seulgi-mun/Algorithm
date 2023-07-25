import java.util.*;

class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;

        int sizee = is_prefix.length();
        if (sizee <= my_string.length()) {
            if (my_string.substring(0, sizee).equals(is_prefix)) {
                answer = 1;
            }
        }

        return answer;
    }
}