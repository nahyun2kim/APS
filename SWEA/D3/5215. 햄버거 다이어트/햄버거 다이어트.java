import java.util.Scanner;

class Solution
{
	static int N, L;
	static int maxScore;
	static int[][] burger;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//0. 테스트케이스 입력
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			N = sc.nextInt(); // N : 재료의 수
			L = sc.nextInt(); // L : 제한 칼로리
			
			burger = new int[N][2];
			for(int i=0; i<N; i++) {
				burger[i][0] = sc.nextInt();
				burger[i][1] = sc.nextInt();
			}
			
			//2. 부분 수열을 돌며 점수의 최댓값 구하기
			maxScore = 0;
			make(0, 0, 0);
			
			//3. 출력
			System.out.printf("#%d %d\n", tc, maxScore);
		}
	}
	
	static void make(int idx, int score, int cal) {
		
		// 제한 칼로리를 넘으면 바로 return
		if (cal > L) {
			return;
			
		// 부분 수열을 다 만들었으면 점수를 비교하고 return
		}else if (idx == N) {
			maxScore = Math.max(maxScore, score);
			return;
		}
		
		// 이 재료를 포함하지 않고 넘길지, 포함하고 넘길지,,, 
		make(idx+1, score, cal);
		make(idx+1, score+burger[idx][0], cal+burger[idx][1]);
	}
}