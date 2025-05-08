document.addEventListener("DOMContentLoaded", function() {
    flatpickr("input[name='pub_date']", {
        dateFormat: "Y-m-d",
        allowInput: true
    });
});

