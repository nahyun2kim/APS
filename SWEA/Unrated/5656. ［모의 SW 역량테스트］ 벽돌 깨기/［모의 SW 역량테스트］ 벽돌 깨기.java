import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Solution {
	static int N, W, H, minAns;
	static int[][] map;
	static int[][] del = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			// 입력받기
			N = sc.nextInt(); // 떨어지는 구슬 개수
			W = sc.nextInt(); // 너비
			H = sc.nextInt(); // 높이
			map = new int[H][W];
			for(int i=0; i<H; i++) {
				for(int j=0; j<W; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			minAns = Integer.MAX_VALUE;
			
			perm(0, map);
			
			// 구슬을 다 떨어 뜨리기 전에 모든 벽돌이 터져 답을 비교하지 못한 경우 남은 벽돌의 수는 0
			if(minAns == Integer.MAX_VALUE)
				minAns = 0;
			
			System.out.printf("#%d %d\n", tc, minAns);
			
			
			
			
		}// test
	}
	
	static void perm(int idx, int[][] arr) {
		if (idx == N) {
			minAns = Math.min(minAns, cntBrick(arr));
			return;
		}
		
		int[][] tmp = new int[H][W];
		for(int i=0; i<H; i++) 
			tmp[i] = arr[i].clone();
		
		for(int i=0; i<W; i++) {
			int h = -1;
			for(int j=0; j<H; j++) {
				if(tmp[j][i] > 0) {
					h = j;
					break;
				}
			}
			if(h == -1) continue;
			
			perm(idx+1, breakBrick(tmp, h, i));
			
		}
		
		
	}
	
	static int[][] breakBrick(int[][] arr, int si, int sj) {
		int[][] tmpArr = new int[H][W];
		for(int i=0; i<H; i++) 
			tmpArr[i] = arr[i].clone();
		Stack<int[]> st = new Stack<>();
		st.add(new int[] {si, sj});
		while(!st.isEmpty()) {
			int[] now = st.pop();
			int range = tmpArr[now[0]][now[1]];
			
			tmpArr[now[0]][now[1]] = 0;
			for(int i=0; i<4; i++) {
				for(int r=1; r<range; r++) {
					int di = now[0] + del[i][0]*r;
					int dj = now[1] + del[i][1]*r;
					if(di>=0 && di<H && dj>=0 && dj<W && tmpArr[di][dj] != 0) {
						st.add(new int[] {di, dj});
					}
				}
			}
		}
		return downBrick(tmpArr);
	}
	
	static int[][] downBrick(int[][] arr) {
		int[][] tmpArr = new int[H][W];
		for(int i=0; i<H; i++) 
			tmpArr[i] = arr[i].clone();
		for(int i=0; i<W; i++) {
			while(true) {
				boolean flag = true;
				for(int j=H-1; j>0; j--) {
					if(tmpArr[j][i] == 0 && tmpArr[j-1][i] > 0) {
						flag = false;
						tmpArr[j][i] = tmpArr[j-1][i];
						tmpArr[j-1][i] = 0;
					}
				}
				if(flag)
					break;
			}
		}
		return tmpArr;
	}
	
	static int cntBrick(int[][] arr) {
		int cnt = 0;
		for(int i=0; i<H; i++) {
			for(int j=0; j<W; j++) {
				if(arr[i][j] > 0)
					cnt++;
			}
		}
		return cnt;
	}
}