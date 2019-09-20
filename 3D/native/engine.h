#pragma once

// Include Standard Headers
#include <stdio.h>
#include <stdlib.h>
#include <functional>

// Include GLAD
//#include "include/glad/glad.h"

// Include GLFW
#include <GLFW/glfw3.h>

// If mac os:
#ifdef __APPLE__
#ifdef TARGET_OS_MAC
#include <OpenGL/OpenGL.h>
#endif
#endif

// Include GLM for 3D math
#include <glm/glm.hpp>
using namespace glm;
using namespace std;

GLFWwindow* window; // This is a global var

int init(

    // For INIT

    int OpenGLVersion =         3,
    int Width =                 800,
    int Height =                600,
    char* Title =               "EGB-Engine",
    GLFWmonitor * Monitor =     NULL,
    GLFWwindow  * Share =       NULL

    ){

    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, OpenGLVersion);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, OpenGLVersion);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    // This one is for mac only
    #ifdef __APPLE__
    #ifdef TARGET_OS_MAC
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
    #endif
    #endif

    /* Initialize the library */
    if (!glfwInit())
        return -1;

    /* Create a windowed mode window and its OpenGL context */
    window = glfwCreateWindow(Width, Height, (char*) Title, Monitor, Share);
    if (!window)
    {
        glfwTerminate();
        return -1;
    }

    glViewport(0, 0, Width, Height);

    /* Make the window's context current */
    glfwMakeContextCurrent(window);

    /* Loop until the user closes the window */
    while (!glfwWindowShouldClose(window))
    {
        /* Render here */
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        /* Swap front and back buffers */
        glfwSwapBuffers(window);
        /* Poll for and process events */
        glfwPollEvents();
    }

    glfwTerminate();

    return 0;
}