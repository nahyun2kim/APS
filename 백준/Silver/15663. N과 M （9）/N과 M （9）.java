import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] nums, sel;
	static boolean[] check;
	static List<int[]> list;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		nums = new int[N];
		for(int i=0; i<N; i++) {
			nums[i] = sc.nextInt();
		}
		Arrays.sort(nums);
		sel = new int[M];
		check = new boolean[N];
		list = new ArrayList<>();
		
		perm(0);
		System.out.println(sb);
	}
	
	static void perm(int idx) {
		if(idx == M) {
			for(int i= list.size()-1; i>=0; i--) {
				if(Arrays.equals(list.get(i), sel))
					return;
			}
			list.add(sel.clone());
			for(int s : sel)
				sb.append(s).append(' ');
			sb.append('\n');
			return;
		}
		
		for(int i=0; i<N; i++) {
			if(check[i] == false) {
				check[i] = true;
				sel[idx] = nums[i];
				perm(idx+1);
				check[i] = false;
			}
		}
	}
}