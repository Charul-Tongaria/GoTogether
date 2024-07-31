function validateInput(input) {
    const fieldRequirement = input.nextElementSibling;
    if (input.value.trim() === '') {
        fieldRequirement.style.color = 'red';
        fieldRequirement.textContent = '* Required';
    } else {
        fieldRequirement.style.color = 'green';
        fieldRequirement.textContent = 'Looks good!';
    }
}
