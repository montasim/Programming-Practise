package com.java;

import java.util.Scanner;

public class Do_While_Loop {
    public static void main(String[] args) {
        int input, i=1;

        Scanner scanner = new Scanner(System.in);

        System.out.println("How many time you want the loop to run? ");

        input = scanner.nextInt();

        do {
            System.out.println(i);
            i++;
        }
        while (input >= i);
    }
}
