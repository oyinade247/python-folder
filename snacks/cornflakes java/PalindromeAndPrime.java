import java.util.Scanner;
public class PalindromeAndPrime{
	public static void main(String [] args){
	   Scanner input = new Scanner(System.in);

		System.out.print("Enter any number: ");
		int numberOne = input.nextInt();

		System.out.print(isPalindrome(numberOne));	 
		System.out.print(isPrime(numberOne));	 	

    }
	public static boolean isPalindrome(int number){
	
         String dividedNumber = "";

	 while(number > 0){
		int remainder = number % 10;
		dividedNumber += remainder;
		number /= 10;	
		
		
	  }
		int convertString = Integer.parseInt(dividedNumber);

		if(number == convertString){
			System.out.println("It is a palindrome");
			return true;
		
			
		}

		return false;
	   
	}


	public static boolean isPrime(int number){
		int count = 2;
		
		while(count < number) {
	
		if(number % count == 0){
			return false;
		}
		count++;
		}
				
		return true;
	}

}
	