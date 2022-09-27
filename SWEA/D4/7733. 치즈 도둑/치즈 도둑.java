import java.util.Scanner;

public class Solution {
	static int N, X, cnt ,maxCnt;
	static int[][] cheese, arr;
	static int[][] del = {{-1,0},{1,0},{0,-1},{0,1}};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			cheese = new int[N][N];
			X = 0; maxCnt = 1;
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					cheese[i][j] = sc.nextInt();
					X = Math.max(X, cheese[i][j]); // 최대 맛있는 정도
				}
			}
			
			for(int i=1; i<X; i++) {
				int ch = eatCheese(i);
				if (ch == 0)
					continue;
				arr = tmpArr();
				cnt = 0;
				for(int r=0; r<N; r++) {
					for(int c=0; c<N; c++) {
						if(arr[r][c] !=0) {
							cnt++;
							arr[r][c] = 0;
							check(r, c);
						}
					}
				}
				maxCnt = Math.max(maxCnt, cnt);
			}
			
			System.out.printf("#%d %d\n", tc, maxCnt);
			
			
			
		}// test
	}// main
	
	static int eatCheese(int day) {
		int count = 0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(cheese[i][j] == day) {
					cheese[i][j] = 0;
					count++;
				}
			}
		}
		return count;
	}
	
	static int[][] tmpArr(){
		int[][] tmp = new int[N][N];
		for(int i=0; i<N; i++) {
			tmp[i] = cheese[i].clone();
		}
		return tmp;
	}
	
	static void check(int r, int c) {
		for (int i=0; i<4; i++) {
			int di = r + del[i][0];
			int dj = c + del[i][1];
			
			if(di >=0 && di<N && dj>=0 && dj<N && arr[di][dj] != 0) {
				arr[di][dj] = 0;
				check(di, dj);
			}
		}
	}
}