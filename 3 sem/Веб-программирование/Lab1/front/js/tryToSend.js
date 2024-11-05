function validateAll() {
    let xIsValid = validateX();
    let yIsValid = validateY();
    let rIsValid = validateR();
    if (xIsValid && yIsValid && rIsValid) {
        return true;
    } else {
        return false;
    }
}


function validateX() {
    const checkboxes = document.getElementsByClassName("checkbox");
    const error = document.getElementById("ErrorX");
    let count = 0;
    var values = ["-4", "-3", "-2", "-1", "0", "1", "2", "3", "4"]
    for (let i = 0; i < values.length; i++) {
        if (checkboxes[i].checked) {
            let value = checkboxes[i].value;
            if (!values.includes(value)) {
                error.innerHTML = "Неверное значение X";
                return false;
            }
            count += 1;
        }
    }
    if (count == 1) {
        error.innerHTML = "";
        return true;
    }
    else {
        error.innerHTML = "Выберите X";
        return false;
    }
}


function validateY() {
    const input = document.getElementById("inputY");
    let value = input.value;
    value = value.replace(",", ".");
    const error = document.getElementById("ErrorY");
    if (value == '') {
        error.innerHTML = "Не введено значение Y";
        return false;
    }
    if (isNaN(value)) {
        error.innerHTML = "Введите число в поле Y";
        return false;
    }
    if (value > 5 || value < -5) {
        error.innerHTML = "Введите число от -5 до 5";
        return false;
    }
    else {
        error.innerHTML = "";
        return true;
    }
}


function validateR() {
    let select = document.getElementById("selectR");
    let value = select.value;
    let error = document.getElementById("ErrorR");
    if (value == 1 || value == 1.5 || value == 2 || value == 2.5 || value == 3) {
        error.innerHTML = "";
        return true;
    }
    error.innerHTML = "Выбрано неверное значение";
    return false;
}


function sendRequest(params) {
    const table = document.getElementById("tableForResult");
    const checkboxes = document.getElementsByClassName("checkbox");
    let valueX = 0;
    for (let i = 0; i < 9; i++) {
        if (checkboxes[i].checked) {
            valueX = checkboxes[i].value;
            break;
        }
    }
    const input = document.getElementById("inputY");
    let valueY = input.value;
    valueY = valueY.replace(",", ".");
    const select = document.getElementById("selectR");
    let valueR = select.value;



    const method = "GET";
    let url = "/fcgi-bin/Lab1.jar";
    url += "?" + params.toString();
    let request = new XMLHttpRequest();

    request.open(method, url, false);
    request.send();
    if (request.status == 200) {
        value = request.responseText;
        table.innerHTML = table.innerHTML + value;
    } else {
        result.innerHTML = table.innerHTML + "<tr><td colspan=6>Ошибка отправки</td></tr>";
    }
}


function tryToSend() {
    const error = document.getElementById("ErrorSend");
    if (validateAll()) {
        error.innerHTML = "";
        sendRequest(params);
    } else {
        error.innerHTML = "Не удалось отправить";
    }
}
