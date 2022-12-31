import java.util.*;

public class Main_1436_영화감독숌 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		int i = 0;
		int cnt = 0;
		int num = 0;
		ArrayList tmp = new ArrayList();
		
//		System.out.println(n);
		
		
		while (true) {
			num ++;
			String s = Integer.toString(num);
//			System.out.println(i);
			if (s.contains("666")) {
				tmp.add(num);
				cnt++;
//				System.out.println(i);
			if (cnt == n) {
				break;
			}
			}
			i++;
		}
		System.out.println(tmp.get(n-1));
//		n.close();
	}

}
