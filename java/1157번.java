import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] res ={-1,-1,0};
        int[] arr=new int[26];
        for(int i=0;i<26;i++){
            arr[i]=0;
        }
        String s=sc.nextLine().toUpperCase();
        for(int i=0;i<s.length();i++){
            arr[s.charAt(i)-'A']+=1;
        }
        for(int i=0;i<26;i++){
            if(res[0]<arr[i]){
                res[0]=arr[i];
                res[1]=i;
                res[2]=0;
            }else if(res[0]==arr[i]){
                res[0]=arr[i];
                res[1]=i;
                res[2]=1;
            }
        }
        if(res[2]==0){
        System.out.println((char)(res[1]+'A'));
        }
        else{
            System.out.println("?");
        }
    }
}