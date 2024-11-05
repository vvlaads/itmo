$(function() {
    var checkboxes = $("input:checkbox");
    checkboxes.on("click", function(event) {
        checkboxes.prop("checked", function(number) {

            return checkboxes[number] == event.target

        })

    })

});