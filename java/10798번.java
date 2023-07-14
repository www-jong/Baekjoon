import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String[] array=new String[5];
        for(int i=0;i<5;i++){
            array[i]=sc.nextLine();
        }
        for(int i=0;i<15;i++){
            for(int j=0;j<5;j++){
                if(array[j].length()>i){
                System.out.print(array[j].charAt(i));
                }else{
                    //break;
                }
            }
        }
    }
}