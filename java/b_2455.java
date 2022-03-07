package wonjong.game.baseball;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class b_2455 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int[] lope=new int[n];
		int min=100000;
		int max=0;
		int sum=0;
		int aver=0;
		int aver_2=0;
		int count=0;
		for(int i=0;i<n;i++) {
			lope[i]=Integer.parseInt(br.readLine());
		}
		Arrays.sort(lope);
		for(int i=lope.length-1;i>=0;i--) {
			count++;
			aver=lope[i]*count;
			if(aver>aver_2) {
				aver_2=aver;
			}

		}
		System.out.println(aver_2);
	
		br.close();
	
	}

}
