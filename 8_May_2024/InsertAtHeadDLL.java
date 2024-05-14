class Node{
	int Data;
	Node next;
	Node prev;

	Node(int Data1,Node next1,Node prev1){
		this.Data=Data1;
		this.next=next1;
		this.prev=prev1;
	}

	Node(int Data1){
		this.Data=Data1;
		this.next=null;
		this.prev=null;
	}
};


public class InsertAtHeadDLL{
	
	private static void print(Node head){
		while(head!=null){
			System.out.println(head.Data);
			head=head.next;
		}
	
	}

	private static Node ConvertArrToLL(int[] arr){
		Node head=  new Node(arr[0]);
		Node prev =  head;
		for(int i=1;i<arr.length;i++){
			Node temp= new Node(arr[i],null,prev);
			prev.next=temp;
			prev=temp;
		}
		return head;

	}

	private static Node InsertBeforeHead(Node head,int Value){
			Node newHead= new Node(Value,head,null);
			head.prev=newHead;
			return newHead;

	}

	private static Node InsertAfterHead(Node head,int Value){
			Node temp= new Node(Value,head.next,head);
			head.next=temp;
			return head;

	}




	public static void main(String[] args){
		int[] arr={1,3,4,5,6,2,3};
		Node head= ConvertArrToLL(arr);
		int pos=3;
		Node new1 = InsertBeforeHead(head,8);
		// Node new2 = InsertAfterHead(head,8);
		System.out.println("Before Head");
		print(new1);
		// System.out.println("After Head");
		// print(new2);
	}
}