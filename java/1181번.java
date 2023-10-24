import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;
class Main {
	static public void main(String []args) throws IOException{

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(br.readLine());
        HashSet<String> hli=new HashSet<>();
        ArrayList<String> li = new ArrayList<>();
        for(int i=0;i<N;i++){
            String tmp = br.readLine();
            if(!hli.contains(tmp)){
                li.add(tmp);
                hli.add(tmp);
            }
        }
        String[] liarray=li.toArray(new String[0]);
        Arrays.sort(liarray,(a,b)->a.length()==b.length()?a.compareTo(b):a.length()-b.length());
        for (String item : liarray) {
            bw.write(item + '\n');
        }
        bw.flush();
        bw.close();

    }
}