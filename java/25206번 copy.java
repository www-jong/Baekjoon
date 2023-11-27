import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        double res=0;
        int N=0;
        for(int i=0;i<20;i++){
            String[] tmp=sc.nextLine().split(" ");
            double point=0;
            //System.out.println(tmp[0]);
            //System.out.println(tmp[1]);
            if(tmp[2].equals("A+")){
                point=4.5;
            }else if(tmp[2].equals("A0")){
                point=4.0;
            }else if(tmp[2].equals("B+")){
                point=3.5;
            }else if(tmp[2].equals("B0")){
                point=3.0;
            }else if(tmp[2].equals("C+")){
                point=2.5;
            }else if(tmp[2].equals("C0")){
                point=2.0;
            }else if(tmp[2].equals("D+")){
                point=1.5;
            }else if(tmp[2].equals("D0")){
                point=1.0;
            }else if(tmp[2].equals("F")){
                point=0;
            }else if(tmp[2].equals("P")){
                point=0;
                N-=Double.parseDouble(tmp[1]);
            }
            N+=Double.parseDouble(tmp[1]);
            res+=Double.parseDouble(tmp[1])*point;
        }

        System.out.println(res/N);
    }
}