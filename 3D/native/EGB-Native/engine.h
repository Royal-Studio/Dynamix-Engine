//=====================================HEADERS===============================================//

// Include Standard Headers
#include <stdio.h>
#include <stdlib.h>
#include <vector>

// Including GLEW
#include <GL/glew.h>

// Including GLUT and checking if its on mac or not
#ifdef __APPLE__
#   include <GLUT/glut.h>
#else
#   include <GL/glut.h>
#endif

// UTILS
#include "tga_parser.h"

//=====================================VARIABLES=============================================//

// Namespaces
using namespace std;

// These will be the rendering functions
int make_resource(void);
void update_fade_factor(void);
void render(void);

// Variables
vector <GLfloat> vertices;
vector <GLushort> element;

struct {
    GLuint vertex_buffer, element_buffer;
    GLuint textures[2];
} g_resources;

//=======================================FUNCS=================================================//

// And the Init Function!
int init(

    int Width,
    int Height,
    char* Title

    ){

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE); // for two color buffers
    glutInitWindowSize(Width, Height); // size of window
    glutCreateWindow(Title); // title of window
    glutDisplayFunc(&render); // render at first
    glutIdleFunc(&update_fade_factor); // render every frame!

    // Init GLEW and checking if opengl 2.0 is available!
    glewInit();
    if (!GLEW_VERSION_2_0){
        fprintf(stderr, "OpenGL 2.0 not available\n");
        return 1;
    }

    // After GLEW Init:
    if (!make_resource){
        fprintf(stderr, "FAILED TO LOAD RESOURCES!\n");
        return 1;
    }

    glutMainLoop();
    return 0;
}

// Shorting Helpers

GLuint make_buffer(
    GLenum target,
    void* buffer_data,
    GLsizei buffer_size
){
    GLuint buffer;
    glGenBuffers(1, &buffer);
    glBindBuffer(target, buffer);
    glBufferData(target, buffer_size, buffer_data, GL_STATIC_DRAW);
    return buffer;
}

GLuint make_texture(char* filename){
    GLuint texture;
    int width, height;
    void* pixels = read_tga(filename, &width, &height);

    if (!pixels)
        return 0;

    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);
}

// CUSTOM

void vertex_and_element_init(vector<GLfloat> vertices, vector<GLushort> element){

    GLfloat* g_vertex_buffer_data = vertices.data();
    GLushort* g_element_buffer_data = element.data();

    g_resources.vertex_buffer = make_buffer(
        GL_ARRAY_BUFFER,
        g_vertex_buffer_data,
        sizeof(g_vertex_buffer_data)
    );

    g_resources.element_buffer = make_buffer(
        GL_ELEMENT_ARRAY_BUFFER,
        g_element_buffer_data,
        sizeof(g_element_buffer_data)
    );

}

void clear_background(GLclampf R, GLclampf G, GLclampf B, GLclampf A){
    glClearColor(R, G, B, A);
    glClear(GL_COLOR_BUFFER_BIT);
    glutSwapBuffers();
}