public class Check {
    public boolean checkPoint(double X, double Y, double R) {
        if (X >= 0 && Y <= 0 && Y >= -R) {
            // y = 2x -r => 2x = y + r
            if (2 * X <= Y + R)
                return true;
            else {
                return false;
            }
        } else if (X <= 0 && X >= (-R / 2) && Y <= 0 && Y >= -R) {
            return true;
        } else if (X <= 0 && Y >= 0) {
            // x^2+y^2=r^2
            if ((X * X + Y * Y) <= (R * R)) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
}
