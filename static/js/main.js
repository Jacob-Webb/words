$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/permutations',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                $("p").text(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

/*
$(function() {
    $('button').click(function() {
        $("p").html("This has changed");
    });
});
*/