import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] map = new int[100][100]; // x좌표와 y좌표는 모두 100이하인 정수
		int mini = 100;		
		int minj = 100;
		int maxi = 0;
		int maxj = 0;
		
		//1. 네 직사각형 입력받고 표시
		for(int t=0; t<4; t++) {
			int si = sc.nextInt();
			int sj = sc.nextInt(); // 왼쪽 아래 x,y
			int ei = sc.nextInt();
			int ej = sc.nextInt(); // 오른쪽 위 x,y
			for(int i=si; i<ei; i++) {
				for(int j=sj; j<ej; j++) {
					map[i][j] = 1;
				}
			}
			mini = Math.min(mini, si);
			minj = Math.min(minj, sj);
			maxi = Math.max(maxi, ei);
			maxj = Math.max(maxj, ej);
		}
		
		//2. 면적 계산
		int sum = 0;
		for(int i=mini; i<maxi; i++) {
			for(int j=minj; j<maxj; j++) {
				sum += map[i][j];
			}
		}
		
		//3. 출력
		System.out.println(sum);
	}
}