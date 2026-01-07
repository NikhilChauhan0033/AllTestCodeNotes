
// CSRF TOKEN HELPER
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// CLEAR FORM (Cancel Button)
function clearForm() {
    const form = document.getElementById("noteForm");
    if (form) {
        form.reset();
        const titleInput = form.querySelector('input[name="title"]');
        if (titleInput) titleInput.focus();
    }
}

// ADD NOTE (AJAX)
document.addEventListener("DOMContentLoaded", function () {
    const noteForm = document.getElementById("noteForm");

    if (noteForm) {
        noteForm.addEventListener("submit", function (e) {
            e.preventDefault();

            const formData = new FormData(noteForm);

            fetch("", {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCSRFToken()
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    alert(data.message);
                    return;
                }

                const noteHTML = `
                    <div id="note-${data.note.id}">
                        <h4>${data.note.title}</h4>
                        <p>${data.note.description}</p>
                        <small>${data.note.created_at}</small>
                        <br>
                        <a href="/edit-note/${data.note.id}/">Edit</a>
                        <button onclick="deleteNote(${data.note.id})">Delete</button>
                    </div>
                    <hr>
                `;

                document
                    .getElementById("notesList")
                    .insertAdjacentHTML("afterbegin", noteHTML);

                clearForm();
            })
            .catch(error => {
                console.error("Add note error:", error);
                alert("Something went wrong");
            });
        });
    }
});

// DELETE NOTE (AJAX)
function deleteNote(noteId) {
    if (!confirm("Delete this note?")) return;

    fetch(`/delete-note/${noteId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCSRFToken(),
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const noteDiv = document.getElementById(`note-${noteId}`);
            if (noteDiv) noteDiv.remove();
        }
    })
    .catch(error => {
        console.error("Delete error:", error);
        alert("Could not delete note");
    });
}

// EDIT NOTE (AJAX)
document.addEventListener("DOMContentLoaded", function () {
    const editForm = document.getElementById("editNoteForm");

    if (editForm) {
        editForm.addEventListener("submit", function (e) {
            e.preventDefault();

            const formData = new FormData(editForm);
            const noteId = window.location.pathname.split("/").filter(Boolean).pop(); // get note_id from URL

            fetch(`/edit-note/${noteId}/`, {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCSRFToken()
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    alert(data.message);
                    return;
                }

                alert("Note updated successfully!");

                // Redirect to dashboard after AJAX success
                window.location.href = "/dashboard/";
            })
            .catch(error => {
                console.error("Edit note error:", error);
                alert("Could not update note");
            });
        });
    }
});
