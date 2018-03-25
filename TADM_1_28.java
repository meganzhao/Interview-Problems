//A function to perform the integer divison without using the / or * operatiors
//The class takes the 2 arguments: divident and divisor

public class TADM_1_28{
	public static int division(int divident, int divisor){
		if (divident < divisor){
			return 0;
		} else{
			return 1 + division(divident-divisor, divisor);
		}
	}

	public static void main(String[] args){
		System.out.println(division(Integer.valueOf(args[0]),Integer.valueOf(args[1])));
	}
}
