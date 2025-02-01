document.getElementById("tdForImg").addEventListener("click", function(event){
    console.log("create");
    let svg = document.getElementById("svg");
    let point = svg.createSVGPoint();
    point.x = event.clientX;
    point.y = event.clientY;
    let correctPoint = point.matrixTransform(svg.getScreenCTM().inverse());
    console.log(correctPoint.x);
    console.log(correctPoint.y);
    document.getElementById("form:xCoordinate").value = correctPoint.x;
    document.getElementById("form:yCoordinate").value = correctPoint.y;
    document.getElementById("form:hiddenButton").click();
});
