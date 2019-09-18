

var EGB = BABYLON;

var canvas = document.getElementById("renderCanvas");
canvas.setAttribute("width", window.innerWidth);
canvas.setAttribute('height', window.innerHeight);

var engine = new EGB.Engine(canvas, true);

function createScene(){

    var scene = new EGB.Scene(engine);

    var camera = new EGB.FreeCamera("FreeCamera", new BABYLON.Vector3(0, 0, 0), scene);
    camera.attachControl(canvas, true);
    camera.speed = 0.2;
    camera.angularSensibility = 5000;

    var light1 = new EGB.HemisphericLight('light1', new EGB.Vector3(1,1,0), scene);
    var light2 = new EGB.PointLight('light2', new EGB.Vector3(0,1,-1), scene);

    var plane = EGB.MeshBuilder.CreateBox("myBox", {width: 15, height: 0.1, depth: 15}, scene);
    plane.translate(EGB.Axis.Y, -2, EGB.Space.WORLD);

    //EGB.SceneLoader.Append('./', 'test.obj', scene, function (scene) {});

    scene.gravity = new EGB.Vector3(0, -0.2, 0);
    camera.applyGravity = true;
    // Set the ellipsoid around the camera
    camera.ellipsoid = new EGB.Vector3(1, 1, 1);

    scene.collisionEnabled = true;
    camera.checkCollisions = true;

    plane.checkCollisions = true;

    return scene;

};

var scene = createScene();

engine.runRenderLoop(function() {
    scene.render();
});

window.addEventListener('resize', function() {
    engine.resize();
});
