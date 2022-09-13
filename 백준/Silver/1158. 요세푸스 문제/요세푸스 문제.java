import java.util.Scanner;
import java.util.Stack;

class Node {
	public int data;
	public Node link;
	public Node prev;
	
	public Node(int data) {
		this.data = data;
		this.link = null;
		this.prev = null;
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Stack<Node> st = new Stack<>();
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		int[] res = new int[N];
		int idx = 0;
		Node curr = new Node(1);
		st.push(curr);
		for(int i=2; i<=N; i++) {
			Node temp = new Node(i);
			st.peek().link = temp;
			temp.prev = st.peek();
			st.push(temp);
		}
		st.peek().link = curr;
		curr.prev = st.peek();
		
		while(idx < N) {
			for(int i=1; i<K; i++) {
				curr = curr.link;
			}
			res[idx++] = curr.data;
			curr.prev.link = curr.link;
			curr.link.prev = curr.prev;
			curr = curr.link; 
		}
		System.out.print("<");
		for(int i=0; i<N-1; i++) {
			System.out.print(res[i]);
			System.out.print(", ");
		}
		System.out.print(res[N-1]+">");
		
	}
}