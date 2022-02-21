import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b7579 {
	static int min_req;
	static int n;
	static int m;
	public static void main(String[] args) throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String[] sss=br.readLine().split(" ");
		n=Integer.parseInt(sss[0]);
		m=Integer.parseInt(sss[1]);
		String[] dd=br.readLine().split(" ");
		String[] ddd=br.readLine().split(" ");
		br.close();
		int[] a=new int[n+1];
		int[] b=new int[n+1];
		a[0]=0;
		b[0]=0;
		int summ=0;
		for(int i=0;i<dd.length;i++) {
			a[i+1]=Integer.parseInt(dd[i]);
			b[i+1]=Integer.parseInt(ddd[i]);
			summ+=Integer.parseInt(ddd[i]);
		}
		int[][] dp=new int[n+1][summ+1];
		dp[0][0]=0;
		dp[0][1]=0;
		min_req=summ;
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=summ;j++) {
				if(j<b[i]) {
					dp[i][j]=dp[i-1][j];
				}else {
					dp[i][j]=Math.max(a[i]+dp[i-1][j-b[i]],dp[i-1][j]);
				}
				if(m<=dp[i][j]) {
					min_req=Math.min(min_req, j);
				}
			}
		}
		System.out.println(min_req);
	}
	
}
