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

document.addEventListener('DOMContentLoaded', function() {
    // Check if the user is logged in
    const isLoggedIn = false; // Replace this with a real check, possibly from Django template or cookies

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(event) {
            if (!isLoggedIn) {
                event.preventDefault(); // Prevent the default action
                alert('You need to be logged in to access this page.');
                window.location.href = '/login/'; // Redirect to the login page
            }
        });
    });
});
