var code = document.getElementById("CODE");
code.setAttribute("style", "overflow: auto;");
code.style.height = window.innerHeight;

newEvent({type: "div", bg: "#6AAAC9"});

$(window).bind('keydown', function(event) {
    if (event.ctrlKey || event.metaKey) {
        switch (String.fromCharCode(event.which).toLowerCase()) {

            case 's':
                check_stuff();
                data = saveData();
                return false;

            case 'r':
                compile(data);
                return false;

        }
    }
});

$("#LEVEL").dialog({
    title: "LEVEL",
    position: {
        my: "left bottom",
        at: "left bottom"
    },
    width: 800,
    height: 600
});

$("#CODE").dialog({
    title: "CODE",
    position: {
        my: "right center",
        at: "right center"
    },
    width: 800,
    height: 600,
    minWidth: 800,
    minHeight: 600
});

$("#menu").dialog({
    title: "MENU",
    position: {
        my: "top",
        at: "top"
    },
    maxWidth: 800,
    maxHeight: 160,
    minWidth: 800,
    minHeight: 160,
    dialogClass: 'no-close'
});

$("#menu-level").click(function(){
    $("#LEVEL").dialog("open");
});
$("#menu-code").click(function(){
    $("#CODE").dialog("open");
});
$("#menu-save").click(function(){
    check_stuff();
});
$("#menu-run").click(function(){
    compile(data);
});