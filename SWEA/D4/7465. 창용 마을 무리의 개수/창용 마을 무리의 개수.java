import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	static int N, M;
	static List<Integer>[] peo;
	static boolean[] check;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			// N: 마을 사람 수 , M: 서로의 관계 수
			N = sc.nextInt();
			M = sc.nextInt();
			peo = new ArrayList[N+1];
			for(int i=1; i<N+1; i++) 
				peo[i] = new ArrayList<>();
			// 입력받기
			for(int i=0; i<M; i++) {
				int p1 = sc.nextInt();
				int p2 = sc.nextInt();
				peo[p1].add(p2);
				peo[p2].add(p1);
			}
			
			check = new boolean[N+1];
			int ans = 0; // 무리의 수
			
			// 무리의 수를 세자
			for(int i=1; i<N+1; i++) {
				if(!check[i]) {
					bfs(i);
					ans++;
				}
			}
			
			System.out.printf("#%d %d\n", tc, ans);
		}
		
		
	}
	
	static void bfs(int x) {
		check[x] = true;
		Queue<Integer> q = new LinkedList<>();
		q.add(x);
		while(!q.isEmpty()) {
			int now = q.poll();
			for(int i=0; i<peo[now].size(); i++) {
				int next = peo[now].get(i);
				if(!check[next]) {
					check[next] = true;
					q.add(next);
				}
			}
		}
	}
}