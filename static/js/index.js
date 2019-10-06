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
$("#menu-save").click(function(){
    Blockly.JavaScript.addReservedWords('code');
    var newCode = Blockly.JavaScript.workspaceToCode(workspace);
    test(newCode);

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

function test(val){
    var EGB = BABYLON;

var canvas = document.getElementById("renderCanvas");
canvas.style.width = "800px";
canvas.style.height = "600px";

var engine = new EGB.Engine(canvas, true);

canvas.style.width = "100%";
canvas.style.height = "100%";

function createScene(){

    var scene = new EGB.Scene(engine);

    var camera = new EGB.UniversalCamera('camera', new EGB.Vector3(0, 2, -10), scene);
    camera.setTarget(EGB.Vector3.Zero());
    camera.attachControl(canvas, true);
    camera.speed = 0.2;
    camera.angularSensibility = 5000;

    var light1 = new EGB.HemisphericLight('light1', new EGB.Vector3(1,1,0), scene);

    eval(val);

    return scene;

};

var scene = createScene();

engine.runRenderLoop(function() {
    scene.render();
});

window.addEventListener('resize', function() {
    engine.resize();
});
}