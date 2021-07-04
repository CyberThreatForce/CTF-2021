
#ifndef _BMP_H
#define _BMP_H
FILE *bmpfile;//input file

typedef struct Pixel
{
	unsigned char r,g,b;
} Pixel;

typedef struct Image
{
	int w,h;
	Pixel* dat;
} Image;

#pragma pack(1)  // disable memory alignment
typedef int int32;
typedef short int16;

struct BMPImHead
{
	int32 size_imhead;
	int32 width;
	int32 height;
	int16 nbplans; // always 1
	int16 bpp;
	int32 compression;
	int32 sizeim;
	int32 hres;
	int32 vres;
	int32 cpalette;
	int32 cIpalette;
};

struct BMPHead
{
	char signature[2];
	int32 taille;
	int32 rsv;
	int32 offsetim;
	struct BMPImHead imhead;
};

Image* load_image(char *bmpfilename, int* pxmax, int* pymax);
Image* NewImage(int w,int h);
void SetPixel(Image*,int i,int j,Pixel p);
Pixel GetPixel(Image*,int i,int j);

#endif
