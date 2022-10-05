import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	static int V, E;
	static int[] inDegree;
	static List<Integer>[] edges;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int tc=1; tc<=10; tc++) {
			sb.append("#").append(tc);
			
			// V: 정점의 개수, E: 간선의 개수
			V = sc.nextInt();
			E = sc.nextInt();
			edges = new ArrayList[V+1];
			for(int i=1; i<=V; i++)
				edges[i] = new ArrayList<>();
			inDegree = new int[V+1];
			
			// 간선의 정보 입력
			for(int i=0; i<E; i++) {
				int st = sc.nextInt();
				int ed = sc.nextInt();
				edges[st].add(ed);
				inDegree[ed]++;
			}
			
			Queue<Integer> q = new LinkedList<>();
			// 우선 진입차수가 0인것들을 먼저 큐에 넣자
			for(int i=1; i<=V; i++) {
				if(inDegree[i] == 0)
					q.add(i);
			}
			
			//그 다음 큐를 돌면서 진행
			while(!q.isEmpty()) {
				int now = q.poll();
				sb.append(" ").append(now);
				
				for(int i=0; i<edges[now].size(); i++) {
					int tmp = edges[now].get(i);
					inDegree[tmp]--;
					if(inDegree[tmp] == 0)
						q.add(tmp);
				}
			}
			
			sb.append("\n");
		}
		
		System.out.println(sb);
	}
}