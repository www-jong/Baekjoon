import java.io.IOException;
import java.util.*;
import java.lang.Math;
public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int[] li=new int[4];
        String[] st =sc.nextLine().split(" ");
        for(int i=0;i<4;i++){
            li[i]=Integer.parseInt(st[i]);
        }
        System.out.println(Math.min(li[0],Math.min(li[1],Math.min(li[2]-li[0],li[3]-li[1]))));
    }
}