import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	static int N, M;
	static int[] nums, sel;
	static boolean[] check;
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
		check = new boolean[N];
		
		perm(0);
		sb = new StringBuilder();
		for(String s : list)
			sb.append(s).append('\n');
		System.out.println(sb);
		
	}
	
	static void perm(int idx) {
		if(idx == M) {
			sb = new StringBuilder();
			for(int s : sel)
				sb.append(s).append(' ');
			list.add(sb.toString());
			return;
		}
		
		for(int i=0; i<N; i++) {
			sel[idx] = nums[i];
			perm(idx+1);
		}
	}
}