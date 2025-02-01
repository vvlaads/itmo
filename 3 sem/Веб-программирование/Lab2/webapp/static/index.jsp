<%@ page contentType="text/html; charset=utf-8" pageEncoding="utf-8" %>
<%@ page import="lab.Point" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="java.text.SimpleDateFormat" %>
<%@ page import="java.util.Date" %>

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>
        Лабораторная 2
    </title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
</head>

<body>
    <header>
        <table id="header">
            <tr id="headerRow">
                <th id="headerName">
                    <h1>Силинцев Владислав Витальевич</h1>
                </th>
                <th id="headerGroup">
                    <h1>P3214</h1>
                </th>
                <th id="headerOption">
                    <h1>311498</h1>
                </th>
            </tr>
        </table>
    </header>
    <table id="main">
        <form id="form">
            <tr id="row1">
                <td id="tdForX">
                    <p id="messageForX" class="label">Значение X:

                        <input type="checkbox" value="-4" id="option1" class="checkbox" name="x"> -4
                        <input type="checkbox" value="-3" id="option2" class="checkbox" name="x"> -3
                        <input type="checkbox" value="-2" id="option3" class="checkbox" name="x"> -2
                        <input type="checkbox" value="-1" id="option4" class="checkbox" name="x"> -1
                        <input type="checkbox" value="0" id="option5" class="checkbox" name="x"> 0
                        <input type="checkbox" value="1" id="option6" class="checkbox" name="x"> 1
                        <input type="checkbox" value="2" id="option7" class="checkbox" name="x"> 2
                        <input type="checkbox" value="3" id="option8" class="checkbox" name="x"> 3
                        <input type="checkbox" value="4" id="option9" class="checkbox" name="x"> 4
                    </p>
                    <span id="ErrorX" class="error"></span>
                </td>
                <td id="tdForImg" rowspan="3">
                    <svg id="svg" width="440" height="440" xmlns="http://www.w3.org/2000/svg">
                        <g transform="scale(2.0)" id="area">
                            <rect width="40" height="80" fill="#3cb0fe" x="110" y="30"/>
                            <path fill="#3cb0fe" d="M110 110 H 30 L 110 30 Z"/>
                            <path d="M110 110 L110,190 A80,80 0 0,1 30,110" fill="#3cb0fe"/>
                        </g>
                        <g transform="scale(2.0)">
                            <path stroke="black" fill="white" d="M110 110 H210 M210 110 L205 107 M210 110 L 205 113
                             M110 110 H 10 M 110 110 V210 M110 110 V10 M110 10 L107 15 M 110 10 L113 15"/>
                        </g>
                        <g transform="scale(2.0)">
                            <path stroke="black" d="M30 108 V 112"/>
                            <path stroke="black" d="M70 108 V 112"/>
                            <path stroke="black" d="M150 108 V 112"/>
                            <path stroke="black" d="M190 108 V 112"/>
                        </g>
                        <g transform="scale(2.0)">
                            <path stroke="black" d="M108 30 H 112"/>
                            <path stroke="black" d="M108 70 H 112"/>
                            <path stroke="black" d="M108 150 H 112"/>
                            <path stroke="black" d="M108 190 H 112"/>
                        </g>
                        <g transform="scale(2.0)">
                            <text x="120" y="10" font-size="x-small">y</text>
                            <text x="210" y="100" font-size="x-small">x</text>

                            <text x="30" y="100" font-size="xx-small">-R</text>
                            <text x="70" y="100" font-size="x-small">-R/2</text>
                            <text x="150" y="100" font-size="x-small">R/2</text>
                            <text x="190" y="100" font-size="x-small">R</text>

                            <text x="120" y="30" font-size="x-small">R</text>
                            <text x="120" y="70" font-size="x-small">R/2</text>
                            <text x="120" y="150" font-size="x-small">-R/2</text>
                            <text x="120" y="190" font-size="x-small">-R</text>
                        </g>
                        <g id="circles">
                        </g>
                    </svg>
                </td>
            </tr>
            <tr id="row2">
                <td id="tdForY">
                    <p id="messageForY" class="label">Значение Y:
                        <input type="text" id="inputY" placeholder="Введите число от -3 до 5" class="input" name="y">
                    </p>
                    <span id="ErrorY" class="error"></span>
                </td>
            </tr>
            <tr id="row3">
                <td id="tdForR">
                    <p id="messageForR" class="label">Значение R:
                        <input type="text" id="inputR" placeholder="Введите число от 1 до 4" class="input" name="r">
                    </p>
                    <span id="ErrorR" class="error"></span>
                </td>
            </tr>
            <tr id="row4">
                <td id="tdForButton" colspan="2">
                    <button id="button">
                        <h2>Отправить</h2>
                    </button>
                    <div id="ErrorSend" class="error"></div>
                </td>
            </tr>
        </form>
        <tr id="row5">
            <td colspan="2">
        </tr>
        <tr id="row6">
            <td id="tdForResult" colspan="2">
                <table id="tableForResult">
                    <tr>
                        <th id="resultX">X</th>
                        <th id="resultY">Y</th>
                        <th id="resultR">R</th>
                        <th id="result">Результат</th>
                        <th id="time">Время отправки</th>
                        <th id="timeForExecution">Время обработки</th>
                    </tr>
                    <%
                        ArrayList<Point> points = (ArrayList<Point>) session.getAttribute("points");
                        if (points!=null){
                            for (Point point: points){
                                out.println("<tr>");
                                out.println("<td>" + point.getX() + "</td>");
                                out.println("<td>" + point.getY() + "</td>");
                                out.println("<td>" + point.getR() + "</td>");
                                out.println("<td>" + point.isCheck() + "</td>");
                                out.println("<td>" + new SimpleDateFormat("HH:mm:ss").format(point.getStartDate()) + "</td>");
                                out.println("<td>" + point.getTime() + "с </td>");
                                out.println("</tr>");
                            }
                        }
                    %>
                </table>
            </td>
        </tr>
    </table>
    <script src="js/script.js"></script>
</body>

</html>