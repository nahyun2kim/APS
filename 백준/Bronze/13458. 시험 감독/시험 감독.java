import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] stuArr = new int[n];
		for(int i=0; i<n; i++) {
			stuArr[i] = sc.nextInt();
		}
		// 시험장 별 학생수 배열 입력받기
		int a = sc.nextInt(); // 총감독
		int b = sc.nextInt(); // 부감독
		
		long ans = 0;
		for(int i=0; i<n; i++) {
			stuArr[i] -= a;
            ans++;
            if(stuArr[i] > 0) {
				//학생 수가 총감독이 볼수있는 수보다 많다면,, 부감독 필요
				ans += stuArr[i]/b;
				if(stuArr[i]%b > 0) {
					ans++;
				}
			}
		}
		System.out.println(ans);
	}
}