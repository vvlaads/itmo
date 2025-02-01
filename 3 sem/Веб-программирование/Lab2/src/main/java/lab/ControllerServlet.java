package lab;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.*;

public class ControllerServlet extends HttpServlet {
    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        RequestDispatcher requestDispatcher = request.getRequestDispatcher("index.jsp");
        requestDispatcher.forward(request, response);
    }

    @Override
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        String[] x = request.getParameterValues("x");
        if (x != null && request.getParameter("y") != null && request.getParameter("r") != null) {
            RequestDispatcher requestDispatcher = request.getRequestDispatcher("./servlet/area");
            requestDispatcher.forward(request, response);
        } else {
            PrintWriter out = response.getWriter();
            out.println("<tr>");
            out.println("<td colspan='6'> Ошибка </td>");
            out.println("</tr>");
            out.close();
        }
    }
}
