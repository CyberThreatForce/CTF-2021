#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <assert.h>
#include <time.h>
#include "bmp.h"

 
Image* NewImage(int w,int h)
{
        Image* I = malloc(sizeof(Image));
        I->w = w;
        I->h = h;
        I->dat = calloc(1,w*h*sizeof(Pixel*));
        return I;
}

/*/////////////////////////////////////FUNCTION THAT STORE PIXELS////////////////////////////////*/
void SetPixel(Image* I,int i,int j,Pixel p)
{
        assert(I && i>=0 && i<I->w && j>=0 && j<I->h);
        I->dat[I->w*j+i] = p;
}

/*/////////////////////////////////////FUNCTION WHICH RETRIEVE PIXELS////////////////////////////////*/
Pixel GetPixel(Image* I,int i,int j)
{
        assert(I && i>=0 && i<I->w && j>=0 && j<I->h);
        return I->dat[I->w*j+i];
}


/*/////////////////////////////////////READING COVER////////////////////////////////*/
Image* load_image(char *bmpfilename, int* pxmax, int* pymax)
{
                ///////////Instantiation
                        struct BMPHead head;
                        Image* I;
                        int pitch;
                        int i = 0, j = 0;
                        unsigned char bgrpix[3];
                        char corrpitch[4] = {0,3,2,1};
                        Pixel p;
                        
                ///////////Opening cover
			printf("Ouverture du fichier\n");
                        bmpfile = fopen(bmpfilename,"rb");
                        if (!bmpfile)
                                return NULL;
                	printf("Header en Lecture du fichier\n");
                ///////////Reading header of the cover
			int bloc_read;
                        bloc_read = fread(&head,sizeof(struct BMPHead),1,bmpfile);
                        if (head.signature[0]!='B' || head.signature[1]!='M')
                                return NULL;  // bad signature, ou BMP not supported.
                        if (head.imhead.bpp!=24)
                                return NULL;  // support only 24 bits for now
                        if (head.imhead.compression!=0)
                                return NULL;  // compression rare
			if (head.imhead.cpalette!=0 || head.imhead.cIpalette!=0)
                                return NULL;

			printf("Checking header: valid\n");
                        I = NewImage(head.imhead.width,head.imhead.height);
                        pitch = corrpitch[(3*head.imhead.width)%4];
                        
                ///////////Pixels are stored from left to right and from up and down
                        for(j=0;j<I->h;j++)
                        {
                                for(i=0;i<I->w;i++)
                                {
                                        fread(&bgrpix,1,3,bmpfile);
                                        p.r = bgrpix[2];//red
                                        p.g = bgrpix[1];//green
                                        p.b = bgrpix[0];//blue
                                        SetPixel(I,i,I->h-j-1,p);
                                }
                                fread(&bgrpix,1,pitch,bmpfile);
                        }
        
                ///////////On stocke la hauteur et la largeur de l'image
                        *pxmax = (int)I->h;
                        *pymax = (int)I->w;
                        printf("loading image : done\n");
        
                ///////////Closing gile
                        fclose(bmpfile);
    
                        return I;
}


char* stringToBinary(char* s) {
    if(s == NULL) return 0; /* Not string in input */
    size_t len = strlen(s);
    char *binary = malloc(len*8 + 1); // char (8 bits) and + (null byte) 1 
    binary[0] = '\0';
    for(size_t i = 0; i < len; ++i) {
        char ch = s[i];
        for(int j = 7; j >= 0; --j){
            if(ch & (1 << j)) {
                strcat(binary,"1");
            } else {
                strcat(binary,"0");
            }
        }
    }
    return binary;
}


