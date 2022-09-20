import java.util.Arrays;
import java.util.Scanner;

// 순열인데 배열이 주어짐
public class Main {
	static int N, M;
	static int[] nums, sel;
	static boolean[] check;
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
		
		permutation(0);
		System.out.println(sb);
	}
	
	static void permutation(int idx) {
		if(idx == M) {
			for(int n : sel)
				sb.append(n).append(' ');
			sb.append('\n');
			return;
		}
		
		for(int i=0; i<N; i++) {
			if(check[i] == false) {
				check[i] = true;
				sel[idx] = nums[i];
				permutation(idx+1);
				check[i] = false;
			}
		}
	}
}