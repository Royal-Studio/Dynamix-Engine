#include "engine.h"
#include <iostream>

void BeforeDraw(){

float vertices[] = {
    -0.5f, -0.5f, 0.0f,
     0.5f, -0.5f, 0.0f,
     0.0f,  0.5f, 0.0f
};
verticesVector.insert(verticesVector.end(), begin(vertices), end(vertices));

unsigned int VBO;
glGenBuffers(1, &VBO);



}
void Draw(float* vertex){



}

int main(){

    init(3, 1000, 800, (char*) "Tutorial");
    return 0;

}