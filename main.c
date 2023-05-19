#include "./objects.h"
#include <stdio.h>
#include <string.h>
#include <raylib.h>

int main(void) {
	RectObject bluebox = Box(100, 100, 50, 50);
	
	InitWindow(320, 640, "RayLib");
	SetTargetFPS(60);
	
	while (!WindowShouldClose()) {
		BeginDrawing();
			ClearBackground(BLACK);
			bluebox.draw(&bluebox);
		EndDrawing();
	}
	CloseWindow();
	return 0;
}
