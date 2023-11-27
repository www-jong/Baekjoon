import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.lang.Math;
import java.util.Arrays;
class Main {
	static public void main(String []args) throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int li[]=new int[N];
        StringTokenizer sd = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            li[i]=Integer.parseInt(sd.nextToken());
        }
        Arrays.sort(li);
        int res = 0;
        
        bw.write(Integer.toString(li[N-M]));
        bw.flush();
        bw.close();

    }
}