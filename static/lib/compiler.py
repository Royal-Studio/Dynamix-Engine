class Compile():
    def __init__(self, config, preload, create, update):
        self.config = config
        self.preload = preload
        self.create = create
        self.update = update
        self.name = self.config["name"]
        self.final = ""

    def compile(self):
        first_parts = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="engine.js"></script>
    <title>""" + self.name + """</title>
</head>
<body>
<script>\n\n"""
        last_parts = """\n</script>
</body>
</html>"""

        config = "var game = new Phaser.Game({\ntype: Phaser.AUTO, width: " + str(self.config["width"]) + \
            ", height: " + str(self.config["height"]) + ", "
        
        for i in self.config["else"].keys():
            config += str(i) + ": " + str(self.config["else"][i]) + ", "

        config_last = "scene: { preload: preload, create: create, update: update });"
        config += config_last

        first_parts += config

c = Compile({"name": "MyAwesomeGame", "width": 800, "height": 600, "else": {}}, [], [], [])
c.compile()