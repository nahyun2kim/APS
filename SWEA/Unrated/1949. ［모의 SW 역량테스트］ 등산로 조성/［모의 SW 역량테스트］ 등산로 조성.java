import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {
	static int N, K, maxCnt;
	static int[][] trail;
	static int[][] del = {{-1,0},{1,0},{0,-1},{0,1}};
	static boolean[][] visit;
	static List<int[]> pos;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			N = sc.nextInt(); // N : 한변의 길이
			K = sc.nextInt(); // K : 최대 공사 가능 깊이
			int maxH = 0; maxCnt = 0; // 최대 봉우리와 산책로 최대 길이
			trail = new int[N][N];
			visit = new boolean[N][N];
			pos = new ArrayList<>();
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					trail[i][j] = sc.nextInt();
					maxH = Math.max(maxH, trail[i][j]);
				}
			}
			
			//2. 입력받으면서 구한 최대 높이의 봉우리들의 좌표를 pos list에 저장
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(trail[i][j] == maxH) {
						pos.add(new int[] {i, j});
					}
				}
			}
			
			//3. 최대 봉우리로부터 산책로를 시작하자
			for(int i=0; i<pos.size(); i++) {
				visit[pos.get(i)[0]][pos.get(i)[1]] = true;
				dfs(pos.get(i)[0], pos.get(i)[1], false, 1);
				visit[pos.get(i)[0]][pos.get(i)[1]] = false;
			}
			
			//4. 출력
			System.out.printf("#%d %d\n", tc, maxCnt);
		}
	}
	
	// 현재 좌표(i, j)와 이미 깎았다는 표시를 해줄 flag, 산책로의 길이 cnt
	static void dfs(int r, int c, boolean flag, int cnt) {
		maxCnt = Math.max(maxCnt, cnt);
		for(int i=0; i<4; i++) {
			int di = r + del[i][0];
			int dj = c + del[i][1];
			
			// 맵을 벗어나지 않고 이미 방문하지 않았다면,,
			if(di>=0 && di<N && dj>=0 && dj<N && !visit[di][dj]) {
				// 현재 높이보다 작다면 방문체크하고 dfs
				if(trail[di][dj] < trail[r][c]) {
					visit[di][dj] = true;
					dfs(di, dj, flag, cnt+1);
					visit[di][dj] = false;
				}
				// 현재 높이보다 크지만 아직 깎은적이 없고, 깎아서 작은 높이를 만들 수 있다면,,
				else if(!flag && trail[di][dj] - K < trail[r][c]) {
					visit[di][dj] = true;
					int tmp = trail[di][dj];
					// 높이를 현재 높이-1로 잠시 바꿔줬다가, dfs끝나면 원상복귀
					trail[di][dj] = trail[r][c] - 1;
					dfs(di, dj, true, cnt+1);
					trail[di][dj] = tmp;
					visit[di][dj] = false;
				}
			}
		}
	}
}