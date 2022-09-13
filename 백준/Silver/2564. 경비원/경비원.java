import java.util.Scanner;

public class Main {
	static int row, col;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		row = sc.nextInt();
		col = sc.nextInt();
		int N = sc.nextInt();
		int[] shop = new int[N];
		for(int i=0; i<N; i++) {
			int dir = sc.nextInt();
			int pos = sc.nextInt();
			shop[i] = findDistance(dir, pos);
		}
		
		int dd = sc.nextInt();
		int dp = sc.nextInt();
		int subDis = findDistance(dd, dp);
		
		int round = 2*(row+col);
		int sum = 0;
		for(int i=0; i<N; i++) {
			int diff = Math.abs(shop[i]-subDis);
			if(diff > row+col)
				diff = round-diff;
			sum += diff;
		}
		
		System.out.println(sum);
		
	}
	
	static int findDistance(int dir, int dis) {
		switch(dir) {
		case 1:
			return dis;
		case 4:
			return row + dis;
		case 2:
			return 2*row + col - dis;
		case 3:
			return 2*row + 2*col - dis;
		}
		return 0;
	}
}