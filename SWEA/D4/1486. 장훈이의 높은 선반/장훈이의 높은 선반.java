import java.util.Scanner;

public class Solution {
	static int N, B, minH;
	static int[] emp;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			N = sc.nextInt(); // N: 점원의 수
			B = sc.nextInt(); // B: 선반의 높이
			emp = new int[N];
			for(int i=0; i<N; i++)
				emp[i] = sc.nextInt();
			
			minH = 200000; // 초기화
			
			//2. 탑의 최소 높이 출력
			comb(0, 0);
			
			//3. 출력
			System.out.printf("#%d %d\n", tc, minH-B);
			
		}
	}
	
	// 직원의 조합을 구하자
	static void comb(int idx, int height) {
		// 선반의 높이 보다 높으면 최소 비교
		if(height >= B) {
			minH = Math.min(minH, height);
			return;
		} else if(idx == N) return;
		
		comb(idx+1, height+emp[idx]);
		comb(idx+1, height);
	}
}