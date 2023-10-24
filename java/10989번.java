import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
class Main {
	static public void main(String []args) throws IOException{

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine());
        int N= Integer.parseInt(br.readLine());
        int[] li=new int[N];
        for(int i=0;i<N;i++){
            li[i]=Integer.parseInt(br.readLine());
        }
        Arrays.sort(li);
        for(int i=0;i<N;i++){
            bw.write(Integer.toString(li[i])+'\n');
        }

        bw.flush();
        bw.close();

    }
}