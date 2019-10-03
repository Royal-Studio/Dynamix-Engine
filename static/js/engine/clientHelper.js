var colors = ['#007a99', '#008080', '#005266', '#279191', '#006080'];
var ids = [];

var values = {
    '0': MAIN_OBJECTS_MeshBuilder,
    '1': MAIN_OBJECTS_CodeArea
};

////////////////////////////////////////////////////////////////////////////////////////////////////////

function GetElementInsideContainer(containerID, childID) {
    var elm = {};
    var elms = document.getElementById(containerID).getElementsByTagName("*");
    for (var i = 0; i < elms.length; i++) {
        if (elms[i].id === childID) {
            elm = elms[i];
            break;
        }
    }
    return elm;
}

function getID(){
    var nodes = document.getElementById("CODE").childNodes;
    var ids2 = [];
    for (var i = 0; i < nodes.length; i++){
        ids2.push(nodes[i].id);
    }
    return ids2;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////

function newEvent(setting){
    var element = document.createElement(setting.type);
    var id = 354260 + getID().length;
    element.style.height = "200px";
    element.style.background = colors[Math.floor(Math.random() * 5)];
    element.style.border = "7px solid #425770";
    element.setAttribute('id', id);
    selectOne(element);
    newEventButton(element);
    code.appendChild(element);
}

function selectOne(name){
    var options = "<select id='one'>";

    options += "\n<option value='0'>MeshBuilder</option>";
    options += "\n<option value='1'>Code</option>";

    options += "\n</select>";
    name.innerHTML = options;
}

function newEventButton(element){
    var btn = document.createElement("BUTTON");
    btn.innerHTML = "NEW EVENT";
    btn.setAttribute("class", "button");
    btn.setAttribute("onclick", "newEvent({type: 'div'})");

    element.appendChild(btn);
}

function check_stuff(){
    for (var i = 0; i < getID().length; i++){
        var id = getID()[i];
        var parent = document.getElementById(id);
        var event = parent.childNodes;
        var value = event[0].options[event[0].selectedIndex].value;

        if (value == 0){
            var element = GetElementInsideContainer(id, id + "two");
            var options = values['0'](id);
            if (element.length == undefined){
                parent.appendChild(options);
            }
        }

        if (value == 1){
            var element = GetElementInsideContainer(id, id + "CodeArea");
            var options = values['1'](id);
            if (element.length == undefined){
                parent.appendChild(options);
            } else {
                console.log(element);
                parent.replaceChild(element[0], options);
            }
        }
    }
}