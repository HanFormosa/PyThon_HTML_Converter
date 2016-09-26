
#include <i2c.h>
#include <math.h>

#include "DSP1701.h"
#include "HardwareProfile.h"
#include "DEE Emulation 16-bit.h"
#define HIGH 1
#define LOW 0
//=====< DSP >================================================================================================
/* Bypass */
//#define PROG_Size      24  // Programe Code 
//#define PARA_Size       2  // Parameter Code 

/* SVS-8000D */
#define PROG_Size    917 // Programe Code 
#define PARA_Size    378 // Parameter Code 

extern void delayms(int);

double vol_tbl[]={
 0                 ,
-0.500000000000000,
-1                ,
-1.50000000000000 ,
-2                ,
-2.50000000000000 ,
-3                ,
-3.50000000000000 ,
-4                ,
-4.50000000000000 ,
-5                ,
-5.50000000000000 ,
-6                ,
-6.50000000000000 ,
-7                ,
-7.50000000000000 ,
-8                ,
-8.50000000000000 ,
-9                ,
-9.50000000000000 ,
-10               ,
-10.5000000000000 ,
-11               ,
-11.5000000000000 ,
-12               ,
-12.5000000000000 ,
-13               ,
-13.5000000000000 ,
-14               ,
-14.5000000000000 ,
-15               ,
-15.5000000000000 ,
-15.5000000000000 ,
-16.5000000000000 ,
-17.5000000000000 ,
-18.5000000000000 ,
-19.5000000000000 ,
-20.5000000000000 ,
-21.5000000000000 ,
-22.5000000000000 ,
-23.5000000000000 ,
-24.5000000000000 ,
-25.5000000000000 ,
-26.5000000000000 ,
-27.5000000000000 ,
-28.5000000000000 ,
-29.5000000000000 ,
-30.5000000000000 ,
-31.5000000000000 ,
-32.5000000000000 ,
-33.5000000000000 ,
-34.5000000000000 ,
-35.5000000000000 ,
-36.5000000000000 ,
-37.5000000000000 ,
-38.5000000000000 ,
-39.5000000000000 ,
-40.5000000000000 ,
-41.5000000000000 ,
-47.5000000000000 ,
-52.5000000000000 ,
-57.5000000000000 ,
-67.5000000000000 ,
-100.000000000000
};

