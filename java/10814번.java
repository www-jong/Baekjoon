package bbb.beakjun;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class b10814 {

	public static void main(String[] args) throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int c=Integer.parseInt(br.readLine());
		HashMap<Integer,HashMap<String,Integer>> map=new HashMap<Integer,HashMap<String,Integer>>();
		int[][] maparr=new int[c][2];
		for (int i=0;i<c;i++) {// map => 인덱스,(이름,나이))
			String[] a=br.readLine().split(" ");
			HashMap<String,Integer> arr=new HashMap<String,Integer>();
			arr.put(a[1], Integer.parseInt(a[0]));
			map.put(i, arr);
			maparr[i][1]=i;
			maparr[i][0]=Integer.parseInt(a[0]);
		}
		//maparr => 나이,가입순
		//나이순, 나이가같으면 가입순
		//-->map.get()순, 같으면 가입순
		
		Arrays.sort(maparr, new Comparator<int[]>() { 
			@Override public int compare(int[] o1, int[] o2) { 
				if(o1[0] == o2[0]) { 
					return o1[1] - o2[1]; 
					}else { return o1[0] - o2[0]; 
				} 
				}
		});
	
		for (int i=0;i<c;i++) {
			int age=0;
			String name=null;
			for (String names:map.get(maparr[i][1]).keySet()) {
				age=map.get(maparr[i][1]).get(names);
				name=names;
				
			}

			bw.write(age+" "+name+"\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
	

}
