const $hElem = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $hElem.css('color', '#FF0000');
});