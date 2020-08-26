package com.java;

import java.util.Scanner;

public class For_Loop {
    public static void main(String[] args) {
        int input, i=1;

        Scanner scanner = new Scanner(System.in);

        System.out.println("How many times you want loop to run?");

        input = scanner.nextInt();

        for (; input >= i; i++){
            System.out.println(i);
        }
    }
}
