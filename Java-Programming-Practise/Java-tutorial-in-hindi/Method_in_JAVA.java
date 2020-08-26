package com.java;

public class Method_in_JAVA {
    static int sum(int a, int b){
        return a + b;
    }

    static void myMethod() {
        System.out.println("I just got executed!");
    }

    public static void main(String[] args) {
        myMethod();
        int sum = sum(1,2);

        System.out.println(sum);
    }
}
