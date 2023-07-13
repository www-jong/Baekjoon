import java.io.IOException;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] res=new int[26];
        for(int i=0;i<26;i++){
            res[i]=-1;
        }
        String tmp=sc.nextLine();
        for(int i=0;i<tmp.length();i++){
            if(res[tmp.charAt(i)-'a']==-1){
            res[tmp.charAt(i)-'a']=i;
            }
        }
        for(int i=0;i<26;i++){
            System.out.print(res[i]+" ");
        }
        System.out.println();
    }
}