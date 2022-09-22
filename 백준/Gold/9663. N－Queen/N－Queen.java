import java.util.Scanner;

public class Main {
	static int N, cnt;
	static int[] map;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map = new int[N];
		cnt = 0;
		putQueen(0);
		System.out.println(cnt);
		
	}
	
	static void putQueen(int row) {
		if(row == N) {
			cnt++;
			return;
		}
		
		for(int i=0; i<N; i++) {
			map[row] = i;
			if(isPossible(row, i))
				putQueen(row+1);
		}
	}
	
	static boolean isPossible(int row, int col) {
		for(int i=0; i<row; i++) {
			if(map[i] == col || Math.abs(row - i) == Math.abs(col - map[i]))
				return false;
		}
		return true;
	}
}