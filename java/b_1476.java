package wonjong.game.baseball;
import java.util.Scanner;

public class b_1476 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int E=sc.nextInt();
		int S=sc.nextInt();
		int M=sc.nextInt();
		int a=1;
		int b=1;
		int c=1;
		int count=1;
		while(E!=a||S!=b||M!=c) {
			a++;
			b++;
			c++;
			count++;
			if(a==16) {a=1;}
			if(b==29) {b=1;}
			if(c==20) {c=1;}
		}
		System.out.println(count);
		
	}

}
