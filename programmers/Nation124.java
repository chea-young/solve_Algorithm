package CodingZone;

import java.util.Scanner;
import java.util.Vector;

public class Nation124 {

	public String solution(int n) {
		  Vector<Integer> num = new Vector<Integer>();
		  int 나머지 = 0;
		  int 몫 =0;
		  String answer = "";
		  
		  몫= n/3;
		  if(n%3==0) {
			  몫--;
		  }

		  if(n%3==1) {
			  나머지 = 1;
		  }else if( n%3==2) {
			  나머지 =2;
		  }else {
			  나머지 =4;
		  }
		  num.add(나머지);
		  //System.out.println(몫+" "+나머지);
		  
		  while(true) {
			 if(몫==0) {
				 if( 몫 == 0) {
					 
				  }else if(num.get(num.size()-1)==4&&몫==1) {
				  }else {
					  num.add(몫);
				  }
				  
				  /*if(num.get(num.size()-1)==4&&몫==1) {
				  }
				  else if (몫 !=0||(num.get(num.size()-1)!=4||몫!=1)) {
					  num.add(몫);
				  }*/
				  
				  for(int i = num.size();i>0;i--) {
					  if(num.get(i-1)==0) {
						  continue;
					  }
					  answer = answer + String.valueOf(num.get(i-1));
				  }
				 break;
			 }

			 if(몫==2) {
				 if( 몫 == 0) {
					 
				  }else if(num.get(num.size()-1)==4&&몫==1) {
				  }else {
					  num.add(몫);
				  }
				  
				  /*if(num.get(num.size()-1)==4&&몫==1) {
				  }
				  else if (몫 !=0||(num.get(num.size()-1)!=4||몫!=1)) {
					  num.add(몫);
				  }*/
				  
				  for(int i = num.size();i>0;i--) {
					  if(num.get(i-1)==0) {
						  continue;
					  }
					  answer = answer + String.valueOf(num.get(i-1));
				  }
				 break;
			 }
			 
			 if(몫==1) {
				 if( 몫 == 0) {
					 
				  }else {
					  num.add(몫);
				  }
				  
				  for(int i = num.size();i>0;i--) {
					  if(num.get(i-1)==0) {
						  continue;
					  }
					  answer = answer + String.valueOf(num.get(i-1));
				  }
				 break;
			 }
			 
			 else {
				 
				 int extra몫=0;
				  
				 if(몫%3==1) {
					 나머지 = 1;
				 }else if(몫%3==2) {
					 나머지 =2;
				 }else if(몫%3==0){
					 
					 나머지 =4;
				 }
				 
				 extra몫= 몫/3;
				 if(extra몫%3==0) {
					 extra몫--;
				  }
				  
				  몫 = extra몫;
				  
				  
				  if(몫==0||몫==1||몫==2||몫==4) {
					  num.add(나머지);
					  
					  if( 몫 == 0) {
							 
					  }else if(num.get(num.size()-1)==4&&몫==1) {
					  }else {
						  num.add(몫);
					  }
					  
					  /*if(num.get(num.size()-1)==4&&몫==1) {
					  }
					  else if (몫 !=0||(num.get(num.size()-1)!=4||몫!=1)) {
						  num.add(몫);
					  }*/
					  
					  for(int i = num.size();i>0;i--) {
						  if(num.get(i-1)==0) {
							  continue;
						  }
						  answer = answer + String.valueOf(num.get(i-1));
					  }
					  break;
				  }else {
					  num.add(나머지);
				  }
				  
				  if( 몫 == 0) {
						 
				  }else if(num.get(num.size()-1)==4&&몫==1) {
				  }else {
					  num.add(몫);
				  }
				  
				  /*if(num.get(num.size()-1)==4&&몫==1) {
				  }
				  else if (몫 !=0||(num.get(num.size()-1)!=4||몫!=1)) {
					  num.add(몫);
				  }*/
				  
				  for(int i = num.size();i>0;i--) {
					  if(num.get(i-1)==0) {
						  continue;
					  }
					  answer = answer + String.valueOf(num.get(i-1));
				  }
			  }
		  }
		  
		  return answer;
	  }
	  
	public static void main(String args[]){
		Nation124 nation = new Nation124();
	    Scanner input = new Scanner(System.in);
	   /* int number = input.nextInt();
	    System.out.println(nation.solution(number));*/
		for(int i=5; i<=25;i++) {
			System.out.println(i+": 124 나라 :"+nation.solution(i));
		}
	    
	}
}
