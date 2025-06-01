/**
 * ```java
 * /**
 * * A simple class that demonstrates greeting by delegating to a HelloWorld instance.
 * */
 * ```
 */
public class Greeter {
    // This method creates a `HelloWorld` object and invokes its `sayHello` method to display a greeting.
    public void greet() {
        HelloWorld hw = new HelloWorld();
        hw.sayHello();
    }

    // This `main` method initializes a `Greeter` object and invokes its `greet()` method to display a greeting message.
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.greet();
    }
}
