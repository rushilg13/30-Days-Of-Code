// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
import java.lang.*;
import java.util.*;

class Three_Sum
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Length of Array: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0; i<n; i++)
        {
            System.out.println("Enter Element " + (i+1) + ": ");
            arr[i] = sc.nextInt();
        }

        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                for(int k=0; k<n; k++)
                {
                    if(i!=j && i!=k && j!=k && (arr[i] + arr[j] + arr[k] == 0))
                    {
                        int res[] = {arr[i], arr[j], arr[k]};
                        System.out.println("Result is: " + (Arrays.toString(res)));
                    }
                }
            }
        }
    }
}