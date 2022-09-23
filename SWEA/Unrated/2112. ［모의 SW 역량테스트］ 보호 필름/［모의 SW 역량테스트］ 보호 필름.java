import java.util.Scanner;

class Solution
{
	static int D, W, K;
	static boolean flagR, flagD;
	static int[] selRow, selDrug;
	static int[][] film;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			sb.append('#').append(tc).append(' ');
			
			D = sc.nextInt(); // 세로
			W = sc.nextInt(); // 가로
			K = sc.nextInt(); // 검사할 줄의 수
			film = new int[D][W];
			for(int i=0; i<D; i++) {
				for(int j=0; j<W; j++) {
					film[i][j] = sc.nextInt();
				}
			}
			
			flagR= false; flagD = false;
			int ans = 0;
			
			if(checkFilm()) {
				sb.append(ans).append('\n');
				continue;
			}	
			for(int i=1; i<K; i++) {
				selRow = new int[i];
				selDrug = new int[i];
				comb(0, 0);
				if(flagR) {
					ans = i;
					sb.append(ans).append('\n');
					break;
				}
			}
			
			if(!flagR) {
				ans = K;
				sb.append(ans).append('\n');
			}
		}
		System.out.println(sb);
	}
	
	static boolean checkFilm() {
		for(int i=0; i<W; i++) {
			int spec = film[0][i];
			int cnt = 1;
			for(int j=1; j<D; j++) {
				if(film[j][i] == spec) {
					cnt++;
					if(cnt >= K)
						break;
				}
				else {
					spec = film[j][i];
					cnt = 1;
				}
			}
			if(cnt < K)
				return false;
		}
		return true;
	}
	
	static int[] changeRow(int row, int drug) {
		int[] origin = new int[W];
		origin = film[row].clone();
		for(int i=0; i<W; i++) {
			film[row][i] = drug;
		}
		return origin;
	}
	
	static void rollback(int row, int[] origin) {
		film[row] = origin;
	}
	
	static void comb(int idx, int selIdx) {
		if(selIdx == selRow.length) {
			selectDrug(0, selRow);
			if(flagD)
				flagR = true;
			return;
		}else if(idx == D)
			return;
		
		selRow[selIdx] = idx;
		comb(idx+1, selIdx+1);
		comb(idx+1, selIdx);
	}
	
	static void selectDrug(int idx, int[] row) {
		if(idx == selDrug.length) {
			int[][] origin = new int[selDrug.length][W];
			for(int i=0; i<selDrug.length; i++) {
				origin[i] = changeRow(row[i], selDrug[i]);
			}
			if(checkFilm())
				flagD = true;
			else {
				for(int i=0; i<selDrug.length; i++) {
					rollback(row[i], origin[i]);
				}
			}
			return;
		}
		
		for(int i=0; i<2; i++) {
			selDrug[idx] = i;
			selectDrug(idx+1, row);
		}
		
	}
}