import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	
	static class Room implements Comparable<Room>{
		private int rNum, sNum, dist;

		public Room(int rNum, int sNum, int dist) {
			this.rNum = rNum;
			this.sNum = sNum;
			this.dist = dist;
		}

		@Override
		public int compareTo(Room o) {
			return this.dist - o.dist;
		}
		
	}
	
	static int N, peo, minAns;
	static int[] stair;
	static boolean[] visit;
	static Room[] room;
	static int[][] map;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			map = new int[N][N];
			peo = 0; minAns = Integer.MAX_VALUE;
			stair = new int[6];
			int s = 0;
			// 입력을 받으면서 사람 수를 세고, 계단의 좌표를 저장
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					map[i][j] = sc.nextInt();
					if(map[i][j] == 1)
						peo++;
					else if(map[i][j] > 1) {
						stair[s] = i;
						stair[s+1] = j;
						stair[s+2] = map[i][j];
						s += 3;
					}
				}
			}
			visit = new boolean[peo];
			int[][] nowSt = new int[3][3]; // 현재 계단이용 인원
			
			// 한번더 for문을 돌면서 방과 계단까지의 거리 저장
			// 방에는 번호를 부여
			room = new Room[peo*2];
			int idx = 0;
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(map[i][j] == 1) {
						room[idx] = new Room(idx, 1, roomToStair(1, i, j));
						room[idx+peo] = new Room(idx, 2, roomToStair(2, i, j));
						idx++;
					}
				}
			}
			
			// 방에서 계단까지 거리를 기준으로 sort
			Arrays.sort(room);
			// 거리 짧은 애부터 내려가라
			goDown(0, 0, nowSt);
			
			System.out.printf("#%d %d\n", tc, minAns);
			
		}// test
	}
	
	static void goDown(int idx, int sel, int[][] arr) {
		// 사람들이 다 내려갔으면 젤 늦게 도착하는 시간과 최종 minAns 비교
		if(sel == peo) {
			int maxMin = 0;
			for(int i=1; i<3; i++) {
				for(int j=0; j<3; j++) {
					if(arr[i][j] != 0) {
						maxMin = Math.max(maxMin, arr[i][j]);
					}
				}
			}
			minAns = Math.min(maxMin, minAns);
			return;
		}else if(idx == peo*2) return;
		
		// room 배열을 뽑아서
		Room rm = room[idx];
		// 아직 내려가지 않았을 때
		if(!visit[rm.rNum]) {
			visit[rm.rNum] = true;
			// 내려가거나
			goDown(idx+1, sel+1, downStair(rm.sNum, rm.dist, arr));
			// 다른 계단 이용하거나
			visit[rm.rNum] = false;
			goDown(idx+1, sel, arr);
		}else {
			// 이미 내려갔다면 다음 인덱스로 넘어가자
			goDown(idx+1, sel, arr);
		}
	}
	
	// 계단의 현재 상황을 입력하는 함수
	// sNum : 계단번호, min : 도착시간
	static int[][] downStair(int sNum, int min, int[][] arr) {
		int[][] tmpArr = new int[3][3];
		for(int i=1; i<3; i++)
			tmpArr[i] = arr[i].clone();
		int idx = -1;
		for(int i=0; i<3; i++) {
			if (tmpArr[sNum][i] <= min) {
				idx = i;
				break;
			} 
		}
		if(idx >= 0)
			tmpArr[sNum][idx] = min + 1 + stair[3*sNum - 1];
		else {
			int mini = 1000;
			for(int i=0; i<3; i++) {
				if(mini > tmpArr[sNum][i]) {
					idx = i;
					mini = tmpArr[sNum][i];
				}
			}
			tmpArr[sNum][idx] += stair[3*sNum - 1];
		}
		return tmpArr;
	}
	
	// 방과 계단 사이의 거리 계산
	static int roomToStair(int i, int x, int y) {
		int sNum = i;
		int sx1 = stair[0];
		int sy1 = stair[1];
		int sy2 = stair[4];
		int sx2 = stair[3];
		switch (sNum) {
		case 1:
			return Math.abs(sx1 - x) + Math.abs(sy1 - y);
			
		case 2:
			return Math.abs(sx2 - x) + Math.abs(sy2 - y);
		}
		return 0;
	}
}