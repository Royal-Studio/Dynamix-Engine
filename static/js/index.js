document.getElementById("LEVEL").style.width = window.innerWidth / 2;
var code = document.getElementById("CODE");
code.style.width = window.innerWidth / 2;
code.setAttribute("style", "overflow: auto;");
code.style.height = window.innerHeight;
code.style.width = window.innerWidth / 2;

var colors = ['#007a99', '#008080', '#005266', '#279191', '#006080'];

////////////////////////////////////////////////////////////////////////////////////////////////////////

function newEvent(setting){
    var element = document.createElement(setting.type);
    element.style.height = "200px";
    element.style.background = colors[Math.floor(Math.random() * 3)];
    element.style.border = "7px solid #425770";
    selectEvent(element);
    newEventButton(element);
    code.appendChild(element);
}

function selectEvent(name){
    var options = "<select id='event'>";
    options += "\n<option value='0'>NewMesh</option>";
    name.innerHTML = options;
}

function newEventButton(element){
    var btn = document.createElement("BUTTON");
    btn.innerHTML = "NEW EVENT";
    btn.setAttribute("class", "button");
    btn.setAttribute("onclick", "newEvent({type: 'div'})");

    element.appendChild(btn);
}

////////////////////////////////////////////////////////////////////////////////////////////////////////

newEvent({type: "div", bg: "#6AAAC9"});
