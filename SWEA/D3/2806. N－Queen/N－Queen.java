import java.util.Scanner;

class Solution
{
	static int N, cnt;
	static int[][] chess; 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//0. 테스트케이스 입력
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			N = sc.nextInt();
			chess = new int[N][N];
			cnt = 0;
			
			//2. 퀸을 놓을 수 있는 경우의 수 계산
			putQueen(0);
			
			//3. 출력
			System.out.printf("#%d %d\n", tc, cnt);
			
			
			
		}
	}
	
	static void putQueen(int r) {
		// 체스판 끝까지 내려왔다면 cnt증가하고 return
		if (r == N) {
			cnt++;
			return;
		}
		
		for(int i=0; i<N; i++) {
			if(!check(r, i)) {
				continue;
			}
			
			chess[r][i] = 1;
			putQueen(r+1);
			chess[r][i] = 0;
		}
	}
	
	//대각선 왼쪽위, 오른쪽위, 위에 queen이 있는지 확인
	static boolean check(int r, int c) {
		int left = c;
		int right = c;
		
		while(r>=0) {
			if(chess[r][c] == 1)
				return false;
			if(left>=0 && chess[r][left] == 1)
				return false;
			if(right<N && chess[r][right] == 1)
				return false;
			r--;
			left--;
			right++;
		}
		return true;
	}
}