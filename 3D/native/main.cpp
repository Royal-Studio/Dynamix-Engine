#include "EGB-Native/engine.h"

int make_resources(void){

    vertex_and_element_init(vertices, element);

    // Make Textures And Shaders

    return 1;
}

void update_fade_factor(void){

}

void render(void){
    clear_background(0.0f, 0.5f, 1.0f, 1.0f);
}

int main(int argc, char** argv){

    GLfloat g_vertex_buffer_data[] = {
        -1.0f, -1.0f,
         1.0f, -1.0f,
        -1.0f,  1.0f,
         1.0f,  1.0f
    };
    vertices.insert(vertices.end(), begin(g_vertex_buffer_data), end(g_vertex_buffer_data));

    GLushort g_element_buffer_data[] = { 0, 1, 2, 3 };
    element.insert(element.end(), begin(g_element_buffer_data), end(g_element_buffer_data));

    glutInit(&argc, argv);
    init(800, 600, (char*) "EGB-Engine");

    return 0;
}