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


function sendForm() {
    const form = document.getElementById("form");

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        if (validateAll()) {
            const formData = new FormData(form);
            const params = new URLSearchParams();
            for (const [key, value] of formData.entries()) {
                if (key == "y") {
                    params.append(key, value.replace(",", "."));
                }
                else {
                    params.append(key, value);
                }
            }
            table = document.getElementById("tableForResult");
            const request = new XMLHttpRequest();
            const method = "GET";
            let url = "/fcgi-bin/Lab1.jar";
            url = url + "?" + params.toString();

            request.open(method, url, false);
            request.send();
            if (request.status == 200) {
                value = request.responseText;
                table.innerHTML = table.innerHTML + value;
            } else {
                table.innerHTML = table.innerHTML + "<tr><td colspan=6>Ошибка отправки</td></tr>";
            }
        }
    })
}

sendForm();
