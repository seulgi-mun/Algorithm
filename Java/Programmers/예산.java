import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;

        Arrays.sort(d);
        // System.out.println(d);

        int tmp = 0;
        for (int i: d) {
            tmp += i;
            if (budget >= tmp) {
                answer += 1;
            }
        }

        return answer;
    }
}