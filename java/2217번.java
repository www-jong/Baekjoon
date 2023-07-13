package wonjong.game.baseball;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class b_2217 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int count=0;
		int max=0;
		int c=0;
		while(true) {
		int[] A=Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		count=count-A[0]+A[1];
		if(count>max) {max=count;}
		c++;
		if(c==4) {break;}
		}
		br.close();
		System.out.println(max);
	
	}

}
