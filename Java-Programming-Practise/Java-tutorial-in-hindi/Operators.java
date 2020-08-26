package com.java;

public class Operators {
    public static void main(String args[]){
    int num1 = 111;
    int num2 = 999;
        System.out.println (num2 + num1);
        System.out.println(num2 - num1);
        System.out.println(num2 * num1);
        System.out.println(num2 / num1);
        System.out.println(num2 % num1);
        //  System.out.println(num1++);
        //  System.out.println(++num1);

        num1 += 111;
        System.out.println(num1);

        num1 -= 111;
        System.out.println(num1);

        num1 *= 111;
        System.out.println(num1);

        num1 /= 111;
        System.out.println(num1);

        if (num1 == num2){
            System.out.println("Equal");
        }
        else if (num1 != num2){
            System.out.println("Not Equal");
        }
        else {
            System.out.println("Invalid");
        }


    }
}
