import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] nums, sel;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		for(int i=0; i<N; i++)
			nums[i] = sc.nextInt();
		Arrays.sort(nums);
		
		sel = new int[M];
		comb(0, 0);
		System.out.println(sb);
	}
	
	static void comb(int idx, int selIdx) {
		if(selIdx == M) {
			for(int s : sel)
				sb.append(s).append(' ');
			sb.append('\n');
			return;
		} else if(idx == N)
			return;
		
		sel[selIdx] = nums[idx];
		comb(idx, selIdx+1);
		comb(idx+1, selIdx);
	}
}