int create_stego(Image* I, char* bmpfilename, char *ppayload, int *keyword)
{
		///////////Instantiation
                        struct BMPHead head;
                        Pixel p;
                        int i = 0,j = 0,u = 0,tailledata,pitch = 0, x = 0, y = 0, xmax = 0, ymax = 0, tailpay = 0, key_lenght = 0;
                        unsigned char bgrpix[3];
                        char corrpitch[4] = {0,3,2,1};
                        int ***bmpfileRGB = NULL;
			int *perm = NULL;
			int *bmpfileRGBone;
			int *cover=NULL;
       
                ///////////Opening stego
                        FILE* bmpfile = fopen(bmpfilename,"wb");
                        if (!bmpfile)
                                return -1;
			printf("Enter in stego\n");	
       			printf("W=%d & H=%d\n", I->w, I->h);

                ///////////Writing header of BMP into stego
                        memset(&head,0,sizeof(struct BMPHead));
                        head.signature[0] = 'B';
                        head.signature[1] = 'M';
                        head.offsetim = sizeof(struct BMPHead);
                        head.imhead.size_imhead = sizeof(struct BMPImHead);
                        head.imhead.width = I->w;
                        head.imhead.height = I->h;
                        head.imhead.nbplans = 1;
                        head.imhead.bpp = 24;
                        pitch = corrpitch[(3*head.imhead.width)%4];
			tailledata = 3*head.imhead.height*head.imhead.width + head.imhead.height*pitch;
                        head.imhead.sizeim = tailledata;
                        head.taille = head.offsetim + head.imhead.sizeim;
                        
			fwrite(&head,sizeof(struct BMPHead),1,bmpfile);
       		
			printf("Writing header: done\n"); 
		///////////Storing height and width
                        xmax = I->h;
                        ymax = I->w;
                ///////////Calloc of pixel storage array
			bmpfileRGBone = (int*)calloc(3*(xmax*ymax)+1, sizeof(int));
			bmpfileRGB=(int***)calloc(3, sizeof(int**));
			for(i = 0; i < 3; i++)
			{
                        	bmpfileRGB[i]=(int**)calloc(xmax, sizeof(int*));
                        	for(j = 0; j<xmax; j++)
                        		bmpfileRGB[i][j]=(int*)calloc(ymax, sizeof(int));
			}
                	perm = (int*)calloc((xmax*ymax), sizeof(int));
			
                ///////////Storing retrieved pixel in I to bmpfileRGB[u][x][y]
                        for(x = 0; x < xmax; x++)
                        {
                        	for (y = 0; y < ymax; y++)//0 for red, 1 for green, 2 blue
                                {
                                	bmpfileRGB[0][x][y] = (int)I->dat[x* (ymax)+y].r;
                                	bmpfileRGB[1][x][y] = (int)I->dat[x* (ymax)+y].g;
                                	bmpfileRGB[2][x][y] = (int)I->dat[x* (ymax)+y].b;
                                }
                        }

		///////////Lenght of Keyword
			printf("Lenght of payload: %d\n", strlen(ppayload));
			printf("Payload working: ");
			for(i = 0; i< strlen(ppayload);i++)
			{
				printf("%c", ppayload[i]);
			}
			printf("\n");
			i = 0;
			printf("keyword:");
			while(keyword[i] != '\0')
			{
				printf("%d", keyword[i]);
				i++;
			}
			key_lenght = i;
			printf("\nLenght of keyword: %d\n", key_lenght);

		///////////Filling the X(cover) with RC4 key schedule
			for(i = 0; i < 3*xmax*ymax; i++)
			{
				bmpfileRGBone[i] = 0;
			}
                        i = 0;
			u = 0, x = 0, y = 0;

			for(u = 0; u < 3; u++)
			{
                        	for(x = 0; x < xmax; x++)
                        	{
                                	for (y = 0; y < ymax; y++)//0 for red, 1 for green, 2 blue
                                	{
                                        	bmpfileRGBone[i] = (int)bmpfileRGB[u][x][y];
						if(i < xmax*ymax)
						{
                                        		perm[i] = i;
						}
                                        	i++;
                                	}
                        	}
			}
			printf("End of permutation\n");
                        j = 0;
                        i = 0;
			printf("Xmax:%d, Ymax: %d\n", xmax, ymax);
                        for(x = 0; x < xmax; x++)
                        {
                                for (y = 0; y < ymax; y++)//0 for red, 1 for green, 2 blue
                                {
                                        j = (j + perm[i] + keyword[i%key_lenght])%(xmax*ymax);
                                        perm[i] ^= perm[j];
                                        perm[j] ^= perm[i];
                                        perm[i] ^= perm[j];
                                        i++;
                                }
                        }

			printf("Message insertion perm[%d]:%d, lenght:%d\n", i, perm[i], strlen(ppayload));

		/////////Message Insertion
			cover = (int*)calloc(strlen(ppayload), sizeof(int));
                        for(i = 0; i < strlen(ppayload); i++)
                        {
				cover[i] = bmpfileRGBone[perm[i]];
				if(ppayload[i] == '1')
				{
					bmpfileRGBone[perm[i]] = (bmpfileRGBone[perm[i]] >> 1) <<1 | 1;
				}
				else
				{
					bmpfileRGBone[perm[i]] = (bmpfileRGBone[perm[i]] >> 1) <<1;
				}
                        }
			printf("\n");
			i = 0;
			printf("cover:");
			for(u = 0; u < 3; u++)
			{
				for(x = 0; x < xmax; x++)
				{
					for(y = 0; y < xmax; y++)
					{
						bmpfileRGB[u][x][y] = bmpfileRGBone[i];
						i++;
					}
				}
			}
			printf("\n");
			
		///////////Storing pixels of stego in I
                        for(x = 0; x < xmax; x++)
                        {
                                for (y = 0; y < ymax; y++)//0 for red, 1 for green, 2 blue
                                {
                                        I->dat[x* (ymax)+y].r = bmpfileRGB[0][x][y];
                                        I->dat[x* (ymax)+y].g = bmpfileRGB[1][x][y];
                                        I->dat[x* (ymax)+y].b = bmpfileRGB[2][x][y];
                                }
                        }
                
                ///////////Writing pîxelsin the new image created (stego)
                        for(j=0;j<I->h;j++)
                        {
                                for(i=0;i<I->w;i++)
                                {
                                        assert(I && i>=0 && i<I->w && j>=0 && j<I->h);
                                        p = I->dat[I->w*(I->h-j-1)+i];//(I->h-j-1) because we write in the sense of BMP
                                        bgrpix[0] = p.b;
                                        bgrpix[1] = p.g;
                                        bgrpix[2] = p.r;
                                        fwrite(&bgrpix,1,3,bmpfile);
                                }
                        }
                        bgrpix[0] = bgrpix[1] = bgrpix[2] = 0;
                        fwrite(&bgrpix,1,pitch,bmpfile);


			printf("CREATE_STEGO : effectue \n");
		///////////FREE
			for(u = 0; u < 3; u++)
			{
                     		for(j = 0; j < xmax; j++)
                        		free(bmpfileRGB[u][j]);
                        	free(bmpfileRGB[u]);
			}
                        free(bmpfileRGB);
		///////////Closing file
                        fclose(bmpfile);
			return 0;
}

