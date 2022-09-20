import java.util.Scanner;

public class Main {
	static int N, minDiff;
	static int[] selA, selB;
	static int[][] S;
	static boolean[] check;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		
		S = new int[N][N];
		for(int i=0; i<N*N; i++)
			S[i/N][i%N] = sc.nextInt();
		
		selA = new int[N/2];
		selB = new int[N/2];
		check = new boolean[N];
		minDiff = Integer.MAX_VALUE;
		
		comb(0,0);
		System.out.println(minDiff);
	}
	
	static int calSynergy() {
		int sy1 = 0;
		int sy2 = 0;
		for(int i=0; i<N/2-1; i++) {
			for(int j=i+1; j<N/2; j++) {
				sy1 += S[selA[i]][selA[j]];
				sy1 += S[selA[j]][selA[i]];
				sy2 += S[selB[i]][selB[j]];
				sy2 += S[selB[j]][selB[i]];
			}	
		}
		return Math.abs(sy1-sy2);
	}
	
	static void comb(int idx, int selIdx) {
		if(selIdx == N/2) {
			if(check[0] == false)
				return;
			int idxA = 0, idxB = 0; 
			for(int i=0; i<N; i++) {
				if(check[i]) {
					selA[idxA++] = i;
				}
				else {
					selB[idxB++] = i;
				}
			}
			minDiff = Math.min(minDiff, calSynergy());
			return;
		} else if(idx == N)
			return;
		
		check[idx] = true;
		comb(idx+1, selIdx+1);
		check[idx] = false;
		comb(idx+1, selIdx);
	}
}