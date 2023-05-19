#include <string.h>
#include <raylib.h>

typedef struct {
    int x, y, width, height;
    int (*draw)(struct RectObject*);
} RectObject;

int drawObject(RectObject* obj) {
    obj->x += 10; // Example: Adding 10 to RectObject.x
    DrawRectangle(obj->x, obj->y, obj->width, obj->height, BLUE);
    return 0;
}

RectObject Box(int x, int y, int width, int height) {
    RectObject that;
    that.x = x;
    that.y = y;
    that.width = width;
    that.height = height;
    that.draw = &drawObject;
    return that;
}

RectObject DefaultBox() {
    return Box(10, 10, 10, 10);
}