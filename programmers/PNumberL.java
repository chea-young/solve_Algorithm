package CodingZone;

import java.util.Vector;

public class PNumberL {
	public static void main(String args[]) {
		PNumberL m1 = new PNumberL();
		String[] a1 = {"1234567891234567891", "97674223", "12345678912345678912"};
		System.out.println(m1.solution(a1));
		
		PNumberL m2 = new PNumberL();
		String[] a2 = {"123","456","789"};
		System.out.println(m2.solution(a2));
		
		PNumberL m3 = new PNumberL();
		String[] a3 = {"12","123","1235","567","88"};
		System.out.println(m3.solution(a3));
		
	}
	
	public boolean solution(Vector<String> phone_book) {
		boolean answer = true;	
		for(int j = 1;j<phone_book.size();j++) {
			double main = phone_book.indexOf(0);
			Double checkt;
			String a = phone_book.indexOf(0);
			checkt = phone_book.indexOf(j).substring(0,phone_book.indexOf(0).length());
			if(main ==checkt) {
				answer = false;
				break;
			}
		}
        return answer;   
    }
}