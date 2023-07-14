import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String s=sc.nextLine();
        int idx=0;
        int res=0;
        while(idx<s.length()){
            if(idx<(s.length()-1)){
                if(idx<(s.length()-2)&&s.substring(idx,idx+3).equals("dz=")){
                    res+=1;
                    idx+=2;
                }else if(s.substring(idx,idx+2).equals("c=")){
                    res+=1;
                    idx+=1;
                }else if(s.substring(idx,idx+2).equals("c-")){
                    res+=1;
                    idx+=1;
                }else if(s.substring(idx,idx+2).equals("d-")){
                    res+=1;
                    idx+=1;
                }else if(s.substring(idx,idx+2).equals("lj")){
                    res+=1;
                    idx+=1;
                }else if(s.substring(idx,idx+2).equals("nj")){
                    res+=1;
                    idx+=1;
                }else if(s.substring(idx,idx+2).equals("s=")){
                    res+=1;
                    idx+=1;
                }else if(s.substring(idx,idx+2).equals("z=")){
                    res+=1;
                    idx+=1;
                }else{
                    res+=1;
                }
            }else{
                res+=1;
            }
        idx+=1;
        }
        System.out.println(res);
    }
}