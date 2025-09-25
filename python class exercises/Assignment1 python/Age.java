/*prompt two user to enter their age 
#collect the two user's age ranging from 1 to 80
#calculate how many years ago that the first user input is twice as old as the second user input and check the first user input on how old he would be if he is twice as old as his son
 



import java.util.Scanner;
public class Age{
	public static void main(String [] args){
       
        Scanner input = new Scanner(System.in);
        
     System.out.print("Enter your age papa chinedu: ");
      int fatherAge = input.nextInt();

	 System.out.print("Enter your age chinedu: ");
      int sonAge = input.nextInt();

	 int fatherAgeTwice = sonAge * 2
 
	if(fatherAge < fatherAgeTwice){
             System.out.printf("Father age will be %d if he is twice as old as his son",(fatherAge - fatherAgeTwice));
         }

	else{
           System.out.printf("%d years ago the father was twice as old as his son",(fatherAgeTwice - fatherAge));
	}

  }
}