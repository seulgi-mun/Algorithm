import java.util.*;

class Solution {
    public List solution(int[] arr) {
        List answer = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            // System.out.println(i);
            if (arr[i] < 50 && arr[i] % 2 != 0) {
                answer.add(arr[i] * 2);
            } else if (arr[i] >= 50 && arr[i] % 2 == 0) {
                answer.add(arr[i] / 2);
            } else {
                answer.add(arr[i]);
            }
        }
        // System.out.println(answer);
        // System.out.println();

        return answer;
    }
}