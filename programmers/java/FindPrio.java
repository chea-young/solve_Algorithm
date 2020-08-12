package java;

public class FindPrio {

	public static void main(String [] args) {
		FindPrio pw = new FindPrio();
		int[] p = {1,1,9,1,1,1};
		int num = 0;
		System.out.println(pw.solution(p, num));
		
		FindPrio pn = new FindPrio();
		int[] q = {2,1,3,2};
		int nu = 2;
		System.out.println(pn.solution(q, nu));
		
	}
	
	class ListNode{
		ListNode rlink;
		ListNode llink;
		int data;
		int index;
	}
	
	public ListNode head;
	public ListNode tail;
	
	public FindPrio() {
		head = null;
		tail = null;
	}
	
	void enqueue(int x, int i) {
		ListNode newnode = new ListNode();
		newnode.data = x;
		newnode.index = i;
		if(head==null) 
			head = tail = newnode;
		else {
			tail.rlink = newnode;
			newnode.llink = tail;
			newnode.rlink = null;
			tail = newnode;
			}
	}
	
	void delete(ListNode p) {
		if(p==null) {
			throw new NullPointerException();
		}
		if(p.llink!=null) {
			p.llink.rlink = p.rlink;
		}else {
			head=head.rlink;
		}
		
		if(p.rlink!=null) {
			p.rlink.llink=p.llink;
		}else {
			tail=tail.llink;
		}
	}
	
	public ListNode findP() {
		ListNode find = head;
		ListNode next = head.rlink;
		
		while(next !=null) {
			if(next.data > find.data) {
				find = next;
				enqueue(head.data, head.index);
			    delete(head);
			    
			    find = head;
			    next = find.rlink;
			}
			else{
				next = next.rlink;
			}
		}
		
		 
			
		
		return find; 
	}
	
	public int solution(int[] priorities, int location) {
		FindPrio a = new FindPrio();
		
        int answer = 0;
        int index = priorities.length;
        int[] print = new int [index];
        
        for(int i = 0;i<index;i++) {
        	a.enqueue(priorities[i], i);
        }
        
        for(int j = 0; j<index; j++) {
        	ListNode ma = a.findP();
        	print[j] = ma.index;
        	a.delete(ma);
        	System.out.println("print"+print[j]);
        }
        
       
        for(int l = 0; l<index; l++) {
        	if(print[l] == location) {
        		answer = l;
        		break;
        	}
        }
        
        
        return answer+1;
    }
}
