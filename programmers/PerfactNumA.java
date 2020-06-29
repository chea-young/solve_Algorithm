package CodingZone;

public class PerfactNumA {
	public static void main(String args[]) {
		PerfactNumA p = new PerfactNumA();
		int [] a = {5,9,10,7};
		int [] b = {2,36,1,3};
		int [] c = {3,2,6};
		int[] n = p.solution(a,5);
		for(int f:n) {
			System.out.print( f+" ");
		}
		System.out.println();
		
		int [] m = p.solution(b,1);
		for(int f:m) {
			System.out.print( f+" ");
		}
		System.out.println();
		
		int [] g = p.solution(c,10);
		for(int f:g) {
			System.out.print( f+" ");
		}
		System.out.println();
		
	}

	
		  public int[] solution(int[] arr, int divisor) {
		      int[] answer = {};
		      
		      int count = 0;
		      
		      int [] check = new int [arr.length];
		      int [] term = new int [arr.length];
		      
		      int ch = 0;
		      while(ch!=arr.length) {
		    	  int min = 1000000;
		    	  int ind = 0;
			      for(int i = 0;i<arr.length;i++) {
			    	  if(arr[i]<min && check[i]==0) {
			    		  min = arr[i];
			    		  ind  = i;
			    	  }
			      }
			      term[ch] = min;
			      if(arr[ind]%divisor==0){
		              count++;
		          }
			      check[ind] = 1;
			      ch++;
		      }
		      
		      if(count==0){
		          answer = new int[1];
		          answer[0] = -1;
		          
		      }else{
		          answer = new int [count];
		          int num = 0;
		          for(int i = 0; i<arr.length;i++){
			          if(term[i]%divisor==0){
			              answer[num] = term[i];
			              num++;
			          }
			      }
		          
		      }
		      return answer;
		  }
}
