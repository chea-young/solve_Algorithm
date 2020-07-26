
public class PreTest {
	public static void main(String[] args) {
		PreTest person = new PreTest();
		int [] term = {1,2,3,4,5};
		int [] num = person.solution(term);
		for(int a: num) {
			System.out.println(a);
		}
		System.out.println("finish");
		
		
	}
	public int[] solution(int[] answers) {
        int[] answer = {};
    
        int [] an1 = new int [answers.length];
        int [] an2 = new int [answers.length];
        int [] an3 = new int [answers.length];
        
        for(int i = 0; i<answers.length;i++) {
        	switch(i%5) {
        	case 0:
        		an1[i] = 1;
        		break;
        	case 1:
        		an1[i] = 2;
        		break;
        	case 2 :
        		an1[i] = 3;
        		break;
        	case 3:
        		an1[i] = 4;
        		break;
        	case 4:
        		an1[i] = 5;
        		break;
        	}
        	
        	switch(i%8) {
        	case 0: case 2: case 4 : case 6:
        		an2[i] = 2;
        		break;
        	case 1 :
        		an2[i] = 1;
        		break;
        	case 3:
        		an2[i] = 3;
        		break;
        	case 5: 
        		an2[i] = 4;
        		break;
        	case 7:
        		an2[i] = 5;
        		break;
        	}
        	
        	switch(i%10) {
        	case 0: case 1:
        		an3[i] = 3;
        		break;
        	case 2: case 3:
        		an3[i] = 1;
        		break;
        	case 4: case 5:
        		an3[i] = 2;
        		break;
        	case 6: case 7:
        		an3[i] = 4;
        		break;
        	case 8: case 9:
        		an3[i] = 5;
        		break;
        	}
        }
       
        int []count = new int [4];
        for(int i=0;i<count.length;i++) {
        	count[i] = 0;
        }
        
        for(int i=0; i<answers.length;i++) {
        	if(answers[i] == an1[i]) {
        		count[1]++;
        	}
        	if(answers[i] == an2[i]) {
        		count[2]++;
        	}
        	if(answers[i] == an3[i]) {
        		count[3]++;
        	}
        }
        int max = count[0];
        for(int i= 0; i<count.length;i++) {
        	if(max<count[i])
        		max = count[i];
        }
        
        int ind = 0;
        for(int i = 0;i<count.length;i++) {
        	if(max==count[i]) {
        		ind++;
        	}
        }
        
        answer = new int [ind];
        ind=0;
        for(int i = 0;i<count.length;i++) {
        	if(max==count[i]) {
        		answer[ind] = i;
        		ind++;
        	}
        }
        return answer;
    }
	
}