double eq_gain_tbl[]={
-12,
-11,
-10                ,
-9,
-8                ,
-7,
-6               ,
-5,
-4,
-3,
-2.5,
-2 ,
-1.5                ,
-1,
0,
0                ,
0,
0,
1,
1.5                ,
2,
2.5               ,
3,
4               ,
5,
6               ,
7,
8               ,
9,
10               ,
11,
12,

};
//-----< DSP Program Code >-----------------------------------------------
//-----< DSP Program Code >-----------------------------------------------
const unsigned char PROGRAM_DATA[PROG_Size*5] ={
};
//-----< DSP Parameter Code >---------------------------------------------
const unsigned char PARAMETER_DATA[] =
{

0x00, 0x00, 0x00, 0x10, 
0x00, 0x00, 0x00, 0x10, 
0x00, 0x00, 0x00, 0x01, 
0x00, 0x01, 0x47, 0xAE, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x01, 0x47, 0xAE, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x20, 0x00, 0x00, 
0x02, 0x80, 0x00, 0x00, 
0x00, 0x7E, 0x5F, 0x50, 
0xFF, 0x07, 0x68, 0xB3, 
0x00, 0x7A, 0x4B, 0x28, 
0x00, 0xF8, 0x82, 0x93, 
0xFF, 0x87, 0x40, 0xCF, 
0x00, 0x7E, 0x97, 0x0C, 
0xFF, 0x07, 0x27, 0x27, 
0x00, 0x7A, 0x56, 0x85, 
0x00, 0xF8, 0xC7, 0x1C, 
0xFF, 0x87, 0x00, 0xB1, 
0x00, 0x7E, 0xCE, 0xAE, 
0xFF, 0x06, 0xE7, 0x65, 
0x00, 0x7A, 0x60, 0x52, 
0x00, 0xF9, 0x09, 0xC1, 
0xFF, 0x86, 0xC2, 0x26, 
0x00, 0x7F, 0x06, 0x3B, 
0xFF, 0x06, 0xA9, 0x70, 
0x00, 0x7A, 0x68, 0x89, 
0x00, 0xF9, 0x4A, 0x84, 
0xFF, 0x86, 0x85, 0x30, 
0x00, 0x7F, 0x3D, 0xBB, 
0xFF, 0x06, 0x6D, 0x48, 
0x00, 0x7A, 0x6F, 0x26, 
0x00, 0xF9, 0x89, 0x6A, 
0xFF, 0x86, 0x49, 0xD1, 
0x00, 0x7F, 0x75, 0x34, 
0xFF, 0x06, 0x32, 0xED, 
0x00, 0x7A, 0x74, 0x26, 
0x00, 0xF9, 0xC6, 0x76, 
0xFF, 0x86, 0x10, 0x09, 
0x00, 0x7F, 0xAC, 0xB0, 
0xFF, 0x05, 0xFA, 0x5A, 
0x00, 0x7A, 0x77, 0x86, 
0x00, 0xFA, 0x01, 0xB2, 
0xFF, 0x85, 0xD7, 0xD6, 
0x00, 0x7F, 0xE4, 0x36, 
0xFF, 0x05, 0xC3, 0x8C, 
0x00, 0x7A, 0x79, 0x45, 
0x00, 0xFA, 0x3B, 0x23, 
0xFF, 0x85, 0xA1, 0x34, 
0x00, 0x80, 0x1B, 0xD0, 
0xFF, 0x05, 0x8E, 0x7E, 
0x00, 0x7A, 0x79, 0x63, 
0x00, 0xFA, 0x72, 0xD4, 
0xFF, 0x85, 0x6C, 0x1F, 
0x00, 0x80, 0x53, 0x87, 
0xFF, 0x05, 0x5B, 0x2A, 
0x00, 0x7A, 0x77, 0xE1, 
0x00, 0xFA, 0xA8, 0xCD, 
0xFF, 0x85, 0x38, 0x90, 
0x00, 0x80, 0x8B, 0x63, 
0xFF, 0x05, 0x29, 0x8B, 
0x00, 0x7A, 0x74, 0xC0, 
0x00, 0xFA, 0xDD, 0x19, 
0xFF, 0x85, 0x06, 0x82, 
0x00, 0x80, 0xC3, 0x6E, 
0xFF, 0x04, 0xF9, 0x99, 
0x00, 0x7A, 0x70, 0x03, 
0x00, 0xFB, 0x0F, 0xC3, 
0xFF, 0x84, 0xD5, 0xEB, 
0x00, 0x80, 0xFB, 0xB0, 
0xFF, 0x04, 0xCB, 0x4D, 
0x00, 0x7A, 0x69, 0xAE, 
0x00, 0xFB, 0x40, 0xD7, 
0xFF, 0x84, 0xA6, 0xC5, 
0x00, 0x81, 0x34, 0x31, 
0xFF, 0x04, 0x9E, 0xA0, 
0x00, 0x7A, 0x61, 0xC6, 
0x00, 0xFB, 0x70, 0x5E, 
0xFF, 0x84, 0x79, 0x07, 
0x00, 0x81, 0x6C, 0xF9, 
0xFF, 0x04, 0x73, 0x8A, 
0x00, 0x7A, 0x58, 0x50, 
0x00, 0xFB, 0x9E, 0x66, 
0xFF, 0x84, 0x4C, 0xA7, 
0x00, 0x81, 0xA6, 0x0E, 
0xFF, 0x04, 0x4A, 0x04, 
0x00, 0x7A, 0x4D, 0x55, 
0x00, 0xFB, 0xCA, 0xFA, 
0xFF, 0x84, 0x21, 0x9C, 
0x02, 0x80, 0x00, 0x00, 
0x00, 0x34, 0x24, 0xA0, 
0xFF, 0xD2, 0x30, 0xFA, 
0x00, 0x11, 0x46, 0xF3, 
0x00, 0xAA, 0x63, 0x1A, 
0xFF, 0xBE, 0x00, 0x59, 
0x00, 0x3A, 0xC2, 0x1B, 
0xFF, 0xCA, 0x4F, 0x5C, 
0x00, 0x14, 0x15, 0x09, 
0x00, 0xA7, 0x27, 0x72, 
0xFF, 0xBF, 0xB2, 0x0E, 
0x00, 0x42, 0x38, 0x92, 
0xFF, 0xC1, 0x34, 0xCB, 
0x00, 0x17, 0x59, 0xE5, 
0x00, 0xA3, 0xD5, 0xEB, 
0xFF, 0xC1, 0x62, 0xD4, 
0x00, 0x4A, 0xA3, 0xBE, 
0xFF, 0xB6, 0xB3, 0xCD, 
0x00, 0x1B, 0x28, 0x4D, 
0x00, 0xA0, 0x6E, 0x23, 
0xFF, 0xC3, 0x12, 0x05, 
0x00, 0x54, 0x22, 0xD4, 
0xFF, 0xAA, 0x98, 0xAA, 
0x00, 0x1F, 0x95, 0xD2, 
0x00, 0x9C, 0xEF, 0xC4, 
0xFF, 0xC4, 0xBE, 0xED, 
0x00, 0x5E, 0xD8, 0xED, 
0xFF, 0x9C, 0xA8, 0x9B, 
0x00, 0x24, 0xBB, 0x32, 
0x00, 0x99, 0x5A, 0x7E, 
0xFF, 0xC6, 0x68, 0xC8, 
0x00, 0x6A, 0xED, 0x80, 
0xFF, 0x8C, 0xA0, 0xE2, 
0x00, 0x2A, 0xB4, 0xC9, 
0x00, 0x95, 0xAE, 0x0D, 
0xFF, 0xC8, 0x0E, 0xC8, 
0x00, 0x78, 0x8C, 0xE6, 
0xFF, 0x7A, 0x35, 0xC5, 
0x00, 0x31, 0xA3, 0x10, 
0x00, 0x91, 0xEA, 0x36, 
0xFF, 0xC9, 0xB0, 0x0E, 
0x00, 0x87, 0xE8, 0xF4, 
0xFF, 0x65, 0x11, 0x6D, 
0x00, 0x39, 0xAB, 0x29, 
0x00, 0x8E, 0x0E, 0xC7, 
0xFF, 0xCB, 0x4B, 0xAF, 
0x00, 0x99, 0x39, 0x99, 
0xFF, 0x4C, 0xD2, 0x9A, 
0x00, 0x42, 0xF7, 0x81, 
0x00, 0x8A, 0x1B, 0x9C, 
0xFF, 0xCC, 0xE0, 0xB0, 
0x00, 0xAC, 0xBD, 0x9E, 
0xFF, 0x31, 0x0B, 0x39, 
0x00, 0x4D, 0xB8, 0x83, 
0x00, 0x86, 0x10, 0x9A, 
0xFF, 0xCE, 0x6E, 0x0B, 
0x00, 0xC2, 0xBB, 0x73, 
0xFF, 0x11, 0x3E, 0xC7, 
0x00, 0x5A, 0x25, 0x68, 
0x00, 0x81, 0xED, 0xB0, 
0xFF, 0xCF, 0xF2, 0xAD, 
0x00, 0xDB, 0x82, 0x12, 
0xFE, 0xEC, 0xE0, 0x89, 
0x00, 0x68, 0x7D, 0x16, 
0x00, 0x7D, 0xB2, 0xDB, 
0xFF, 0xD1, 0x6D, 0x74, 
0x00, 0xF7, 0x6A, 0x00, 
0xFE, 0xC3, 0x51, 0x88, 
0x00, 0x79, 0x07, 0x25, 
0x00, 0x79, 0x60, 0x21, 
0xFF, 0xD2, 0xDD, 0x32, 
0x01, 0x16, 0xD6, 0x6A, 
0xFE, 0x93, 0xDE, 0x54, 
0x00, 0x8C, 0x15, 0x02, 
0x00, 0x74, 0xF5, 0x94, 
0xFF, 0xD4, 0x40, 0xAD, 
0x01, 0x3A, 0x36, 0x62, 
0xFE, 0x5D, 0xBC, 0x7F, 
0x00, 0xA2, 0x03, 0x30, 
0x00, 0x70, 0x73, 0x52, 
0xFF, 0xD5, 0x96, 0x9E, 
0x00, 0x40, 0x00, 0x00, 
0x00, 0x7F, 0xD2, 0xB9, 
0x0F, 0x00, 0x5A, 0x8F, 
0x00, 0x7F, 0xD2, 0xB9, 
0x00, 0xFF, 0xA5, 0x61, 
0x0F, 0x80, 0x5A, 0x7F, 
0x00, 0x7F, 0xCF, 0xB4, 
0x0F, 0x00, 0x60, 0x97, 
0x00, 0x7F, 0xCF, 0xB4, 
0x00, 0xFF, 0x9F, 0x57, 
0x0F, 0x80, 0x60, 0x85, 
0x00, 0x58, 0x53, 0x40, 
0x00, 0xB0, 0xA6, 0x81, 
0x00, 0x58, 0x53, 0x40, 
0x0F, 0x5C, 0x08, 0x53, 
0x0F, 0xC2, 0xAA, 0xAB, 
0x00, 0x7F, 0xC9, 0xAC, 
0x0F, 0x00, 0x6C, 0xA7, 
0x00, 0x7F, 0xC9, 0xAC, 
0x00, 0xFF, 0x93, 0x41, 
0x0F, 0x80, 0x6C, 0x90, 
0x00, 0x7F, 0xCC, 0xB0, 
0x0F, 0x00, 0x66, 0x9F, 
0x00, 0x7F, 0xCC, 0xB0, 
0x00, 0xFF, 0x99, 0x4C, 
0x0F, 0x80, 0x66, 0x8B, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x58, 0x51, 0x20, 
0x00, 0xB0, 0xA2, 0x3F, 
0x00, 0x58, 0x51, 0x20, 
0x0F, 0x5C, 0x0D, 0xFA, 
0x0F, 0xC2, 0xAD, 0x87, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x0E, 
0x0F, 0x00, 0x20, 0x34, 
0x00, 0x7F, 0xE0, 0x51, 
0x00, 0xFF, 0xDF, 0xCC, 
0x0F, 0x80, 0x1F, 0xA1, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x01, 
0x00, 0x00, 0x00, 0x01, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x20, 0x00, 
0x00, 0x20, 0x00, 0x00, 
0x0F, 0xFE, 0x2B, 0xE3, 
0x00, 0x22, 0xBE, 0x2C, 
0x0F, 0xEA, 0xAA, 0xAB, 
0x00, 0x6A, 0xAA, 0xAB, 
0x0F, 0x9A, 0x69, 0xA7, 
0x00, 0xFD, 0xF7, 0xDF, 
0x08, 0x3C, 0x6C, 0x20, 
0x03, 0xF5, 0xAA, 0x23, 
0x01, 0x80, 0x00, 0x00, 
0x01, 0x00, 0x00, 0x00, 
0x00, 0x33, 0x33, 0x33, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x07, 0xDC, 
0x00, 0x00, 0x08, 0x00, 
0x00, 0x7F, 0xF0, 0x00, 
0x0F, 0xFE, 0x2B, 0xE3, 
0x00, 0x22, 0xBE, 0x2C, 
0x0F, 0xEA, 0xAA, 0xAB, 
0x00, 0x6A, 0xAA, 0xAB, 
0x0F, 0x9A, 0x69, 0xA7, 
0x00, 0xFD, 0xF7, 0xDF, 
0x08, 0x3C, 0x6C, 0x20, 
0x03, 0xF5, 0xAA, 0x23, 
0x01, 0x80, 0x00, 0x00, 
0x01, 0x00, 0x00, 0x00, 
0x00, 0x33, 0x33, 0x33, 
0x00, 0x8F, 0x9E, 0x4D, 
0x00, 0x00, 0x07, 0xDC, 
0x00, 0x00, 0x08, 0x00, 
0x00, 0x7F, 0xF0, 0x00, 
0x00, 0x40, 0x00, 0x00, 
0x00, 0x00, 0x03, 0xC0, 
0x00, 0x00, 0x00, 0xB6, 
0x0F, 0x80, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00, 
0x00, 0x06, 0x4A, 0x36, 
0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x07, 0x1C, 
0x0F, 0xFE, 0x2B, 0xE3, 
0x00, 0x22, 0xBE, 0x2C, 
0x0F, 0xEA, 0xAA, 0xAB, 
0x00, 0x6A, 0xAA, 0xAB, 
0x0F, 0x9A, 0x69, 0xA7, 
0x00, 0xFD, 0xF7, 0xDF, 
0x08, 0x3C, 0x6C, 0x20, 
0x03, 0xF5, 0xAA, 0x23, 
0x01, 0x80, 0x00, 0x00, 
0x01, 0x00, 0x00, 0x00, 
0x00, 0x33, 0x33, 0x33, 
0x00, 0x8F, 0x9E, 0x4D, 
0x00, 0x00, 0x07, 0xDC, 
0x00, 0x00, 0x08, 0x00, 
0x00, 0x7F, 0xF0, 0x00, 
0x0F, 0x80, 0x00, 0x00, 
0x00, 0x80, 0x00, 0x00,  

};
//-----< DSP Register Code >----------------------------------------------
unsigned char DSP_Regist[] =
{
//0X00, 0X18, 0X08, 0X00, 0X00, 0X00, 0X00, 0XFF, 0X22, 0X00, 0XFF, 0X02, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01
//0X00, 0X18, 0X08, 0X00, 0X00, 0X00, 0X00, 0X00, 0X22, 0X00, 0X00, 0X77, 0X00, 0XEF, 0X00, 0X00, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01
0X00, 0X18, 0X08, 0X00, 0X00, 0X00, 0X00, 0XFF, 0XAA, 0X00, 0XFF, 0X02, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01
//0x00, 0x18, 0x08, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x22, 0x00, 0xFF, 0x02, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01
};

