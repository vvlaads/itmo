import com.fastcgi.FCGIInterface;

import java.nio.charset.StandardCharsets;

public class Request {
    public String getRequestBody(FCGIInterface fcgiInterface) {
        return new String(fcgiInterface.request.inStream.buff, StandardCharsets.UTF_8);
    }
}
