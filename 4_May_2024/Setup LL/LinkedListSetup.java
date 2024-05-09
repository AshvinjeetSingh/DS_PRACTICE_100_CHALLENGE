class Node { 
    int data; 
    Node next; 

    Node(int data) { 
    this.data = data;
    this.next=null;
      }  //constructor to create a new node
};

public class LinkedListSetup {

    // code to convert arr to LL
    private static Node convertArrToLL(int[] arr){
        Node head = new Node(arr[0]);
        Node mover=head;
        for(int i=1;i<arr.length;i++){
            Node temp = new Node(arr[i]);
            mover.next=temp;
            mover=temp;
        }

        return head;
    };

    private static void traverseLL(int[] arr){
        Node head = convertArrToLL(arr);
        Node mover=head;
        int cnt=0;
        while (mover!=null){
            System.out.println(mover.data);
            mover=mover.next;
            cnt++;
        }
        System.out.println("cnt is "+cnt);
    };

    // main function
   public static void main(String[] args) {
      int[] intArray = {1,2,3,4,5,6,7,8,9,10};
      Node text= new Node(intArray[1]);
      Node ans=convertArrToLL(intArray);
      traverseLL(intArray);
      System.out.println(ans.data);
   }
}