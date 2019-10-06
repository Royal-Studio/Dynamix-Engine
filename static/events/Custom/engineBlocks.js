Blockly.Blocks['box'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Variable Name:")
        .appendField(new Blockly.FieldTextInput("myBox"), "varname");
    this.appendValueInput("name")
        .setCheck("String")
        .appendField("NAME:");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height:");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(180);
 this.setTooltip("This will make a sphere");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['code'] = {
  init: function() {
    this.appendValueInput("code")
        .setCheck("String")
        .appendField("Code");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(165);
 this.setTooltip("Write Your Code Here");
 this.setHelpUrl("");
  }
};

//================================================================================================//
//================================================================================================//

Blockly.JavaScript['box'] = function(block) {
  var text_varname = block.getFieldValue('varname');
  var value_name = Blockly.JavaScript.valueToCode(block, 'name', Blockly.JavaScript.ORDER_ATOMIC);
  var value_height = Blockly.JavaScript.valueToCode(block, 'height', Blockly.JavaScript.ORDER_ATOMIC);
  var value_width = Blockly.JavaScript.valueToCode(block, 'width', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'var ' + text_varname + ' = new EGB.MeshBuilder.CreateBox('+
  value_name + ', {height: ' + value_height + ', width: ' + value_width + '}, scene);';
  return code;
};

Blockly.JavaScript['code'] = function(block) {
  var value_code = Blockly.JavaScript.valueToCode(block, 'code', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'eval("' + value_code.replace("'", "").replace("'", "").replace('"', "'").replace('"', "'") + '");';
  return code;
};