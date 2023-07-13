import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class b9663 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static int count;
	public static void main(String[] args) throws IOException {
		int n=Integer.parseInt(br.readLine());
		
		br.close();
		//ArrayList<Integer> arr=new ArrayList<Integer>();
		int[] arr=new int[n];
		for(int i=0;i<n;i++) {
			arr[i]=-1;
		}
		fun(0,0,arr,n);
		System.out.println(count);
		bw.flush();
		
		bw.close();

	}

	private static void fun(int x,int qu,int[] arr,int n) throws IOException {
		if(qu==n) {
			count++;
			return;
		}
		for(int i=0;i<n;i++) {
			int check=0;
			for(int j=0;j<n;j++) {
				if(arr[j]==i) {
					check=1;
					break;
				}
				if(x-j>=0 && i-j>=0) {
					if(arr[x-j]==i-j) {
						check=1;
						break;
					}
				}
				if(x-j>=0&&i+j<n) {
					if(arr[x-j]==i+j) {
						check=1;
						break;
					}
				}
				
			}
			if(check==0) {
				arr[x]=i;
				fun(x+1,qu+1,arr,n);
				arr[x]=-1;
			}
		}	
		return;
	}
	
}
