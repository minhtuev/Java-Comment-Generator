/**
 * This `Greeter` class demonstrates basic Java composition by creating a `HelloWorld` instance to print a greeting, showcasing object interaction.
 */
public class Greeter {
    // This method creates a `HelloWorld` instance and invokes its `sayHello` method to print a greeting.
    public void greet() {
        HelloWorld hw = new HelloWorld();
        hw.sayHello();
    }

    // This main method initializes a Greeter object and invokes its greet method to display a greeting message.
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.greet();
    }
}
