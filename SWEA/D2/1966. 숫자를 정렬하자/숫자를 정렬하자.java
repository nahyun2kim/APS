import java.util.Scanner;
class Solution
{
	static int[] arr;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			arr = new int[N];
			for(int i=0; i<N; i++)
				arr[i] = sc.nextInt();
			
			quickSort(0, N-1);
			StringBuilder sb = new StringBuilder();
			sb.append('#').append(tc);
			for(int a : arr)
				sb.append(' ').append(a);
			System.out.println(sb);
		}
	}
	
	static void quickSort(int left, int right) {
		if (left < right) {
			int pivot = HoarePartition(left, right);
//			int pivot = LomutoPartition(left, right);
			quickSort(left, pivot-1);
			quickSort(pivot+1, right);
		}
	}

	static int HoarePartition(int left, int right) {
		int pivot = arr[left];
		int L = left+1;
		int R = right;
		while(L <= R) {
			while(L <=R && arr[L] <= pivot)
				L++;
			while(arr[R] > pivot)
				R--;
			if(L < R)
				swap(L, R);
		}
		swap(left, R);
		return R;
	}
	
	static int LomutoPartition(int left, int right) {
		int pivot = arr[right];
		int idx = left - 1;
		for(int i=left; i<=right-1; i++) {
			if(arr[i] <= pivot) {
				idx++;
				swap(idx, i);
			}
		}
		swap(idx+1, right);
		return idx+1;
	}
	
	static void swap(int a, int b) {
		int temp = arr[a];
		arr[a] = arr[b];
		arr[b] = temp;
	}
}