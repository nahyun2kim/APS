import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//1. 입력
		int R = sc.nextInt(); // R : 가로길이
		int C = sc.nextInt(); // C : 세로길이
		int N = sc.nextInt(); // N : 자르는 횟수
		
		List<Integer> cutR = new ArrayList<>();
		List<Integer> cutC = new ArrayList<>();
		
		cutR.add(0);
		cutC.add(0);
		
		for(int i=0; i<N; i++) {
			int dir = sc.nextInt(); // 자르는 방향 (0이면 가로, 1이면 세로)
			if(dir == 0) {
				cutR.add(sc.nextInt());
			} else {
				cutC.add(sc.nextInt());
			}
		}
		
		cutR.add(C);
		cutC.add(R);
		
		//2. 정렬
		Collections.sort(cutR);
		Collections.sort(cutC);
		
		//3. 가장 큰 조각 확인
		int maxR = 0;
		int maxC = 0;
		
		for(int i=1; i<cutC.size(); i++) 
			maxR = Math.max(maxR, cutC.get(i)-cutC.get(i-1));
		
		for(int i=1; i<cutR.size(); i++) 
			maxC = Math.max(maxC, cutR.get(i)-cutR.get(i-1));
		
		int ans = maxR * maxC;
		
		//4. 출력
		System.out.println(ans);
	}
}
