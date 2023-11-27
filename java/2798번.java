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
        int M= Integer.parseInt(st.nextToken());
        int res =0;
        int[] li=new int[N];
        st=new StringTokenizer(br.readLine());
        int idx=0;
        while (st.hasMoreTokens()){
            li[idx]=Integer.parseInt(st.nextToken());
            idx++;
        }
        for(int i=0;i<N;i++){
            for(int j=i+1;j<N;j++){
                for(int k=j+1;k<N;k++){
                    if(li[i]+li[j]+li[k]<=M&&res<li[i]+li[j]+li[k]){
                        res=li[i]+li[j]+li[k];
                    }
                }
            }
        }
        bw.write(Integer.toString(res));
        bw.flush();
        bw.close();

    }
}