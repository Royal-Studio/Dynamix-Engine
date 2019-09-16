from direct.showbase.ShowBase import ShowBase

class myApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

if __name__ == "__main__":
    app = myApp()
    app.run()