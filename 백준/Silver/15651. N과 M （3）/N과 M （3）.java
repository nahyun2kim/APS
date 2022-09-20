import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] sel;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		sel = new int[M];
		
		permutation(0);
		System.out.println(sb);
		
	}
	
	static void permutation(int idx) {
		if (idx == M) {
			for (int s : sel) {
				sb.append(s).append(' ');
			}
			sb.append('\n');
			return;
		}
		
		for(int i=0; i<N; i++) {
			sel[idx] = i+1;
			permutation(idx+1);
		}
	}
}