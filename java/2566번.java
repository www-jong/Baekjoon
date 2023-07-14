import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] res ={-1,0,0};
        int[][] array=new int[9][9];
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                array[i][j]=sc.nextInt();
                if(array[i][j]>res[0]){
                    res[0]=array[i][j];
                    res[1]=i+1;
                    res[2]=j+1;
                }
            }
            sc.nextLine();
        }
        System.out.println(res[0]+"\n"+res[1]+" "+res[2]);
    }
}