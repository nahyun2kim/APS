import java.util.Scanner;

public class Solution {
	static int minCost;
	static int[] voucher = new int[4]; 
	static int[] month = new int[12];
	static boolean[] check;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			for(int i=0; i<4; i++)
				voucher[i] = sc.nextInt();
			for(int i=0; i<12; i++)
				month[i] = sc.nextInt();
			
			minCost = voucher[3]; // 초기 최솟값을 연간 이용권으로 설정
			
			check = new boolean[12];
			voucherPerchase(0, 0);
			
			System.out.printf("#%d %d\n", tc, minCost);
			
		}// test
	}// main
	
	static void voucherPerchase(int mon, int cost) {
		if(mon == 12) {
			minCost = Math.min(minCost, cost);
			return;
		}
		if(cost >= minCost)
			return;
		
		for(int i=0; i<3; i++) {
			if (i == 0) {
				check[mon] = true;
				voucherPerchase(mon+1, cost+voucher[i]*month[mon]);
				check[mon] = false;
			}else if(i == 1) {
				check[mon] = true;
				voucherPerchase(mon+1, cost+voucher[i]);
				check[mon] = false;
			}else {
				for(int m=mon; m<mon+3 && m<12; m++)
					check[mon] = true;
				int nm = mon+3;
				if (nm > 12)
					nm = 12;
				voucherPerchase(nm, cost+voucher[i]);
				for(int m=mon; m<mon+3 && m<12; m++)
					check[mon] = false;
			
			}
		}
	}
}