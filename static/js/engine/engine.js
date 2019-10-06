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

    return scene;

};

var scene = createScene();

engine.runRenderLoop(function() {
    scene.render();
});

window.addEventListener('resize', function() {
    engine.resize();
});