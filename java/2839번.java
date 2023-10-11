import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.lang.Math;
class Main {
	static public void main(String []args) throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int res = -1;
        int checker=0;
        for(int i=N/5;i>=0;i--){
            for(int j=0;j<7;j++){
                if(i*5+j*3==N){
                    checker=1;
                    res=i+j;
                    break;
                }
            }
            if(checker==1){
                break;
            }
        }
        bw.write(Integer.toString(res));
        bw.flush();
        bw.close();

    }
}