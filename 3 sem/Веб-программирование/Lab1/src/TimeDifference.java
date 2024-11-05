import java.util.Date;

public class TimeDifference {
    public double getTimeDifference(Date date1, Date date2) {
        long timeStart = date1.getTime();
        long timeStop = date2.getTime();
        double difference = timeStop - timeStart;
        difference /= 1000.0;
        return difference;
    }
}
