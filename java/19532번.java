import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main {
	static public void main(String []args) throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        String[] wboard=new String[8];
        String[] bboard=new String[8];
        String[] tmp={"WBWBWBWB","BWBWBWBW"};
        for(int i=0;i<8;i++){
            if(i%2==0){
                wboard[i]=tmp[i%2];
                bboard[i]=tmp[i%2+1];
            }else{
                wboard[i]=tmp[i%2];
                bboard[i]=tmp[i%2-1];
            }
        }
        for(int i=0;i<8;i++){
            bw.write(wboard[i]);
        }
        String res = "0";
        
        bw.flush();
        bw.close();

    }
}