$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('div#hello').text(data.hello);
  });
});
