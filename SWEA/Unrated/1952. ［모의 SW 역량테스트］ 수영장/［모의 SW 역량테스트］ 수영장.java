import java.util.Scanner;

// check 필요없는데 왜했지...?
public class Solution {
	static int minCost;
	static int[] voucher = new int[4]; 
	static int[] month = new int[12];
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			for(int i=0; i<4; i++)
				voucher[i] = sc.nextInt();
			for(int i=0; i<12; i++)
				month[i] = sc.nextInt();
			
			minCost = voucher[3]; // 초기 최솟값을 연간 이용권으로 설정
			
			//2. 구매시작하자
			voucherPerchase(0, 0);
			
			//3. 출력
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
		
		// i=0이면 일일이용권, i=1이면 1개월이용권, i=2이면 3개월이용권
		for(int i=0; i<3; i++) {
			if (i == 0) {
				voucherPerchase(mon+1, cost+voucher[i]*month[mon]);
			}else if(i == 1) {
				voucherPerchase(mon+1, cost+voucher[i]);
			}else {
				int nm = mon+3;
				if (nm > 12)  // 달을 초과했다면 12월까지만 적용
					nm = 12;
				voucherPerchase(nm, cost+voucher[i]);
			}
		}
	}
}