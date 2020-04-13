(function($) {
    $(document).scroll(function() {
        var $nav = $("nav.navbar");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
    $(document).ready(function() {
        $("a.btn-add-current").click(function() {
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/add-card-current/',
                data: { id: id },
                success: location.reload(),
            });
        });

        $("a.btn-add-finish").click(function() {
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/add-card-finish/',
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
        });

        $("a#check").click(function(e) {
            e.preventDefault();
            $(this).hide();
            $(this).next("p#hidden").show();
        })

    });

})(jQuery);