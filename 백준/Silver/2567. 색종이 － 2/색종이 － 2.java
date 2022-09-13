import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//1. 입력- 색종이의 수
		int N = sc.nextInt();
		int[][] paper = new int[102][102];
		for(int i=0; i<N; i++) {
			
			//2. 입력 - 색종이의 위치
			int row = sc.nextInt();
			int col = sc.nextInt();
			for(int j=row; j<row+10; j++) {
				for(int k=col; k<col+10; k++) {
					// 색종이의 위치에 있는 곳은 값을 1로 바꿔줌
					paper[j][k] = 1;
				}
			}
		}
		//3. 주변이 0이면 그부분은 둘레에 해당
		int cnt = 0;
		for(int i=1; i<101; i++) {
			for(int j=1; j<101; j++) {
				if(paper[i][j]==1) {
					if(paper[i+1][j] == 0)
						cnt++;
					if(paper[i-1][j] == 0)
						cnt++;
					if(paper[i][j+1] == 0)
						cnt++;
					if(paper[i][j-1] == 0)
						cnt++;
				}
			}
		}
		
		//4. 출력
		System.out.println(cnt);
	}
}