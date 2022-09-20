import java.util.Arrays;
import java.util.Scanner;

// 중복 순열인데 배열 받아서
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
		permutation(0);
		System.out.println(sb);
		
	}
	
	static void permutation(int idx) {
		if(idx == M) {
			for(int s : sel) {
				sb.append(s).append(' ');
			}
			sb.append('\n');
			return;
		}
		
		for(int i=0; i<N; i++) {
			sel[idx] = nums[i];
			permutation(idx+1);
		}
	}
}