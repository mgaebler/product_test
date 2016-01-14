"use strict";

window.add_wysiwyg_editor = function(selector) {
    if (!selector) {
        selector = "#id_body";
    };

    var random = (new Date).getTime();
    var toolbar = '<div class="wysiwyg-toolbar btn-group" id="toolbar-' + random + '">';
    toolbar += '<a class="btn btn-default glyphicon glyphicon-bold" data-wysihtml5-command="bold"></a>';
    toolbar += '<a class="btn btn-default glyphicon glyphicon-italic" data-wysihtml5-command="italic"></a>';
    toolbar += '</div>';

    wysihtml5ParserRules.tags.a.set_attributes = {
        "rel": "nofollow",
        "target": "_blank"
    };

    $(selector).before(toolbar);
    var editor = new wysihtml5.Editor($(selector)[0], {
      toolbar: 'toolbar-' + random,
      parserRules:  wysihtml5ParserRules
    });
};

(function($) {
    $(document).ready(function() {
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

        $(".answer-post-link").on("click", function(e) {
            var modal = $('#edit-post-modal').modal();
            $.get($(this).attr("href"), function(data) {
                $(".modal-content").html(data);
            });
            return false;
        });

        $(".toogle-answers-link").on("click", function(e) {
            var answers_id = $(this).attr("data");
            $(".answers-" + answers_id).slideToggle();
        });

        var answer_id, post_id, body, title;  // Makes it available in post below
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
                $(".forum-entry-body", post).html(body);
                $('#edit-post-modal').modal("hide");
            });

            return false;
        })

        $(document).on("click", ".update-answer-button", function(e) {
            var form = $(this).parent("form");
            var action = form.attr("action");
            var csrf = $("input[name=csrfmiddlewaretoken]", form).val();
            answer_id = $("#answer_id", form).val();
            body = $("#id_body", form).val();

            var data = {
                "body": body,
                "csrfmiddlewaretoken": csrf,
            };

            $.post(action, data, function(content) {
                var answer = $("#answer-" + answer_id);
                $(".forum-entry-body", answer).html(body);
                $('#edit-post-modal').modal("hide");
            });

            return false;
        })

        $(".delete-gallery-image").on("click", function(e) {
            var link = $(this);
            var answer = window.confirm("Möchtest Du das Bild wirklich löschen?")
            if (answer) {
                $.get(link.attr("href"), function(data) {
                    link.parents(".image-wrapper").remove();
                });
                return false;
            }
            return false;
        });
    })
})(window.jQuery);
