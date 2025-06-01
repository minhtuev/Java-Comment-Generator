/**
 * This class handles greetings by invoking methods on a HelloWorld instance.
 */
public class Greeter {
    // This method creates a `HelloWorld` instance and invokes its `sayHello()` method to display a greeting.
    public void greet() {
        HelloWorld hw = new HelloWorld();
        hw.sayHello();
    }

    // Launches a greeting application by initializing a Greeter instance and triggering its greeting method.
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.greet();
    }
}
