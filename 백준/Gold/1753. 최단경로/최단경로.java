import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int V, E;
	static final int INF = Integer.MAX_VALUE;
	static int[] d;
	static boolean[] visit;
	static List<int[]>[] list;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		V = sc.nextInt();
		E = sc.nextInt();
		int st = sc.nextInt();
		list = new ArrayList[V+1];
		for(int i=1; i<=V; i++)
			list[i] = new ArrayList<>();
		
		for(int i=0; i<E; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int w = sc.nextInt();
			list[u].add(new int[] {v, w});
		}
		
		visit = new boolean[V+1];
		d = new int[V+1];
		Arrays.fill(d, INF);
		
		dijkstra(st);
		
		for(int i=1; i<=V; i++) {
			if(d[i] == INF)
				System.out.println("INF");
			else
				System.out.println(d[i]);
		}
	}
	
	static int findSmallIdx() {
		int min = INF;
		int idx = 0;
		for(int i=1; i<=V; i++) {
			if(!visit[i] && min > d[i]) {
				min = d[i];
				idx = i;
			}
		}
		return idx;
	}
	
	static void dijkstra(int st) {
		d[st] = 0;
		for(int i=0; i<V-1; i++) {
			int idx = findSmallIdx();
			if(idx == 0) break;
			
			visit[idx] = true; // 방문처리
			
			// 방문저리 후 갱신 시작
			for(int j=0; j<list[idx].size(); j++) {
				int v = list[idx].get(j)[0];
				int w = list[idx].get(j)[1];
				
				// 방문하지 않았고, 시작부터  v 까지 가는데 idx를 거쳐 가는게 더 빠르다면 갱신하자
				if(!visit[v] && d[v] > d[idx] + w)
					d[v] = d[idx] + w;
			}
		}
	}
}