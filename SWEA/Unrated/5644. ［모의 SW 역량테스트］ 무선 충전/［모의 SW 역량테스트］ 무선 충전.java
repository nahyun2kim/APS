import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Solution {
	static int A, ans;
	static int[][] map, bc;
	static int[][] del = {{0,0},{0,-1},{1,0},{0,1},{-1,0}}; // 상우하좌
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int M = sc.nextInt(); // 이동 시간
			A = sc.nextInt(); // BC 개수
			
			// 이동 정보 입력
			int[] user1 = new int[M+1];
			int[] user2 = new int[M+1];
			for(int i=1; i<=M; i++)
				user1[i] = sc.nextInt();
			for(int i=1; i<=M; i++)
				user2[i] = sc.nextInt();
			
			// 충전기 정보 입력
			bc = new int[A][4];
			for(int i=0; i<A; i++) {
				for(int j=0; j<4; j++) {
					bc[i][j] = sc.nextInt();
				}
			}
			
			// 성능으로 내림차순 sort
			Arrays.sort(bc, new Comparator<int[]>(){

				@Override
				public int compare(int[] o1, int[] o2) {
					return o2[3] - o1[3];
				}
			});
			
			// map에 어떤 충전기들이 있는지 표시
			map = new int[11][11];
			for(int b=0; b<A; b++) {
				BCinfo(bc[b][0], bc[b][1], bc[b][2], b);
			}
			boolean[] using = new boolean[A];
			
			ans = 0;
			
			// M초 동안 이동할건데....
			int u1x=1, u1y = 1;
			int u2x = 10, u2y = 10;
			for(int i=0; i<=M; i++) {
				u1x += del[user1[i]][0];
				u1y += del[user1[i]][1];
				u2x += del[user2[i]][0];
				u2y += del[user2[i]][1];
				
				int flag1 = -1, flag2 = -2;
				for(int j=0; j<A; j++) {
					if((map[u1x][u1y] & (1<<j))>0) {
						if(flag1 == flag2) { // 만약에 같은 공유기를 사용하고 있는데, 내가 다른 공유기를 사용할 수 있으면,,
							using[j] = true;
							break;
						}
						if(flag1 < 0) { // 아직 공유기 사용 안했으면,,
							flag1 = j;
							using[j] = true;
						}
					}
					if((map[u2x][u2y] & (1<<j))>0) {
						if(flag1 == flag2) {
							using[j] = true;
							break;
						}
						if(flag2 < 0) {
							flag2 = j;
							using[j] = true;
						}
					}
				}
				
				// 충전 성능을 ans에 더해줘
				for(int j=0; j<A; j++) {
					if(using[j])
						ans += bc[j][3];
				}
				Arrays.fill(using, false);
			}
			System.out.printf("#%d %d\n", tc, ans);
			
			
		}// test
	}
	// x,y : bc좌표, r: bc범위, k: 몇번째 bc인지
	static void BCinfo(int x, int y, int r, int k) {
		for(int i=x-r; i<=x+r; i++) {
			for(int j=y-r; j<=y+r; j++) {
				if(i>0 && i<11 && j>0 && j<11 && (Math.abs(i-x)+Math.abs(j-y))<=r) {
					map[i][j] = map[i][j] | (1<<k);
				}	
			}
		}
	}
}