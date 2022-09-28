#include <stddef.h>

typedef char           CHAR;

typedef unsigned char  UCHAR;
typedef unsigned short UINT_16;
typedef unsigned int   UINT_32;

typedef signed char    SCHAR;
typedef signed short   SINT_16;
typedef signed int     SINT_32;

typedef float          FLOAT_32;
typedef double         FLOAT_64;

/*
 * Two common methods for defining a boolean type - 
 * initially use the typedef enum.
 */

typedef enum { FALSE = 0 , TRUE  = 1} BOOL;

/*
#define BOOL unsigned int
#define FALSE 0
#define TRUE 1
*/

