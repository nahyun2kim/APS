import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//1. 입력
		int N = sc.nextInt(); // N : 학생수
		int K = sc.nextInt(); // K : 방 최대 인원 수
		int[][] student = new int[6][2];
		for(int i=0; i<N; i++) {
			int gender = sc.nextInt();  // 성별
			int grade = sc.nextInt()-1; // 학년
			student[grade][gender]++;
		}
		
		//2. 돌아가며 방개수 카운트
		int cnt=0;
		for(int i=0; i<6; i++) {
			if(student[i][0] % K == 0)
				cnt += student[i][0]/K;
			else
				cnt += student[i][0]/K + 1;
			if(student[i][1] % K == 0)
				cnt += student[i][1]/K;
			else
				cnt += student[i][1]/K + 1;
		}
		
		//3. 출력
		System.out.println(cnt);
	}
}