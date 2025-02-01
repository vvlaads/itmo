package lab;

import java.util.Date;

public class Point {
    private double x;
    private double y;
    private double r;
    private boolean check;
    private Date startDate;
    private double time;

    public Point(double x, double y, double r, boolean check) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.check = check;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getR() {
        return r;
    }

    public void setR(double r) {
        this.r = r;
    }

    public boolean isCheck() {
        return check;
    }

    public void setCheck(boolean check) {
        this.check = check;
    }

    public Date getStartDate() {
        return startDate;
    }

    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }

    public double getTime() {
        return time;
    }

    public void setTime(double time) {
        this.time = time;
    }
}
