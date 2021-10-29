#include "rtw_capi.h"
#ifdef HOST_CAPI_BUILD
#include "untitled_capi_host.h"
#define sizeof(s) ((size_t)(0xFFFF))
#undef rt_offsetof
#define rt_offsetof(s,el) ((uint16_T)(0xFFFF))
#define TARGET_CONST
#define TARGET_STRING(s) (s)    
#else
#include "builtin_typeid_types.h"
#include "untitled.h"
#include "untitled_capi.h"
#include "untitled_private.h"
#ifdef LIGHT_WEIGHT_CAPI
#define TARGET_CONST                  
#define TARGET_STRING(s)               (NULL)                    
#else
#define TARGET_CONST                   const
#define TARGET_STRING(s)               (s)
#endif
#endif
static const rtwCAPI_Signals rtBlockSignals [ ] = { { 0 , 1 , TARGET_STRING (
"untitled/Fuzzy Logic  Controller" ) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 ,
0 } , { 1 , 0 , TARGET_STRING ( "untitled/Derivative" ) , TARGET_STRING ( ""
) , 0 , 0 , 0 , 0 , 0 } , { 2 , 0 , TARGET_STRING ( "untitled/Sum" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 0 } , { 3 , 0 , TARGET_STRING (
"untitled/Transfer Fcn" ) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 0 } , { 4
, 0 , TARGET_STRING ( "untitled/Transfer Fcn1" ) , TARGET_STRING ( "" ) , 0 ,
0 , 0 , 0 , 0 } , { 5 , 1 , TARGET_STRING (
"untitled/Fuzzy Logic  Controller/Defuzzify Outputs" ) , TARGET_STRING ( "" )
, 0 , 0 , 0 , 0 , 0 } , { 6 , 0 , TARGET_STRING (
"untitled/Radians to Degrees/Gain" ) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 ,
0 } , { 7 , 0 , TARGET_STRING ( "untitled/Radians to Degrees1/Gain" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 0 } , { 0 , 0 , ( NULL ) , ( NULL ) ,
0 , 0 , 0 , 0 , 0 } } ; static const rtwCAPI_BlockParameters
rtBlockParameters [ ] = { { 8 , TARGET_STRING ( "untitled/thets_ref" ) ,
TARGET_STRING ( "Value" ) , 0 , 0 , 0 } , { 9 , TARGET_STRING (
"untitled/thrust" ) , TARGET_STRING ( "Value" ) , 0 , 0 , 0 } , { 10 ,
TARGET_STRING ( "untitled/Transfer Fcn" ) , TARGET_STRING ( "A" ) , 0 , 1 , 0
} , { 11 , TARGET_STRING ( "untitled/Transfer Fcn" ) , TARGET_STRING ( "C" )
, 0 , 2 , 0 } , { 12 , TARGET_STRING ( "untitled/Transfer Fcn1" ) ,
TARGET_STRING ( "A" ) , 0 , 1 , 0 } , { 13 , TARGET_STRING (
"untitled/Transfer Fcn1" ) , TARGET_STRING ( "C" ) , 0 , 2 , 0 } , { 14 ,
TARGET_STRING ( "untitled/Fuzzy Logic  Controller/Output Sample Points" ) ,
TARGET_STRING ( "Value" ) , 0 , 3 , 0 } , { 15 , TARGET_STRING (
"untitled/Radians to Degrees/Gain" ) , TARGET_STRING ( "Gain" ) , 0 , 0 , 0 }
, { 16 , TARGET_STRING ( "untitled/Radians to Degrees1/Gain" ) ,
TARGET_STRING ( "Gain" ) , 0 , 0 , 0 } , { 0 , ( NULL ) , ( NULL ) , 0 , 0 ,
0 } } ; static int_T rt_LoggedStateIdxList [ ] = { - 1 } ; static const
rtwCAPI_Signals rtRootInputs [ ] = { { 0 , 0 , ( NULL ) , ( NULL ) , 0 , 0 ,
0 , 0 , 0 } } ; static const rtwCAPI_Signals rtRootOutputs [ ] = { { 0 , 0 ,
( NULL ) , ( NULL ) , 0 , 0 , 0 , 0 , 0 } } ; static const
rtwCAPI_ModelParameters rtModelParameters [ ] = { { 0 , ( NULL ) , 0 , 0 , 0
} } ;
#ifndef HOST_CAPI_BUILD
static void * rtDataAddrMap [ ] = { & rtB . pyxx1a5lgc , & rtB . gh32rfp5sa ,
& rtB . mzz3dbumyh , & rtB . jkb3o2dfgf , & rtB . df0o0kcdix , & rtB .
pyxx1a5lgc , & rtB . fdxn1nte3a , & rtB . of21yu54hh , & rtP .
thets_ref_Value , & rtP . thrust_Value , & rtP . TransferFcn_A [ 0 ] , & rtP
. TransferFcn_C [ 0 ] , & rtP . TransferFcn1_A [ 0 ] , & rtP . TransferFcn1_C
[ 0 ] , & rtP . OutputSamplePoints_Value [ 0 ] , & rtP . Gain_Gain_kxei4o4340
, & rtP . Gain_Gain , } ; static int32_T * rtVarDimsAddrMap [ ] = { ( NULL )
} ;
#endif
static TARGET_CONST rtwCAPI_DataTypeMap rtDataTypeMap [ ] = { { "double" ,
"real_T" , 0 , 0 , sizeof ( real_T ) , SS_DOUBLE , 0 , 0 , 0 } } ;
#ifdef HOST_CAPI_BUILD
#undef sizeof
#endif
static TARGET_CONST rtwCAPI_ElementMap rtElementMap [ ] = { { ( NULL ) , 0 ,
0 , 0 , 0 } , } ; static const rtwCAPI_DimensionMap rtDimensionMap [ ] = { {
rtwCAPI_SCALAR , 0 , 2 , 0 } , { rtwCAPI_VECTOR , 2 , 2 , 0 } , {
rtwCAPI_VECTOR , 4 , 2 , 0 } , { rtwCAPI_VECTOR , 6 , 2 , 0 } } ; static
const uint_T rtDimensionArray [ ] = { 1 , 1 , 2 , 1 , 1 , 2 , 1 , 101 } ;
static const real_T rtcapiStoredFloats [ ] = { 0.0 } ; static const
rtwCAPI_FixPtMap rtFixPtMap [ ] = { { ( NULL ) , ( NULL ) ,
rtwCAPI_FIX_RESERVED , 0 , 0 , 0 } , } ; static const rtwCAPI_SampleTimeMap
rtSampleTimeMap [ ] = { { ( const void * ) & rtcapiStoredFloats [ 0 ] , (
const void * ) & rtcapiStoredFloats [ 0 ] , 0 , 0 } } ; static
rtwCAPI_ModelMappingStaticInfo mmiStatic = { { rtBlockSignals , 8 ,
rtRootInputs , 0 , rtRootOutputs , 0 } , { rtBlockParameters , 9 ,
rtModelParameters , 0 } , { ( NULL ) , 0 } , { rtDataTypeMap , rtDimensionMap
, rtFixPtMap , rtElementMap , rtSampleTimeMap , rtDimensionArray } , "float"
, { 3171796158U , 980796643U , 3806988549U , 393953395U } , ( NULL ) , 0 , 0
, rt_LoggedStateIdxList } ; const rtwCAPI_ModelMappingStaticInfo *
untitled_GetCAPIStaticMap ( void ) { return & mmiStatic ; }
#ifndef HOST_CAPI_BUILD
void untitled_InitializeDataMapInfo ( void ) { rtwCAPI_SetVersion ( ( *
rt_dataMapInfoPtr ) . mmi , 1 ) ; rtwCAPI_SetStaticMap ( ( *
rt_dataMapInfoPtr ) . mmi , & mmiStatic ) ; rtwCAPI_SetLoggingStaticMap ( ( *
rt_dataMapInfoPtr ) . mmi , ( NULL ) ) ; rtwCAPI_SetDataAddressMap ( ( *
rt_dataMapInfoPtr ) . mmi , rtDataAddrMap ) ; rtwCAPI_SetVarDimsAddressMap (
( * rt_dataMapInfoPtr ) . mmi , rtVarDimsAddrMap ) ;
rtwCAPI_SetInstanceLoggingInfo ( ( * rt_dataMapInfoPtr ) . mmi , ( NULL ) ) ;
rtwCAPI_SetChildMMIArray ( ( * rt_dataMapInfoPtr ) . mmi , ( NULL ) ) ;
rtwCAPI_SetChildMMIArrayLen ( ( * rt_dataMapInfoPtr ) . mmi , 0 ) ; }
#else
#ifdef __cplusplus
extern "C" {
#endif
void untitled_host_InitializeDataMapInfo ( untitled_host_DataMapInfo_T *
dataMap , const char * path ) { rtwCAPI_SetVersion ( dataMap -> mmi , 1 ) ;
rtwCAPI_SetStaticMap ( dataMap -> mmi , & mmiStatic ) ;
rtwCAPI_SetDataAddressMap ( dataMap -> mmi , NULL ) ;
rtwCAPI_SetVarDimsAddressMap ( dataMap -> mmi , NULL ) ; rtwCAPI_SetPath (
dataMap -> mmi , path ) ; rtwCAPI_SetFullPath ( dataMap -> mmi , NULL ) ;
rtwCAPI_SetChildMMIArray ( dataMap -> mmi , ( NULL ) ) ;
rtwCAPI_SetChildMMIArrayLen ( dataMap -> mmi , 0 ) ; }
#ifdef __cplusplus
}
#endif
#endif
