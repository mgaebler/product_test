$(function() {
    $(".needs-confirmation").on("click", function(e) {
        if (confirm("Möchtest Du wirklich alle Daten dieser Umfrage löschen?")) {
            window.location = $(this).attr("href");
        };
        return false;
    });
})
