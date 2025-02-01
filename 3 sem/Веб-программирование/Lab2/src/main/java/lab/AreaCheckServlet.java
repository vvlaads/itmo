package lab;

import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class AreaCheckServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws NumberFormatException, IOException, ClassCastException {
        Date startDate = new Date();
        HttpSession httpSession = request.getSession();
        response.setContentType("text/html; charset=UTF-8");
        PrintWriter out = response.getWriter();
        String[] array = request.getParameterValues("x");
        ArrayList<Point> points = (ArrayList<Point>) httpSession.getAttribute("points");
        if (points == null) {
            points = new ArrayList<>();
        }
        for (String element : array) {
            double x = Double.parseDouble(element);
            double y = Double.parseDouble(request.getParameter("y"));
            double r = Double.parseDouble(request.getParameter("r"));
            Point point = new Point(x, y, r, check(x, y, r));
            point.setStartDate(startDate);
            point.setTime(new Date().getTime() - startDate.getTime());
            points.add(points.size(), point);
            out.println("<tr>");
            out.println("<td>" + point.getX() + "</td>");
            out.println("<td>" + point.getY() + "</td>");
            out.println("<td>" + point.getR() + "</td>");
            out.println("<td>" + point.isCheck() + "</td>");
            out.println("<td>" + new SimpleDateFormat("HH:mm:ss").format(point.getStartDate()) + "</td>");
            out.println("<td>" + point.getTime() + "с </td>");
            out.println("</tr>");
        }
        httpSession.setAttribute("points", points);
        out.close();
    }

    private boolean check(double x, double y, double r) {
        if (x >= 0 && y >= 0 && x <= r / 2 && y <= r) return true;
        if (x <= 0 && y >= 0 && y <= x + r) return true;
        return x <= 0 && y <= 0 && (x * x + y * y) <= r * r;
    }
}
