import java.util.Scanner;
public class InvestmentAmount{
	public static void main(String [] args){

	Scanner input = new Scanner(System.in);

	System.out.print("Enter investment amount: ");
	int investment = input.nextInt();

	System.out.print("Enter monthly rate: ");
	double percent = input.nextInt();

	System.out.print("Enter number of years: ");
	double years  = input.nextInt();


	
	System.out.print(getInvestment(investment , percent, years));
	
	
	
	}

	public static double getInvestment(int investmentAmount, double monthlyRate, int year ){

		double rate = 1 +(monthlyRate / 100);
		double futureInvestment =  investmentAmount * Math.pow(rate, year);
		
				
		double total = futureInvestment;

		return total;
	}
}