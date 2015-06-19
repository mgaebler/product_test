var TREN = TREN || {};

$(function() {
    $(".needs-confirmation").on("click", function(e) {
        if (confirm("Möchtest Du wirklich alle Daten dieser Umfrage löschen?")) {
            window.location = $(this).attr("href");
        };
        return false;
    });

    // /my/umfragen
    $(".survey-button a.done").on("mouseover", function(e) {
        TREN.survey_button_title = $(this).html();
        $(this).html("Bearbeiten");
    });

    $(".survey-button a.done").on("mouseout", function(e) {
        $(this).html(TREN.survey_button_title);
    });

})
