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


public class CreateDLL{
	
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

	public static void main(String[] args){
		int[] arr={1,3,4,5,6,2,3};
		Node head= ConvertArrToLL(arr);
		print(head);
	}
}