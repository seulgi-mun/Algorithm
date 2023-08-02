import java.util.*;

class Solution {
    public int solution(int n, String control) {
        int answer = n;

        String[] word = control.split("");

        for (int i = 0; i < word.length; i++) {
            if (word[i].equals("w")) {
                answer += 1;
            } else if (word[i].equals("s")) {
                answer -= 1;
            } else if (word[i].equals("d")) {
                answer += 10;
            } else if (word[i].equals("a")) {
                answer -= 10;
            }
        }

        return answer;
    }
}