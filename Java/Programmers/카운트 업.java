import java.util.*;

class Solution {
    public List solution(int start, int end) {
        List<Integer> answer = new ArrayList<>();

        for (int i = start; i < end+1; i++) {
            answer.add(i);
        }
        return answer;
    }
}