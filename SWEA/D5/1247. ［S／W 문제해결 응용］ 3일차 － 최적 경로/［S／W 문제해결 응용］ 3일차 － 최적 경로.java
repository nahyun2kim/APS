import java.util.Scanner;

class Solution
{
	static int N, minDis;
	static int[] comp, home;
	static int[][] cus;
	static boolean[] check;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//0. 테스트 케이스 입력
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			N = sc.nextInt();
			comp = new int[2]; home = new int[2];
			cus = new int[N][2];
			check = new boolean[N];
			for(int i=0; i<2; i++) {
				comp[i] = sc.nextInt();
			}
			for(int i=0; i<2; i++) {
				home[i] = sc.nextInt();
			}
			for(int i=0; i<N; i++) {
				cus[i][0] = sc.nextInt();
				cus[i][1] = sc.nextInt();
			}
			minDis = Integer.MAX_VALUE;
			
			//2. 방문 시작
			findDis(0, 0, -1);
			
			//3. 출력
			System.out.printf("#%d %d\n", tc, minDis);
		}
	}
	
	// 순열으로 집의 방문 순서를 구할건데,, 중간에 dis가 minDis보다 많으면 멈추고
	// 집을 다 방문하면 집까지 도착거리를 구한 후 최소를 비교하자
	static void findDis(int idx, int dis, int sel) {
		if(idx == N) {
			dis += calDis(sel, -1);
			minDis = Math.min(minDis, dis);
			return;
		}
		if(dis > minDis)
			return;
		for(int i=0; i<N; i++) {
			if(check[i] == false) {
				check[i] = true;
				findDis(idx+1, dis+calDis(sel, i), i);
				check[i] = false;
			}
		}
	}
	
	// 두 곳 사이의 거리 구하기
	// sel이 -1일때는 회사 출발의 의미, i가 -1일때는 집 도착의 의미
	static int calDis(int sel, int i) {
		int selx, sely, x, y;
		if(sel == -1) {
			selx = comp[0];
			sely = comp[1];
		}else {
			selx = cus[sel][0];
			sely = cus[sel][1];
		}
		if(i == -1) {
			x = home[0];
			y = home[1];
		}else {
			x = cus[i][0];
			y = cus[i][1];
		}
		
		return Math.abs(selx - x)+Math.abs(sely - y);
	}
}