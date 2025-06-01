public class Greeter {
    public void greet() {
        HelloWorld hw = new HelloWorld();
        hw.sayHello();
    }

    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.greet();
    }
}
