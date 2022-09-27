import java.util.Scanner;

public class Solution {
	static int N, X, cnt ,maxCnt;
	static int[][] cheese, arr;
	static int[][] del = {{-1,0},{1,0},{0,-1},{0,1}};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			N = sc.nextInt();       // N: 치즈 한변의 길이
			cheese = new int[N][N];
			X = 0; 
			maxCnt = 1; // ! 치즈는 무조건 한덩이부터 시작 !
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					cheese[i][j] = sc.nextInt();
					X = Math.max(X, cheese[i][j]); // 최대 맛있는 정도
				}
			}
			
			//2. 최대 맛있는 정도의 날까지만 치즈 덩어리를 세보자
			for(int i=1; i<X; i++) {
				int ch = eatCheese(i);
				
				// 만약 요정이 먹지 않았다면 날을 넘기자
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
				// 최대 덩어리의 개수 비교
				maxCnt = Math.max(maxCnt, cnt);
			}
			
			//3. 출력
			System.out.printf("#%d %d\n", tc, maxCnt);
			
			
			
		}// test
	}// main
	
	//요정이 날짜에 맞는 치즈를 먹음
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
	
	// 덩어리의 개수를 세기 위해 임시로 사용할 치즈 배열 복사
	static int[][] tmpArr(){
		int[][] tmp = new int[N][N];
		for(int i=0; i<N; i++) {
			tmp[i] = cheese[i].clone();
		}
		return tmp;
	}
	
	// 한 덩어리를 체크해줄 함수
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