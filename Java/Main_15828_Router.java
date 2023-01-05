import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;



public class Main_15828_Router {

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder res = new StringBuilder();
		int n = Integer.parseInt(in.readLine());
		
		Queue<Integer> q = new LinkedList<>();
		
		
		while (true) {
			int info = Integer.parseInt(in.readLine());
			
			if (info == -1) {
				break;
			}
			
			if (info == 0) {
				q.remove();
			} else if (n > q.size()) {
				q.add(info);
			}
				
		}
		
		if (q.isEmpty()) {
			System.out.println("empty");
		} else {
			for (int i : q) {
				res.append(i + " ");
			}
			System.out.println(res);
		}

	}

}
