///////////////////////////////////////////////////////////////////////////////////////////////////
  
var config_obj = document.getElementById("config");
var init_obj = document.getElementById("init");
var preload_obj = document.getElementById("preload");
var create_obj = document.getElementById("create");
var update_obj = document.getElementById("update");
  
var config = "name: My Awesome Game\nwidth: 800\nheight: 600\n\n\
language:\n  init: JS\n  preload: JS\n  create: JS\n  update: JS\n";
var init = "";
var preload = "";
var create = "";
var update = "";
  
$("#config").append(config);
$("#init").append(init);
$("#preload").append(preload);
$("#create").append(create);
$("#update").append(update);

$("#run-game").dialog({
    autoOpen: false,
    width: 1000,
    height: 800,
    modal: false,
});
  
$("#load-game").dialog({
    autoOpen: false,
    width: 550,
    height: 300,
    modal: false,
});

$("#import-asset").dialog({
    autoOpen: false,
    width: 500,
    height: 400,
    modal: false,
});

$("#export-game").dialog({
    autoOpen: false,
    width: 550,
    height: 305,
    modal: false,
});

$("#run-button").click(function(){
    $("#run-game").dialog("open");
});
  
$("#load-button").click(function(){
    $("#load-game").dialog("open");
});

$("#import-button").click(function(){
    $("#import-asset").dialog("open");
});

$("#export-button").click(function(){
    $("#export-game").dialog("open");
});

$("#load-game-button").click(function(){
    var name = $("#load-name").val();
    var data = {name: name};
    var response = load(data);
    console.log(response);
    $("#load-game").dialog("close");
});
  
$("#save-button").click(function(){
    save_button();
});

function save_button(){
    data = {
        config: $("#config").val(),
        init: $("#init").val(),
        preload: $("#preload").val(),
        create: $("#create").val(),
        update: $("#update").val(),
    };
    save("/save", data);
}
  
$("#run-button").click(function(){
    data = {
        config: $("#config").val(),
        init: $("#init").val(),
        preload: $("#preload").val(),
        create: $("#create").val(),
        update: $("#update").val(),
    };
    run("/run", data);
});
  
function save(url, data){
    $.post(url, data, function(){
        console.log("Saving..." + data);
    });
}

function run(url, data_to_send){
    $.post(url, data_to_send, function(data, status){
        console.log("Recieved..." + data + "\nStatus: " + status);
  
        data = JSON.parse(data);
        var game_frame = document.getElementById("game-frame");
  
        game_frame.setAttribute("src", data["path"] + ".html");
        game_frame.style.width = data["width"];
        game_frame.style.height = data["height"];
  
    });
}
  
function load(name){
    $.post("/load", name, function(data, status){
        console.log("Loading...:" + name + "\n Recieved: " + data + "\nStatus: " + status);
        var final_data = JSON.parse(data);
  
        var config = final_data["config"];
        var init = final_data["init"];
        var preload = final_data["preload"];
        var create = final_data["create"];
        var update = final_data["update"];

        $("#config").empty();
        $("#config").val(config);
        
        $("#init").empty();
        $("#init").val(init);
        
        $("#preload").empty();
        $("#preload").val(preload);

        $("#create").empty();
        $("#create").val(create);

        $("#update").empty();
        $("#update").val(update);
  
    });
}

$(window).bind('keydown', function(event){
    if (event.ctrlKey || event.metaKey){
        switch (String.fromCharCode(event.which).toLowerCase()){
            case 's':
                event.preventDefault();
                save_button();
                break;
            
            case 'l':
                event.preventDefault();
                $("#load-game").dialog("open");
                break;
            
            case 'r':
                event.preventDefault();
                document.getElementById("run-button").click();
                break;
            
            case 'i':
                event.preventDefault();
                $("#import-asset").dialog("open");
                break;
            
            case 'e':
                event.preventDefault();
                $("#export-game").dialog("open");
                break;
        }
    }
});
  
//===============================================================================================//
  
function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
  
function openCode(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
  
//===============================================================================================//