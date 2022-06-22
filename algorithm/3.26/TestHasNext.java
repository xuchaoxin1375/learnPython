import java.util.Scanner;

/*
 * @Description: 
 * @Version: 2.0
 * @Author: xuchaoxin
 * @Date: 2021-03-27 10:50:53
 * @LastEditors: xuchaoxin
 * @LastEditTime: 2021-03-27 11:04:32
 */

/*test in the windows OS platform:
 */
public class TestHasNext {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("testing");
        /* attention,this is to judge before input any contents:
        we found that the scanner need you input something,only input entered,the judge could return result(true/false) */
        System.out.println(scanner.hasNext());
        /* test continuos */
        while (scanner.hasNext()) {
            System.out.println(scanner.next());
        }
        System.out.println("testOver.");
        scanner.close();
    }
}
/* 
test like this input:

testing
3 4 5 
true
3
4
5
^Z
testOver.
 

test2:

testing
^Z
false
testOver.

*/