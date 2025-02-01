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
    if (count >= 1) {
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
    if (value > 5 || value < -3) {
        error.innerHTML = "Введите число от -3 до 5";
        return false;
    }
    else {
        error.innerHTML = "";
        return true;
    }
}


function validateR() {
    const input = document.getElementById("inputR");
    let value = input.value;
    value = value.replace(",", ".");
    const error = document.getElementById("ErrorR");
    if (value == '') {
        error.innerHTML = "Не введено значение R";
        return false;
    }
    if (isNaN(value)) {
        error.innerHTML = "Введите число в поле R";
        return false;
    }
    if (value > 4 || value < 1) {
        error.innerHTML = "Введите число от 1 до 4";
        return false;
    }
    else {
        error.innerHTML = "";
        return true;
    }
}


function createFormListener() {
    const form = document.getElementById("form");
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        if (validateAll()) {
            const formData = new FormData(form);
            let array = [];
            let y;
            let r;
            for (const [key, value] of formData.entries()) {
                switch(key) {
                    case "x":
                        array.push(value);
                        break;
                    case "y":
                        y = value.replace(",", ".");
                        break;
                    case "r":
                        r = value.replace(",", ".");
                        break;
                }
            }
            sendMessage(array, y, r);
        }
    })
}

function sendMessage(x, y, r){
    let table = document.getElementById("tableForResult");
    let formBody = "";
    for (let i=0; i<x.length; i++){
        formBody += "x=" + x[i] + "&";
    }
    formBody += "y=" + y + "&";
    formBody += "r=" + r;
    $.ajax({
        url: "./index",
        type: "POST",
        contentType: "application/x-www-form-urlencoded",
        data: formBody,
        success: function(response){
            table.innerHTML += response;
            createPoints(x, y, r);
        }
    });
}

function createSVGListener(){
    const svg = document.getElementById("svg");
    svg.addEventListener("click", function(event){
        if (validateR()){
            let point = svg.createSVGPoint();
            point.x = event.clientX;
            point.y = event.clientY;
            let correctPoint = point.matrixTransform(svg.getScreenCTM().inverse());
            let r = document.getElementById("inputR").value.replace(",", ".");
            let x = Number(correctPoint.x);
            let y = 440 - Number(correctPoint.y);
            x -= 220;
            y -= 220;
            x = x * r / 160;
            y = y * r / 160;
            array = [];
            array.push(x);
            sendMessage(array, y, r);
        }
    });
}

function createPoints(array, y, r){
    const svg = document.getElementById("svg");
    let circles = document.getElementById("circles");
    for (let i=0; i<array.length; i++){
        let valueX = array[i];
        let valueY = y;
        valueX = valueX * 160 / r;
        valueY = valueY * 160 / r;
        valueX += 220;
        valueY += 220;
        valueY = 440 - valueY;
        circles.innerHTML += `<circle cx="${valueX}" cy="${valueY}" r="2" fill="#fd2f5b"/>`;
    }
}

function createInputRListener(){
    const table = document.getElementById("tableForResult");
    const input = document.getElementById("inputR");
    input.addEventListener("input", function(event){
        if (validateR()){
            let valueR = input.value.replace(",", ".");
            let circles = document.getElementById("circles");
            circles.innerHTML = "";
            for (const row of table.rows){
                let x = row.cells[0].textContent;
                if (!isNaN(x)) {
                    let y = row.cells[1].textContent;
                    array = [];
                    array.push(x);
                    createPoints(array, y, valueR);
                }
            }
        }
    });
}

window.onload = createFormListener();
window.onload = createSVGListener();
window.onload = createInputRListener();
