import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//1. 입력
		int N = sc.nextInt(); // N : 전체 날짜 수
		int K = sc.nextInt(); // K : 연속적인 날짜 수
		int[] temp = new int[N];
		
		//2. 처음 K일 동안은 더해서 sum을 구함
		int sum = 0;
		for(int i=0; i<K; i++) {
			temp[i] = sc.nextInt();
			sum += temp[i];
		}
		
		//3. K일 이후에는 젤 왼쪽날을 빼주고 오른쪽날을 더해주며 최대온도 비교
		int sumMax = sum;
		for(int i=K; i<N; i++) {
			temp[i] = sc.nextInt();
			sum = sum - temp[i-K] + temp[i];
			sumMax = Math.max(sumMax, sum);
		}
		
		//4. 출력
		System.out.println(sumMax);
	}
}