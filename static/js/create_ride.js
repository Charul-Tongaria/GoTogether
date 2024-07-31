document.getElementById("decrement").addEventListener("click", function() {
    var value = parseInt(document.getElementById("num_passengers").value, 10);
    value = isNaN(value) ? 0 : value;
    value < 1 ? value = 1 : '';
    value--;
    document.getElementById("num_passengers").value = value;
});

document.getElementById("increment").addEventListener("click", function() {
    var value = parseInt(document.getElementById("num_passengers").value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById("num_passengers").value = value;
});
