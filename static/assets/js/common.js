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
                done: location.reload(),
            });
        });

        $("a.btn-add-finish").click(function() {
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/add-card-finish/',
                data: { id: id },
                done: location.reload(),
            });
        });

        $("a.btn-remove").click(function() {
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/remove-card/',
                data: { id: id },
                done: location.reload(),
            });
        });

        function isValidEmailAddress(emailAddress) {
            var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
            return pattern.test(emailAddress);
        };

        $("button.btn-small").click(function() {
            var email = $("input#MERGE0").val();
            var log = $("form#subscription").serialize();
            console.log(log);
            if(isValidEmailAddress(email)) {
                $.ajax({
                    type: "POST",
                    dataType: 'jsonp',
                    url: 'https://smartia.us13.list-manage.com/subscribe/post',
                    data: $("form#subscription").serialize(),
                    done: $("p.success").show(),
                });
            }
        });

        $("#reg").click(function() {
            if ($("input#id_is_subscribed").prop( "checked" )) {
                console.log("ololo");
                var email = $("input#id_email").val();
                if(isValidEmailAddress(email)) {
                    $.ajax({
                        type: "POST",
                        dataType: 'jsonp',
                        url: 'https://smartia.us13.list-manage.com/subscribe/post',
                        data: 'u=c06b10e38a025e33133083f8e&id=1e212793ec&MERGE0=' + email,
                    });
                }
            }
        })

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
        });

        $("p.question").click(function(e) {
            e.preventDefault();
            $(this).next("div.answer").toggle("slow");
        })

    });

})(jQuery);