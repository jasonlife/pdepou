/**
 * Util functions
 */

var utils = {
    /**
     * Function that shows a message error
     * @param type: Error type
     * @param text: Text to show
     */
    show_pnotify: function(type, text) {
        new PNotify({
            text: text,
            hide: true,
            delay: 4000,
            type: type
        });
    },

    /**
     * Function that obtains a post modal template
     * @param post_id: Post's id to template download
     */
    get_post: function (post_id) {
        // If the modal is not we bring
        var $modal = $("#modal_" + post_id);
        if ($modal.length == 0) {
            $.get("blog/post/?post_id=" + post_id, function (html) {
                $("#modals").append(html);
                var $modal = $("#modal_" + post_id);
                $modal.modal("show");
                utils.get_gists($modal);
            }).fail(function () {
                utils.show_pnotify("warning", "Ha habido un problema obteniendo el post");
            });
        } else $modal.modal("show");
    },

    /**
     * Function that obtains the post's gists
     * @param $modal: Modal JQuery object
     */
    get_gists: function($modal) {
        var $gists = $modal.find("div[gist^='https://gist.github.com/']");
        if($gists.length) {
            $gists.each(function(index, element) {
                $.getJSON($(element).attr("gist") + "on?callback=?", function(data) {
                    $(element).append(data.div);
                    utils.add_stylesheet_gist(data.stylesheet)
                });
            });
        }
    },

    /**
     * Function that add gist's style
     * @param url: Gist url
     */
    add_stylesheet_gist: function(url) {
        var $head = $("head");
        if ($head.find("link[rel='stylesheet'][href='" + url + "']").length < 1)
            $head.append('<link rel="stylesheet" href="' + url + '" type="text/css" />');
    },

    /**
     * Function that get all comment attrs
     * @param post_id: Comment's post id
     * @param csrf_token: Form's csrf token
     * @returns {*}
     */
    get_comment: function(post_id, csrf_token) {
        return {
            "name": $("#comment_name_" + post_id).val(),
            "email": $("#comment_email_" + post_id).val(),
            "text": $("#comment_body_" + post_id).val(),
            "post_id": post_id,
            "csrfmiddlewaretoken": csrf_token
        };
    },

    /**
     * Function that puts the new comment in the HTML
     * @param post_id: Comment's post id
     * @param html: Html with the new comment returned by the server
     */
    put_new_comment: function(post_id, html) {
        var $comments = $("#comments_" + post_id);
        $comments.prepend(html);
        $("#modal_" + post_id).animate({scrollTop: $comments.position().top}, "slow");
        $("#comment_name_" + post_id).val("");
        $("#comment_email_" + post_id).val("");
        $("#comment_body_" + post_id).val("");
    },

    /**
     * Función que envia el comentario al servidor
     * @param post_id: Comment's post id
     * @param post_slug: Comment's post slug
     * @param csrf_token: Form's csrf token
     * @returns {boolean}
     */
    send_comment: function(post_id, post_slug, csrf_token) {
        var json = utils.get_comment(post_id, csrf_token);
        $.post("blog/post/", json, function (html) {
            utils.show_pnotify("success", "Comentario publicado");
            location.hash = "#" + post_slug;
            utils.put_new_comment(post_id, html);
        }).fail(function () {
            utils.show_pnotify("warning", "Ha habido un problema al publicar el comentario")
        });
        return false;
    },

    /**
     * Function that get all email attrs
     * @param csrf_token: Form's csrf token
     * @returns {*}
     */
    get_email: function (csrf_token) {
        return {
            "csrfmiddlewaretoken": csrf_token,
            "name": $("#name_email").val(),
            "email": $("#from_email").val(),
            "text": $("#body_email").val()
        };
    },

    /**
     * Function that sends an email to the server
     * @param csrf_token
     * @returns {boolean}
     */
    send_email: function(csrf_token) {
        var json = utils.get_email(csrf_token);
        $.post("contact/contact/", json, function () {
            utils.show_pnotify("success", "Mensaje enviado correctamente");
            $("html body").animate({scrollTop: $("body").position().top}, "slow");
            $("#name_email").val("");
            $("#body_email").val("");
            $("#from_email").val("");
        }).fail(function () {
            utils.show_pnotify("warning", "Ha habido un problema al enviar el mensaje");
        });
        return false;
    }
};
