# About

EGB-Engine is a game engine build originally to thank [Royal Studios](https://discord.gg/g63g9zJ) team.

EGB-Engine is build with aim of simplifying the task of game development,
while not losing all the sweet things game engines offer! Currently going pre-alpha
after this documentation is written and is able to make a full blown
web game!

The EGB-Engine use Phaser 3 as logic, rendering and physics engine due to building a custom engine can be both resource hungry and not a good idea!
Phaser was choosed due to it meeting all requirement:

1. Cross-platform
2. Web based
3. Easy to use
4. Small in size

Currently, The EGB-Engine is 2D, but 3D engine also be added on version 2 or 3 with help
of babylon engine.

A WYSIWYG editor for the engine will be added soon as well as native exporting and 
steam/google play/apple app store/ ... in version 1.0

# Authors

MAIN AUTHOR:
    [Elham Aryanpur](http://www.github.com/ElhamAryanpur)

# Installation
You can setup EGB in this simple 4 steps!

1. First make sure you have Python 3.6.x or above is installed. then:
```
pip install flask
```

2. Clone this repository:
```
mkdir EGB-Engine
cd EGB-Engine

git clone https://www.github.com/ElhamAryanpur/EGB-Engine.git
```

3. Run the server:
```
python server.py
```

4. Head over to `127.0.0.1:5000` on your browser and BOOM! The engine is up and running!

Prebuild binaries will be avaliable ASAP!

# Ways Around

## Shortcuts:

`ctrl-s` = Save The Code

`ctrl-l` = Load The Code From Project

`ctrl-r` = Run The Game

`ctrl-i` = Import assets

`ctrl-e` = Export Game

## Tabs:

`FILE` Tab is used for main options such as load and save.

`CONFIG` Tab is used for configurations such as width, height, name

`INIT` Tab is used for code that is executed before any of game code

`PRELOAD` Tab is used for loading assets

`CREATE` Tab is used to create objects in the world

`UPDATE` Tab is used to add listeners and change data accordingly. From all other tabs, only update tab is run for infinity.

# Languages

`EGB-Engine` mainly use `JavaScript` as scripting language due games being web based. But `ELang` is also supported. `ELang` is custom made programming language aiming to look exactly like Human's English language as in syntax and behavior! It is very very easy, like talking to computers ;)

Don't worry, your `ELang` code will also be compiled automatically. `ELang` do not have any special keys in syntax, meaning there will be no ;(),$# or others! Everything is with words!

You do not have to add semi-colons at end of each line!
You do not have to add () for calling a function! 
...

Now it's only you and the code! For a full list of examples, please refer to `static/lib/ELangJS_syntax.elpp` in `master branch`!

`JS` is refered to JavaScript code in `Config` Tab. To change the language from JavaScript to ELang, just change the `JS` to `EL`!

# Detailed Guide

For code example, we will use:

`sky.png` as an asset image

`My Awesome Game` as example project

`Helper_JS` this is a library is is shipped with your game which is used to automate common tasks and as a helper to your code for ease of use!

## Config

In the config tab, you will always see some information automatically generated for you to quick start!

`name` refer the name of the project

`width` refer to width of the scene

`height` refer to height of the scene

`languages` refer to which tab use what language! Please see `Languages` guide above!

`else` this is not automatically added, but is used for extra configurations like physics!

The Examples are automatically generated so you can change configurations accordingly! The configuration uses `YAML` language for syntax!

## INIT

In this tab, you will write code that will be run as soon as window is opened!

No Code will be auto generated here.

Example usage can be getting data from server or making functions that will help you along the way!

Can be ELang and JS!

```
function sayHello(){
    alert("Hello World!"); 
}
```
 as `JS` example

```
define sayHello with arg
show Hello World
end
```

as `ELang` example



## PRELOAD

is used for loading assets you imported! Remember to always use `asset/<your asset name>` for refering to your asset!

Does not have automatically generated code

Can be used with `JS` and `EL`

### Normal JS:
```
this.load.image('sky', 'asset/sky.png');
```

### Using Helper:
```
load_image(this, 'sky', 'asset/sky.png');
```

### Normal ELang:
```
function this.load.image 'sky' 'asset/sky.png'
```

### Using Helper:
```
function load_image this 'sky' 'asset/sky.png'
```

## CREATE
This tab is used to create object on scene like showing asset you loaded or making collisions!

Does Not Have Automatically Generated Code

Can be used with `JS` and `EL`

### Normal JS:
```
this.add.image(0, 0, 'sky').setOrigin(0, 0).setScale(1).refreshBody();
```
### Using Helper:
```
add_image_standard(this, 0, 0, 'sky', scale=1);
```
### ELang:
```
function this.add.image 0 0 'sky'
```
### Using Helper:
```
function add_image_standard this 0 0 'sky' scale=1
```

## Update
This Tab is run for infinite and mostly contain data about detections like if this or that key is pressed!

Does Not have any auto generated code

Can be used with `JS` and `EL`

# MORE DOC WILL BE ADDED SOON! YOU CAN ALSO REFER TO PHASER'S DOCS AS ANY CODE COMPATIBLE WITH THEM CAN BE COMPATIBLE WITH US TOO!