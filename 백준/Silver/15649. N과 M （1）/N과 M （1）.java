import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] nums;
	static int[] sel;
	static boolean[] check;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//1. 입력
		N = sc.nextInt();
		M = sc.nextInt();
		
		nums = new int[N];
		for(int i=1; i<=N; i++)
			nums[i-1] = i;
		sel = new int[M];
		check = new boolean[N];
		
		//2. 순열 진행
		purmutation(0);
		System.out.println(sb);
		
	}

	private static void purmutation(int idx) {
		// 뽑을 개수 만큼 뽑았으면 출력
		if(idx == M) {
			for(int s : sel) {
				sb.append(s).append(' ');
			}
			sb.append('\n');
			return;
		}
		
		// 숫자를 돌면서 내가 안방문한 숫자면 들러서 sel에 넣어라
		for(int i=0; i<N; i++) {
			if(check[i] == false) {
				check[i] = true;
				sel[idx] = nums[i];
				purmutation(idx+1);
				check[i] = false;
			}
		}
	}
}