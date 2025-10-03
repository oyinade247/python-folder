import java.util.Scanner;
public class Discount{
	public static void main(String [] args){

	Scanner input = new Scanner(System.in);

	System.out.print("Enter a price: ");
	int amount = input.nextInt();

	System.out.print("Enter percentage: ");
	double percent = input.nextInt();

	
	System.out.print(getMyDiscount(amount , percent));
	
	
	
	}

	public static double getMyDiscount(int price, double percentage ){

		double totalPercentage =  percentage / 100;
		
		double discount = price * totalPercentage;
		
		double total = price - discount;

		return total;
	}
}