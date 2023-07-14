import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);


        int N=sc.nextInt();
        sc.nextLine();
        int res=N;
        for(int i=0;i<N;i++){
            int[] check=new int[26];
            int[] ch2=new int[26];
            int ch=0;
            for(int j=0;j<26;j++){
                check[j]=0;
                ch2[j]=0;
            }
            String s=sc.nextLine();
            int tmp_idx=s.charAt(0)-'a';
            for(int j=0;j<s.length();j++){
                int idx=s.charAt(j)-'a';
                if(check[idx]==0){
                    check[idx]=1;
                    if(j!=0){
                    ch2[tmp_idx]=1;
                    }
                }else{
                    if(ch2[idx]!=0){
                        if(res>=1){
                        res-=1;
                        break;
                        }
                    }
                }
                tmp_idx=idx;
            }
        }

        System.out.println(res);
    }
}