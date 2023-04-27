class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;

        long cost = 0;
        for (int i = 1; i < count + 1; i++) {
            cost += (price * i);
        }

        if (cost <= money) {
            answer = 0;
        } else {
            answer = cost - money;
        }

        return answer;
    }
}