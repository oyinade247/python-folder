/*prompt user to enter their score
collect user score
Check if the user score is greater than 90 or equals to 90 and give the result as A
Check again if the user score is greater than 80 and less than or equals  to 89 and give the result as B
Check again if the user score is greater than 70 and less than or equals  to 79 and give the result as C
#Check again if the user score is greater than 60 and less than or equals  to 69 and give the result as D
# else output F



import java.util.Scanner;
public class NumericalScore{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);
	
	System.out.print("Enter any score in numerical value: ");	
	int score = input.nextInt();

	if(score >= 90){
	 System.out.print("A");
	}
	
	else if(score >= 80 && score <= 89){
	 System.out.print("B");
	}
	
	else if(score >= 70 && score <= 79){
	 System.out.print("C");
	}

	else if(score >= 60 && score <= 69){
	 System.out.print("D");
	}

	else{
	 System.out.print("F");
	}
	}
}