//-----< DSP  >--------------------------------------------------------
unsigned char Parameter_Hex[5];
unsigned char Param_Hex[4];
unsigned char DSP_Busy_FLAG;
//=====< DSP  >==========================================================================================
//-----<  DSP >------------------------------------------------------------
void LoadDSP( void )
{
 DSP_Write( DSP_Core, 0, 0x00, 0x00, 0x18, 0, 2 );                 // 

  DSP_All_Write( PROGRAM_DATA, PARAMETER_DATA );

  DSP_Write( DSP_Core, 0, DSP_Regist, 0, 0, 24, 3 );                // 

  DSP_Write( DSP_Core, 0, 0x00, 0x00, 0x1C, 0, 2 );                 // 
}

void DSP_All_Write( const unsigned char *ProgData, const unsigned char *ParaData )
{
  unsigned int Length;
  int Index;


  DSP_Busy_FLAG = HIGH;
  Length = PROG_Size * 5;
  IdleI2C1( );
  StartI2C1( );                               // START 
  IdleI2C1( );
  MasterWriteI2C1( DSP_Chip_Address );              //  DSP Chip Address
while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  MasterWriteI2C1( 0x04 );                          //  DSP Programe Address High Byte
while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  MasterWriteI2C1( 0x00 );                          //  DSP Programe Address Low Byte
while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  for( Index = 0; Index < Length; Index++ )
  { MasterWriteI2C1( ProgData[Index] );
while( !I2C1STATbits.ACKSTAT ) break;
	IdleI2C1( );
  }
  if( PROG_Size < 1024 )
  {
    for( Index = 1024 - PROG_Size; Index > 0; Index-- )
    {
      I2C_Write_Loop( 0x00, 4 );
      MasterWriteI2C1( 0x01 );
while( !I2C1STATbits.ACKSTAT ) break;
      IdleI2C1( );
    }
  }
  StopI2C1( );
  IdleI2C1( );                              // STOP 

  Length = PARA_Size * 4;                    //

  IdleI2C1( );
  StartI2C1( );                               // START 
  IdleI2C1( );
  MasterWriteI2C1( DSP_Chip_Address );              //  DSP Chip Address
while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  MasterWriteI2C1( 0x00 );                          //  DSP Parameter Address High Byte
while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  MasterWriteI2C1( 0x00 );                          //  DSP Parameter Address Low Byte
while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  for( Index = 0; Index < Length; Index++ )
  {
	MasterWriteI2C1( ParaData[Index] );
	while( !I2C1STATbits.ACKSTAT ) break;
  	IdleI2C1( );
  }
  if( Length < 4096 )
  {
    for ( Index = 1024 - PARA_Size; Index > 0; Index-- )
      I2C_Write_Loop( 0x00, 4 );
  }
  StopI2C1( );                                // STOP 
  IdleI2C1( );
  DSP_Busy_FLAG = LOW;
}
//-----<  DSP >------------------------------------------------------------
void DSP_Write( int Address1, int Address2, unsigned char *Data, unsigned char Data1, unsigned char Data2, int Length, unsigned char Mode )
{
  int Index = 0;
  unsigned char Address1_H = Address1 >> 8;
  unsigned char Address1_L = Address1;
  unsigned char Address2_H = Address2 >> 8;
  unsigned char Address2_L = Address2;
  DSP_Busy_FLAG = HIGH;
  IdleI2C1( );
  StartI2C1( );                               // START 
  IdleI2C1( );
  MasterWriteI2C1( DSP_Chip_Address );              //  DSP Chip Address
  while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  MasterWriteI2C1( Address1_H );                    //  DSP Sub Address High Byte
  while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  MasterWriteI2C1( Address1_L );                    //  DSP Sub Address Low Byte
  while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
  switch( Mode )
  {
    case 1:
      break;
    case 2:
    {
      MasterWriteI2C1( Data1 );
  while( !I2C1STATbits.ACKSTAT ) break;
  	  IdleI2C1( );
      MasterWriteI2C1( Data2 );
  while( !I2C1STATbits.ACKSTAT ) break;
  	  IdleI2C1( );
      break;
    }
    case 3:
    {
      for( Index = 0; Index < Length; Index++ )
      {
        MasterWriteI2C1( Data[Index] );
  while( !I2C1STATbits.ACKSTAT ) break;
  	    IdleI2C1( );
      }
      break;
    }
    case 4:
    {
      MasterWriteI2C1( Address2_H );
  while( !I2C1STATbits.ACKSTAT ) break;
  	  IdleI2C1( );
      MasterWriteI2C1( Address2_L );
  while( !I2C1STATbits.ACKSTAT ) break;
  	  IdleI2C1( );
      break;
    }
  }
  StopI2C1( );                   // STOP 
  IdleI2C1( );
  DSP_Busy_FLAG = LOW;
}
//-----<  DSP >----------------------------------------------------
void SafeloadSingleParamWrite( int Address, float Parameter, int Location, unsigned char Enable )
{
  Format_Fix( Parameter );                                                // 
  Parameter_Hex[0] = 0x00;
  Parameter_Hex[1] = Param_Hex[0];
  Parameter_Hex[2] = Param_Hex[1];
  Parameter_Hex[3] = Param_Hex[2];
  Parameter_Hex[4] = Param_Hex[3];
  DSP_Write( SAFELOAD_DATA_0 + Location, 0, Parameter_Hex, 0, 0, 5, 3 );  //  DATA
  DSP_Write( SAFELOAD_ADDRESS_0 + Location, Address, 0, 0, 0, 0, 4 );     //  ADDRESS
  if ( Enable )
    DSP_Write( DSP_Core, 0, 0x00, 0x00, 0x3C, 0, 2 );                     // DSP 
}

