import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] paper = new int[100][100];
		for(int i=0; i<N; i++) {
			int row = sc.nextInt()-1;
			int col = sc.nextInt()-1;
			for(int j=row; j<row+10; j++) {
				for(int k=col; k<col+10; k++) {
					paper[j][k] = 1;
				}
			}
		}
		int sum = 0;
		for(int i=0; i<100; i++) {
			for(int j=0; j<100; j++) {
				sum += paper[i][j];
			}
		}
		
		System.out.println(sum);
	}
}
