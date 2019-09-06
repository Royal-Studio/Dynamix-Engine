from os import getcwd, system, remove
import platform

class ELang():
    def __init__(self, data):
        self.filename = data
        self.data = []
        self.comp_data = []
        self.commands = []
        self.vars = {}
        self.func_var = {}
        self.func = False
        self.data_types = ["string", "int"]
        self.features = [
            "show",
            "variable",
            "add",
            "subtract",
            "multiply",
            "divide",
            "if",
            "end",
            "define",
            "function",
            "function-variable",
            "change",
            "native"
        ]

    def reader(self, file_name=None):
        self.data = self.filename.split("\n")
    
    def clean(self):
        # let's make our first list to gather first datas
        data = []
        for i in self.data:
            # This will replace any new line from every lines and append to data list
            i = str(i).replace("\n", "")
            data.append(i)
        
        # let's make second list to save second loop data
        new_data = []
        for i in data:
            # and now let's delete any lines that is blank and append to new_data list
            if i != "": new_data.append(i)
        
        # Let's change values of data by redefining it to contain new_data values
        data = new_data
        
        # Save data to global data and delete useless variables        
        self.data = data
        del data
        del new_data
    
    def indentify(self):
        # Do a loop in data
        for i in self.data:
            # Split each to have clear view
            o = i.split()
            # Check if first word is a keyword!
            if o[0].lower() in self.features:
                # Deleting the keyword and putting them into a list
                i = i.replace(str(str(o[0]) + " "), "")
                data = [o[0].lower(), [i]]
                # And appending it to commands
                self.commands.append(data)
    
    def parse(self):
        data = []
        for i in self.commands:
            o = i[1][0].split()
            if i[0] == self.features[0]:
                data.append(i)
            elif i[0] == self.features[1]:
                var_data = str(i[1][0])
                data_word = str(o[0])
                equalt_word = str(o[1])
                var_data = var_data.replace(str(data_word + " "), "")
                var_data = var_data.replace(str(equalt_word) + " ", "")
                this_data = ["var", [o[0], var_data]]
                data.append(this_data) 
            elif i[0] == self.features[2]:
                this_data = ["add", [o[0], o[2], o[4]]]
                data.append(this_data)
            elif i[0] == self.features[3]:
                this_data = ["sub", [o[0], o[2], o[4]]]
                data.append(this_data)
            elif i[0] == self.features[4]:
                this_data = ["mul", [o[0], o[2], o[4]]]
                data.append(this_data)
            elif i[0] == self.features[5]:
                this_data = ["div", [o[0], o[2], o[4]]]
                data.append(this_data)
            elif i[0] == self.features[6]:
                this_data = ["if", [o[0], o[1], o[2]]]
                data.append(this_data)
            elif i[0] == self.features[7]:
                data.append(["end"])
            elif i[0] == self.features[8]:
                this_data = ["def", [o[0]], []]
                del o[0]
                del o[0]
                for p in o:
                    this_data[2].append(p)
                data.append(this_data)
            elif i[0] == self.features[9]:
                this_data = ["func", o[0], []]
                del o[0]
                for p in o:
                    this_data[2].append(p)
                data.append(this_data)
            elif i[0] == self.features[10]:
                var_data = str(i[1][0])
                data_word = str(o[0])
                equalt_word = str(o[1])
                var_data = var_data.replace(str(data_word + " "), "")
                var_data = var_data.replace(str(equalt_word) + " ", "")
                this_data = ["func-var", [o[0], var_data]]
                data.append(this_data) 
            elif i[0] == self.features[11]:
                this_data = ["change", [o[0], o[2]]]
                data.append(this_data)
            
            elif i[0] == self.features[12]:
                data.append(i)
                
        self.data = data

    def compile(self):
        self.reader()
        self.clean()
        self.indentify()
        self.parse()
        self.commands = []
        for i in self.data:
            if i[0] == "show":
                self.comp_data = i[1]
                self.show()
            elif i[0] == "var":
                if self.func:
                    self.func_var[i[1][0]] = i[1][1]
                else:
                    self.vars[i[1][0]] = i[1][1]
                self.comp_data = [i[1][0], i[1][1]]
                self.var()
            elif i[0] == "add":
                self.comp_data = [i[1][0], i[1][1], i[1][2]]
                self.add()
            elif i[0] == "sub":
                self.comp_data = [i[1][0], i[1][1], i[1][2]]
                self.sub()
            elif i[0] == "mul":
                self.comp_data = [i[1][0], i[1][1], i[1][2]]
                self.mul()
            elif i[0] == "div":
                self.comp_data = [i[1][0], i[1][1], i[1][2]]
                self.div()
            elif i[0] == "if":
                self.comp_data = [i[1][0], i[1][1], i[1][2]]
                self.if_statement()
            elif i[0] == "end":
                self.comp_data = [i[0]]
                self.end()
            elif i[0] == "def":
                self.comp_data = [i[1], i[2]]
                self.define()
            elif i[0] == "func":
                self.comp_data = [i[1], i[2]]
                self.function()
            elif i[0] == "func-var":
                if self.func:
                    self.func_var[i[1][0]] = i[1][1]
                else:
                    self.vars[i[1][0]] = i[1][1]
                self.comp_data = [i[1][0], i[1][1]]
                self.function_var()
            elif i[0] == "change":
                self.comp_data = [i[1][0], i[1][1]]
                self.change()
            if i[0] == "native":
                self.comp_data = i[1]
                self.native()

        code = self.finalize()
        return code

    def show(self):
        if self.func:
            if self.comp_data[0] not in self.func_var:
                to_show = 'console.log( "' + self.comp_data[0] + '" );\n'

            else:
                to_show = 'console.log( ' + self.comp_data[0] + ' );\n'
        
        else:
            if self.comp_data[0] not in self.vars:
                to_show = 'console.log( "' + self.comp_data[0] + '" );\n'

            else:
                to_show = 'console.log( ' + self.comp_data[0] + ' );\n'

        self.commands.append(to_show)
    
    def var(self):
        try:
            data = int(self.comp_data[1])
            type_of_data = "int"
        except ValueError:
            data = self.comp_data[1]
            type_of_data = "string"

        if type_of_data == "string":
            to_show = 'var ' + self.comp_data[0] + ' = "' + data + '";\n'
        else:
            to_show = 'var ' + self.comp_data[0] + ' = ' + str(data) + ';\n'

        self.commands.append(to_show)

    def add(self):
        if self.comp_data[2] in self.vars:
            data_on_var = True
        else:
            data_on_var = False

        if self.comp_data[1] in self.vars:
            comp_data1 = self.comp_data[1]
        else:
            comp_data1 = self.comp_data[1]
        
        if self.comp_data[0] in self.vars:
            comp_data0 = self.comp_data[0]
        else:
            comp_data0 = self.comp_data[0]
        
        try:
            data0 = int(comp_data0)
            data1 = int(comp_data1)
        except ValueError:
            data0 = comp_data0
            data1 = comp_data1

        if data_on_var:
            to_show = '' + self.comp_data[2] + ' = ' + str(data0) + ' + ' + str(data1) + ';\n'
        else:
            to_show = 'var ' + self.comp_data[2] + ' = ' + str(data0) + ' + ' + str(data1) + ';\n'

            try:
                self.vars[self.comp_data[2]] = data0 + data1
            except ValueError:
                self.vars[self.comp_data[2]] = str(data0) + str(data1)

        self.commands.append(to_show)
    
    def sub(self):
        if self.comp_data[2] in self.vars:
            data_on_var = True
        else:
            data_on_var = False

        if self.comp_data[1] in self.vars:
            comp_data1 = self.vars[self.comp_data[1]]
        else:
            comp_data1 = self.comp_data[1]
        
        if self.comp_data[0] in self.vars:
            comp_data0 = self.vars[self.comp_data[0]]
        else:
            comp_data0 = self.comp_data[0]
        
        try:
            data0 = int(comp_data0)
            data1 = int(comp_data1)
            type_of_data = "int"
        except ValueError:
            data0 = comp_data0
            data1 = comp_data1
            type_of_data = "string"
        
        if type_of_data == "string":
            print("ERR: YOU CAN NOT SUBTRACT STRINGS!\n ERR ON {} AND {}".format(comp_data0, comp_data1))
            exit()

        if data_on_var:
            to_show = '' + self.comp_data[2] + ' = ' + str(data0) + ' - ' + str(data1) + ';\n'
        else:
            to_show = 'var ' + self.comp_data[2] + ' = ' + str(data0) + ' - ' + str(data1) + ';\n'
            try:
                self.vars[self.comp_data[2]] = data0 - data1
            except ValueError:
                self.vars[self.comp_data[2]] = str(data0) + str(data1)

        self.commands.append(to_show)

    def mul(self):
        if self.comp_data[2] in self.vars:
            data_on_var = True
        else:
            data_on_var = False

        if self.comp_data[1] in self.vars:
            comp_data1 = self.vars[self.comp_data[1]]
        else:
            comp_data1 = self.comp_data[1]
        
        if self.comp_data[0] in self.vars:
            comp_data0 = self.vars[self.comp_data[0]]
        else:
            comp_data0 = self.comp_data[0]
        
        try:
            data0 = int(comp_data0)
            data1 = int(comp_data1)
            type_of_data = "int"

        except ValueError:
            data0 = comp_data0
            data1 = comp_data1
            type_of_data = "string"
        
        try:
            type_int = True
            data1 = int(data1)
        except ValueError:
            type_int = False

        if type_int == False:
            print("ERR: YOU CAN NOT MULTIPLY STRINGS WITH STRING OR MULTIPLY!\n ERR ON {} AND {}".format(comp_data0, comp_data1))

        else:
            if type_of_data == "string":
                if type_int:
                    if data_on_var:
                        to_show = 'for(var i = 0; i > ' + str(data1) + ' ; i++){ ' + self.comp_data[2] + ' += "' + str(data0) + '"};\n'
                    else:
                        to_show = 'var ' + self.comp_data[2] + ' =  "";' + \
                        '\nfor(var i = 0; i < ' + str(data1) + ' ; i++){ ' + self.comp_data[2] + ' += "' + str(data0) + '";}\n'
                        try:
                            self.vars[self.comp_data[2]] = data0 * data1
                        except ValueError:
                            self.vars[self.comp_data[2]] = str(data0) * str(data1)
            else:
                if data_on_var:
                    to_show = '' + self.comp_data[2] + ' = ' + str(data0) + ' * ' + str(data1) + ' ;\n'
                else:
                    to_show = 'var ' + self.comp_data[2] + ' = ' + str(data0) + ' * ' + str(data1) + ' ;\n'
                    try:
                        self.vars[self.comp_data[2]] = data0 * data1
                    except ValueError:
                        self.vars[self.comp_data[2]] = str(data0) * str(data1)

            self.commands.append(to_show)
    
    def div(self):
        if self.comp_data[2] in self.vars:
            data_on_var = True
        else:
            data_on_var = False

        if self.comp_data[1] in self.vars:
            comp_data1 = self.vars[self.comp_data[1]]
        else:
            comp_data1 = self.comp_data[1]
        
        if self.comp_data[0] in self.vars:
            comp_data0 = self.vars[self.comp_data[0]]
        else:
            comp_data0 = self.comp_data[0]

        try:
            data0 = int(comp_data0)
            data1 = int(comp_data1)
            type_of_data = "int"
        except ValueError:
            data0 = comp_data0
            data1 = comp_data1
            type_of_data = "string"

        if type_of_data == "string":
            print("ERR: YOU CAN NOT DIVIDE STRINGS!\n ERR ON {} AND {}".format(comp_data0, comp_data1))
            exit()

        if data_on_var:
            to_show = '' + self.comp_data[2] + ' = ' + str(data1) + ' / ' + str(data0) + ';\n'
        else:
            to_show = 'var ' + self.comp_data[2] + ' = ' + str(data1) + ' / ' + str(data0) + ';\n'
            try:
                self.vars[self.comp_data[2]] = data0 / data1
            except ValueError:
                self.vars[self.comp_data[2]] = ""

        self.commands.append(to_show)
    
    def function_var(self):
        to_show = 'var ' + self.comp_data[0] + ' = ' + str(self.comp_data[1]) + ';\n'

        self.commands.append(to_show)
    
    def if_statement(self):
        if self.comp_data[0] not in self.vars:
            data1 = False
        else:
            data1 = True
        if self.comp_data[2] not in self.vars:
            data2 = False
        else:
            data2 = True
        
        try:
            self.comp_data[0] = int(self.comp_data[0])
            data1_int = True
        except ValueError:
            data1_int = False
            pass
        
        try:
            self.comp_data[2] = int(self.comp_data[2])
            data2_int = True
        except ValueError:
            data2_int = False
            pass

        if data1:
            if data2:
                to_show = 'if (' + str(self.comp_data[0]) + ' ' + self.comp_data[1] + ' ' + str(self.comp_data[2]) + "){\n"
            else:
                if data2_int:
                    to_show = 'if (' + str(self.comp_data[0]) + ' ' + self.comp_data[1] + ' ' + str(self.comp_data[2]) + "){\n"
                else:
                    to_show = 'if (' + str(self.comp_data[0]) + ' ' + self.comp_data[1] + ' "' + str(self.comp_data[2]) + '"){\n'
        else:
            if data2:
                if data1_int:
                    to_show = 'if (' + str(self.comp_data[0]) + ' ' + self.comp_data[1] + ' ' + str(self.comp_data[2]) + "){\n"
                else:
                    to_show = 'if ("' + str(self.comp_data[0]) + '" ' + self.comp_data[1] + ' ' + str(self.comp_data[2]) + "){\n"
            else:
                if data1_int:
                    if data2_int:
                        to_show = 'if (' + str(self.comp_data[0]) + ' ' + self.comp_data[1] + ' ' + str(self.comp_data[2]) + "){\n"
                    else:
                        to_show = 'if (' + str(self.comp_data[0]) + ' ' + self.comp_data[1] + ' "' + str(self.comp_data[2]) + '"){\n'
                else:
                    if data2_int:
                        to_show = 'if ("' + str(self.comp_data[0]) + '" ' + self.comp_data[1] + ' ' + str(self.comp_data[2]) + "){\n"
                    else:
                        to_show = 'if ("' + str(self.comp_data[0]) + '" ' + self.comp_data[1] + ' "' + str(self.comp_data[2]) + '"){\n'

        self.commands.append(to_show)
    
    def end(self):
        self.commands.append('}\n')
    
    def define(self):
        self.func = True
        self.func_var = {}

        for i in self.comp_data[1]:
            self.func_var[i] = ""
        
        to_show = 'function ' + self.comp_data[0][0] + ' = []('
        for i in self.comp_data[1]:
            to_show += '' + i + ','
        
        to_show = to_show[:-1]
        to_show += '){\n'
        self.commands.append(to_show)
    
    def function(self):
        to_show = '' + self.comp_data[0] + '('
        for i in self.comp_data[1]:
            to_show += ' ' + i + ','
        to_show = to_show[:-1]
        to_show += ');\n'
        self.commands.append(to_show)

    def change(self):
        to_show = "" + self.comp_data[0] + ' = ' + self.comp_data[1] + ';\n'
        
        self.commands.append(to_show)

    def native(self):
        self.commands.append(self.comp_data[0])

    def finalize(self):
        first_parts = ''

        for i in self.commands:
            first_parts += str(i)
        return first_parts