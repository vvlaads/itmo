const form = document.getElementById("form");

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(form);
    const params = new URLSearchParams();
    for (const [key, value] of formData.entries()) {
        params.append(key, value);
    }
    alert(params);
    let request = new XMLHttpRequest();

    const method = "GET";
    let url = "/fcgi-bin/Lab1.jar";
    url = url + "?" + params.toString();
    alert(url);

    request.open(method, url, false);
    request.send();
    if (request.status == 200) {
        value = request.responseText;
        table.innerHTML = table.innerHTML + value;
    } else {
        result.innerHTML = table.innerHTML + "<tr><td colspan=6>Ошибка отправки</td></tr>";
    }
})