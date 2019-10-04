function MAIN_OBJECTS_MeshBuilder(id){
    var select = document.createElement("SELECT");
    select.setAttribute("id", id + "two");
    select.setAttribute('class', 'two');
    select.setAttribute('name', 'MAIN_OBJECTS_MeshBuilder');

    var option = document.createElement("OPTION");
    option.setAttribute("value", "0");
    option.innerHTML = "Create Sphere";

    select.appendChild(option);

    option = document.createElement("OPTION");
    option.setAttribute("value", "1");
    option.innerHTML = "Create Box";

    select.appendChild(option);

    return select;
}

function MAIN_OBJECTS_CodeArea(id){
    var code = document.createElement("textarea");
    code.setAttribute("id", id + "two");
    code.setAttribute("style", "border: 0px; width: 100%; height: 200px; resize: none;");
    code.setAttribute('name', 'MAIN_OBJECTS_CodeArea')

    return code;
}

//====================================MeshBuilder=============================================//

function OPTIONS_CreateSphere(){
    var sphereObject = document.createElement("div");
    sphereObject.id = 'CreateSphere';
    var name = document.createElement("INPUT");
    name.name = "name";
}