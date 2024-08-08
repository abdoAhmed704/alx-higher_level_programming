#!/usr/bin/node

var $charater = $('#character');
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function( result ) {
      $charater.text(result.name);
    }
  });
  