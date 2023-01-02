import java.util.*;


public class Main_2164_카드2 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		Queue<Integer> q = new LinkedList<>();
		
		for (int i = 1; i < n+1; i++) {
			q.add(i);
		}
		
		while (true) {
			if (q.size() == 1) {
				System.out.println(q.poll());
				break;
			}
			q.poll();
			q.add(q.poll());
		}
//		System.out.println(q);

	}

}
