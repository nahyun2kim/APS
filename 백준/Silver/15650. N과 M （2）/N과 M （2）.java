import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] nums;
	static int[] sel;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		
		nums = new int[N];
		for(int i=1; i<=N; i++)
			nums[i-1] = i;
		sel = new int[M];
		comb(0, 0);
		
	}
	
	public static void comb(int idx, int selIdx) {
		if(selIdx == M) {
			for(int s : sel)
				System.out.print(s+" ");
			System.out.println();
			return;
		} else if(idx == N)
			return;
		
		sel[selIdx] = nums[idx];
		comb(idx+1, selIdx+1);
		comb(idx+1, selIdx);
	}
}