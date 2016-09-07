public class BubbleSort {

	public static void main(String[] args) {
		int input[] = { 1, 2, 4, 5, 6, 77, 45 };
		printArray(input);
		int[] sorted = sort(input);
		printArray(sorted);
	}

	private static int[] sort(int[] input) {
		int n = input.length;
		for (int pass = 1; pass <= input.length; pass++) {
			
			for (int current = 0; current < n - pass; current++) {
				if(input[current] > input[current + 1]){
					int temp = input[current];
					input[current]= input[current + 1];
					input[current + 1] = temp;
				}
			}
			System.out.println("Pass " + pass);
			printArray(input);
		}
		
		return input;
	}

	private static void printArray(int[] input) {
		for (int i = 0; i < input.length; i++) {
			System.out.println(input[i]);
		}
		
	}

	
}