int main( int argc, char** argv)
{
                ///////////Instantiation
                        int xmax = 0, ymax = 0, i = 0, j = 0, cpt2 = 0, erreur = 0, x = 0, y = 0;
                        char *payload = NULL; 
			char *password = "General crypto: Hill cipher 2*2 ascii_lowercase+digits+space respectively in order stop  Cipher ovrjiaveaswjiqtrwlq1yklkxpqju2uptmkklwyyqwzthmma8mkwd8m8eekww5ew25hkk2hqkq5ty8qkknt2wnw8ui";
                        Image *I;

                ///////////Term of use of the program
                        if(argc<4)
			{
                                 printf("use:appname inputname password stego\n");
				 return EXIT_FAILURE;
			}
                        else
                        {
				int *keyword = NULL;
				char *output = NULL;
				payload = (char*)calloc(strlen(password), sizeof(char));
				keyword=(int*)calloc(strlen(argv[2]), sizeof(int));
				printf("keyword:");
				for(i=0;i<strlen(argv[2]);i++)
				{
					keyword[i] = (int)argv[2][i];
					printf("%d",keyword[i]);
				}
				printf("\n");
				payload = stringToBinary(password);
				printf("Phrase: %s\n", payload);
                                I = load_image(argv[1], &xmax, &ymax);//Loading cover in I
				printf("Longueur payload: %d\n", strlen(payload));
				create_stego(I,  argv[3],  payload, keyword);
			///////////FREE
				free(I->dat);
				free(keyword);
				free(payload);
                        	free(I);
                        	return EXIT_SUCCESS;
                        }
}
