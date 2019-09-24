var EGB = BABYLON;

var canvas = document.getElementById("renderCanvas");
canvas.setAttribute("width", window.innerWidth);
canvas.setAttribute('height', window.innerHeight);

var engine = new EGB.Engine(canvas, true);

function createScene(){

    var scene = new EGB.Scene(engine);
    scene.gravity = new EGB.Vector3(0, -0.2, 0);
    scene.collisionEnabled = true;

    var camera = new EGB.FreeCamera("FreeCamera", new BABYLON.Vector3(0, 0, 0), scene);
    camera.attachControl(canvas, true);
    camera.speed = 0.2;
    camera.angularSensibility = 5000;
    camera.applyGravity = true;
    // Set the ellipsoid around the camera
    camera.ellipsoid = new EGB.Vector3(1, 1, 1);
    //camera.ellipsoidOffset = 0.5;
    camera.checkCollisions = true;
    camera._needMoveForGravity = true;

    var light1 = new EGB.HemisphericLight('light1', new EGB.Vector3(1,1,0), scene);
    var light2 = new EGB.PointLight('light2', new EGB.Vector3(0,1,-1), scene);

    var plane = EGB.MeshBuilder.CreateBox("myBox", {width: 15, height: 0.1, depth: 15}, scene);
    plane.position.y = -2;
    plane.checkCollisions = true;
    plane.freezeWorldMatrix();

    return scene;

};

var scene = createScene();

engine.runRenderLoop(function() {
    scene.render();
});

window.addEventListener('resize', function() {
    engine.resize();
});