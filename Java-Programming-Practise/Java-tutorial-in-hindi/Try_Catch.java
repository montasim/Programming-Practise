package com.java;

public class Try_Catch {
    public static void main(String[] args) {
        String Cars[] ={"Honda", "Toyota", "Audi", "Bantly"};

        try {
            System.out.println(Cars[5]);
        }
        catch (Exception e){
            System.out.println(e);
        }

        System.out.println(Cars[1]);
    }
}
