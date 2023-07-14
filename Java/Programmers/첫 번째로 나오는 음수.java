class Solution {
    public int solution(int[] num_list) {
        int answer = -1;

        // num_list.map(i => i < 0 )
        for (int i = 0; i < num_list.length; i++) {
            if (num_list[i] < 0) {
                answer = i;
                break;
            }
        }
        // System.out.println(num_list);

        return answer;
    }
}