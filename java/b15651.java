package bbb.beakjun;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class b15651 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	public static void main(String[] args) throws IOException {
		String line[]=br.readLine().split(" ");
		br.close();
		int n=Integer.parseInt(line[0]);
		int m=Integer.parseInt(line[1]);
		System.out.println(line[0]);
		ArrayList<Integer> arr=new ArrayList<Integer>();
		fun(n,m,arr);
		bw.flush();
		
		bw.close();

	}

	private static void fun(int n,int m,ArrayList<Integer> arr) throws IOException {
		
		if(arr.size()==m) {
			String res=Integer.toString(arr.get(0));
			for(int i=1;i<=arr.size()-1;i++) {
					res=res+" "+arr.get(i);
			}
			try {
				bw.write(res);
				bw.newLine();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return;
		}
		for(int i=1;i<=n;i++) {
			arr.add(i);
			fun(n,m,arr);
			arr.remove(arr.size()-1);
		}	
		return;
	}
	
}
