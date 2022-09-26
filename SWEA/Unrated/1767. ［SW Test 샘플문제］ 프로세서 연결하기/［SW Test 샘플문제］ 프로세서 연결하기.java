import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {
	static int N, C, maxCnt, minLen;
	static int[] sel;
	static int[][] processor;
	static int[][] del = {{-1,0},{1,0},{0,-1},{0,1}};
	static List<int[]> core;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			processor = new int[N][N];
			core = new ArrayList<>();
			for(int i=0; i<N*N; i++) {
				processor[i/N][i%N] = sc.nextInt();
				if (processor[i/N][i%N] == 1 && i/N != 0 && i/N != N-1 && i%N != 0 && i%N != N-1) {
					int[] tmp = new int[] {i/N, i%N};
					core.add(tmp);
				}
			}
			maxCnt = 0;
			minLen = Integer.MAX_VALUE;
			C = core.size();
			sel = new int[C];
		
			perm(0);
			System.out.printf("#%d %d\n", tc, minLen);
			
		}
	}
	
	public static void perm(int idx) {
		if(idx == C) {
			int[] res = wire();
			if (maxCnt < res[0]) {
				maxCnt = res[0];
				minLen = res[1];
			}else if(maxCnt == res[0]) {
				minLen = Math.min(minLen, res[1]);
			}
			return;
		}
		boolean flag = false;
		for(int d=0; d<4; d++) {
			
			if(check(core.get(idx)[0], core.get(idx)[1], d, processor)) {
				flag = true;
				sel[idx] = d;
				perm(idx+1);
			}
		}
		if(!flag) {
			sel[idx] = -1;
			perm(idx+1);
		}
	}
	
	public static int[] wire() {
		int[][] temp = new int[N][N];
		for(int i=0; i<N; i++) {
			temp[i] = processor[i].clone();
		}
		int cnt = 0;
		int wireLen = 0;
		for(int i=0; i<C; i++) {
			if(sel[i] < 0)
				continue;
			int di = core.get(i)[0] + del[sel[i]][0];
			int dj = core.get(i)[1] + del[sel[i]][1];
			if(check(core.get(i)[0], core.get(i)[1], sel[i], temp)) {
				cnt++;
				while(di>=0 && di<N && dj>=0 && dj<N) {
					temp[di][dj] = 1;
					wireLen++;
				di += del[sel[i]][0];
				dj += del[sel[i]][1];
				}
			}else
				continue;
		}
		return new int[] {cnt, wireLen};
	}
	
	public static boolean check(int i, int j, int d, int[][] arr) {
		if (i==0 || i==N-1 || j==0 || j==N-1)
			return false;

		int di = i + del[d][0];
		int dj = j + del[d][1];
		while(di>=0 && di<N && dj>=0 && dj<N) {
			if(arr[di][dj] == 1)
				return false;
			di += del[d][0];
			dj += del[d][1];
		}
		return true;
	}
}