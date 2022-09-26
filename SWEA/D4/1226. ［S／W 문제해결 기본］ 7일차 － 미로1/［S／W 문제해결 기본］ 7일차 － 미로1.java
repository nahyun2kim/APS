import java.util.Scanner;
import java.util.Stack;

public class Solution {
	static int si, sj;
	static boolean flag;
	static int[][] del = {{0,1},{1,0},{0,-1},{-1,0}};
	static char[][] maze;
	static boolean[][] visited;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int tc=1; tc<=10; tc++) {
			sc.nextInt(); // 테스트번호 입력받고 흘리기
			
			//1. 입력
			maze = new char[16][16];
			for(int i=0; i<16; i++) {
				String tmp = sc.next();
				for(int j=0; j<16; j++) {
					maze[i][j] = tmp.charAt(j);
					// 입력을 받으면서 출발지 미리 찾기
					if(maze[i][j] == '2') {
						si = i; sj = j;
					}
				}
			}
			visited = new boolean[16][16];
			flag = false;
			
			//2. 출발지부터 dfs 시작!
			dfs(si, sj);
			
			//3. 출력 
			//도착지를 찾았는 지 표시하는 flag가 true일 경우 1을 출력, 못찾았으면 0을 출력
			if (flag == true) {
				System.out.printf("#%d %d\n", tc, 1);
			}else {
				System.out.printf("#%d %d\n", tc, 0);
			}
			
			
		}// test
	}// main
	
	static void dfs(int si, int sj) {
		Stack st = new Stack();
		st.add(new int[] {si, sj});
		
		// 갈수 있는 길들을 다 스택에 넣고 스택이 빌때까지 진행
		while(!st.empty()) {
			int[] now = (int[]) st.pop();
			// 중간에 도착지를 찾으면 flag에 표시해두고 break
			if(maze[now[0]][now[1]] == '3') {
				flag = true;
				break;
			}
			visited[now[0]][now[1]] = true;
			// 상하좌우로 갈 수 있는 길이면 스택에 저장
			for(int i=0; i<4; i++) {
				int di = now[0] + del[i][0];
				int dj = now[1] + del[i][1];
				if(check(di, dj)) {
					st.add(new int[] {di, dj});
				}
			}
		}
	} 
	
	// 미로를 벗어나지 않고, 벽이아니며, 방문하지 않았는지 체크
	static boolean check(int i, int j) {
		if(i<0 || i>=16 || j<0 || j>=16)
			return false;
		if(maze[i][j] == '1' || visited[i][j] == true)
			return false;
		return true;
	}
}