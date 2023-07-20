import java.io.IOException;
import java.util.*;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> A=new ArrayList<Integer>();
        ArrayList<Integer> B=new ArrayList<Integer>();
        
        for(int i=0;i<3;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            if(i!=2){
            sc.nextLine();}
            A.add(a);
            B.add(b);
        }
        int[] res = {0,0};
        Collections.sort(A);
        Collections.sort(B);
        if(A.get(0).equals(A.get(1))){res[0]=A.get(2);}
        else{res[0]=A.get(0);
        }
        if(B.get(0).equals(B.get(1))){res[1]=B.get(2);}
        else{res[1]=B.get(0);}
        System.out.println(res[0]+" "+res[1]);
    }
}