void SafeloadSingleParamWrite2( int Address, float Parameter, int Location, unsigned char Enable )
{
  //Format_Fix( Parameter );                                                // 
  Parameter_Hex[0] = 0x00;
  Parameter_Hex[1] = 0x00;
  Parameter_Hex[2] = 0x00;
  Parameter_Hex[3] = 0x00;
  Parameter_Hex[4] = Parameter;

  DSP_Write( SAFELOAD_DATA_0 + Location, 0, Parameter_Hex, 0, 0, 5, 3 );  //  DATA
  DSP_Write( SAFELOAD_ADDRESS_0 + Location, Address, 0, 0, 0, 0, 4 );     //  ADDRESS
  if ( Enable )
    DSP_Write( DSP_Core, 0, 0x00, 0x00, 0x3C, 0, 2 );                     //  DSP 
}
//-----<  >--------------------------------------------------------
void Format_Fix( float Param_Dec )
{
  long Param223;
  long Param227;
  Param223 = Param_Dec * 8388608;         // Multiply decimal number by 2^23
  Param227 = Param223 + 134217728;        // Convert to positive binary
  Param_Hex[3]=(char)Param227;            // Get byte 3 (LSBs) of parameter value
  Param_Hex[2]=(char)( Param227 >> 8 );   // Get byte 2 of parameter value
  Param_Hex[1]=(char)( Param227 >> 16 );  // Get byte 1 of parameter value
  Param_Hex[0]=(char)( Param227 >> 24 );  // Get byte 0 (MSBs) of parameter value
  Param_Hex[0] = Param_Hex[0] ^ 0x08;     // Invert sign bit to get correct sign
}
//-----< I2C  >---------------------------------------------------------
void I2C_Write_Loop( unsigned char Data, unsigned char Count )
{
  for(; Count > 0; Count--) {
	MasterWriteI2C1( Data );
while( !I2C1STATbits.ACKSTAT ) break;
  IdleI2C1( );
}
}
//----< DSP Read Data >---------------------------------------------------------
//long DSPRealRead( int Address )
//{
//  unsigned long Data = 0;
//  DSP_Busy_FLAG = HIGH;
//  IdleI2C( );                           //  I2C BUS 
//  StartI2C( );                          // START 
//  WriteI2C( DSP_Chip_Address | 0x01 );  //  DSP Chip Address ( Read )
//  WriteI2C( 0x03 );
//  Nop( );
//  Nop( );
//  WriteI2C( ( char )( Address >> 8 ) );
//  WriteI2C( ( char )Address );
//  Nop( );
//  Nop( );
//  Data = ( unsigned long )ReadI2C( ) << 24;
//  Data |= ( unsigned long )ReadI2C( ) << 16;
//  Data |= ( unsigned long )ReadI2C( ) << 8;
//  //Data |= ReadI2C();
//  DSP_Busy_FLAG = LOW;
//  return( Data );
//}

