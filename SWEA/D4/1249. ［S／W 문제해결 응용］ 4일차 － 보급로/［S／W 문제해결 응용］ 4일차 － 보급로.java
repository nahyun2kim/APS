import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Solution {
	static class Pos implements Comparable<Pos>{
		int i, j, value;

		public Pos(int i, int j, int value) {
			this.i = i;
			this.j = j;
			this.value = value;
		}

		@Override
		public int compareTo(Pos o) {
			return this.value - o.value;
		}
		
	}
	static int N;
	static final int INF = Integer.MAX_VALUE;
	static int[][] map, dp;
	static int[][] del = {{0,1},{1,0},{0,-1},{-1,0}}; // 우하좌상(시계방향)
	static boolean[][] visit;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			map = new int[N][N];
			for(int i=0; i<N; i++) {
				String num = sc.next();
				for(int j=0; j<N; j++) {
					map[i][j] = num.charAt(j) - '0';
				}
			}
			
			visit = new boolean[N][N];

			dp = new int[N][N];
			for(int i=0; i<N; i++) {
				Arrays.fill(dp[i], INF);
			}
			// 시작점은 0으로 만들어줘..
			dp[0][0] = 0;
			
			fillDP(0, 0);
			
			System.out.printf("#%d %d\n", tc, dp[N-1][N-1]);
			
		}// test
	}
	
	static void fillDP(int sx, int sy) {
		PriorityQueue<Pos> pq = new PriorityQueue<>();
		pq.add(new Pos(sx, sy, dp[sx][sy]));
		while(!pq.isEmpty()) {
			Pos now = pq.poll();
			if(visit[now.i][now.j]) continue;
			// 방문 체크
			visit[now.i][now.j] = true;
			
			// 4방향 다 살펴보자
			for(int d=0; d<4; d++) {
				int di = now.i + del[d][0];
				int dj = now.j + del[d][1];
				// 방문하지 않고, 범위안에 들어올 때
				if(di>=0 && di<N && dj>=0 && dj<N && !visit[di][dj]) {
					// 더 짧은 경로가 있다면 갱신하고, 큐에 넣어주자
					if(dp[di][dj] > dp[now.i][now.j] + map[di][dj]) {
						dp[di][dj] = dp[now.i][now.j] + map[di][dj];
						pq.add(new Pos(di, dj, dp[di][dj]));
					}
				}
			}
		}
	}
}