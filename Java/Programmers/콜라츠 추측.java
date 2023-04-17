class Solution {
    public int solution(int num) {
        int answer = 0;
        long numm = num;
        int i = 0;

        while(numm != 1) {
            if (i >= 500) {
                answer = -1;
                break;
            }

            if (numm % 2 == 0) {
                numm = numm / 2;
                i++;
            } else {
                numm = (numm * 3) + 1;
                i++;
            }

            if (numm == 1){
                answer = i;
                break;
            }
        }

        return answer;
    }
}