//=====< DSP  >==============================================================================================
//-----< Volume Control >------------------------------------------------------
void Volume_Slow( unsigned int Vol_Address, double dB, double SW_Rate )	//	sw rate	
{
  double Vol, Index, Rate;
  DSP_Busy_FLAG = HIGH;
  Vol = pow( 10,( dB / 20 ) );
  SafeloadSingleParamWrite( Vol_Address, Vol, 0, 1 );
  Rate = 0.5;
  for( Index = 1; Index < SW_Rate; Index++ )
  {
    Rate = Rate / 2;
  }
  SafeloadSingleParamWrite( Vol_Address + 1, Rate, 0, 1 );
  DSP_Busy_FLAG = LOW;
}
//-----< Peaking Filter >------------------------------------------------------
void Peaking( unsigned int Address, double Boost, double Frequency, double Q, double Gain )
{
  double WO,SinW0,CosW0,Alpha,A,A0,GainLinear;
  double Coeff[] = { 0, 0, 0, 0, 0 };            // Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=B2 , Coeff[3]=A1 , Coeff[4]=A2
  DSP_Busy_FLAG = HIGH;
  A = pow( 10, Boost / 40 );
  WO =( 6.2831853071795862 * Frequency ) / 48000;
  SinW0 = sin( WO );
  CosW0 = cos( WO );
  Alpha = SinW0 / ( 2 * Q );
  A0 = 1.0 + ( Alpha / A );
  Coeff[3] = -( 2 * CosW0 ) / A0;
  Coeff[4] = ( 1 - ( Alpha / A )) / A0;
  GainLinear = pow( 10, Gain / 20 ) / A0;
  Coeff[0] = ( 1 + ( Alpha * A)) * GainLinear;
  Coeff[1] = -( 2 * CosW0 ) * GainLinear;
  Coeff[2] = ( 1 - ( Alpha * A)) * GainLinear;
  Coeff[3] = -Coeff[3];
  Coeff[4] = -Coeff[4];
  Filter_Write( Address, Coeff);
  DSP_Busy_FLAG = LOW;
}
//-----< General HighPass 2 Order Filter >-------------------------------------
void General_HighPass_2Order( unsigned int Address, double Frequency, double Q, double Gain )
{
    double WO,SinW0,CosW0,Alpha,A0,GainLinear;
  	double Coeff[] = { 0, 0, 0, 0, 0 };            // Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=B2 , Coeff[3]=A1 , Coeff[4]=A2
    DSP_Busy_FLAG = HIGH;
    WO = ( 6.2831853071795862 * Frequency ) / 48000;
    SinW0 = sin( WO );
    CosW0 = cos( WO );
    Alpha = SinW0 / ( 2 * Q );
    A0 = 1.0 + Alpha;
	GainLinear = pow( 10, Gain / 20 );
    Coeff[3] = -( 2 * CosW0 ) / A0;
    Coeff[4] = ( 1 - Alpha ) / A0;
    Coeff[1] = ( -( 1 + CosW0 ) / A0 ) * GainLinear;
    Coeff[0] = -Coeff[1]/2;
    Coeff[2] = Coeff[0];
	Coeff[3] = -Coeff[3];
  	Coeff[4] = -Coeff[4];
  	Filter_Write( Address, Coeff );
    DSP_Busy_FLAG = LOW;
}
//-----< General LowPass 2 Order Filter >-------------------------------------
void General_LowPass_2Order( unsigned int Address, double Frequency, double Q, double Gain )
{
	double WO,SinW0,CosW0,Alpha,A0,GainLinear;
  	double Coeff[] = { 0, 0, 0, 0, 0 };            // Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=B2 , Coeff[3]=A1 , Coeff[4]=A2
    DSP_Busy_FLAG = HIGH;
    WO = ( 6.2831853071795862 * Frequency ) / 48000;
    SinW0= sin( WO );
    CosW0= cos( WO );
    Alpha = SinW0 / ( 2 * Q );
    A0 = 1.0 + Alpha;
	GainLinear = pow( 10, Gain / 20 );
    Coeff[3]= -( 2 * CosW0 ) / A0;
    Coeff[4]= ( 1 - Alpha ) / A0;
    Coeff[1]= (( 1 - CosW0 ) / A0 ) * GainLinear;
    Coeff[0]= Coeff[1] / 2;
    Coeff[2]= Coeff[0];
	Coeff[3] = -Coeff[3];
  	Coeff[4] = -Coeff[4];
  	Filter_Write( Address, Coeff);
    DSP_Busy_FLAG = LOW;
}
//----< Limiter control >-----------------------------------------------------
void Limiter( unsigned int Address, double RMS_tc_ms, double Decay, double Threshold )		//Threshold min= -24db, max= 24db , acddress= Threshold address
{
 static double Index, RMS_tc, Buffer, Decay_Buffer, Decay_Complement, Decay_Complement_cnt=0;
  DSP_Busy_FLAG = HIGH;
  RMS_tc = 0.00000524520874023438 * RMS_tc_ms;
  Buffer = pow( 10, ( Threshold / 20 ));
  if( Decay == 23 ) Decay_Complement = 0;
  else
  {
    Decay_Buffer = 0.03125;
    Decay_Complement_cnt = 0.0000038147;
    for( Index = 5; Index < Decay; Index++ )
    {
      Decay_Buffer = Decay_Buffer / 2;
      Decay_Complement_cnt = Decay_Complement_cnt * 2;
    }
    Decay_Complement = 0.999996185302734 - Decay_Complement_cnt;
  }
  SafeloadSingleParamWrite( Address, Buffer, 0, 1 );
  SafeloadSingleParamWrite( Address + 1, RMS_tc, 0, 1 );
  SafeloadSingleParamWrite( Address + 2, Decay_Buffer, 0, 1 );
  SafeloadSingleParamWrite( Address + 3, Decay_Complement, 0, 1 );
  DSP_Busy_FLAG = LOW;
}
//----< HighPass filter 1 order >-----------------------------------------------------
/*
void HighPass_Filter_1Order( unsigned int Address, double Frequency, double Gain )
{
  double GainLinear, WO;
  double Coeff[] = { 0, 0, 0 };							//Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=A1
  WO = ( 6.2831853071795864 * Frequency ) / 48000;
  GainLinear = pow( 10, Gain / 20 );
  Coeff[2] = pow( 2.7, -WO );
  Coeff[0] = GainLinear * Coeff[2];
  Coeff[1] = -Coeff[2] * GainLinear;
  Filter_Write_1Order( Address, Coeff );
}*/

