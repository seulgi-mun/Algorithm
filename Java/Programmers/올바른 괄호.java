import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int pair = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                pair += 1;
            } else {
                if (pair >= 1) {
                    pair -= 1;
                } else {
                    pair += 1;
                }
            }
        }

        if (pair != 0) {
            answer = false;
        }

        return answer;
    }
}