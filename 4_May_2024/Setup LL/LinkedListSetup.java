class Node { 
    int data; 
    Node next; 

    Node(int data) { 
    this.data = data;
    this.next=null;
      }  //constructor to create a new node
};

public class LinkedListSetup {

   public static void main(String[] args) {
      int[] intArray = {1,2,3,4,5,6,7,8,9,10};
      Node text= new Node(intArray[1]);
      System.out.println(text.data);
   }
}