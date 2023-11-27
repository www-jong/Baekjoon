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
        int li[] = new int[5];
        int res = 0;
        for(int i=0;i<5;i++){
            int tmp = Integer.parseInt(br.readLine());
            res+=tmp;
            li[i]=tmp;
            }
        Arrays.sort(li);
        bw.write(Integer.toString(res/5)+'\n'+Integer.toString(li[2]));
        bw.flush();
        bw.close();

    }
}