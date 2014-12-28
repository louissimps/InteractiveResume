/**
 * Created by simpsonls on 12/17/2014.
 */
$(function () {
  $('[data-toggle="popover"]').popover()
})


var bootstrap_themes = ['cerulean', 'cosmo', 'cyborg', 'darkly', 'flatly', 'journal', 'lumen', 'readable', 'sandstone', 'simplex', 'slate', 'spacelab', 'superhero', 'united', 'yeti'];

/**
*
* Got Idea from : http://josephguadagno.net/post/2014/05/23/Bootstrap-Theme-Switcher
 */

var themeName = "default";
$(document).ready(function() {
    /* For theme switching */
    themeName = $.cookie("themeName");
    FillList();


});
function FillList()
{
    var theme = "amelia";
    var list = $("#theme_list");

    for(var x in bootstrap_themes)
    {
        theme = $.trim(bootstrap_themes[x]);
        var li = $('<li>');
        var a = $('<a>',{
            text: theme,
            class: theme,
            title: 'Select this to set current bootswatch theme to ' + theme,
            href: '#'
        });
        $(a).on('click', function()
        {
            setTheme(this);
        });
        li.appendTo(list);
        a.appendTo(li);
        if(themeName == theme)
            setTheme(a);

    }
    //"<li><a title="Select this to set current bootswatch theme to amelia" href="#">amelia</a></li><li><a title="Select this to set current bootswatch theme to cerulean" href="#">cerulean</a></li><li><a title="Select this to set current bootswatch theme to cosmo" href="#">cosmo</a></li><li><a title="Select this to set current bootswatch theme to cyborg" href="#">cyborg</a></li><li><a title="Select this to set current bootswatch theme to darkly" href="#">darkly</a></li><li><a title="Select this to set current bootswatch theme to flatly" href="#">flatly</a></li><li><a title="Select this to set current bootswatch theme to journal" href="#">journal</a></li><li><a title="Select this to set current bootswatch theme to lumen" href="#">lumen</a></li><li><a title="Select this to set current bootswatch theme to readable" href="#">readable</a></li><li><a title="Select this to set current bootswatch theme to sandstone" href="#">sandstone</a></li><li><a title="Select this to set current bootswatch theme to simplex" href="#">simplex</a></li><li><a title="Select this to set current bootswatch theme to slate" href="#">slate</a></li><li><a title="Select this to set current bootswatch theme to spacelab" href="#">spacelab</a></li><li><a title="Select this to set current bootswatch theme to superhero" href="#">superhero</a></li><li><a title="Select this to set current bootswatch theme to united" href="#">united</a></li><li><a title="Select this to set current bootswatch theme to yeti" href="#">yeti</a></li>"


}
function setTheme(obj) {
    var cssLink = "//maxcdn.bootstrapcdn.com/bootswatch/3.3.1/"+$(obj).text()+"/bootstrap.min.css";
    $('#bootstrapTheme').attr('href', cssLink);

    $.cookie("themeName", $(obj).text(), { expires: 7, path: "/" });
    //$.cookie("themePath", themePath, { expires: 7, path: "/" });
}
