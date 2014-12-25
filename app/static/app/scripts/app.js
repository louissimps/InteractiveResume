/**
 * Created by simpsonls on 12/17/2014.
 */
$(function () {
  $('[data-toggle="popover"]').popover()
})


/**
*
* From: http://josephguadagno.net/post/2014/05/23/Bootstrap-Theme-Switcher
 */
$(document).ready(function() {
    /* For theme switching */
    var themeName = $.cookie("themeName");
    var themePath = $.cookie("themePath");
    if (themeName !== undefined) {
        setTheme(themeName, themePath);
    }

});

function setTheme(themeName, themePath) {
    var cssLink = "//maxcdn.bootstrapcdn.com/bootswatch/3.3.1/"+themeName+"/bootstrap.min.css";
    $('#bootstrapTheme').attr('href', cssLink);

    $.cookie("themeName", themeName, { expires: 7, path: "/" });
    $.cookie("themePath", themePath, { expires: 7, path: "/" });
}