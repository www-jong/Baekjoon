import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[][] maps=new int[100][100];
        for(int i=0;i<100;i++){
            for(int j=0;j<100;j++){
                maps[i][j]=0;
            }
        }
        int N=sc.nextInt();
        sc.nextLine();
        for(int i=0;i<N;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            for(int j=0;j<10;j++){
                for(int k=0;k<10;k++){
                    maps[a+j][b+k]=1;
                }
            }
            sc.nextLine();
        }
        int res =0;
        for(int i=0;i<100;i++){
            for(int j=0;j<100;j++){
                if(maps[i][j]==1){
                    res+=1;
                }
            }
        }
        System.out.println(res);
    }
}