package wonjong.game.baseball;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class b_13458 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N=Integer.parseInt(br.readLine());
		int[] A=Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int sum=Arrays.stream(A).sum();
		long count=N;
		int[] bc=Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		for(int stu:A) {
			stu-=bc[0];
			if(stu>0) {
			count+=Math.ceil((float)stu/bc[1]);
			}
		}

		br.close();
		System.out.println(count);
	
	}

}
