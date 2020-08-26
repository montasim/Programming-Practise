package com.java;

import java.util.Scanner;

public class Switch {
    public static void main(String[] args) {

        int age;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Your Age");

        age = scanner.nextInt();

        switch (age){
            case 18:
                System.out.println("Congratulation");
                break;

            case 50:
                System.out.println("Congratulation");
                break;

            default:
                System.out.println("Sorry");
        }
    }
}
