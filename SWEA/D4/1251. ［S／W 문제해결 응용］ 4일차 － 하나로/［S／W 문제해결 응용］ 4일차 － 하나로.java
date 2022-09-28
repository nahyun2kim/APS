import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Solution {
	static int N;
	static double E;
	static int[] p;
	static int[][] island;
	static double[][] edges;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			// 섬의 좌표를 저장
			island = new int[N][2];
			for(int j=0; j<2; j++) {
				for(int i=0; i<N; i++) {
					island[i][j] = sc.nextInt();
				}
			}
			E = sc.nextDouble();
			// 임의로 간선들을 생성함
			edges = new double[N*(N-1)/2][3];
			int idx = 0;
			for(int i=0; i<N; i++) {
				for(int j=i+1; j<N; j++) {
					edges[idx][0] = i;
					edges[idx][1] = j;
					edges[idx++][2] = calLength(i, j);
				}
			}
			
			Arrays.sort(edges, new Comparator<double[]>() {
				@Override
				public int compare(double[] o1, double[] o2) {
					if (o1[2] > o2[2]) return 1;
					else if(o1[2] < o2[2]) return -1;
					return 0;
				}
			});
			
//			for(double[] d : edges)
//				System.out.println(Arrays.toString(d));
			
			// 대표자를 저장할 p 배열 생성
			p = new int[N];
			// makeSet과정 진행
			for(int i=0; i<N; i++) {
				p[i] = i;
			}
			// 정렬된 간선들을 뽑아보자 N-1만큼!
			int pick = 0;
			double ans = 0;
			for(int i=0; i<edges.length; i++) {
				int st = findSet((int)edges[i][0]);
				int ed = findSet((int)edges[i][1]);
				if(p[st] != p[ed]) {
					union(st, ed);
					ans += edges[i][2];
					pick++;
				}
				
				if(pick == N-1) break;
			}
			
			System.out.printf("#%d %d\n", tc, Math.round(ans));
			
		}
	}
	
	static double calLength(int a, int b) {
		int ax = island[a][0];
		int ay = island[a][1];
		int bx = island[b][0];
		int by = island[b][1];
		return (Math.pow((ax-bx), 2) + Math.pow((ay-by), 2))*E;
	}
	
	static int findSet(int x) {
		if(p[x] != x) {
			p[x] = findSet(p[x]);
		}
		return p[x];
	}
	
	static void union(int x, int y) {
		p[findSet(y)] = findSet(x);
	}
}