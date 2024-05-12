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



public class InsertLLAtK{
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

	private static Node InsertAtK(Node head,int value,int position){
		if(head==null || position==1){
			Node temp=new Node(value,head);
			return temp;
		}
		Node sentinal=new Node(0);
		sentinal.next=head;
		Node current=sentinal.next;
		int cnt=0;
		while(current.next!=null){
			cnt++;
			if(cnt==position){
				Node valve=new Node(value,current.next);
				current.next=valve;
				break;
			}
			current=current.next;
		}
		return head;
	}

	public static void main(String[] args){
		int[] arr={1,2,3,4,5,6,7,8,9,10};
		int value=4;
		int position=4;
		Node node =convertArrToLL(arr);
		Node temp=node;
		Node ans=InsertAtK(node,value,position);
		System.out.println("LL is");
		while (ans!=null){
			System.out.println(ans.Data);
			ans=ans.next;
		};
	}
};