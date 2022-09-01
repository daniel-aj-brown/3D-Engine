# A Software 3D Graphics Renderer.
 
The aim of this project was to learn how computers render 3D graphics. To do this, a 3D scene was created and a simple unit cube can be seen rotating around a world axis.
 
Upon initialisation the Engine will create an instance of a camera, the unit cube and a world axes. The controls are as follows:
 
- Move the camera forward, backward, left and right with the "WASD" keys.
- Move the camera up and down with the Up and Down keys.
- Rotate the camera left and right with the Left and Right keys.
 
The 3D effect is created by keeping track of all vertices in 3D space, multiplying them by rotation and translation matrices to mimic movement through 3D space. Once the location in 3D space has been calculated, the vertices of each face are then projected onto a 2D plane by using a projection matrix, in relation to the camera's location. If the screen coordinates are larger than the clip amount designated by the user, defaulted to 2 the face is clipped as drawing a face too close to the camera would slow down the program.
 
Next, by calculating the cross products of two vectors calculated from three vertices on each face we can find the normal to the face which is then normalised. This normal is then compared with the camera's look direction with the dot product, if the value of less than 0 the face is visible and must be drawn. The dot product is then calculated between the normal and the single light in the scene to determine its shading.
 
Finally a polygon of the appropriate shade is drawn on the screen for each face to give the illusion of 3D.
 
More objects can be added to the scene to create a basic 3D world.
