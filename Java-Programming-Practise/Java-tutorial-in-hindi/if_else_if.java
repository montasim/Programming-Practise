package com.java;

import java.util.Scanner;

public class if_else_if {
    public static void main(String args[]){

        //int num1, num2;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter num1: ");
        int num1 = scanner.nextInt();

        System.out.println("Enter num2");
        int num2 = scanner.nextInt();

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