void High_shelving( unsigned int Address, double Boost, double Frequency, double Q, double Gain )
{
  double WO,SinW0,CosW0,Alpha,A,A0,GainLinear;
  double Coeff[] = { 0, 0, 0, 0, 0 };            // Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=B2 , Coeff[3]=A1 , Coeff[4]=A2
  DSP_Busy_FLAG = HIGH;
  A = pow( 10, Boost / 40 );
  WO =( 6.2831853071795862 * Frequency ) / 48000;
  SinW0 = sin( WO );
  CosW0 = cos( WO );
  //Alpha = (SinW0 /2 )*sqrt((A+1/A)*(1/S-1)+2);
  Alpha = SinW0 / ( 2 * Q );
  A0 = (A+1) - (A-1)*CosW0 + 2*sqrt(A)*Alpha;

  Coeff[3] = (2*( (A-1) - (A+1)*CosW0))/A0;
  Coeff[4] = ((A+1) - (A-1)*CosW0- 2*sqrt(A)*Alpha)/A0;
  GainLinear = pow( 10, Gain / 20 ) / A0;
  Coeff[0] = A*( (A+1) + (A-1)*CosW0 + 2*sqrt(A)*Alpha ) * GainLinear;
  Coeff[1] = -2*A*( (A-1) + (A+1)*CosW0 ) * GainLinear;
  Coeff[2] = A*( (A+1) + (A-1)*CosW0 - 2*sqrt(A)*Alpha ) * GainLinear;
  Coeff[3] = -Coeff[3];
  Coeff[4] = -Coeff[4];
  Filter_Write( Address, Coeff);
  DSP_Busy_FLAG = LOW;
}


void Low_shelving( unsigned int Address, double Boost, double Frequency, double Q, double Gain )
{
  double WO,SinW0,CosW0,Alpha,A,A0,GainLinear;
  double Coeff[] = { 0, 0, 0, 0, 0 };            // Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=B2 , Coeff[3]=A1 , Coeff[4]=A2
  DSP_Busy_FLAG = HIGH;
  A = pow( 10, Boost / 40 );
  WO =( 6.2831853071795862 * Frequency ) / 48000;
  SinW0 = sin( WO );
  CosW0 = cos( WO );
  //Alpha = (SinW0 /2 )*sqrt((A+1/A)*(1/S-1)+2);
  Alpha = SinW0 / ( 2 * Q );
  A0 = (A+1)+ (A-1)*CosW0 + 2*sqrt(A)*Alpha;

  Coeff[3] =  (-2*( (A-1) + (A+1)*CosW0 )) / A0;
  Coeff[4] = ( (A+1) + (A-1)*CosW0 - 2*sqrt(A)*Alpha) / A0;
  GainLinear = pow( 10, Gain / 20 ) / A0;
  Coeff[0] = A*( (A+1) - (A-1)*CosW0 + 2*sqrt(A)*Alpha ) * GainLinear;
  Coeff[1] =2*A*( (A-1) - (A+1)*CosW0 ) * GainLinear;
  Coeff[2] = A*( (A+1) - (A-1)*CosW0 - 2*sqrt(A)*Alpha ) * GainLinear;
  Coeff[3] = -Coeff[3];
  Coeff[4] = -Coeff[4];
  Filter_Write( Address, Coeff);
  DSP_Busy_FLAG = LOW;
}

//----< HighPass filter 1 order >-----------------------------------------------------
void HighPass_Filter_1Order( unsigned int Address, double Frequency, double Gain )
{
  double GainLinear, WO;
  double Coeff[] = { 0, 0, 0 };							//Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=A1
  DSP_Busy_FLAG = HIGH;
  WO = ( 6.2831853071795864 * Frequency ) / 48000;
  GainLinear = pow( 10, Gain / 20 );
  Coeff[2] = pow( 2.7, -WO );
  Coeff[0] = GainLinear * Coeff[2] * ( 1 + ( WO / 2 ));
  Coeff[1] = -Coeff[2] * GainLinear * ( 1 + ( WO / 2 ));
  Filter_Write_1Order( Address, Coeff );
  DSP_Busy_FLAG = LOW;
/*
0.868042707443237	0X00 ,	0X6F ,	0X1C ,	0X06 ,
-0.868042707443237	0X0F ,	0X90 ,	0XE3 ,	0XFA ,
0.868042707443237	0X00 ,	0X6F ,	0X1C ,	0X06 ,
*/
}

