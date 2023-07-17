import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
				// 1 2~7, 8~19, 20~37 38~61
				//   6    12    18     24
				int res = 1;
				int idx = 0;
				while(true){
					if(res>=N){
						System.out.println(idx+1);
						break;
                    }
                    idx+=1;
                    res+=idx*6;
                }
    }
}