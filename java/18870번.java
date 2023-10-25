import java.io.*;
import java.util.*;
import java.lang.Math;
class Main {
	static public void main(String []args) throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        HashSet<Integer> sli=new HashSet<>();
        HashMap<Integer,Integer> map=new HashMap<>();
        int[] li=new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            int tmp=Integer.parseInt(st.nextToken());
            sli.add(tmp);
            li[i]=tmp;
        }
        Integer[] ali=sli.toArray(new Integer[0]);
        Arrays.sort(ali);
        for(int i=0;i<ali.length;i++){
            map.put(ali[i],i);
        }
        for(int i=0;i<N;i++){
            bw.write(Integer.toString(map.get(li[i]))+" ");
        }
        bw.flush();
        bw.close();

    }
}