document.addEventListener('DOMContentLoaded', function() {
    const cities = [
        "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Ahmedabad", "Surat",
        "Kanpur", "Nagpur", "Indore", "Bhopal", "Visakhapatnam", "Vadodara", "Coimbatore", "Mysore", "Chandigarh", "Guwahati"
    ];
    const populateDropdowns = () => {
        const leavingDropdown = document.getElementById('leaving_from_dropdown');
        const goingDropdown = document.getElementById('going_to_dropdown');
    
        cities.forEach(city => {
            const option = document.createElement('option');
            option.value = city;
            option.textContent = city;
            leavingDropdown.appendChild(option);
            goingDropdown.appendChild(option.cloneNode(true));
        });
    };
    
    // Set the input field value based on dropdown selection
    const setInputValue = (inputId, value) => {
        document.getElementById(inputId).value = value;
    };
    
    // Initialize dropdowns on page load
    window.onload = populateDropdowns;
});

function changePassengerCount(change) {
    const input = document.getElementById('passenger_count');
    let currentValue = parseInt(input.value, 10);
    currentValue += change;

    if (currentValue < 1) {
        currentValue = 1;
    } else if (currentValue > 10) {
        currentValue = 10;
    }

    input.value = currentValue;
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const oldPassword = document.querySelector('#old_password');
    const newPassword = document.querySelector('#password');
    const confirmPassword = document.querySelector('#confirm_password');
    const errorMessage = document.querySelector('.error-message');
    
    form.addEventListener('submit', function(event) {
        errorMessage.textContent = '';
        if (newPassword.value === oldPassword.value) {
            errorMessage.textContent = 'New password cannot be the same as the old password.';
            event.preventDefault();
        } else if (newPassword.value !== confirmPassword.value) {
            errorMessage.textContent = 'Passwords do not match.';
            event.preventDefault();
        }
    });
});

