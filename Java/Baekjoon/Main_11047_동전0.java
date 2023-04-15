import java.util.Scanner;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_11047_동전0 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
//		Scanner in = new Scanner(System.in);
//		ArrayList<Integer> coin = new ArrayList<Integer>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int[] coin = new int[n];
		
		for (int i = 0; i < n; i++) {
			coin[i] = Integer.parseInt(br.readLine());
		}
		
		int cnt = 0;
		for (int i = n-1; i >= 0; i--) {
			if (coin[i] <= k) {
				cnt += (k / coin[i]);
				k = (k % coin[i]);
			}
		}
		System.out.println(cnt);
			
	}

}
