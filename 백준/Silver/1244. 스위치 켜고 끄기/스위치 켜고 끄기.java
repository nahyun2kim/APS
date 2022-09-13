import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int[] swi;
	public static void main(String[] args) {
		int N = sc.nextInt();
		swi = new int[N];
		for(int i=0; i<N; i++)
			swi[i] = sc.nextInt();
		int S = sc.nextInt();
		for(int i=0; i<S; i++) {
			changeSwi(sc.nextInt());
		}
		int idx = 0;
		while(idx<N) {
			System.out.printf("%d ", swi[idx++]);
			if (idx%20 == 0)
				System.out.println();
		}
		
	}//main end
	
	static void changeSwi(int num) {
		int cmd = sc.nextInt();
		if(num == 1) {
			for(int i=cmd; i<=swi.length; i+=cmd)
				swi[i-1] ^= 1;
		}
		else {
			int i = cmd-1;
			swi[i] ^= 1;
			int idx = 1;
			while(i-idx>=0 && i+idx<swi.length && swi[i-idx]==swi[i+idx]) {
				swi[i-idx] ^= 1;
				swi[i+idx] ^= 1;
				idx++;
			}
		}
	}
}