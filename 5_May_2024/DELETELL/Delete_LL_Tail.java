class Node{
	int Data;
	Node next;

	Node(int Data1){
		this.Data=Data1;
		this.next=null;
	}
};



public class Delete_LL_Tail{
	private static Node convertArrToLL(int[] arr){
		Node head=new Node(arr[0]);
		Node mover=head;
		for(int i=1;i<arr.length;i++){
			Node temp=new Node(arr[i]);
			mover.next=temp;
			mover=temp;
			
		}
		return head;
	}

	private static Node deleteTail(Node head){
		// System.out.print(head.Data);
		if (head==null || head.next==null) return null;
		Node temp=head;
		while( temp.next.next!=null){
			temp=temp.next;
		}
		temp.next=null;
		return head;
	}

	private static void printLL(Node head){
		Node mover =head;
		while (mover!=null){
			System.out.print(mover.Data+" ");
			mover=mover.next;
		}
	}

	public static void main(String[] args){
		int[] arr={1,2,3,4,5,6,7,8,9,10};
		Node node =convertArrToLL(arr);
		Node ans=deleteTail(node);
		printLL(node);
		// System.out.print(ans);
	}
};