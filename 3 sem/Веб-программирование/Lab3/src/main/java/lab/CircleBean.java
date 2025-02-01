package lab;

import jakarta.enterprise.context.SessionScoped;
import jakarta.inject.Inject;
import jakarta.inject.Named;

import java.io.Serializable;

@Named("circleBean")
@SessionScoped
public class CircleBean implements Serializable {
    private double correctX;
    private double correctY;
    private String color;
    @Inject
    private PointBean pointBean;

    public void transform(double x, double y) {
        double r = pointBean.parseCoordinate(pointBean.getR());
        correctX = x;
        correctY = y;
        correctX = correctX * 160 / r;
        correctY = correctY * 160 / r;
        correctX += 220;
        correctY += 220;
        correctY = 440 - correctY;
        color = pointBean.check(x, y, r) ? "red" : "grey";
    }

    public double getCorrectX() {
        return correctX;
    }

    public void setCorrectX(double correctX) {
        this.correctX = correctX;
    }

    public double getCorrectY() {
        return correctY;
    }

    public void setCorrectY(double correctY) {
        this.correctY = correctY;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}
