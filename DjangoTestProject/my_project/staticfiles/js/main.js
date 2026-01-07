function clearForm() {
    const form = document.getElementById("noteForm");
    if (form) {
        form.reset();
        form.querySelector('input[name="title"]').focus();
    }
}
