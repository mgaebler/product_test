(function($) {
    $(document).ready(function() {

        "use strict";
        var survey_button_title;

        $(".needs-confirmation").on("click", function(e) {
            if (confirm("Möchtest Du wirklich alle Daten dieser Umfrage löschen?")) {
                window.location = $(this).attr("href");
            };
            return false;
        });

        // /my/umfragen
        $(".survey-button a.done").on("mouseover", function(e) {
            survey_button_title = $(this).html();
            $(this).html("Bearbeiten");
        });

        $(".survey-button a.done").on("mouseout", function(e) {
            if (survey_button_title) {
                $(this).html(survey_button_title);
            };
        });
    
    })
})(window.jQuery);
