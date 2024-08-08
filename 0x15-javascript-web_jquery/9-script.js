#!/usr/bin/node
$(document).ready(function(){
    var $hello = $('#hello');
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function( result ) {
            $hello.text(result.hello)
        }
    });
});
