import java.io.*;
import java.util.*;
import java.lang.Math;
class test {
	static public void main(String []args) throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int res = 0;
        System.out.println(N/5);
        System.out.println((int)N/5);
        
        bw.write(res);
        bw.flush();
        bw.close();

    }
}