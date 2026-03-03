// We first start with a class then everything sits underneath the class first shout out 
// We end our code in java with ; like SQL
public class first {
    public static void main(String[] args){

        System.out.println("I like steak");
        System.out.println("It's wonderful");



//variable = a reuseable container for a value just like python has
// Primitive = simple value stored directly in memory (stack) so probably in the stack, this is right here for the taking
// Reference = memory address (stack) that points to the (heap) the heap holds the data in a little farther in the memory
//Primitive vs Reference
//int           string
//double this is like a float        array
//char          object
//boolean
//2 steps to creating a variable 1. declaration 2. assignment

        int age = 23;
        int year = 2025;
        int quantity = 3;
        double price = 1.1;
        char grade = 'A';
        boolean isStudent = true; 
        //
        //java used kamel case for variable names

        String name = "Sebastian";

        System.out.println("Hello " + name);


        System.out.println(age);
        System.out.println("The year is " + year);
        System.out.println(price);
        System.out.println(grade);
        System.out.println(isStudent);


        if(isStudent){
            System.out.println("You're a wizard harry");
        }
        else{
            System.out.println("You're not a wizard harry");
        }

    }

}