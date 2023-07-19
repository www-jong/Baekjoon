import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = 0;
        while(true){
            n=sc.nextInt();
            ArrayList<String> s=new ArrayList<String>();
            int d=0;
            if(n==-1){
                break;
            }
            for(int i=1;i<=(n/2)+1;i++){
                if(n%i==0){
                    s.add(String.valueOf(i));
                    d+=i;
                }
            }
            if(d==n){
                String str=String.join(" + ",s);
                System.out.print(n+" = "+str+"\n");
                
            }else{
                System.out.printf("%d is NOT perfect.\n",n);
            }
        }
    }
}