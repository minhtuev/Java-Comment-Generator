/**
 * Public class `Greeter` defines the main structure and logic for this component.
 */
public class Greeter {
    // Public method `greet` performs a specific task
    public void greet() {
        HelloWorld hw = new HelloWorld();
        hw.sayHello();
    }

    // Public method `main` performs a specific task
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.greet();
    }
}
