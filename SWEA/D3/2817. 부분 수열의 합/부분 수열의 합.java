import java.util.Scanner;

class Solution
{
	static int N, K, cnt;
	static int[] arr;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			K = sc.nextInt();
			cnt = 0;
			arr = new int[N];
			for(int i=0; i<N; i++)
				arr[i] = sc.nextInt();
			
			subSeq(0, 0);
			System.out.printf("#%d %d\n", tc, cnt);
		}
	}
	
	static void subSeq(int idx, int sum) {
		if (idx == N) {
			if (sum == K)
				cnt++;
			return;
		}
		
		subSeq(idx+1, sum);
		subSeq(idx+1, sum+arr[idx]);
	}
}