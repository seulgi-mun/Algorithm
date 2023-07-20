import java.util.*;

class Solution {
    public List solution(int[] num_list, int n) {
        List answer = new ArrayList<>();

        for (int i = n-1; i < num_list.length; i++) {
            answer.add(num_list[i]);
            // System.out.println(i);
        }

        return answer;
    }
}