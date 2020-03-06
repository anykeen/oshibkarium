( function( $ ){
    $( document ).ready( function () {
        $( "a.btn-add" ).click( function(){
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/add-card/',
                data: {id: id},
                success: location.reload(),
              });
        } );

        $( "a.btn-remove" ).click( function(){
            var id = $(this).data('id');
            $.ajax({
                type: "POST",
                url: '/api/user/remove-card/',
                data: {id: id},
                success: location.reload(),
              });
        } );

    } );

} )( jQuery );