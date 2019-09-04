function load_image(self, name, url){
    self.load.image(name, url);
}

function add_image_standard(self, name, x, y){
    self.add.image(name, x, y).setOrigin(0,0);
}

function add_image(self, name, x, y){
    self.add.image(name, x, y);
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

function keys_cursors_event(cursor, left, right, up, down, otherwise){
    if (cursor.left.isDown){
        left();
    } else if (cursor.right.isDown){
        right();
    } else if (cursor.up.isDown){
        up();
    } else if (cursor.down.isDown){
        down();
    } else {
        otherwise();
    }
}