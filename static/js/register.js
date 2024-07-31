document.addEventListener("DOMContentLoaded", function() {
    const usernameInput = document.getElementById('id_username');
    const firstNameInput = document.getElementById('id_first_name');
    const lastNameInput = document.getElementById('id_last_name');
    const emailInput = document.getElementById('id_email');
    const password1Input = document.getElementById('id_password1');
    const password2Input = document.getElementById('id_password2');

    const usernameReq = document.getElementById('username-req');
    const firstNameReq = document.getElementById('first-name-req');
    const lastNameReq = document.getElementById('last-name-req');
    const emailReq = document.getElementById('email-req');
    const password1Req = document.getElementById('password1-req');
    const password2Req = document.getElementById('password2-req');

    usernameInput.addEventListener('input', () => {
        if (usernameInput.value.length >= 3) {
            usernameReq.classList.remove('red');
            usernameReq.classList.add('green');
        } else {
            usernameReq.classList.remove('green');
            usernameReq.classList.add('red');
        }
    });

    firstNameInput.addEventListener('input', () => {
        if (firstNameInput.value.trim() !== '') {
            firstNameReq.classList.remove('red');
            firstNameReq.classList.add('green');
        } else {
            firstNameReq.classList.remove('green');
            firstNameReq.classList.add('red');
        }
    });

    lastNameInput.addEventListener('input', () => {
        if (lastNameInput.value.trim() !== '') {
            lastNameReq.classList.remove('red');
            lastNameReq.classList.add('green');
        } else {
            lastNameReq.classList.remove('green');
            lastNameReq.classList.add('red');
        }
    });

    emailInput.addEventListener('input', () => {
        const emailPattern = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
        if (emailPattern.test(emailInput.value)) {
            emailReq.classList.remove('red');
            emailReq.classList.add('green');
        } else {
            emailReq.classList.remove('green');
            emailReq.classList.add('red');
        }
    });

    password1Input.addEventListener('input', () => {
        if (password1Input.value.length >= 8 && /\d/.test(password1Input.value)) {
            password1Req.classList.remove('red');
            password1Req.classList.add('green');
        } else {
            password1Req.classList.remove('green');
            password1Req.classList.add('red');
        }
    });

    password2Input.addEventListener('input', () => {
        if (password2Input.value === password1Input.value) {
            password2Req.classList.remove('red');
            password2Req.classList.add('green');
        } else {
            password2Req.classList.remove('green');
            password2Req.classList.add('red');
        }
    });
});
