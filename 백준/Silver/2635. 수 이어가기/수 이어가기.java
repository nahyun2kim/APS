import java.util.Scanner;

public class Main {
	static int N;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//1. 입력
		N = sc.nextInt(); // 첫번째 수
		
		//2. 두번째 수를 N보다 작은 수로 다 해보자
		int max = 0;
		int second = 0;
		for(int i=0; i<=N; i++) {
			if(max < maxCnt(i)) {
				max = maxCnt(i);
				second = i;
			}
		}
		
		//3. 구한 두번째 값으로 출력
		System.out.println(max);
		System.out.print(N+" ");
		int curr = N;
		int next = second;
		while(next >=0) {
			System.out.print(next+" ");
			int temp = next;
			next = curr - next;
			curr = temp;
		}
	}
	
	static int maxCnt(int num) {
		int next = N - num;
		int cnt = 2;
		while(next>=0) {
			cnt++;
			int temp = next;
			next = num-next; 
			num = temp;
		}
		return cnt;
	}
}