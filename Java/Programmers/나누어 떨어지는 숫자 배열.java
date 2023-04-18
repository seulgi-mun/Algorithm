import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
         ArrayList<Integer> tmp = new ArrayList<Integer>();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % divisor == 0) {
                tmp.add(arr[i]);
            }
        }

        if (tmp.isEmpty()) {
            tmp.add(-1);
        }

        answer = new int[tmp.size()];

        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }

        Arrays.sort(answer);

        return answer;
    }
}