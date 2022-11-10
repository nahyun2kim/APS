import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());
        for (int i = 1; i <= testCase; i++) {
            st = new StringTokenizer(br.readLine());
            int year = Integer.parseInt(st.nextToken());
            int month = Integer.parseInt(st.nextToken());
            int day;

            int changeMonth = month - 1;

            if (changeMonth == 0) {
                year -= 1;
                changeMonth = 12;
            }

            switch (changeMonth) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                day = 31;
                break;

            case 4:
            case 6:
            case 9:
            case 11:
                day = 30;
                break;

            default:
                if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
                    day = 29;
                } else {
                    day = 28;
                }
            }

            sb.append(year + " " + changeMonth + " " + day).append("\n");
        }
        
        System.out.println(sb);
    }
}