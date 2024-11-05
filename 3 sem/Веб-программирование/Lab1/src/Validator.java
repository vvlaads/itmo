public class Validator {
    public boolean validateX(double x) {
        for (int i = -4; i <= 4; i++) {
            if (x == i) {
                return true;
            }
        }
        return false;
    }

    public boolean validateY(double y) {
        if (y >= -5 && y <= 5) {
            return true;
        }
        return false;
    }

    public boolean validateR(double r) {
        for (double i = 1; i <= 3; i += 0.5) {
            if (r == i) {
                return true;
            }
        }
        return false;
    }
}
