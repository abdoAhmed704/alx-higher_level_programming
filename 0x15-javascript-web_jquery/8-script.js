#!/usr/bin/node
var $movies = $('#list_movies');
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function( result ) {
        $.each(result.results, function(i, movie){
            $movies.append('<li>'+ movie.title +'</li>')
        });
    }
  });
  