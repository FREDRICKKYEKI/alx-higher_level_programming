/**
 * Write a JavaScript script that fetches and prints how to say “Hello”
 * depending on the language
 *  - You should use this API service:
 *    https://www.fourtonfish.com/hellosalut/hello/
 *  - The language code will be the value entered in the tag
 *    INPUT#language_code (ex: es, fr, en etc.)
 *  - The translation must be fetched when the user clicks on
 *    INPUT#btn_translate OR presses ENTER when the focus is on
 *    INPUT#language_code
 *  - The translation of “Hello” must be displayed in the HTML tag DIV#hello
 *  - You can’t use document.querySelector to select the HTML tag
 *  - You must use the JQuery API
 *  - You script must work when imported from the <head> tag
 */
window.onload = () => {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(
      'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
};