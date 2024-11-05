import java.nio.charset.StandardCharsets;
import java.text.SimpleDateFormat;
import java.util.Date;

import com.fastcgi.FCGIInterface;

public class Main {
    public static void main(String[] args) {
        String fileName = "Lab1.jar";
        var fcgiInterface = new FCGIInterface();
        Request request = new Request();

        while (fcgiInterface.FCGIaccept() >= 0) {
            try {
                Date timeStart = new Date();
                String requestBody = request.getRequestBody(fcgiInterface);
                int index = requestBody.indexOf(fileName + "?");
                if (index != -1) {
                    index += fileName.length() + 1;
                    int endIndex = requestBody.indexOf(Character.MIN_VALUE + 1, index);
                    if (endIndex != -1) {
                        String[] params = requestBody.substring(index, endIndex).split("&");
                        try {
                            double x = Double.parseDouble(params[0].replace("x=", ""));
                            double y = Double.parseDouble(params[1].replace("y=", ""));
                            double r = Double.parseDouble(params[2].replace("r=", ""));
                            Validator validator = new Validator();
                            if (validator.validateX(x) && validator.validateY(y) && validator.validateR(r)) {
                                boolean result = new Check().checkPoint(x, y, r);
                                String content = "<tr>";
                                content += "\n<td>%s</td>".formatted(x);
                                content += "\n<td>%s</td>".formatted(y);
                                content += "\n<td>%s</td>".formatted(r);
                                content += "\n<td>%s</td>".formatted(result);
                                content += "\n<td>%s</td>".formatted(new SimpleDateFormat("HH:mm:ss")
                                        .format(timeStart));
                                content += "<td>%s</td>".formatted(new TimeDifference()
                                        .getTimeDifference(timeStart, new Date()) + " сек.");
                                content += "\n</tr>";
                                var httpResponse = """
                                        HTTP/1.1 200 OK
                                        Content-Type: text/html
                                        Content-Length: %d

                                        %s
                                        """.formatted(content.getBytes(StandardCharsets.UTF_8).length, content);
                                System.out.println(httpResponse);
                            }
                        } catch (NumberFormatException e) {
                            continue;
                        }
                    }
                }
            } catch (NullPointerException e) {
                continue;
            }
        }
    }
}