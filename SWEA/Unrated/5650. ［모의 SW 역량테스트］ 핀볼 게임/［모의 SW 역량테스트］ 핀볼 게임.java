import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {
	static int N, maxCnt;
	static int[][] del = {{0, 0}, {-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static int[][] map;
	static Map<Integer, int[]> wormhole;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			map = new int[N][N];
			wormhole = new HashMap<>();
			maxCnt = 0;
			
			// 맵을 입력받으면서 웜홀의 위치 저장해두기
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					map[i][j] = sc.nextInt();
					if(map[i][j] > 5) {
						if(!wormhole.containsKey(map[i][j])) {
							int[] tmp = new int[4];
							tmp[0] = i; tmp[1] = j;
							wormhole.put(map[i][j], tmp);
						}else {
							wormhole.get(map[i][j])[2] = i;
							wormhole.get(map[i][j])[3] = j;
						}
					}
				}
			}
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					for(int d=1; d<5; d++) {
						if(map[i][j] == 0) {
							dfs(i, j, d);
						}
					}
				}
			}

			System.out.printf("#%d %d\n", tc, maxCnt);
			
			
			
			
		}// test
	}
	
	// r, c: 좌표
	// d : 진행방향 1~4 -> 상하좌우
	// flag : 벽을 만났는지 표시, 끝났는지
	
	static void dfs(int r, int c, int d) {
		int cnt = 0;
		boolean flag = false;
		int dir = d;
		int di = r + del[dir][0];
		int dj = c + del[dir][1];
		
		while(di>=0 && di<N && dj>=0 && dj<N) {
			if(di == r && dj == c) {
				maxCnt = Math.max(maxCnt, cnt);
				return;
			}
			// 블랙홀을 만났을 때 바로 지금까지의 cnt 비교
			if(map[di][dj] == -1) {
				maxCnt = Math.max(maxCnt, cnt);
				return;
			}
			// 웜홀 만났을 때
			if(map[di][dj] >5) {
				int[] tmp = findWormhole(di, dj, map[di][dj]);
				di = tmp[0] + del[dir][0];
				dj = tmp[1] + del[dir][1];
				continue;
			
			// 블록을 만났을 때
			}else if(map[di][dj] > 0) {
				cnt++;
				dir = changeDir[map[di][dj]][dir];
				// 막힌 블록을 만났으면 이제 그만 돌아
				if(dir == 0) {
					flag = true;
					break;
				}
			}
			di += del[dir][0];
			dj += del[dir][1];
		}
		
		// 벽을 만났을 때,
		if(di == -1 || di == N || dj == -1 || dj == N) {
			maxCnt = Math.max(maxCnt, 2*cnt + 1);
			return;
		}
		// 막힌 블록을 만났을 때,,
		if(flag) {
			maxCnt = Math.max(maxCnt, 2*cnt - 1);
			return;
		}
		
	}
	
	static int[] findWormhole(int i, int j, int value) {
		int[] pos = new int[2];
		int[] tmp = wormhole.get(value);
		if(tmp[0] == i && tmp[1] == j) {
			pos[0] = tmp[2];
			pos[1] = tmp[3];
		}else {
			pos[0] = tmp[0];
			pos[1] = tmp[1];
		}
		return pos;
	}
	
	// 행 : 만나는 블럭, 열 : 현재 진행방향
	static int[][] changeDir = 
				{{0,0,0,0,0},
				{0,0,4,1,0},
				{0,4,0,2,0},
				{0,3,0,0,2},
				{0,0,3,0,1},
				{0,0,0,0,0}};
}