//----< LowPass filter 1 order >-----------------------------------------------------
void LowPass_filter_1Order( unsigned int Address, double Frequency, double Gain )
{
  double GainLinear, WO;
  double Coeff[] = { 0, 0, 0 };							//Coeff[0]=B0 , Coeff[1]=B1 , Coeff[2]=A1
  DSP_Busy_FLAG = HIGH;
  WO = ( 6.2831853071795862 * Frequency ) / 48000;
  GainLinear = pow( 10, Gain / 20 );
  Coeff[2] = pow( 2.7, -WO );
  Coeff[0] = GainLinear * ( 1.0 - Coeff[2] );
  Coeff[1] = 0;
  Filter_Write_1Order( Address, Coeff );
  DSP_Busy_FLAG = LOW;
/*
0.131957292556763	0X00 ,	0X10 ,	0XE3 ,	0XFA ,
0					0X00 ,	0X00 ,	0X00 ,	0X00 ,
0.868042707443237	0X00 ,	0X6F ,	0X1C ,	0X06 ,
*/
}
//----< 2 Order Filter  >-----------------------------------------------------
void Filter_Write( unsigned int Address, double *Data )
{
  SafeloadSingleParamWrite( Address, Data[0], 0, 0 );
  SafeloadSingleParamWrite( Address + 1, Data[1], 1, 0 );
  SafeloadSingleParamWrite( Address + 2, Data[2], 2, 0 );
  SafeloadSingleParamWrite( Address + 3, Data[3], 3, 0 );
  SafeloadSingleParamWrite( Address + 4, Data[4], 4, 1 );
}
//----< 1 Order Filter  >-----------------------------------------------------
void Filter_Write_1Order( unsigned int Address, double *Data )
{
  SafeloadSingleParamWrite( Address, Data[0], 0, 0 );
  SafeloadSingleParamWrite( Address + 1, Data[1], 1, 0 );
  SafeloadSingleParamWrite( Address + 2, Data[2], 2, 1 );
}
//-----< Phase >----------------------------------------------------------------------
void PHASE_Delay( unsigned int Address, long Data )
{
  unsigned char Phase_Delay[5];
  DSP_Busy_FLAG = HIGH;
  Data = Data + 1;
  Phase_Delay[4] = (char)Data;            // Get (LSBs) of parameter value
  Phase_Delay[3] = (char)( Data >> 8 );   // Get of parameter value
  Phase_Delay[2] = (char)( Data >> 16 );  // Get of parameter value
  Phase_Delay[1] = (char)( Data >> 24 );  // Get (MSBs) of parameter value
  Phase_Delay[0] = 0x00;
  	Mute(MUTE,1);

  DSP_Write( SAFELOAD_DATA_0, 0, Phase_Delay, 0, 0, 5, 3 );    // DATA
  DSP_Write( SAFELOAD_ADDRESS_0, Address, 0, 0, 0, 0, 4 );     //  ADDRESS
	delayms(10)
  DSP_Write( DSP_Core, 0, 0x00, 0x00, 0x3C, 0, 2 );            // DSP 
	Mute(MUTE,0);
  DSP_Busy_FLAG = LOW;
}

void Mute( unsigned int Address, unsigned char Status )
{
  if ( Status )
  {
    SafeloadSingleParamWrite( Address, 0, 0, 0 );
    SafeloadSingleParamWrite( Address+ 1, 0.0009765625, 1, 1 );
  }
  else
  {
    SafeloadSingleParamWrite( Address, 1, 0, 0 );
    SafeloadSingleParamWrite( Address + 1, 0.0009765625, 1, 1 );
  }
}

void Flash_XOVER_HPF( unsigned int type, double Freq, unsigned int XOVER_HPF_SW, unsigned int Cross_Hipass_12dB , unsigned int Cross_Hipass_24dB)
{

 switch (type)
{
 case 0: //disable
    SafeloadSingleParamWrite2( XOVER_HPF_SW, 0, 0, 1 );

 break;

 case 1: //butterworth -12dB
      General_HighPass_2Order( Cross_Hipass_12dB,  Freq, 0.70710681,0 );
      SafeloadSingleParamWrite2( XOVER_HPF_SW, 1, 0, 1 );

 break;

 case 2: //butterworth -24dB

      General_HighPass_2Order( Cross_Hipass_12dB,  Freq, 0.5412, 0);
      General_HighPass_2Order( Cross_Hipass_24dB,  Freq, 1.3065, 0);
      SafeloadSingleParamWrite2( XOVER_HPF_SW, 2, 0, 1 );

 break;

 case 3: //bessel -12dB
      General_HighPass_2Order( Cross_Hipass_12dB,  Freq, 0.57735, 0 );
      SafeloadSingleParamWrite2( XOVER_HPF_SW, 1, 0, 1 );

 break;

 case 4: //bessel -24dB
      General_HighPass_2Order( Cross_Hipass_12dB, Freq, 0.57735, 0 );
      General_HighPass_2Order( Cross_Hipass_24dB, Freq, 0.57735, 0);
      SafeloadSingleParamWrite2( XOVER_HPF_SW, 2, 0, 1);

 break;
 case 5: //L-R -12dB
      General_HighPass_2Order( Cross_Hipass_12dB,  Freq, 0.5, 0);
      SafeloadSingleParamWrite2( XOVER_HPF_SW, 1, 0, 1 );

 break;

 case 6: //L-R -24dB
      General_HighPass_2Order( Cross_Hipass_12dB,  Freq, 0.70710681, 0);
      General_HighPass_2Order( Cross_Hipass_24dB,  Freq, 0.70710681, 0);
      SafeloadSingleParamWrite2( XOVER_HPF_SW, 2, 0, 1);

 break;
}
}


void Flash_XOVER_LPF( unsigned int type, double Freq, unsigned int XOVER_LPF_SW, unsigned int Cross_Lowpass_12dB , unsigned int Cross_Lowpass_24dB)
{

 switch (type)
{
 case 0: //disable
    SafeloadSingleParamWrite2( XOVER_LPF_SW, 0, 0, 1 );

 break;

 case 1: //butterworth -12dB
      General_LowPass_2Order( Cross_Lowpass_12dB,  Freq, 0.70710681,0 );
      SafeloadSingleParamWrite2( XOVER_LPF_SW, 1, 0, 1 );

 break;

 case 2: //butterworth -24dB

      General_LowPass_2Order( Cross_Lowpass_12dB,  Freq, 0.5412, 0);
      General_LowPass_2Order( Cross_Lowpass_24dB,  Freq, 1.3065, 0);
      SafeloadSingleParamWrite2( XOVER_LPF_SW, 2, 0, 1 );

 break;

 case 3: //bessel -12dB
      General_LowPass_2Order( Cross_Lowpass_12dB,  Freq, 0.57735, 0 );
      SafeloadSingleParamWrite2( XOVER_LPF_SW, 1, 0, 1 );

 break;

 case 4: //bessel -24dB
      General_LowPass_2Order( Cross_Lowpass_12dB, Freq, 0.57735, 0 );
      General_LowPass_2Order( Cross_Lowpass_24dB, Freq, 0.57735, 0);
      SafeloadSingleParamWrite2( XOVER_LPF_SW, 2, 0, 1);

 break;
 case 5: //L-R -12dB
      General_LowPass_2Order( Cross_Lowpass_12dB,  Freq, 0.5, 0);
      SafeloadSingleParamWrite2( XOVER_LPF_SW, 1, 0, 1 );

 break;

 case 6: //L-R -24dB
      General_LowPass_2Order( Cross_Lowpass_12dB,  Freq, 0.70710681, 0);
      General_LowPass_2Order( Cross_Lowpass_24dB,  Freq, 0.70710681, 0);
      SafeloadSingleParamWrite2( XOVER_LPF_SW, 2, 0, 1);

 break;
}
}


