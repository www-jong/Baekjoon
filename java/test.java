import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class test {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<String> lines = new ArrayList<String>();
        for(int i=0; i<N;i++){
            lines.add(br.readLine());
        }
        System.out.println(lines);

    }

    public static void main(String[] args) throws IOException {
        new test().solution();
    }
}
