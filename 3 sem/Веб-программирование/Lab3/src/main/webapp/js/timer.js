function getTime() {
    let timer = document.getElementById("timer");
    let date = new Date();
    let hours = String(date.getHours()).padStart(2, '0');
    let minutes = String(date.getMinutes()).padStart(2, '0');
    let seconds = String(date.getSeconds()).padStart(2, '0');
    let time = `${hours}:${minutes}:${seconds}`;
    timer.innerHTML = time;
    setTimeout(getTime, 11000);
}

getTime();
