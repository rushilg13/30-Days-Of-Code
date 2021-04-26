// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

import java.lang.*;
import java.util.*;

class Two_Sum
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Length of Array: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        int res[] = new int[2];
        for(int i=0; i<n; i++)
        {
            System.out.println("Enter Element " + (i+1) + ": ");
            arr[i] = sc.nextInt();
        }
        System.out.println("Enter Target Value: ");
        int target = sc.nextInt();
        for(int i=0; i<n-1; i++)
        {
            if ((arr[i] + arr[i+1]) == target)
            {
                res[0] = i;
                res[1] = i+1;
                break;
            }
        }
        System.out.println("Result is: " + (Arrays.toString(res)));
    }
}