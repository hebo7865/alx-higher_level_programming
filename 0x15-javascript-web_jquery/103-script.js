$(document).ready(function () {
  $('input#btn_translate').on('click', function () {
    const lang = $('input#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, (data) => {
      $('div#hello').text(data.hello);
    });
  });
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      $('#btn_translate').click();
    }
  });
});
