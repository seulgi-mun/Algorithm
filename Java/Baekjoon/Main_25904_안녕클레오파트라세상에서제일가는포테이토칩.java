import java.util.*;

public class Main_25904_안녕클레오파트라세상에서제일가는포테이토칩 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		int k = in.nextInt();
		int []t = new int[n];
		
		for (int i = 0; i < n; i ++) {
			t[i] = in.nextInt();
		}
		
		int j = k;
		while (true) {
			for (int i = 0; i < n; i++) {
				if (t[i] >= j) {
					j += 1;
					continue;
				} else {
					
					System.out.println(i+1);
					System.exit(0);
				}
			}
		}
		
	}

}
