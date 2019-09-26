var EGB = BABYLON;

var canvas = document.getElementById("renderCanvas");
canvas.setAttribute("width", window.innerWidth);
canvas.setAttribute('height', window.innerHeight);

var engine = new EGB.Engine(canvas, true);

function createScene(){

    var scene = new EGB.Scene(engine);

    var camera = new EGB.UniversalCamera('camera', new EGB.Vector3(0, 2, -10), scene);
    camera.setTarget(EGB.Vector3.Zero());
    camera.attachControl(canvas, true);
    camera.speed = 0.2;
    camera.angularSensibility = 5000;

    var light1 = new EGB.HemisphericLight('light1', new EGB.Vector3(1,1,0), scene);
    //var light2 = new EGB.PointLight('light2', new EGB.Vector3(0,1,-1), scene);

    var sphere  = new EGB.MeshBuilder.CreateSphere('sphere', {}, scene);

    var plane = EGB.MeshBuilder.CreateBox("myBox", {width: 15, height: 0.1, depth: 15}, scene);


    var gizmoManager = new BABYLON.GizmoManager(scene);
    gizmoManager.positionGizmoEnabled = true;
    gizmoManager.boundingBoxGizmoEnabled = true;
    gizmoManager.gizmos.positionGizmo.updateGizmoRotationToMatchAttachedMesh = false;

    gizmoManager.attachableMeshes = [sphere, plane];

    return scene;

};

var scene = createScene();

engine.runRenderLoop(function() {
    scene.render();
});

window.addEventListener('resize', function() {
    engine.resize();
});