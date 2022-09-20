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
		comb(0, 0);
		System.out.println(sb);
	}
	
	public static void comb(int idx, int selIdx) {
		if(selIdx == M) {
			for(int s : sel)
				sb.append(s).append(' ');
			sb.append('\n');
			return;
		} else if(idx == N)
			return;
		
		sel[selIdx] = idx+1;
		comb(idx, selIdx+1);
		comb(idx+1, selIdx);
	}
}