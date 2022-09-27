import java.util.Scanner;

public class Main {
	static int N, maxCnt;
	static int[][] map;
	static int[][] del = {{-1,0},{1,0},{0,-1},{0,1}};
	static boolean[][] visited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map = new int[N][N];
		maxCnt = 1;
		int maxH = 0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				map[i][j] = sc.nextInt();
				maxH = Math.max(maxH, map[i][j]);
			}
		}
		int cnt;
		for(int h=0; h<maxH; h++) {
			cnt = 0;
			visited = new boolean[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(map[i][j] > h && !visited[i][j]) {
						cnt++;
						dfs(i, j, h);
					}
				}
			}
			maxCnt = Math.max(maxCnt, cnt);
		}
		
		System.out.println(maxCnt);
	}
	
	static void dfs(int r, int c, int h) {
		visited[r][c] = true;
		for(int i=0; i<4; i++) {
			int di = r + del[i][0];
			int dj = c + del[i][1];
			
			if(di>=0 && di<N && dj>=0 && dj<N && map[di][dj] > h && !visited[di][dj]) {
				dfs(di, dj, h);
			}
		}
	}
}