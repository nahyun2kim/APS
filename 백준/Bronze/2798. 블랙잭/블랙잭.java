import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//1. 입력
		int N = sc.nextInt(); // N : 카드의 개수
		int M = sc.nextInt(); // M : 목표 수
		int[] card = new int[N];
		for(int i=0; i<N; i++)
			card[i] = sc.nextInt();
		
		//2. 무식하게 다 돌면서 M을 넘지 않는 한에서 max값 찾기
		int max = 0;
		for(int i=0; i<N-2; i++) {
			for(int j=i+1; j<N-1; j++) {
				for(int k=j+1; k<N; k++) {
					int sum = card[i]+card[j]+card[k];
					if(sum <= M)
						max = Math.max(max, sum);
				}
			}
		}
		
		//3. 출력
		System.out.println(max);
	}
}