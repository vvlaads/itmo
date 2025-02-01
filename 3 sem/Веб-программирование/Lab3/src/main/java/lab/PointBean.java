package lab;

import jakarta.enterprise.context.SessionScoped;
import jakarta.inject.Inject;
import jakarta.inject.Named;

import java.io.Serializable;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

@Named("pointBean")
@SessionScoped
public class PointBean implements Serializable {
    private String x;
    private String y;
    private String r;
    private double coordinateX;
    private double coordinateY;
    private ArrayList<Point> points = new ArrayList<>();
    @Inject
    private PointService pointService;

    public double parseCoordinate(String coordinate) {
        return Double.parseDouble(coordinate.replace(",", "."));
    }

    public void submit() {
        System.out.println(x);
        System.out.println(x.equals("1.0"));
        Date startDate = new Date();
        String date = new SimpleDateFormat("HH:mm:ss").format(startDate);
        double valueX = parseCoordinate(x);
        double valueY = parseCoordinate(y);
        double valueR = parseCoordinate(r);
        boolean result = check(valueX, valueY, valueR);
        Point point = new Point(valueX, valueY, valueR, result, date, new Date().getTime() - startDate.getTime());
        points.add(point);
        pointService.addPoint(point);
    }

    public void createPoint() {
        Date startDate = new Date();
        String date = new SimpleDateFormat("HH:mm:ss").format(startDate);
        double valueR = parseCoordinate(r);

        coordinateX -= 220;
        coordinateY = 440 - coordinateY;
        coordinateY -= 220;
        coordinateX *= valueR / 160;
        coordinateY *= valueR / 160;
        boolean result = check(coordinateX, coordinateY, valueR);
        Point point = new Point(coordinateX, coordinateY, valueR, result, date, new Date().getTime() - startDate.getTime());
        points.add(point);
        pointService.addPoint(point);
    }

    public boolean check(double x, double y, double r) {
        if (x <= 0 && y >= 0 && y <= r && x >= -r / 2) return true;
        if (x <= 0 && y <= 0 && y >= -x / 2 - r / 2) return true;
        return x >= 0 && y <= 0 && x * x + y * y <= r * r / 4;
    }

    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public String getR() {
        return r;
    }

    public void setR(String r) {
        this.r = r;
    }

    public double getCoordinateX() {
        return coordinateX;
    }

    public void setCoordinateX(double coordinateX) {
        this.coordinateX = coordinateX;
    }

    public double getCoordinateY() {
        return coordinateY;
    }

    public void setCoordinateY(double coordinateY) {
        this.coordinateY = coordinateY;
    }

    public ArrayList<Point> getPoints() {
        return points;
    }

    public void setPoints(ArrayList<Point> points) {
        this.points = points;
    }
}
