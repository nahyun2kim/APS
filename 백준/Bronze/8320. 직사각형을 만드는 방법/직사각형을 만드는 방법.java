import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//1. 입력
		int N = sc.nextInt(); // N : 넓이가 1인 정사각형 수
		
		//2. 카운트(가로*세로가 정사각형의 수를 넘지않을때까지)
		int cnt = 0;
		for(int i=1; i<=N; i++) {
			for(int j=i; i*j<=N; j++) {
				cnt++;
			}
		}
		
		//3. 출력
		System.out.println(cnt);
	}
}