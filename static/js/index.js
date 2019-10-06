var code = document.getElementById("CODE");
code.setAttribute("style", "overflow: auto;");
code.style.height = window.innerHeight;

//newEvent({type: "div", bg: "#6AAAC9"});

/*$(window).bind('keydown', function(event) {
    if (event.ctrlKey || event.metaKey) {
        switch (String.fromCharCode(event.which).toLowerCase()) {

            case 's':
                return false;

            case 'r':
                compile(data);
                return false;

        }
    }
});*/

$("#LEVEL").dialog({
    autoOpen: false,
    title: "LEVEL",
    position: {
        my: "center center",
        at: "center center"
    },
    width: 800,
    height: 600
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

var workspace = Blockly.inject('CODE',{
    toolbox: MainToolBox,
    zoom: {
        controls: true,
        wheel: true,
        startScale: 1.0,
        maxScale: 3,
        minScale: 0.3,
        scaleSpeed: 1.2
    },
    trashcan: true
});