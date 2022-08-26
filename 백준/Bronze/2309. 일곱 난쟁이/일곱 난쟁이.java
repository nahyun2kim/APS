import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		//1. 입력
		List<Integer> dwarf = new ArrayList<>();
		int sum = 0;
		for(int i=0; i<9; i++) {
			dwarf.add(sc.nextInt());
			sum += dwarf.get(i);
		}
		
		//2. 일곱난쟁이가 아닌 두명을 빼자
		int ans = sum - 100;
		boolean check = false;
		for(int i=0; i<8; i++) {
			for(int j=i+1; j<9; j++) {
				if(dwarf.get(i)+dwarf.get(j) == ans) {
					dwarf.remove(j);
					dwarf.remove(i);
					check = true;
					break;
				}
			}
			if(check)
				break;
		}
		
		//3. 리스트 정렬
		Collections.sort(dwarf);
		
		//4. 출력
		for(int x : dwarf)
			System.out.println(x);
		
	}
}