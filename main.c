#include <stdio.h>
#include <string.h>
#include <stddef.h>
#include <raylib.h>

int widthScreen = 225;
int heightScreen = 450;
float unit = (225/45);
int clicks[] = {};

int update(void) {}

int draw(Font OpenSansBold) {
	for(int x = 0; x < 3; x++) {
		for(int y = 0; y < 5; y++) {
			DrawRectangle((unit*(10*x))+(unit*(1+x)), heightScreen-(unit*(11*y)), unit*10, unit*10, ColorFromHSV(0, 0, 0.153));
		}
	}
	DrawRectangle(unit, heightScreen-unit*11, unit*21, unit*10, ColorFromHSV(0, 0, 0.153));
	DrawTextEx(OpenSansBold, ".", (Vector2){ unit*2.5+unit*25-MeasureText(".", 35)/2, heightScreen-unit*6-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "0", (Vector2){ unit+unit*21/2-MeasureText("0", 35)/2, heightScreen-unit*6-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "1", (Vector2){ unit+unit*4-MeasureText("1", 35)/2, heightScreen-unit*2-unit*15-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "2", (Vector2){ unit*2+unit*15-MeasureText("2", 35)/2, heightScreen-unit*2-unit*15-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "3", (Vector2){ unit*3+unit*25-MeasureText("3", 35)/2, heightScreen-unit*2-unit*15-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "4", (Vector2){ unit+unit*5-MeasureText("4", 35)/2, heightScreen-unit*3-unit*25-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "5", (Vector2){ unit*2+unit*15-MeasureText("5", 35)/2, heightScreen-unit*3-unit*25-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "6", (Vector2){ unit*3+unit*25-MeasureText("6", 35)/2, heightScreen-unit*3-unit*25-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "7", (Vector2){ unit+unit*5-MeasureText("7", 35)/2, heightScreen-unit*4-unit*35-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "8", (Vector2){ unit*2+unit*15-MeasureText("8", 35)/2, heightScreen-unit*4-unit*35-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
	DrawTextEx(OpenSansBold, "9", (Vector2){ unit*3+unit*25-MeasureText("9", 35)/2, heightScreen-unit*4-unit*35-35/2}, 35, 1, ColorFromHSV(0, 0, 0.65));
}

int main(void) {
	InitWindow(widthScreen, heightScreen, "GUessProgress Calculator");
	// SetWindowState(FLAG_WINDOW_UNDECORATED);
	const char* fontFile = "OpenSans-Bold.ttf";
	int fontSize = 35;
	Font OpenSansBold = LoadFontEx(fontFile, fontSize, NULL, 0);
	SetTargetFPS(60);
	
	while (!WindowShouldClose()) {
		update();
		BeginDrawing();
			ClearBackground(BLACK);
			draw(OpenSansBold);
		EndDrawing();
	}
	CloseWindow();
	return 0;
}
