class Solution {
    public int gcd(int a, int b) {
        for(int i=Math.min(a, b); i>0; i--) {
            if(a % i == 0 && b % i == 0) return i;
        }
        return 0;
    }
    
    public int lcm(int a, int b) {
        for(int i=Math.max(a, b); i<=a*b; i++) {
            if(i % a == 0 && i % b == 0) return i;
        }
        return 0;
    }
    
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        answer[0] = gcd(n, m);
        answer[1] = lcm(n, m);
        return answer;
    }
}