function load_image(self, name, url){
    self.load.image(name, url);
}

function add_image_standard(self, name, x, y, scale=1){
    self.add.image(x, y, name).setOrigin(0,0).setScale(scale).refreshBody;
}

function add_image(self, name, x, y, scale=1){
    self.add.image(x, y, name).setScale(scale).refreshBody;
}

function load_sprite(self, name, url, width, height){
    self.add.image(name, url, { frameWidth: width, frameHeight: height });

}

function physic_sprite(self, x, y, name, bounce=0, should_collide=false){
    var sprite = self.physics.add.sprite(x, y, name);
    sprite.setBounce(bounce);
    if (should_collide == true){
        sprite.setCollideWorldBounds(true);
        self.physics.add.collider(sprite);
    }
    return sprite;
}

function keys_cursors_init(self){
    var cursor = self.input.keyboard.createCursorKeys();
    return cursor
}

function keys_cursors_event(cursor, left_func, right_func, up_func, down_func, otherwise_func){
    if (cursor.left.isDown){
        left_func();
    } else if (cursor.right.isDown){
        right_func();
    } else if (cursor.up.isDown){
        up_func();
    } else if (cursor.down.isDown){
        down_func();
    } else {
        otherwise_func();
    }
}