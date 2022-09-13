import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int m = sc.nextInt();
		
		if(h==0 && m<45) {
			h = 24;
			}
		
		int min = 60*h + m - 45;
		h = min/60;
		m = min%60;
		
		System.out.printf("%d %d",h,m);
		
		
	}
}
