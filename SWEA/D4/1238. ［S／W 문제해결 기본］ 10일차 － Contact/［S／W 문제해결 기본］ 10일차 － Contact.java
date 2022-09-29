import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	static int end;
	static int[] check;
	static boolean[] visit;
	static List<Integer>[] contact;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int tc=1; tc<=10; tc++) {
			// N: 입력받는 연락 데이터 길이
			int N = sc.nextInt();
			// st: 시작점
			int st = sc.nextInt();
			
			contact = new ArrayList[101];
			for(int i=0; i<101; i++)
				contact[i] = new ArrayList<>();
			// 연락망을 입력받기
			for(int i=0; i<N/2; i++) {
				int from = sc.nextInt();
				int to = sc.nextInt();
				contact[from].add(to);
			}
			// 방문체크
			visit = new boolean[101];
			// 몇번째로 연락받았는지 입력
			check = new int[101];
			// 시작점을 첫번째로 설정
			check[st] = 1;
			// 마지막 연락이 몇번째인지 저장해 둘 변수
			end = 0;
			
			// 연락시작
			call(st);
			
			// 마지막 연락 받은 사람 중 최대 번호를 찾자
			int ans = 0;
			for(int i=1; i<101; i++) {
				if(check[i] == end)
					ans = Math.max(ans, i);
			}
			System.out.printf("#%d %d\n", tc, ans);
			
		}// test
	}
	
	static void call(int x) {
		visit[x] = true;
		Queue<Integer> q = new LinkedList<>();
		q.add(x);
		
		// 큐가 다 빌 때까지 진행
		while(!q.isEmpty()) {
			int now = q.poll();
			int num = check[now]+1;
			
			if(contact[now].size() == 0)
				continue;
			
			// 더 연락을 돌일 애가 있으면 방문처리하고 큐에 넣고 몇번째 연락인지 기록
			for(int i=0; i<contact[now].size(); i++) {
				int n = contact[now].get(i);
				if(!visit[n]) {
					visit[n] = true;
					q.add(n);
					check[n] = num;
					end = Math.max(end, num);
				}
			}
		}
	}
}