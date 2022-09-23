import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {
	static int N, maxDis, sx, sy;
	// 방향은 왼쪽아래, 오른쪽아래, 오른쪽위, 왼쪽위로 사각형을 만들 계획,,
	static int[][] delta = {{1,-1}, {1, 1}, {-1, 1}, {-1, -1}};
	static int[][] map;
	static List<Integer> list;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			sb.append('#').append(tc).append(' ');
			
			N = sc.nextInt(); // 한변의 길이
			map = new int[N][N];
			for(int i=0; i<N*N; i++)
				map[i/N][i%N] = sc.nextInt();
			maxDis = 0;
			
			for(int i=0; i<N-2; i++) {
				for(int j=1; j<N-1; j++) {
					// 출발지에 따라 리스트 리셋해주고 첫 출발지의 정보 넣어주기
					list = new ArrayList<>();
					list.add(map[i][j]);
					sx = i; sy = j;
					dfs(i, j, 0, 0);
				}
			}
			// 최댓값이 0이라면 만들 수 있는 사각형이 없다는 의미, -1출력
			if(maxDis == 0)
				sb.append(-1).append('\n');
			else
				sb.append(maxDis).append('\n');
		}
		System.out.println(sb);
	}
	
	static void dfs(int x, int y, int didx, int cnt) {
		// 사각형을 돌아 출발지에 도착했다면, 최댓값 비교
		if(x == sx && y == sy && cnt>0) {
			maxDis = Math.max(maxDis, cnt);
			return;
		}
		
		// 내가 온방향으로 계속 가거나 아니면 방향을 한번 꺾거나 할 수 있음
		for(int i=didx; i<=didx+1 && i<4; i++) {
			if(check(x+delta[i][0], y+delta[i][1])) {
				list.add(map[x+delta[i][0]][y+delta[i][1]]);
				dfs(x+delta[i][0], y+delta[i][1], i, cnt+1);
				list.remove(list.size()-1);
			}
		}
		
		
	}
	
	// 다음 지점으로 갈 수 있는지 확인
	static boolean check(int row, int col) {
		// 다시 돌아돌아 출발지로 왔다면 true
		if(row == sx && col == sy)
			return true;
		// 맵을 벗어난다면 false
		if(row<0 || row>=N || col<0 || col>=N)
			return false;
		// 이미 방문한 디저트의 숫자와 같다면 false
		if(list.contains(map[row][col])) {
			return false;
		}
		return true;
	}
}