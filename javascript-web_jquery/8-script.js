$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  success: function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
