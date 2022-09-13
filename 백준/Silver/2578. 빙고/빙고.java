import java.util.Scanner;

public class Main {
	static int[][] arr;
	static int diag1, diag2;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//1. 빙고판 입력 & 지울 숫자들 입력
		arr = new int[6][6];
		for(int i=0; i<5; i++) {
			for(int j=0; j<5; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		int[] removeBingo = new int[25];
		for(int i=0; i<25; i++) {
			removeBingo[i] = sc.nextInt();
		}
		
		//2. 초기화해주고 removeBingo를 순회하며 빙고판 지우기
		diag1 = 0;
		diag2 = 0;
		cnt = 0;
		for(int i=0; i<25; i++) {
			cnt = checkBingo(removeBingo[i]);
			if(cnt >= 3) {
				System.out.println(i+1);
				break;
			}
			
		}
	}
	
	static int cnt;
	static int checkBingo(int num) {
		int idx = 0;
		while(idx<25) {
			if(arr[idx/5][idx%5] == num) {
				break;
			}
			idx++;
		}
		int row = idx/5;
		int col = idx%5;
		arr[row][5]++;
		if(arr[row][5] == 5)
			cnt++;
		arr[5][col]++;
		if(arr[5][col] == 5)
			cnt++;
		
		if(row == col) {
			diag1++;
			if(diag1 == 5) {
				cnt++;
			}
		} 
		if(row + col == 4) {
			diag2++;
			if(diag2 == 5) {
				cnt++;
			}
		}
		
		return cnt;
	}
}