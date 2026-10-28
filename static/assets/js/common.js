(function($) {
    $(document).scroll(function() {
        var $nav = $("nav.navbar");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
    $(document).ready(function() {
        // Всплывашка «войдите в Ошибкариум» (.background в base.html) для незарегистрированных.
        $(".unauth").click(function(e) {
            e.preventDefault();
            $(".background").show();
        });
        $(".btn-close").click(function(e) {
            e.preventDefault();
            $(".background").hide();
        });

        // Кнопки на карточке: сначала дождаться ответа сервера, потом перезагрузить страницу.
        // Раньше location.reload() вызывался сразу (как значение поля done), а ссылка href=""
        // сама уводила на ту же страницу — браузер обрывал POST, и ничего не сохранялось.
        function cardAction(url) {
            return function(e) {
                e.preventDefault();
                $.post(url, { id: $(this).data('id') }).always(function() {
                    location.reload();
                });
            };
        }

        $("a.btn-add-current").click(cardAction('/api/user/add-card-current/'));
        $("a.btn-add-finish").click(cardAction('/api/user/add-card-finish/'));
        $("a.btn-remove").click(cardAction('/api/user/remove-card/'));

        $("a.btn-add-current-index").click(function(e) {
            e.preventDefault();
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/add-card-current/',
                data: { id: id },
                done: $(this).removeClass("btn-add-current-index").addClass("btn-remove-index").parent(".index").addClass("highlight").find('.tooltiptext').text('Убрать из «моих»'),
            });
        });

        $("a.btn-remove-index").click(function(e) {
            e.preventDefault();
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/remove-card/',
                data: { id: id },
                done: $(this).removeClass("btn-remove-index").addClass("btn-add-current-index").parent(".index").removeClass("highlight").find('.tooltiptext').text('Добавить к моим ошибкам'),
            });
        });

        function isValidEmailAddress(emailAddress) {
            var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
            return pattern.test(emailAddress);
        };

        $("button.btn-small").click(function() {
            var email = $("input#MERGE0").val();
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
        });

        $("#editor").click(function() {
            var email = $("input#email").val();
            var name = $("input#name").val();
            if(isValidEmailAddress(email)) {
                $.ajax({
                    type:"POST",
                    url: "/api/request-editor/",
                    data: {
                        email: email,
                        name: name,
                    },
                    done: $("p.sent").show(),
                });
            }
        });

        $("a#clarity_pos").click(function(e) {
            e.preventDefault();
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/card/clarity-pos/',
                data: { id: id },
                done: $("p.thanx").show(),
            });
        });

        $("a#clarity_neg").click(function(e) {
            e.preventDefault();
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/card/clarity-neg/',
                data: { id: id },
                done: $("p.thanx").show(),
            });
        });

        $("a#scrolltocards").click(function(e) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: $("#pests").offset().top
            }, 1000);
        });

        $("a#check").click(function(e) {
            e.preventDefault();
            $(this).hide();
            $(this).next("p#hidden").show();
        });
        if ($(window).width() < 769) {
            $("p.question").click(function(e) {
                e.preventDefault();
                $(this).next("div.answer").toggle("slow");
            })
        }
        $("i.fa-bars").click(function(e) {
            e.preventDefault();
            $("i.fa-bars").hide();
            $("i.fa-times").show();
            $("nav.navbar").addClass("opened-menu");
            $(".collapse").addClass("opened");
        });
        $("i.fa-times").click(function(e) {
            e.preventDefault();
            $("i.fa-times").hide();
            $("i.fa-bars").show();
            $("nav.navbar").removeClass("opened-menu");
            $(".collapse").removeClass("opened");
        });

        $("#fb_s").click(function(e) {
            e.preventDefault();
            FB.ui({
                method: 'share',
                href: window.location.href,
            }, function(response){});
        });

        $("#tw_s").click(function(e) {
            e.preventDefault();
            window.open("https://twitter.com/intent/tweet?url=" + window.location.href, "", "width=400,height=500,top=200,left=400")
        });

        $(".secondary-menu a").click(function(e) {
            e.preventDefault();
            var anchor = $(this).attr('href');
            $('html, body').animate({
                scrollTop: $(anchor).offset().top - 80
            }, 500);
            $(".secondary-menu a.active").removeClass("active");
            $(this).addClass("active");
        });

        var content = $("#content").offset().top - 80;
        var synt = $("#synt").offset().top - 80;
        var lex = $("#lex").offset().top - 80;
        var misc = $("#misc").offset().top - 80;

        if ($(window).width() < 769) {
            $(window).scroll(function() {
                var winTop = $(window).scrollTop();
                if(winTop >= content && winTop <= lex){
                    $(".secondary-menu a.active").removeClass("active");
                    $('#acon').addClass("active");
                } else if(winTop >= lex && winTop <= synt){
                    $(".secondary-menu a.active").removeClass("active");
                    $('#alex').addClass("active");
                } else if(winTop >= synt && winTop <= misc){
                    $(".secondary-menu a.active").removeClass("active");
                    $('#asynt').addClass("active");
                }  else if(winTop >= misc){
                    $(".secondary-menu a.active").removeClass("active");
                    $('#amisc').addClass("active");
                }
            });
        };

    });

})(jQuery);