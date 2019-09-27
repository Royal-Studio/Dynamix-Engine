class Editor{
    constructor(EGB){
        this.objects = {};
        this.EGB = EGB;
        this.scene;
    }

    NewMesh(settings){
        var mesh;
        if (settings.type = "box"){
            mesh = this.EGB.MeshBuilder.CreateBox(settings.name, settings.config, settings.scene);
        } else if (settings.type = "plane"){
            mesh = this.EGB.MeshBuilder.CreatePlane(settings.name, settings.config, settings.scene);
        } else if (settings.type = "sphere"){
            mesh = new this.EGB.MeshBuilder.CreateSphere(settings.name, settings.config, this.scene);
        } else if (settings.type = "ground"){
            mesh = this.EGB.MeshBuilder.CreateGround(settings.name, settings.config, settings.scene);
        } else if (settings.type = "tiledbox"){
            mesh = this.EGB.MeshBuilder.CreateTiledBox(settings.name, settings.config, settings.scene);
        } else if (settings.type = "tiledplane"){
            mesh = this.EGB.MeshBuilder.CreateTiledPlane(settings.name, settings.config, settings.scene);
        } else if (settings.type = "cylinder"){
            mesh = this.EGB.MeshBuilder.CreateCylinder(settings.name, settings.config, settings.scene);
        } else if (settings.type = "disc"){
            mesh = this.EGB.MeshBuilder.CreateDisc(settings.name, settings.config, settings.scene);
        } else if (settings.type = "torus"){
            mesh = this.EGB.MeshBuilder.CreateTorus(settings.name, settings.config, settings.scene);
        } else if (settings.type = "torusknot"){
            mesh = this.EGB.MeshBuilder.CreateTorusKnow(settings.name, settings.config, settings.scene);
        } else if (settings.type = "groundfromheightmap"){
            mesh = this.EGB.MeshBuilder.CreateSphere(settings.name, settings.url, settings.config, settings.scene);
        } else if (settings.type = "tiledground"){
            mesh = this.EGB.MeshBuilder.CreateTiledGround(settings.name, settings.config, settings.scene);
        } else {
            mesh = false;
        }
        return mesh;
    }
}