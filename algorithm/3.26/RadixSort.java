import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/*
 * @Description: 
 * @Version: 2.0
 * @Author: xuchaoxin
 * @Date: 2021-03-27 08:12:30
 * @LastEditors: xuchaoxin
 * @LastEditTime: 2021-03-27 12:05:56
 */
public class RadixSort {
    public static void sort(int[] number, int d, int radix) 
    {

        /* k: to traverse the number[] */
        int k = 0;
        /* n: as divisor to get digits to sort in that weight */
        int n = 1;
        /*
         * m: count the times of sort has been executed (the numbers is sorted in which
         * weight )
         */
        int m = 1;
        /*
         * handle the numbers input:the array stores complete numbers rather than signal
         * radix (or use a pointer array non_matrix structure to auxiliary the sort)
         */
        int[][] buckets = new int[radix][number.length];
        /*
         * the count array convey the sort method:counting sort（it's a stable sort
         * algorithm,and it is linear time sort method in many occasions ); (counting
         * the element of each bucket) the number of the buckets depends on the radix
         */
        int[] count = new int[radix];
        /* we need to sort d times */
        while (m <= d) {/* traverse the elements:to build the buckets */
            for (int i = 0; i < number.length; i++) {
                /* get the radix(lsd in the range(0,radix)) */
                int lsd = ((number[i] / n) % radix);
                /*
                 * according to the lsd ,to insert the elements to the buckets array separately
                 */
                buckets[lsd][count[lsd]] = number[i];
                /*
                 * counting radix (in count to calculate the index of the next element to place
                 * in the buckets
                 */
                count[lsd]++;
            }
            /* traverse all the buckets */
            for (int i = 0; i < radix; i++) {
                if (count[i] != 0)
                    /*
                     * traverse the elements in the same buckets; use the core part idea of the of
                     * counting sort: in the later,we iterate the number d times( digit d is the
                     * highest-order digit. ) (not by merge the sorted buckets)
                     */
                    for (int j = 0; j < count[i]; j++) {
                        /*
                         * update the elements in the input array(number[]):it can be think of as a sort
                         * pass
                         */
                        number[k] = buckets[i][j];
                        k++;
                    }
                /*
                 * reset all the counting array's elements in time(as soon as the bucket is
                 * used)
                 */
                count[i] = 0;
            }
            /*
             * update the weight to get new signal digits(number.lenth digits totally every
             * time) to make a new round sort
             */
            n *= radix;
            /* reset k */
            k = 0;
            /* counting the rounds that have been executed */
            m++;
        }
    }

    /**
     * the max in the input numbers
     */
    public static int max(int[] number) {
        // Arrays.sort(number);
        // return number[number.length-1];
        int maxElement = number[0];
        for (int i = 0; i < number.length; i++) {
            if (maxElement < number[i]) {
                maxElement = number[i];
            }
        }
        return maxElement;
    }

    /* get d(the highest-order digit) */
    public static int getD(int maxElement, int radix) {
        int d = 0;
        while (maxElement > 0) {
            maxElement /= radix;
            d++;
        }
        return d;
    }

    public static void main(String[] args) {
        // Scanner sc=new Scanner(System.in);
        // ArrayList<Integer> list=new ArrayList<>();
        // System.out.println("testing...");
        // /* attention! use Ctrl+z to end your input(if you use windows OS ) */
        // while(sc.hasNextInt()){//not use hasNext()
        //     int num= sc.nextInt();
        //     list.add(num);
        // }
        // sc.close();
        
        // /*list to int[] */
        // // int[] numbers=new int[list.size()];
        // // for(int i=0;i<list.size();i++){
        // //     numbers[i]=list.get(i);
        // // }
        // // Integer[] numbers=(Integer[])list.toArray();
        // /* another method to transition: */
        // int[] numbers=list.stream().mapToInt(Integer::intValue).toArray();

        
        /* use the built input to test the function: */
        // int[] numbers = { 73, 22, 93, 43, 55, 14, 28, 656844, 35649, 8441, 353, 10 };

        
        /* use random sequence to test: */
        Random random=new Random();
        int[] numbers=new int[100];
        for(int i=0;i<100;i++){
            numbers[i]=random.nextInt(900);
        }
        System.out.println("the input sequence is:");
        for(int element:numbers){
            System.out.print(element+" ");
        }
        System.out.println("");

        int d = getD(max(numbers), 100);
        RadixSort.sort(numbers, d,100);
        System.out.println("the sorted sequence:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        // System.out.println(getD(max(numbers), radix));
    }
}