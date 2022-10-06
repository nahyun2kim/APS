import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	static int N, M, L;
	static int[][] map;
	static int[][] del = {{1,0},{0,-1},{0,1},{-1,0}}; // 하 좌 우 상
	static boolean[][] visit;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt(); // 지하 세로 크기
			M = sc.nextInt(); // 지하 가로 크기
			int R = sc.nextInt(); // 맨홀 세로 위치
			int C = sc.nextInt(); // 맨홀 가로 위치
			L = sc.nextInt(); // 도망 소요 시간
			
			// 지하 맵 입력
			map = new int[N][M];
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			
			visit = new boolean[N][M];
			
			int ans = 0;
			
			// dfs나 bfs나 할건디........
			Queue<int[]> q = new LinkedList<>();
			q.add(new int[] {R, C, 1});
			visit[R][C] = true; // 미리 방문처리
			
			while(!q.isEmpty()) {
				int[] nowPos = q.poll();
				int nowTime = nowPos[2];
//				System.out.println(Arrays.toString(nowPos));
				if(nowTime > L) continue;
				ans++; // 탈주범이 있을 공간 +1
				int now = numToDir(map[nowPos[0]][nowPos[1]]); // 현재 터널 모양
				for(int d=0; d<4; d++) {
					if((1<<d & now) > 0) { // 내 터널 방향일때
						int di = nowPos[0] + del[d][0];
						int dj = nowPos[1] + del[d][1];
						if(di<0 || di>=N || dj<0 || dj>=M || visit[di][dj]) continue;
						int next = numToDir(map[di][dj]);
						if((1<<(3-d) & next) > 0) { // 다음 갈 터널모양과 이어지면
							visit[di][dj] = true; // 방문처리하고
							q.add(new int[] {di, dj, nowTime+1}); // 큐에 넣자
						}
					}
				}
			}
			System.out.printf("#%d %d\n", tc, ans);
			
		}// test
		
	}
	
	static int numToDir(int x){
		// 오른쪽부터 하 좌 우 상
		switch (x) {
		case 1:
			return Integer.parseInt("1111", 2);
		case 2:
			return Integer.parseInt("1001", 2);
		case 3:
			return Integer.parseInt("0110", 2);
		case 4:
			return Integer.parseInt("1100", 2);
		case 5:
			return Integer.parseInt("0101", 2);
		case 6:
			return Integer.parseInt("0011", 2);
		case 7:
			return Integer.parseInt("1010", 2);
		}
		return 0;
	}
}