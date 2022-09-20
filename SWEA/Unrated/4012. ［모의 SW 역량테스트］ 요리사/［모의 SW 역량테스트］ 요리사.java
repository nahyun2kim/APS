import java.util.Scanner;

class Solution
{
	static int N, minDiff;
	static int[] sel;
	static int[][] dish;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//0. 테스트케이스 입력
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			
			//1. 입력
			N = sc.nextInt();
			dish = new int[N][N];
			
			for(int i=0; i<N*N; i++) {
				dish[i/N][i%N] = sc.nextInt();
			}
			
			sel = new int[N/2];
			minDiff = Integer.MAX_VALUE;
			
			//2. 조합으로 재료 반 나누기
			comb(0,0);
			
			//3. 출력
			System.out.printf("#%d %d\n", tc, minDiff);
		}
	}
	
	// 재료를 뽑았으면 for문을 돌며 재료들의 시너지를 계산
	static int synergy(int[] arr) {
		int res = 0;
		for(int i=0; i<N/2-1; i++) {
			for(int j=i+1; j<N/2; j++) {
				res += dish[arr[i]-1][arr[j]-1];
				res += dish[arr[j]-1][arr[i]-1];
			}
		}
		return res;
	}
	
	// 한 음식의 재료로 다른 음식의 재료 찾기
	static int[] getArr2(int[] arr) {
		int[] arr2 = new int[N/2];
		int idx1 = 0;
        int idx2 = 0;
        for(int i=1; i<=N; i++) {
            if(idx1 == N/2 || arr[idx1] != i) {
                arr2[idx2++] = i;
            } else{
                idx1++;
            }
            if(idx2 == 9) break;
        }
        return arr2;
	}
	
	
	// 재료를 조합으로 구했으면, 시너지의 차를 구해서 최솟값 비교
	static void comb(int idx, int selIdx) {
		if(selIdx == N/2) {
			// 어차피 조합 중 반만 구하면 차는 똑같으므로!
			if(sel[0] != 1)
				return;
			int sy1 = synergy(sel);
			int sy2 = synergy(getArr2(sel));
			minDiff = Math.min(minDiff, Math.abs(sy1-sy2));
			return;
		} else if (idx == N)
			return;
		
		sel[selIdx] = idx+1;
		comb(idx+1, selIdx+1);
		comb(idx+1, selIdx);
	}
}