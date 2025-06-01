public class Main {
    public static void main(String[] args) {
        ParkingGarage garage = new ParkingGarage(2);

        Car car1 = new Car("ABC123", "Red");
        Car car2 = new Car("XYZ789", "Blue");
        Car car3 = new Car("LMN456", "Black");

        garage.parkCar(car1);
        garage.parkCar(car2);
        garage.parkCar(car3);  // Should fail

        garage.listCars();
        garage.removeCar("XYZ789");
        garage.listCars();
    }
}
