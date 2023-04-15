import java.util.*;

public class Main_11536_줄세우기 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		String[] name = new String[n];
		String[] asc_name = new String[n];
		boolean asc = false;
		boolean desc = false;
		
		for (int i = 0; i < n; i++) {
			asc_name[i] = name[i] = in.next();
		}
		
		Arrays.sort(asc_name);
		
		for (int i = 0; i < n; i++) {
			if (asc_name[i] == name[i]) {
				asc = true;
			} else {
				asc = false;
				break;
			}
		}
		
		if (asc == true) {
			System.out.println("INCREASING");
			System.exit(0);
		}
		
		for (int i = 0; i < n; i++) {
			if (asc_name[n-1-i] == name[i]) {
				desc = true;
			} else {
				desc = false;
				break;
			}
		}
		
		
		if (desc == true) {
			System.out.println("DECREASING");
			System.exit(0);
		}
		
		System.out.println("NEITHER");
	}

}
