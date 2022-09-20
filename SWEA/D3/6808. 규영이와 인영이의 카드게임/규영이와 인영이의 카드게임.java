import java.util.Scanner;

class Solution
{
	static int[] ky, iy, iyCard;
	static int kwin, iwin;
	static boolean[] check;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			ky = new int[9];
			for(int i=0; i<9; i++)
				ky[i] = sc.nextInt();
			iy = selectCard();
			iyCard = new int[9];
			check = new boolean[9];
			kwin = 0; iwin = 0;
			permutation(0);
			
			System.out.printf("#%d %d %d\n", tc, kwin, iwin);
		}
	}
	
	static int[] selectCard() {
		int[] card = new int[19];
		for(int i=0; i<9; i++) {
			card[ky[i]]++;
		}
		int idx = 0;
		int[] iy = new int[9];
		for(int i=1; i<19; i++) {
			if(card[i] == 0)
				iy[idx++] = i;
		}
		return iy;
	}
	
	static int winOrLose(int[] iy) {
		int kScore = 0;
		int iScore = 0;
		for(int i=0; i<9; i++) {
			if(ky[i] > iy[i])
				kScore += ky[i] + iy[i];
			else if(ky[i] < iy[i])
				iScore += ky[i] + iy[i];
		}
		if(kScore > iScore)
			return 1;
		else if(kScore < iScore)
			return 2;
		return 0;
		
	}
	
	static void permutation(int idx) {
		if(idx == 9) {
			int win = winOrLose(iyCard);
			if(win == 1)
				kwin++;
			else if(win == 2)
				iwin++;
			return;
		}
		
		for(int i=0; i<9; i++) {
			if(check[i] == false) {
				check[i] = true;
				iyCard[idx] = iy[i];
				permutation(idx+1);
				check[i] = false;
			}
		}
	}
}