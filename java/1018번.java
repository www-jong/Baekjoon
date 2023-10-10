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
        int M = Integer.parseInt(st.nextToken());
        String[] wans=new String[8];
        String[] bans=new String[8];
        String[] board=new String[N];
        String[] tmp={"WBWBWBWB","BWBWBWBW"};
        for(int i=0;i<8;i++){
            if(i%2==0){
                wans[i]=tmp[i%2];
                bans[i]=tmp[i%2+1];
            }else{
                wans[i]=tmp[i%2];
                bans[i]=tmp[i%2-1];
            }
        }
        int res = 100000;
        for(int i=0;i<N;i++){
            board[i]=br.readLine();
        }
        for(int x=0;x<N-7;x++){
            for(int y=0;y<M-7;y++){
                int tmp_val1=0;
                int tmp_val2=0;
                for(int k=0;k<8;k++){
                    for(int p=0;p<8;p++){
                        if(board[x+k].charAt(y+p)!=wans[k].charAt(p)){
                            tmp_val1++;
                        }
                        if(board[x+k].charAt(y+p)!=bans[k].charAt(p)){
                            tmp_val2++;
                        }
                    }
                }
                res=Math.min(res,tmp_val1);
                res=Math.min(res,tmp_val2);
            }
        }

        bw.write(Integer.toString(res));
        bw.flush();
        bw.close();

    }
}