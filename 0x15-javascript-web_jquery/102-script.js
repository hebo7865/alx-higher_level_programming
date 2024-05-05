$(document).ready(function () {
  $('unput#btn_translate').on('click', function () {
    const lang = $('input#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, (data) => {
      $('div#hello').text(data.hello);
    });
  });
});
