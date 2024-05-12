class Node{
	int Data;
	Node next;

	Node(int Data1,Node node1){
		this.Data=Data1;
		this.next=node1;
	}

	Node(int Data1){
		this.Data=Data1;
		this.next=null;
	}
};



public class InsertLLTail{
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

	private static Node InserTail(Node head,int value){
		Node temp=head;
		while (temp.next!=null){
			temp=temp.next;
		}
		Node last=new Node(value);
		temp.next=last;
		return head;
	}

	public static void main(String[] args){
		int[] arr={1,2,3,4,5,6,7,8,9,10};
		int value=11;
		Node node =convertArrToLL(arr);
		Node temp=node;
		Node ans=InserTail(node,value);
		System.out.println("LL is");
		while (ans!=null){
			System.out.println(ans.Data);
			ans=ans.next;
		};
	}
};