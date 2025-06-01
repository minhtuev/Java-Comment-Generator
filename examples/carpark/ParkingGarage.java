import java.util.ArrayList;

public class ParkingGarage {
    private ArrayList<Car> parkedCars;
    private int capacity;

    public ParkingGarage(int capacity) {
        this.capacity = capacity;
        this.parkedCars = new ArrayList<>();
    }

    public boolean parkCar(Car car) {
        if (parkedCars.size() >= capacity) {
            System.out.println("Garage is full. Cannot park " + car.getLicensePlate());
            return false;
        }
        parkedCars.add(car);
        System.out.println("Parked car: " + car.getLicensePlate());
        return true;
    }

    public boolean removeCar(String licensePlate) {
        for (Car car : parkedCars) {
            if (car.getLicensePlate().equals(licensePlate)) {
                parkedCars.remove(car);
                System.out.println("Removed car: " + licensePlate);
                return true;
            }
        }
        System.out.println("Car not found: " + licensePlate);
        return false;
    }

    public void listCars() {
        System.out.println("Cars currently parked:");
        for (Car car : parkedCars) {
            car.displayInfo();
        }
    }
}
