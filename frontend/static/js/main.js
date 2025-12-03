document.addEventListener('DOMContentLoaded', function () {
    // Edit Modal Logic
    const editButtons = document.querySelectorAll('.edit-btn');
    const editForm = document.getElementById('edit-form');

    if (editButtons.length > 0 && editForm) {
        editButtons.forEach(button => {
            button.addEventListener('click', function () {
                const id = this.getAttribute('data-id');
                const firstName = this.getAttribute('data-firstname');
                const lastName = this.getAttribute('data-lastname');
                const email = this.getAttribute('data-email');
                const position = this.getAttribute('data-position');
                const department = this.getAttribute('data-department');
                const salary = this.getAttribute('data-salary');
                const status = this.getAttribute('data-status');

                // Update Form Action
                editForm.action = `/candidates/${id}/edit`;

                // Populate Fields
                const fields = {
                    'edit_first_name': firstName,
                    'edit_last_name': lastName,
                    'edit_email': email,
                    'edit_position': position,
                    'edit_department': department,
                    'edit_expected_salary': salary,
                    'edit_status': status
                };

                for (const [id, value] of Object.entries(fields)) {
                    const field = document.getElementById(id);
                    if (field) field.value = value;
                }
            });
        });
    }

    // Delete Modal Logic
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const deleteForm = document.getElementById('delete-form');

    if (deleteButtons.length > 0 && deleteForm) {
        deleteButtons.forEach(button => {
            button.addEventListener('click', function () {
                const id = this.getAttribute('data-id');
                deleteForm.action = `/candidates/${id}/delete`;
            });
        });
    }

    // Auto-dismiss flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('[role="alert"]');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(msg => {
                msg.style.transition = "opacity 0.5s ease";
                msg.style.opacity = "0";
                setTimeout(() => msg.remove(), 500);
            });
        }, 5000);
    }
});
