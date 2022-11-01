import java.util.*;
class Solution {
    public String[] solution(String[] files) {
        int size = files.length;

        List<String[]> list = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            String[] strArr = new String[5];
            strArr[0] = files[i]; //원본
            strArr[3] = String.valueOf(i); //기존 정렬 
            String header = ""; //머리
            String number = ""; //숫자
            
            int idx = 0;
            for(;idx < files[i].length();idx++) {
                char c = files[i].charAt(idx);
                if(57 >= (int) c && (int) c >= 48) break; //숫자면 탈출
                header += files[i].charAt(idx); //숫자가 아니면 넣음 
            }
            
            for(;idx <files[i].length();idx++) {
                char c = files[i].charAt(idx);
                if(!(57 >= (int) c && (int) c >= 48)) break; //숫자가 아니면
                number += files[i].charAt(idx); //숫자가 아니면 넣음 
            }
            strArr[1] = header.toUpperCase();
            strArr[2] = number;
            
            list.add(strArr);
            
        }

        // 정렬
        Collections.sort(list, new Comparator<String[]>() {

            @Override
            public int compare(String[] o1, String[] o2) {
                int value = o1[1].compareTo(o2[1]); // 해더비교
                if (value == 0) { // 해더가 같다면
                    int a = Integer.parseInt(o1[2]);
                    int b = Integer.parseInt(o2[2]);
                    return a - b;
                } else {
                    return value;
                }
            }

        });

        // 테스트
        for (String[] s : list) {
            System.out.print("[" + s[0] + "]  [" + s[1] + "] [" + s[2] + "]  [" + s[3] + "]\n");
        }

        // 결과값 옮겨 적기
        String[] answer = new String[list.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i)[0];
        }


        return answer;
    }

}