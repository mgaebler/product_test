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

        $(".edit-post-link").on("click", function(e) {
            var modal = $('#edit-post-modal').modal();
            $.get($(this).attr("href"), function(data) {
                $(".modal-content").html(data);
            });
            return false;
        });

        var post_id, body, title;  // Makes it available in post beliw
        $(document).on("click", ".update-post-button", function(e) {
            var form = $(this).parent("form");
            var action = form.attr("action");
            var csrf = $("input[name=csrfmiddlewaretoken]", form).val();
            post_id = $("#post_id", form).val();
            body = $("#id_body", form).val();
            title = $("#id_title", form).val();

            var data = {
                "body": body,
                "title": title,
                "csrfmiddlewaretoken": csrf,
            };

            $.post(action, data, function(content) {
                var post = $("#post-" + post_id);
                $(".forum-entry-title h3", post).html(title);
                $(".forum-entry-body p", post).html(body);
                $('#edit-post-modal').modal("hide");
            });

            return false;
        })

    })
})(window.jQuery);
