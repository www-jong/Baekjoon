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
        String a=br.readLine();
        char[] li = a.toCharArray();
        int[] li2=new int[a.length()];
        for(int i=0;i<a.length();i++){
            li2[i]=li[i]-'0';
        }
        Arrays.sort(li2);
        for(int i=(a.length()-1);i>=0;i--){
            bw.write(Integer.toString(li2[i]));
        }
        bw.flush();
        bw.close();

    }
}