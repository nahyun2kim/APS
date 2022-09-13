import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//0. 대결의 횟수 입력
		int N = sc.nextInt();
		for(int tc=0; tc<N; tc++) {
			
			//1. 입력
			int size1 = sc.nextInt();
			int[] child1 = new int[size1];
			for(int i=0; i<size1; i++) 
				child1[i] = sc.nextInt();

			int size2 = sc.nextInt();
			int[] child2 = new int[size2];
			for(int i=0; i<size2; i++) 
				child2[i] = sc.nextInt();
			
			//2. 받은 숫자로 대결
			char ans = fightCard(child1, child2);
				
			//3. 출력
			System.out.println(ans);
		}
	}
	
	 static char fightCard(int[] arr1, int[] arr2) {
		 int[] cnt1 = new int[5];
		 int[] cnt2 = new int[5];
		 
		 for(int i=0; i<arr1.length; i++)
			 cnt1[arr1[i]]++;
		 for(int i=0; i<arr2.length; i++)
			 cnt2[arr2[i]]++;
		 
		 char res = 'D';
		 for(int i=4; i>0; i--) {
			 if(cnt1[i]>cnt2[i]) {
				 res = 'A';
				 break;
			 } else if(cnt1[i]<cnt2[i]) {
				 res = 'B';
				 break;
			 }
		 }
		 return res;
	 }
}