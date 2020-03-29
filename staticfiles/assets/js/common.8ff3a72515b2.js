(function($) {
    $(document).scroll(function() {
        var $nav = $("nav.navbar");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
    $(document).ready(function() {
        $("a.btn-add").click(function() {
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/add-card/',
                data: { id: id },
                success: location.reload(),
            });
        });

        $("a.btn-remove").click(function() {
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/remove-card/',
                data: { id: id },
                success: location.reload(),
            });
        });
        $(document).ajaxStop(function() {
            window.location.reload();
        });

        $("a#scrolltocards").click(function(e) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: $("#cards").offset().top
            }, 1000);
        })

    });

})(jQuery);