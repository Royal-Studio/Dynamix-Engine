#include <stdio.h>
#include <stdlib.h>
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>

using namespace std;
using namespace glm;

int main(){

    // Initialise GLFW
    glewExperimental = true; // Needed for core profile
    if( !glfwInit() ){
        fprintf( stderr, "Failed to initialize GLFW\n" );
        return -1;
    }

    glfwWindowHint(GLFW_SAMPLES, 4); // 4x antialiasing! This was easier than I thought!
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3); // We want OpenGL 3.3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE); // We don't want the old OpenGL 

    // Open a window and create its OpenGL context
    GLFWwindow* window; // (In the accompanying source code, this variable is global for simplicity)
    window = glfwCreateWindow( 1000, 800, "Hello World", NULL, NULL);
    if( window == NULL ){
        fprintf( stderr, "FAILED to open GLFW window. If you have an Intel GPU, \
         they are not 3.3 compatible.\n" );
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window); // Init GLEW
    glewExperimental = true; // Needed in core profile

    if ( glewInit() != GLEW_OK ){
        fprintf( stderr, "Failed To Initialize GLEW\n" );
        return -1;
    }

    // Creating Vertex Array Object ( VAO )
    GLuint VertexArrayID;
    glGenVertexArrays(1, &VertexArrayID);
    glBindVertexArray(VertexArrayID);

    // An array of 3 vectors which represents 3 vertices
    //static

    // Ensure we can capture escape key being pressed below
    glfwSetInputMode( window, GLFW_STICKY_KEYS, GL_TRUE );

    do {
        // Clear the screen. It can cause flickering, so it's there nonetheless.
        glClear( GL_COLOR_BUFFER_BIT );

        // Draw nothing...

        // Swap Buffers
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    while( glfwGetKey(window, GLFW_KEY_ESCAPE) != GLFW_PRESS && 
    glfwWindowShouldClose(window) == 0 );

    return 0;
}