import java.util.Scanner;
public class DivideSquare{
	public static void main(String [] args){

	Scanner input = new Scanner(System.in);

	System.out.print("Enter any number: ");
	int numberOne = input.nextInt();

	 System.out.print(getSquare(numberOne));
	}

	public static double getSquare(int number){

	     if(number % 5 == 0){
		return Math.sqrt(number);

		}
	     	
		return number % 5;
		

	     
	   
	}
}

 