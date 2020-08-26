package com.java;

import java.util.Scanner;

public class Java_Arrays {
    public static void main(String[] args) {
        int [] marks;
        int input;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Array Size: ");

        input = scanner.nextInt();

//        for (int i = 0; i <= input; i++){
//            marks[i] = scanner.nextInt();
//        }

        String Cars[] ={"Honda", "Toyota", "Audi", "Bantly"};

        for (String value:Cars)
            System.out.println(value);
    }
}
