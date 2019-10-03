function MAIN_OBJECTS_MeshBuilder(id){
    var select = document.createElement("SELECT");
    select.setAttribute("id", id + "two");
    select.setAttribute('class', 'two');

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
    code.setAttribute("id", id + "CodeArea");
    code.setAttribute("style", "border: 0px;");

    return code;
}

class options{
    constructor(){}

//====================================MeshBuilder=============================================//
    createSphere(){
        var sphereObject = document.createElement("div");
        sphereObject.id = 'CreateSphere';
        var name = document.createElement("INPUT");
        name.name = "name";
    }
}