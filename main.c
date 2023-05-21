#include <stdio.h>
#include <string.h>
#include <raylib.h>

int widthScreen = 225;
int heightScreen = 450;
float unit = (225/45);
int clicks[] = {};

int update(void) {
}

int draw(void) {
	for(int x = 0; x < 3; x++) {
		for(int y = 0; y < 5; y++) {
			DrawRectangle((unit*(10*x))+(unit*(1+x)), heightScreen-(unit*(11*y)), unit*10, unit*10, ColorFromHSV(0, 0, 0.2));
		}
	}
	DrawRectangle(unit, heightScreen-unit*11, unit*21, unit*10, ColorFromHSV(0, 0, 0.153));
}

int main(void) {
	InitWindow(widthScreen, heightScreen, "GUessProgress Calculator");
	// SetWindowState(FLAG_WINDOW_UNDECORATED);
	
	SetTargetFPS(60);
	
	while (!WindowShouldClose()) {
		update();
		BeginDrawing();
			ClearBackground(BLACK);
			draw();
		EndDrawing();
	}
	CloseWindow();
	return 0;
}
