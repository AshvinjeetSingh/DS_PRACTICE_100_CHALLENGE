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


public class DeleteKDLL{
	
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

private static Node deleteHead(Node head){
		if(head==null || head.next==null) return null;
		Node temp=head;
		head=head.next;
		head.prev=null;
		temp.next=null;
		return head;

	}


private static Node deleteTail(Node head){
		if(head==null || head.next==null) return null;
		Node temp=head;
		while(temp.next!=null){
			temp=temp.next;
		}
		Node tail= temp.prev;
		tail.next=null;
		temp.prev=null;



		return head;

	}

	private static Node deleteAtGivenPosition(Node head,int pos){
		if(head==null) return null;
		Node sentinal=new Node(0);
		sentinal.next=head;
		Node current=sentinal.next;
		int cnt=0;
		while(current.next!=null){
				cnt++;
				if(cnt==pos){
					break;
				}
				current=current.next;
		}

		Node back =current.prev;
		Node front=current.next;
		if(back== null && front==null){
			return null;
		}
		else if(back==null && front!=null){
				deleteHead(head);
		}
		else if(back!=null && front==null){
			deleteTail(head);
		}

		back.next=front;
		front.prev=back;
		current.next=null;
		current.prev=null;
		return head;

	}



	public static void main(String[] args){
		int[] arr={1,3,4,5,6,2,3};
		Node head= ConvertArrToLL(arr);
		int pos=3;
		Node new1 = deleteAtGivenPosition(head,pos);
		print(new1);
	}
}