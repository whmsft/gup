#include <string.h>
#include <raylib.h>

typedef struct {
    int x, y, width, height;
    int (*draw)(struct RectObject*);
    int (*update)(struct RectObject*);
} RectObject;

int updateObject(RectObject* obj) {
    obj->x += 10;
    return 0;
}

int drawObject(RectObject* obj) {
    obj->x += 10;
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
    that.update = &updateObject;
    return that;
}

RectObject DefaultBox() {
    return Box(10, 10, 10, 10);
}