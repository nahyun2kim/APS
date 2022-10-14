import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {
	static int N, M, K;
	static int[][] map;
	static List<int[]> micro;
	static int[][] del = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }; // 상하좌우
	static int[] switchDir = { 1, 0, 3, 2 }; // 하상우좌

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt(); // 셀의 개수
			M = sc.nextInt(); // 격리 시간
			K = sc.nextInt(); // 미생물 군집의 수
			map = new int[N][N];
			micro = new ArrayList<>();
			
			for(int i=0; i<K; i++) {
				int r = sc.nextInt();
				int c = sc.nextInt();
				int n = sc.nextInt();
				int d = sc.nextInt()-1;
				map[r][c]++;
				micro.add(new int[] {r, c, n, d});
			}
			
			for(int t=0; t<M; t++) {
				move();
				sumMicro();
			}
			int ans = 0;
			for(int i=0; i<micro.size(); i++) {
				ans += micro.get(i)[2];
			}
			
			System.out.printf("#%d %d\n", tc, ans);
			
		} // tc

	}
	
	static void move() {
		for(int i=0; i<micro.size(); i++) {
			int di = micro.get(i)[0] + del[micro.get(i)[3]][0];
			int dj = micro.get(i)[1] + del[micro.get(i)[3]][1];
			map[micro.get(i)[0]][micro.get(i)[1]]--;
			map[di][dj]++;
			if(di == 0 || dj == 0 || di == N-1 || dj == N-1) {
				micro.get(i)[2] /= 2;
				micro.get(i)[3] = switchDir[micro.get(i)[3]];
			}
			micro.get(i)[0] = di;
			micro.get(i)[1] = dj;
		}
	}
	
	static void sumMicro() {
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				// 미생물이 여러 곳에 뭉쳤다면,,,!
				if(map[i][j] >1) {
					int[][] tmp = new int[map[i][j]][5];
					int idx=0;
					for(int k=0; k<micro.size(); k++) {
						if(micro.get(k)[0] == i && micro.get(k)[1] == j) {
							tmp[idx++] = new int[] {k, i, j, micro.get(k)[2], micro.get(k)[3]};
						}
					}
					int max = 0;
					int max_idx = 0;
					for(int k=0; k<map[i][j]; k++) {
						if (tmp[k][3] > max) {
							max = tmp[k][3];
							max_idx = k;
						}
					}
					for(int k=map[i][j]-1; k>=0; k--) {
						if(k != max_idx) {
							micro.get(tmp[max_idx][0])[2] += micro.get(tmp[k][0])[2];
						}
					}
					for(int k=map[i][j]-1; k>=0; k--) {
						if(k != max_idx) {
							micro.remove(tmp[k][0]);
						}
					}
					map[i][j] = 1;
				}
			}
		}
	}
}
