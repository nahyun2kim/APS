import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	static int N, M;
	static int[] nums, sel;
	static Set<String> list = new LinkedHashSet<>();
	static StringBuilder sb;
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
		sb = new StringBuilder();
		for(String s : list)
			sb.append(s).append('\n');
		System.out.println(sb);
		
	}
	
	static void comb(int idx, int selIdx) {
		if(selIdx == M) {
			sb = new StringBuilder();
			for(int s : sel)
				sb.append(s).append(' ');
			list.add(sb.toString());
			return;
		} else if(idx == N)
			return;
		
		sel[selIdx] = nums[idx];
		comb(idx, selIdx+1);
		comb(idx+1, selIdx);
	}
}