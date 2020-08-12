package java;
public class DeviceDevelop {
	public static void main(String args[]) {
		int [] progesses = {93, 30, 55};
		int [] speeds = {1,30,5};
		
		Solution s = new Solution();
		
		for(int a: s.solution(progesses,speeds)) {
			System.out.println(a);
		}
	}

}

class Solution {
    int front;
    int rear;
    int [] stack;
    int length;
    int count;
    
    public Solution(){
        front = 0;
        rear = 0;
        count = 0;
        length = 10;
        stack = new int [length];
    }
    
    public void enqueue(int num){
        if(count == stack.length-1){
            int oldsize = length;
            length +=10;
            int [] term = new int [length];
            for(int i = 0;i<count; i++){
                term[i] = stack[front];
                front = (front+1)%oldsize;
            }
            stack = term;
            front = 1;
            rear = count;
        }
        
        stack[rear] = num;
        rear = (rear+1)%length;
        count++;
    }
    
    public int dequeue(){
    	if(count==0) {
    		return -1;
    	}
        count--;
        int a = stack[front];
        front = (front+1)%length;
        return a;
    }
    
    public int peek(){
    	if(count==0) {
    		return -1;
    	}
        return stack[front];
    }
    
    public void delete() {
    	if(count==0) {
    		return;
    	}
        count--;
        front = (front+1)%length;
    }
    
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer;
        for(int i = 0; i<progresses.length;i++){
            int a = 100-progresses[i];
            int b = a/speeds[i];
            if(a%speeds[i] !=0)
                b++;
            enqueue(b);
        }
        answer = new int [count];
        
        int idx = 0;
        while(count !=0){
        	int n = 0;
            int p = dequeue();
            n++;
            
            while(count !=0 &&peek()<=p){
                delete();
                n++;
            }
            answer[idx++] = n;
        }
        int [] term = new int [idx];
        for(int i = 0;i<term.length;i++) {
        	term[i] = answer[i];
        }
        answer = term;
        return answer;
    }
}