void PEQ_ONOFF(unsigned int ON,unsigned int PEQ_SW_ADDR){

	if(ON){
      SafeloadSingleParamWrite( PEQ_SW_ADDR, 1, 0, 0 );
      SafeloadSingleParamWrite( PEQ_SW_ADDR+1, 0, 1, 1 );
	}else {
      SafeloadSingleParamWrite( PEQ_SW_ADDR, 0, 0, 0 );
      SafeloadSingleParamWrite( PEQ_SW_ADDR+1, 1, 1, 1 );
	}

}


void Flash_PEQ( unsigned int band ,double Freq, double Gain ,double Q,  unsigned int PEQ_ADDR )
{



      if(band==0x01)  Peaking( PEQ_ADDR,     Gain, Freq, Q, 0 );
 else if(band==0x02)  Peaking( PEQ_ADDR+5,   Gain, Freq, Q, 0 );
 else if(band==0x03)  Peaking( PEQ_ADDR+10,  Gain, Freq, Q, 0 );
 else if(band==0x04)  Peaking( PEQ_ADDR+15,  Gain, Freq, Q, 0 );
 else if(band==0x05)  Peaking( PEQ_ADDR+20,  Gain, Freq, Q, 0 );

}


void DSP_Data_Capture_Read(unsigned int address,unsigned char *level_out)
{
  	IdleI2C1( );
  	StartI2C1( );
  	IdleI2C1( );
  	MasterWriteI2C1(0x68 );
	IdleI2C1( );
  	MasterWriteI2C1(0x08);
	IdleI2C1( );
  	MasterWriteI2C1(0x1a);
	IdleI2C1( );
 	MasterWriteI2C1((address&0xFF00)>>8);
	IdleI2C1( );
  	MasterWriteI2C1(address&0x00FF);
	IdleI2C1( );
  	StopI2C1( );

	IdleI2C1( );
        StartI2C1( );                               // START 
	IdleI2C1( );
	MasterWriteI2C1(0x68);          //EEPROM I2C address / Write
	IdleI2C1( );
	MasterWriteI2C1(0x08);
	IdleI2C1( );
  	MasterWriteI2C1(0x1a);
  	IdleI2C1( );
  	RestartI2C1();
	IdleI2C1( );
	MasterWriteI2C1(0x69 );          //EEPROM I2C address / Write
	IdleI2C1( );
	level_out[0]=MasterReadI2C1();
//		Level_CH2[0]=MasterReadI2C1();
	IdleI2C1( );
	AckI2C1();
	IdleI2C1( );
	level_out[1]=MasterReadI2C1();
	IdleI2C1( );
	AckI2C1();
	IdleI2C1( );
	level_out[2]=MasterReadI2C1();
	IdleI2C1( );
	StopI2C1( );
	IdleI2C1( );
}

double Level_ReadBack_to_dB(unsigned char *lvl , unsigned int addr){
    
unsigned long lvl_sum;
double lvl_tmp;

    double lvl_dB;
        DSP_Data_Capture_Read(addr,lvl);

        lvl_sum=(unsigned long)lvl[0]*65536+(unsigned long)lvl[1]*256+(unsigned long)lvl[2];

        lvl_tmp=((double)lvl_sum/524288);
        //if(lvl[1]<=0xFF && lvl[1]>=0x80 && lvl[0]==0x00)
        //   lvl_dB=-24;
        //else
            lvl_dB=20*log10(lvl_tmp);
    
    return lvl_dB;

}

/*** DSP Variables *********************************************/
/*extern unsigned long Delay_time_CH1=0,Delay_time_CH2=0;
extern unsigned int HPF_type_CH1=0, HPF_type_CH2=0;
extern double HPF_Freq_CH1=0, HPF_Freq_CH2=0;

extern unsigned int LPF_type=0;
extern double LPF_Freq=0;

extern unsigned int PEQ_Full_Range_ON=0, PEQ_Sub_ON=0;
extern unsigned int PEQ_Full_Range_Func=0,PEQ_Sub_Func=0;;
extern double PEQ_FR_Freq_1=0,PEQ_FR_Freq_2=0,PEQ_FR_Freq_3=0,PEQ_FR_Freq_4=0,PEQ_FR_Freq_5=0,
	   PEQ_Sub_Freq_1=0,PEQ_Sub_Freq_2=0,PEQ_Sub_Freq_3=0,PEQ_Sub_Freq_4=0,PEQ_Sub_Freq_5=0;

extern double PEQ_FR_Gain_1=0,PEQ_FR_Gain_2=0,PEQ_FR_Gain_3=0,PEQ_FR_Gain_4=0,PEQ_FR_Gain_5=0,
	   PEQ_Sub_Gain_1=0,PEQ_Sub_Gain_2=0,PEQ_Sub_Gain_3=0,PEQ_Sub_Gain_4=0,PEQ_Sub_Gain_5=0;

extern double PEQ_FR_Q_1=0,PEQ_FR_Q_2=0,PEQ_FR_Q_3=0,PEQ_FR_Q_4=0,PEQ_FR_Q_5=0,
	   PEQ_Sub_Q_1=0,PEQ_Sub_Q_2=0,PEQ_Sub_Q_3=0,PEQ_Sub_Q_4=0,PEQ_Sub_Q_5=0;

extern double Limiter_FR_Threshold=0,Limiter_FR_Attack=0,Limiter_FR_Release=0,
	   Limiter_SUB_Threshold=0,Limiter_SUB_Attack=0,Limiter_SUB_Release=0;
*/
