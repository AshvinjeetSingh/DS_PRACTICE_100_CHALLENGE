class Node{
	int Data;
	Node next;

	Node(int Data1){
		this.Data=Data1;
		this.next=null;
	}
};



public class Delete_LL_Head{
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

	private static Node deleteHead(Node head){
		if (head==null) return null;
		Node temp=head;
		head=head.next;
		System.out.println("Head\t"+head.Data);
		return head;
	}

	public static void main(String[] args){
		int[] arr={1,3,22};
		Node node =convertArrToLL(arr);
		deleteHead(node);
		// System.out.print(ans);
	}
};