#include "rt_logging_mmi.h"
#include "Pendulum_capi.h"
#include <math.h>
#include "Pendulum.h"
#include "Pendulum_private.h"
#include "Pendulum_dt.h"
extern void * CreateDiagnosticAsVoidPtr_wrapper ( const char * id , int nargs
, ... ) ; RTWExtModeInfo * gblRTWExtModeInfo = NULL ; void
raccelForceExtModeShutdown ( boolean_T extModeStartPktReceived ) { if ( !
extModeStartPktReceived ) { boolean_T stopRequested = false ;
rtExtModeWaitForStartPkt ( gblRTWExtModeInfo , 1 , & stopRequested ) ; }
rtExtModeShutdown ( 1 ) ; }
#include "slsv_diagnostic_codegen_c_api.h"
#include "slsa_sim_engine.h"
const int_T gblNumToFiles = 0 ; const int_T gblNumFrFiles = 0 ; const int_T
gblNumFrWksBlocks = 0 ;
#ifdef RSIM_WITH_SOLVER_MULTITASKING
boolean_T gbl_raccel_isMultitasking = 1 ;
#else
boolean_T gbl_raccel_isMultitasking = 0 ;
#endif
boolean_T gbl_raccel_tid01eq = 0 ; int_T gbl_raccel_NumST = 2 ; const char_T
* gbl_raccel_Version = "10.3 (R2021a) 14-Nov-2020" ; void
raccel_setup_MMIStateLog ( SimStruct * S ) {
#ifdef UseMMIDataLogging
rt_FillStateSigInfoFromMMI ( ssGetRTWLogInfo ( S ) , & ssGetErrorStatus ( S )
) ;
#else
UNUSED_PARAMETER ( S ) ;
#endif
} static DataMapInfo rt_dataMapInfo ; DataMapInfo * rt_dataMapInfoPtr = &
rt_dataMapInfo ; rtwCAPI_ModelMappingInfo * rt_modelMapInfoPtr = & (
rt_dataMapInfo . mmi ) ; const int_T gblNumRootInportBlks = 0 ; const int_T
gblNumModelInputs = 0 ; extern const char * gblInportFileName ; extern
rtInportTUtable * gblInportTUtables ; const int_T gblInportDataTypeIdx [ ] =
{ - 1 } ; const int_T gblInportDims [ ] = { - 1 } ; const int_T
gblInportComplex [ ] = { - 1 } ; const int_T gblInportInterpoFlag [ ] = { - 1
} ; const int_T gblInportContinuous [ ] = { - 1 } ; int_T enableFcnCallFlag [
] = { 1 , 1 } ; const char * raccelLoadInputsAndAperiodicHitTimes ( SimStruct
* S , const char * inportFileName , int * matFileFormat ) { return
rt_RAccelReadInportsMatFile ( S , inportFileName , matFileFormat ) ; }
#include "simstruc.h"
#include "fixedpoint.h"
#include "slsa_sim_engine.h"
#include "simtarget/slSimTgtSLExecSimBridge.h"
B rtB ; X rtX ; DW rtDW ; static SimStruct model_S ; SimStruct * const rtS =
& model_S ; static real_T i0jep5xwfb ( real_T x , const real_T params [ 3 ] )
; static void geida10htv ( const real_T x [ 101 ] , const real_T params [ 3 ]
, real_T y [ 101 ] ) ; static real_T i0jep5xwfb ( real_T x , const real_T
params [ 3 ] ) { real_T y ; y = 0.0 ; if ( ( params [ 0 ] != params [ 1 ] )
&& ( params [ 0 ] < x ) && ( x < params [ 1 ] ) ) { y = 1.0 / ( params [ 1 ]
- params [ 0 ] ) * ( x - params [ 0 ] ) ; } if ( ( params [ 1 ] != params [ 2
] ) && ( params [ 1 ] < x ) && ( x < params [ 2 ] ) ) { y = 1.0 / ( params [
2 ] - params [ 1 ] ) * ( params [ 2 ] - x ) ; } if ( x == params [ 1 ] ) { y
= 1.0 ; } return y ; } static void geida10htv ( const real_T x [ 101 ] ,
const real_T params [ 3 ] , real_T y [ 101 ] ) { real_T a ; real_T b ; real_T
c ; real_T x_p ; int32_T i ; a = params [ 0 ] ; b = params [ 1 ] ; c = params
[ 2 ] ; for ( i = 0 ; i < 101 ; i ++ ) { x_p = x [ i ] ; y [ i ] = 0.0 ; if (
( a != b ) && ( a < x_p ) && ( x_p < b ) ) { y [ i ] = 1.0 / ( b - a ) * (
x_p - a ) ; } if ( ( b != c ) && ( b < x_p ) && ( x_p < c ) ) { y [ i ] = 1.0
/ ( c - b ) * ( c - x_p ) ; } if ( x_p == b ) { y [ i ] = 1.0 ; } } } void
MdlInitialize ( void ) { rtX . dofzbcbfvq [ 0 ] = 0.0 ; rtX . oig2rykllt [ 0
] = 0.0 ; rtX . dofzbcbfvq [ 1 ] = 0.0 ; rtX . oig2rykllt [ 1 ] = 0.0 ; rtDW
. cgjsg2uzpw = ( rtInf ) ; rtDW . ki1hmp0vfz = ( rtInf ) ; } void MdlStart (
void ) { { bool externalInputIsInDatasetFormat = false ; void *
pISigstreamManager = rt_GetISigstreamManager ( rtS ) ;
rtwISigstreamManagerGetInputIsInDatasetFormat ( pISigstreamManager , &
externalInputIsInDatasetFormat ) ; if ( externalInputIsInDatasetFormat ) { }
} MdlInitialize ( ) ; } void MdlOutputs ( int_T tid ) { real_T outputMFCache
[ 505 ] ; real_T phdm1lhib2 [ 101 ] ; real_T tmp_e [ 101 ] ; real_T tmp_g [
101 ] ; real_T tmp_i [ 101 ] ; real_T tmp_m [ 101 ] ; real_T tmp_p [ 101 ] ;
real_T p3dw3ieyfw [ 9 ] ; real_T inputMFCache [ 6 ] ; real_T tmp [ 3 ] ;
real_T g1b3awnb1z ; real_T lastTime ; real_T mfVal ; real_T x_idx_1 ; real_T
* lastU ; int32_T i ; int32_T inputID ; static const int8_T b [ 9 ] = { 2 , 3
, 1 , 5 , 4 , 1 , 4 , 3 , 5 } ; static const int8_T d [ 18 ] = { 2 , 3 , 1 ,
2 , 3 , 1 , 2 , 3 , 1 , 2 , 2 , 2 , 1 , 1 , 1 , 3 , 3 , 3 } ; static const
real_T c [ 3 ] = { 0.0 , 2.0 , 5.0 } ; static const real_T b_p [ 3 ] = { -
5.0 , - 2.0 , 0.0 } ; rtB . axschpirno = 0.0 ; rtB . axschpirno += rtP .
TransferFcn3_C [ 0 ] * rtX . dofzbcbfvq [ 0 ] ; rtB . axschpirno += rtP .
TransferFcn3_C [ 1 ] * rtX . dofzbcbfvq [ 1 ] ; rtB . g4v5j4qgvt = rtP .
Gain_Gain * rtB . axschpirno ; rtB . ijcpe01hdq = 0.0 ; rtB . ijcpe01hdq +=
rtP . TransferFcn2_C [ 0 ] * rtX . oig2rykllt [ 0 ] ; rtB . ijcpe01hdq += rtP
. TransferFcn2_C [ 1 ] * rtX . oig2rykllt [ 1 ] ; rtB . aebifh0pvl = rtP .
Gain_Gain_euln0ijgco * rtB . ijcpe01hdq ; rtB . bgxpngmvlh = rtP .
thets_ref1_Value - rtB . g4v5j4qgvt ; if ( ( rtDW . cgjsg2uzpw >= ssGetT (
rtS ) ) && ( rtDW . ki1hmp0vfz >= ssGetT ( rtS ) ) ) { rtB . o1bcqkln1h = 0.0
; } else { lastTime = rtDW . cgjsg2uzpw ; lastU = & rtDW . a0wnci0dl4 ; if (
rtDW . cgjsg2uzpw < rtDW . ki1hmp0vfz ) { if ( rtDW . ki1hmp0vfz < ssGetT (
rtS ) ) { lastTime = rtDW . ki1hmp0vfz ; lastU = & rtDW . ntkdb0tjdq ; } }
else if ( rtDW . cgjsg2uzpw >= ssGetT ( rtS ) ) { lastTime = rtDW .
ki1hmp0vfz ; lastU = & rtDW . ntkdb0tjdq ; } rtB . o1bcqkln1h = ( rtB .
bgxpngmvlh - * lastU ) / ( ssGetT ( rtS ) - lastTime ) ; } rtB . hzxm5aw2pv [
0 ] = rtB . bgxpngmvlh ; rtB . hzxm5aw2pv [ 1 ] = rtB . o1bcqkln1h ; lastTime
= 0.0 ; tmp [ 0 ] = - 80.0 ; tmp [ 1 ] = - 40.0 ; tmp [ 2 ] = 0.0 ;
inputMFCache [ 0 ] = i0jep5xwfb ( rtB . hzxm5aw2pv [ 0 ] , tmp ) ; tmp [ 0 ]
= - 40.0 ; tmp [ 1 ] = 0.0 ; tmp [ 2 ] = 40.0 ; inputMFCache [ 1 ] =
i0jep5xwfb ( rtB . hzxm5aw2pv [ 0 ] , tmp ) ; tmp [ 0 ] = 0.0 ; tmp [ 1 ] =
40.0 ; tmp [ 2 ] = 80.0 ; inputMFCache [ 2 ] = i0jep5xwfb ( rtB . hzxm5aw2pv
[ 0 ] , tmp ) ; inputMFCache [ 3 ] = i0jep5xwfb ( rtB . hzxm5aw2pv [ 1 ] ,
b_p ) ; tmp [ 0 ] = - 2.5 ; tmp [ 1 ] = 0.0 ; tmp [ 2 ] = 2.5 ; inputMFCache
[ 4 ] = i0jep5xwfb ( rtB . hzxm5aw2pv [ 1 ] , tmp ) ; inputMFCache [ 5 ] =
i0jep5xwfb ( rtB . hzxm5aw2pv [ 1 ] , c ) ; for ( i = 0 ; i < 9 ; i ++ ) {
x_idx_1 = inputMFCache [ d [ i ] - 1 ] ; if ( 1.0 > x_idx_1 ) { g1b3awnb1z =
x_idx_1 ; } else { g1b3awnb1z = 1.0 ; } x_idx_1 = inputMFCache [ d [ i + 9 ]
+ 2 ] ; if ( ( g1b3awnb1z > x_idx_1 ) || ( muDoubleScalarIsNaN ( g1b3awnb1z )
&& ( ! muDoubleScalarIsNaN ( x_idx_1 ) ) ) ) { g1b3awnb1z = x_idx_1 ; }
lastTime += g1b3awnb1z ; p3dw3ieyfw [ i ] = g1b3awnb1z ; } rtB . pvtxzoiu5m [
0 ] = rtB . bgxpngmvlh ; rtB . pvtxzoiu5m [ 1 ] = rtB . o1bcqkln1h ; tmp [ 0
] = - 25.0 ; tmp [ 1 ] = - 15.0 ; tmp [ 2 ] = - 5.0 ; geida10htv ( rtP .
OutputSamplePoints_Value , tmp , tmp_p ) ; tmp [ 0 ] = - 10.0 ; tmp [ 1 ] =
0.0 ; tmp [ 2 ] = 10.0 ; geida10htv ( rtP . OutputSamplePoints_Value , tmp ,
tmp_e ) ; tmp [ 0 ] = 5.0 ; tmp [ 1 ] = 15.0 ; tmp [ 2 ] = 25.0 ; geida10htv
( rtP . OutputSamplePoints_Value , tmp , tmp_i ) ; tmp [ 0 ] = 0.0 ; tmp [ 1
] = 10.0 ; tmp [ 2 ] = 20.0 ; geida10htv ( rtP . OutputSamplePoints_Value ,
tmp , tmp_m ) ; tmp [ 0 ] = - 20.0 ; tmp [ 1 ] = - 10.0 ; tmp [ 2 ] = 0.0 ;
geida10htv ( rtP . OutputSamplePoints_Value , tmp , tmp_g ) ; for ( i = 0 ; i
< 101 ; i ++ ) { phdm1lhib2 [ i ] = 0.0 ; outputMFCache [ 5 * i ] = tmp_p [ i
] ; outputMFCache [ 5 * i + 1 ] = tmp_e [ i ] ; outputMFCache [ 5 * i + 2 ] =
tmp_i [ i ] ; outputMFCache [ 5 * i + 3 ] = tmp_m [ i ] ; outputMFCache [ 5 *
i + 4 ] = tmp_g [ i ] ; } for ( i = 0 ; i < 9 ; i ++ ) { x_idx_1 = p3dw3ieyfw
[ i ] ; for ( inputID = 0 ; inputID < 101 ; inputID ++ ) { g1b3awnb1z =
phdm1lhib2 [ inputID ] ; mfVal = outputMFCache [ ( 5 * inputID + b [ i ] ) -
1 ] ; if ( ( mfVal > x_idx_1 ) || ( muDoubleScalarIsNaN ( mfVal ) && ( !
muDoubleScalarIsNaN ( x_idx_1 ) ) ) ) { mfVal = x_idx_1 ; } if ( ( g1b3awnb1z
< mfVal ) || ( muDoubleScalarIsNaN ( g1b3awnb1z ) && ( ! muDoubleScalarIsNaN
( mfVal ) ) ) ) { g1b3awnb1z = mfVal ; } phdm1lhib2 [ inputID ] = g1b3awnb1z
; } } if ( lastTime == 0.0 ) { rtB . hvxvauopvm = 0.0 ; } else { lastTime =
0.0 ; mfVal = 0.0 ; for ( i = 0 ; i < 101 ; i ++ ) { mfVal += phdm1lhib2 [ i
] ; } if ( mfVal == 0.0 ) { rtB . hvxvauopvm = ( rtP .
OutputSamplePoints_Value [ 0 ] + rtP . OutputSamplePoints_Value [ 100 ] ) /
2.0 ; } else { for ( i = 0 ; i < 101 ; i ++ ) { lastTime += rtP .
OutputSamplePoints_Value [ i ] * phdm1lhib2 [ i ] ; } rtB . hvxvauopvm = 1.0
/ mfVal * lastTime ; } } UNUSED_PARAMETER ( tid ) ; } void MdlOutputsTID1 (
int_T tid ) { UNUSED_PARAMETER ( tid ) ; } void MdlUpdate ( int_T tid ) {
real_T * lastU ; if ( rtDW . cgjsg2uzpw == ( rtInf ) ) { rtDW . cgjsg2uzpw =
ssGetT ( rtS ) ; lastU = & rtDW . a0wnci0dl4 ; } else if ( rtDW . ki1hmp0vfz
== ( rtInf ) ) { rtDW . ki1hmp0vfz = ssGetT ( rtS ) ; lastU = & rtDW .
ntkdb0tjdq ; } else if ( rtDW . cgjsg2uzpw < rtDW . ki1hmp0vfz ) { rtDW .
cgjsg2uzpw = ssGetT ( rtS ) ; lastU = & rtDW . a0wnci0dl4 ; } else { rtDW .
ki1hmp0vfz = ssGetT ( rtS ) ; lastU = & rtDW . ntkdb0tjdq ; } * lastU = rtB .
bgxpngmvlh ; UNUSED_PARAMETER ( tid ) ; } void MdlUpdateTID1 ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlDerivatives ( void ) { XDot * _rtXdot ;
_rtXdot = ( ( XDot * ) ssGetdX ( rtS ) ) ; _rtXdot -> dofzbcbfvq [ 0 ] = 0.0
; _rtXdot -> dofzbcbfvq [ 0 ] += rtP . TransferFcn3_A [ 0 ] * rtX .
dofzbcbfvq [ 0 ] ; _rtXdot -> dofzbcbfvq [ 1 ] = 0.0 ; _rtXdot -> dofzbcbfvq
[ 0 ] += rtP . TransferFcn3_A [ 1 ] * rtX . dofzbcbfvq [ 1 ] ; _rtXdot ->
dofzbcbfvq [ 1 ] += rtX . dofzbcbfvq [ 0 ] ; _rtXdot -> dofzbcbfvq [ 0 ] +=
rtB . hvxvauopvm ; _rtXdot -> oig2rykllt [ 0 ] = 0.0 ; _rtXdot -> oig2rykllt
[ 0 ] += rtP . TransferFcn2_A [ 0 ] * rtX . oig2rykllt [ 0 ] ; _rtXdot ->
oig2rykllt [ 1 ] = 0.0 ; _rtXdot -> oig2rykllt [ 0 ] += rtP . TransferFcn2_A
[ 1 ] * rtX . oig2rykllt [ 1 ] ; _rtXdot -> oig2rykllt [ 1 ] += rtX .
oig2rykllt [ 0 ] ; _rtXdot -> oig2rykllt [ 0 ] += rtP . thrust1_Value ; }
void MdlProjection ( void ) { } void MdlTerminate ( void ) { } static void
mr_Pendulum_cacheDataAsMxArray ( mxArray * destArray , mwIndex i , int j ,
const void * srcData , size_t numBytes ) ; static void
mr_Pendulum_cacheDataAsMxArray ( mxArray * destArray , mwIndex i , int j ,
const void * srcData , size_t numBytes ) { mxArray * newArray =
mxCreateUninitNumericMatrix ( ( size_t ) 1 , numBytes , mxUINT8_CLASS ,
mxREAL ) ; memcpy ( ( uint8_T * ) mxGetData ( newArray ) , ( const uint8_T *
) srcData , numBytes ) ; mxSetFieldByNumber ( destArray , i , j , newArray )
; } static void mr_Pendulum_restoreDataFromMxArray ( void * destData , const
mxArray * srcArray , mwIndex i , int j , size_t numBytes ) ; static void
mr_Pendulum_restoreDataFromMxArray ( void * destData , const mxArray *
srcArray , mwIndex i , int j , size_t numBytes ) { memcpy ( ( uint8_T * )
destData , ( const uint8_T * ) mxGetData ( mxGetFieldByNumber ( srcArray , i
, j ) ) , numBytes ) ; } static void mr_Pendulum_cacheBitFieldToMxArray (
mxArray * destArray , mwIndex i , int j , uint_T bitVal ) ; static void
mr_Pendulum_cacheBitFieldToMxArray ( mxArray * destArray , mwIndex i , int j
, uint_T bitVal ) { mxSetFieldByNumber ( destArray , i , j ,
mxCreateDoubleScalar ( ( double ) bitVal ) ) ; } static uint_T
mr_Pendulum_extractBitFieldFromMxArray ( const mxArray * srcArray , mwIndex i
, int j , uint_T numBits ) ; static uint_T
mr_Pendulum_extractBitFieldFromMxArray ( const mxArray * srcArray , mwIndex i
, int j , uint_T numBits ) { const uint_T varVal = ( uint_T ) mxGetScalar (
mxGetFieldByNumber ( srcArray , i , j ) ) ; return varVal & ( ( 1u << numBits
) - 1u ) ; } static void mr_Pendulum_cacheDataToMxArrayWithOffset ( mxArray *
destArray , mwIndex i , int j , mwIndex offset , const void * srcData ,
size_t numBytes ) ; static void mr_Pendulum_cacheDataToMxArrayWithOffset (
mxArray * destArray , mwIndex i , int j , mwIndex offset , const void *
srcData , size_t numBytes ) { uint8_T * varData = ( uint8_T * ) mxGetData (
mxGetFieldByNumber ( destArray , i , j ) ) ; memcpy ( ( uint8_T * ) & varData
[ offset * numBytes ] , ( const uint8_T * ) srcData , numBytes ) ; } static
void mr_Pendulum_restoreDataFromMxArrayWithOffset ( void * destData , const
mxArray * srcArray , mwIndex i , int j , mwIndex offset , size_t numBytes ) ;
static void mr_Pendulum_restoreDataFromMxArrayWithOffset ( void * destData ,
const mxArray * srcArray , mwIndex i , int j , mwIndex offset , size_t
numBytes ) { const uint8_T * varData = ( const uint8_T * ) mxGetData (
mxGetFieldByNumber ( srcArray , i , j ) ) ; memcpy ( ( uint8_T * ) destData ,
( const uint8_T * ) & varData [ offset * numBytes ] , numBytes ) ; } static
void mr_Pendulum_cacheBitFieldToCellArrayWithOffset ( mxArray * destArray ,
mwIndex i , int j , mwIndex offset , uint_T fieldVal ) ; static void
mr_Pendulum_cacheBitFieldToCellArrayWithOffset ( mxArray * destArray ,
mwIndex i , int j , mwIndex offset , uint_T fieldVal ) { mxSetCell (
mxGetFieldByNumber ( destArray , i , j ) , offset , mxCreateDoubleScalar ( (
double ) fieldVal ) ) ; } static uint_T
mr_Pendulum_extractBitFieldFromCellArrayWithOffset ( const mxArray * srcArray
, mwIndex i , int j , mwIndex offset , uint_T numBits ) ; static uint_T
mr_Pendulum_extractBitFieldFromCellArrayWithOffset ( const mxArray * srcArray
, mwIndex i , int j , mwIndex offset , uint_T numBits ) { const uint_T
fieldVal = ( uint_T ) mxGetScalar ( mxGetCell ( mxGetFieldByNumber ( srcArray
, i , j ) , offset ) ) ; return fieldVal & ( ( 1u << numBits ) - 1u ) ; }
mxArray * mr_Pendulum_GetDWork ( ) { static const char * ssDWFieldNames [ 3 ]
= { "rtB" , "rtDW" , "NULL_PrevZCX" , } ; mxArray * ssDW =
mxCreateStructMatrix ( 1 , 1 , 3 , ssDWFieldNames ) ;
mr_Pendulum_cacheDataAsMxArray ( ssDW , 0 , 0 , ( const void * ) & ( rtB ) ,
sizeof ( rtB ) ) ; { static const char * rtdwDataFieldNames [ 4 ] = {
"rtDW.cgjsg2uzpw" , "rtDW.a0wnci0dl4" , "rtDW.ki1hmp0vfz" , "rtDW.ntkdb0tjdq"
, } ; mxArray * rtdwData = mxCreateStructMatrix ( 1 , 1 , 4 ,
rtdwDataFieldNames ) ; mr_Pendulum_cacheDataAsMxArray ( rtdwData , 0 , 0 , (
const void * ) & ( rtDW . cgjsg2uzpw ) , sizeof ( rtDW . cgjsg2uzpw ) ) ;
mr_Pendulum_cacheDataAsMxArray ( rtdwData , 0 , 1 , ( const void * ) & ( rtDW
. a0wnci0dl4 ) , sizeof ( rtDW . a0wnci0dl4 ) ) ;
mr_Pendulum_cacheDataAsMxArray ( rtdwData , 0 , 2 , ( const void * ) & ( rtDW
. ki1hmp0vfz ) , sizeof ( rtDW . ki1hmp0vfz ) ) ;
mr_Pendulum_cacheDataAsMxArray ( rtdwData , 0 , 3 , ( const void * ) & ( rtDW
. ntkdb0tjdq ) , sizeof ( rtDW . ntkdb0tjdq ) ) ; mxSetFieldByNumber ( ssDW ,
0 , 1 , rtdwData ) ; } return ssDW ; } void mr_Pendulum_SetDWork ( const
mxArray * ssDW ) { ( void ) ssDW ; mr_Pendulum_restoreDataFromMxArray ( (
void * ) & ( rtB ) , ssDW , 0 , 0 , sizeof ( rtB ) ) ; { const mxArray *
rtdwData = mxGetFieldByNumber ( ssDW , 0 , 1 ) ;
mr_Pendulum_restoreDataFromMxArray ( ( void * ) & ( rtDW . cgjsg2uzpw ) ,
rtdwData , 0 , 0 , sizeof ( rtDW . cgjsg2uzpw ) ) ;
mr_Pendulum_restoreDataFromMxArray ( ( void * ) & ( rtDW . a0wnci0dl4 ) ,
rtdwData , 0 , 1 , sizeof ( rtDW . a0wnci0dl4 ) ) ;
mr_Pendulum_restoreDataFromMxArray ( ( void * ) & ( rtDW . ki1hmp0vfz ) ,
rtdwData , 0 , 2 , sizeof ( rtDW . ki1hmp0vfz ) ) ;
mr_Pendulum_restoreDataFromMxArray ( ( void * ) & ( rtDW . ntkdb0tjdq ) ,
rtdwData , 0 , 3 , sizeof ( rtDW . ntkdb0tjdq ) ) ; } } mxArray *
mr_Pendulum_GetSimStateDisallowedBlocks ( ) { mxArray * data =
mxCreateCellMatrix ( 1 , 3 ) ; mwIndex subs [ 2 ] , offset ; { static const
char * blockType [ 1 ] = { "Scope" , } ; static const char * blockPath [ 1 ]
= { "Pendulum/Scope1" , } ; static const int reason [ 1 ] = { 0 , } ; for (
subs [ 0 ] = 0 ; subs [ 0 ] < 1 ; ++ ( subs [ 0 ] ) ) { subs [ 1 ] = 0 ;
offset = mxCalcSingleSubscript ( data , 2 , subs ) ; mxSetCell ( data ,
offset , mxCreateString ( blockType [ subs [ 0 ] ] ) ) ; subs [ 1 ] = 1 ;
offset = mxCalcSingleSubscript ( data , 2 , subs ) ; mxSetCell ( data ,
offset , mxCreateString ( blockPath [ subs [ 0 ] ] ) ) ; subs [ 1 ] = 2 ;
offset = mxCalcSingleSubscript ( data , 2 , subs ) ; mxSetCell ( data ,
offset , mxCreateDoubleScalar ( ( double ) reason [ subs [ 0 ] ] ) ) ; } }
return data ; } void MdlInitializeSizes ( void ) { ssSetNumContStates ( rtS ,
4 ) ; ssSetNumPeriodicContStates ( rtS , 0 ) ; ssSetNumY ( rtS , 0 ) ;
ssSetNumU ( rtS , 0 ) ; ssSetDirectFeedThrough ( rtS , 0 ) ;
ssSetNumSampleTimes ( rtS , 1 ) ; ssSetNumBlocks ( rtS , 19 ) ;
ssSetNumBlockIO ( rtS , 9 ) ; ssSetNumBlockParams ( rtS , 113 ) ; } void
MdlInitializeSampleTimes ( void ) { ssSetSampleTime ( rtS , 0 , 0.0 ) ;
ssSetOffsetTime ( rtS , 0 , 0.0 ) ; } void raccel_set_checksum ( ) {
ssSetChecksumVal ( rtS , 0 , 2319637232U ) ; ssSetChecksumVal ( rtS , 1 ,
3368601055U ) ; ssSetChecksumVal ( rtS , 2 , 2687453391U ) ; ssSetChecksumVal
( rtS , 3 , 224007361U ) ; }
#if defined(_MSC_VER)
#pragma optimize( "", off )
#endif
SimStruct * raccel_register_model ( ssExecutionInfo * executionInfo ) {
static struct _ssMdlInfo mdlInfo ; ( void ) memset ( ( char * ) rtS , 0 ,
sizeof ( SimStruct ) ) ; ( void ) memset ( ( char * ) & mdlInfo , 0 , sizeof
( struct _ssMdlInfo ) ) ; ssSetMdlInfoPtr ( rtS , & mdlInfo ) ;
ssSetExecutionInfo ( rtS , executionInfo ) ; { static time_T mdlPeriod [
NSAMPLE_TIMES ] ; static time_T mdlOffset [ NSAMPLE_TIMES ] ; static time_T
mdlTaskTimes [ NSAMPLE_TIMES ] ; static int_T mdlTsMap [ NSAMPLE_TIMES ] ;
static int_T mdlSampleHits [ NSAMPLE_TIMES ] ; static boolean_T
mdlTNextWasAdjustedPtr [ NSAMPLE_TIMES ] ; static int_T mdlPerTaskSampleHits
[ NSAMPLE_TIMES * NSAMPLE_TIMES ] ; static time_T mdlTimeOfNextSampleHit [
NSAMPLE_TIMES ] ; { int_T i ; for ( i = 0 ; i < NSAMPLE_TIMES ; i ++ ) {
mdlPeriod [ i ] = 0.0 ; mdlOffset [ i ] = 0.0 ; mdlTaskTimes [ i ] = 0.0 ;
mdlTsMap [ i ] = i ; mdlSampleHits [ i ] = 1 ; } } ssSetSampleTimePtr ( rtS ,
& mdlPeriod [ 0 ] ) ; ssSetOffsetTimePtr ( rtS , & mdlOffset [ 0 ] ) ;
ssSetSampleTimeTaskIDPtr ( rtS , & mdlTsMap [ 0 ] ) ; ssSetTPtr ( rtS , &
mdlTaskTimes [ 0 ] ) ; ssSetSampleHitPtr ( rtS , & mdlSampleHits [ 0 ] ) ;
ssSetTNextWasAdjustedPtr ( rtS , & mdlTNextWasAdjustedPtr [ 0 ] ) ;
ssSetPerTaskSampleHitsPtr ( rtS , & mdlPerTaskSampleHits [ 0 ] ) ;
ssSetTimeOfNextSampleHitPtr ( rtS , & mdlTimeOfNextSampleHit [ 0 ] ) ; }
ssSetSolverMode ( rtS , SOLVER_MODE_SINGLETASKING ) ; { ssSetBlockIO ( rtS ,
( ( void * ) & rtB ) ) ; ( void ) memset ( ( ( void * ) & rtB ) , 0 , sizeof
( B ) ) ; } { real_T * x = ( real_T * ) & rtX ; ssSetContStates ( rtS , x ) ;
( void ) memset ( ( void * ) x , 0 , sizeof ( X ) ) ; } { void * dwork = (
void * ) & rtDW ; ssSetRootDWork ( rtS , dwork ) ; ( void ) memset ( dwork ,
0 , sizeof ( DW ) ) ; } { static DataTypeTransInfo dtInfo ; ( void ) memset (
( char_T * ) & dtInfo , 0 , sizeof ( dtInfo ) ) ; ssSetModelMappingInfo ( rtS
, & dtInfo ) ; dtInfo . numDataTypes = 19 ; dtInfo . dataTypeSizes = &
rtDataTypeSizes [ 0 ] ; dtInfo . dataTypeNames = & rtDataTypeNames [ 0 ] ;
dtInfo . BTransTable = & rtBTransTable ; dtInfo . PTransTable = &
rtPTransTable ; dtInfo . dataTypeInfoTable = rtDataTypeInfoTable ; }
Pendulum_InitializeDataMapInfo ( ) ; ssSetIsRapidAcceleratorActive ( rtS ,
true ) ; ssSetRootSS ( rtS , rtS ) ; ssSetVersion ( rtS ,
SIMSTRUCT_VERSION_LEVEL2 ) ; ssSetModelName ( rtS , "Pendulum" ) ; ssSetPath
( rtS , "Pendulum" ) ; ssSetTStart ( rtS , 0.0 ) ; ssSetTFinal ( rtS , 80.0 )
; { static RTWLogInfo rt_DataLoggingInfo ; rt_DataLoggingInfo .
loggingInterval = ( NULL ) ; ssSetRTWLogInfo ( rtS , & rt_DataLoggingInfo ) ;
} { { static int_T rt_LoggedStateWidths [ ] = { 2 , 2 } ; static int_T
rt_LoggedStateNumDimensions [ ] = { 1 , 1 } ; static int_T
rt_LoggedStateDimensions [ ] = { 2 , 2 } ; static boolean_T
rt_LoggedStateIsVarDims [ ] = { 0 , 0 } ; static BuiltInDTypeId
rt_LoggedStateDataTypeIds [ ] = { SS_DOUBLE , SS_DOUBLE } ; static int_T
rt_LoggedStateComplexSignals [ ] = { 0 , 0 } ; static RTWPreprocessingFcnPtr
rt_LoggingStatePreprocessingFcnPtrs [ ] = { ( NULL ) , ( NULL ) } ; static
const char_T * rt_LoggedStateLabels [ ] = { "CSTATE" , "CSTATE" } ; static
const char_T * rt_LoggedStateBlockNames [ ] = { "Pendulum/Transfer Fcn3" ,
"Pendulum/Transfer Fcn2" } ; static const char_T * rt_LoggedStateNames [ ] =
{ "" , "" } ; static boolean_T rt_LoggedStateCrossMdlRef [ ] = { 0 , 0 } ;
static RTWLogDataTypeConvert rt_RTWLogDataTypeConvert [ ] = { { 0 , SS_DOUBLE
, SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } , { 0 , SS_DOUBLE , SS_DOUBLE , 0 ,
0 , 0 , 1.0 , 0 , 0.0 } } ; static int_T rt_LoggedStateIdxList [ ] = { 0 , 1
} ; static RTWLogSignalInfo rt_LoggedStateSignalInfo = { 2 ,
rt_LoggedStateWidths , rt_LoggedStateNumDimensions , rt_LoggedStateDimensions
, rt_LoggedStateIsVarDims , ( NULL ) , ( NULL ) , rt_LoggedStateDataTypeIds ,
rt_LoggedStateComplexSignals , ( NULL ) , rt_LoggingStatePreprocessingFcnPtrs
, { rt_LoggedStateLabels } , ( NULL ) , ( NULL ) , ( NULL ) , {
rt_LoggedStateBlockNames } , { rt_LoggedStateNames } ,
rt_LoggedStateCrossMdlRef , rt_RTWLogDataTypeConvert , rt_LoggedStateIdxList
} ; static void * rt_LoggedStateSignalPtrs [ 2 ] ; rtliSetLogXSignalPtrs (
ssGetRTWLogInfo ( rtS ) , ( LogSignalPtrsType ) rt_LoggedStateSignalPtrs ) ;
rtliSetLogXSignalInfo ( ssGetRTWLogInfo ( rtS ) , & rt_LoggedStateSignalInfo
) ; rt_LoggedStateSignalPtrs [ 0 ] = ( void * ) & rtX . dofzbcbfvq [ 0 ] ;
rt_LoggedStateSignalPtrs [ 1 ] = ( void * ) & rtX . oig2rykllt [ 0 ] ; }
rtliSetLogT ( ssGetRTWLogInfo ( rtS ) , "tout" ) ; rtliSetLogX (
ssGetRTWLogInfo ( rtS ) , "" ) ; rtliSetLogXFinal ( ssGetRTWLogInfo ( rtS ) ,
"" ) ; rtliSetLogVarNameModifier ( ssGetRTWLogInfo ( rtS ) , "none" ) ;
rtliSetLogFormat ( ssGetRTWLogInfo ( rtS ) , 4 ) ; rtliSetLogMaxRows (
ssGetRTWLogInfo ( rtS ) , 0 ) ; rtliSetLogDecimation ( ssGetRTWLogInfo ( rtS
) , 1 ) ; rtliSetLogY ( ssGetRTWLogInfo ( rtS ) , "" ) ;
rtliSetLogYSignalInfo ( ssGetRTWLogInfo ( rtS ) , ( NULL ) ) ;
rtliSetLogYSignalPtrs ( ssGetRTWLogInfo ( rtS ) , ( NULL ) ) ; } { static
struct _ssStatesInfo2 statesInfo2 ; ssSetStatesInfo2 ( rtS , & statesInfo2 )
; } { static ssPeriodicStatesInfo periodicStatesInfo ;
ssSetPeriodicStatesInfo ( rtS , & periodicStatesInfo ) ; } { static
ssJacobianPerturbationBounds jacobianPerturbationBounds ;
ssSetJacobianPerturbationBounds ( rtS , & jacobianPerturbationBounds ) ; } {
static ssSolverInfo slvrInfo ; static boolean_T contStatesDisabled [ 4 ] ;
static real_T absTol [ 4 ] = { 1.0E-6 , 1.0E-6 , 1.0E-6 , 1.0E-6 } ; static
uint8_T absTolControl [ 4 ] = { 0U , 0U , 0U , 0U } ; static real_T
contStateJacPerturbBoundMinVec [ 4 ] ; static real_T
contStateJacPerturbBoundMaxVec [ 4 ] ; { int i ; for ( i = 0 ; i < 4 ; ++ i )
{ contStateJacPerturbBoundMinVec [ i ] = 0 ; contStateJacPerturbBoundMaxVec [
i ] = rtGetInf ( ) ; } } ssSetSolverRelTol ( rtS , 0.001 ) ; ssSetStepSize (
rtS , 0.0 ) ; ssSetMinStepSize ( rtS , 0.0 ) ; ssSetMaxNumMinSteps ( rtS , -
1 ) ; ssSetMinStepViolatedError ( rtS , 0 ) ; ssSetMaxStepSize ( rtS , 1.6 )
; ssSetSolverMaxOrder ( rtS , - 1 ) ; ssSetSolverRefineFactor ( rtS , 1 ) ;
ssSetOutputTimes ( rtS , ( NULL ) ) ; ssSetNumOutputTimes ( rtS , 0 ) ;
ssSetOutputTimesOnly ( rtS , 0 ) ; ssSetOutputTimesIndex ( rtS , 0 ) ;
ssSetZCCacheNeedsReset ( rtS , 0 ) ; ssSetDerivCacheNeedsReset ( rtS , 0 ) ;
ssSetNumNonContDerivSigInfos ( rtS , 0 ) ; ssSetNonContDerivSigInfos ( rtS ,
( NULL ) ) ; ssSetSolverInfo ( rtS , & slvrInfo ) ; ssSetSolverName ( rtS ,
"VariableStepAuto" ) ; ssSetVariableStepSolver ( rtS , 1 ) ;
ssSetSolverConsistencyChecking ( rtS , 0 ) ; ssSetSolverAdaptiveZcDetection (
rtS , 0 ) ; ssSetSolverRobustResetMethod ( rtS , 0 ) ; ssSetAbsTolVector (
rtS , absTol ) ; ssSetAbsTolControlVector ( rtS , absTolControl ) ;
ssSetSolverAbsTol_Obsolete ( rtS , absTol ) ;
ssSetSolverAbsTolControl_Obsolete ( rtS , absTolControl ) ;
ssSetJacobianPerturbationBoundsMinVec ( rtS , contStateJacPerturbBoundMinVec
) ; ssSetJacobianPerturbationBoundsMaxVec ( rtS ,
contStateJacPerturbBoundMaxVec ) ; ssSetSolverStateProjection ( rtS , 0 ) ;
ssSetSolverMassMatrixType ( rtS , ( ssMatrixType ) 0 ) ;
ssSetSolverMassMatrixNzMax ( rtS , 0 ) ; ssSetModelOutputs ( rtS , MdlOutputs
) ; ssSetModelLogData ( rtS , rt_UpdateTXYLogVars ) ;
ssSetModelLogDataIfInInterval ( rtS , rt_UpdateTXXFYLogVars ) ;
ssSetModelUpdate ( rtS , MdlUpdate ) ; ssSetModelDerivatives ( rtS ,
MdlDerivatives ) ; ssSetSolverMaxConsecutiveMinStep ( rtS , 1 ) ;
ssSetSolverShapePreserveControl ( rtS , 2 ) ; ssSetTNextTid ( rtS , INT_MIN )
; ssSetTNext ( rtS , rtMinusInf ) ; ssSetSolverNeedsReset ( rtS ) ;
ssSetNumNonsampledZCs ( rtS , 0 ) ; ssSetContStateDisabled ( rtS ,
contStatesDisabled ) ; ssSetSolverMaxConsecutiveMinStep ( rtS , 1 ) ; }
ssSetChecksumVal ( rtS , 0 , 2319637232U ) ; ssSetChecksumVal ( rtS , 1 ,
3368601055U ) ; ssSetChecksumVal ( rtS , 2 , 2687453391U ) ; ssSetChecksumVal
( rtS , 3 , 224007361U ) ; { static const sysRanDType rtAlwaysEnabled =
SUBSYS_RAN_BC_ENABLE ; static RTWExtModeInfo rt_ExtModeInfo ; static const
sysRanDType * systemRan [ 5 ] ; gblRTWExtModeInfo = & rt_ExtModeInfo ;
ssSetRTWExtModeInfo ( rtS , & rt_ExtModeInfo ) ;
rteiSetSubSystemActiveVectorAddresses ( & rt_ExtModeInfo , systemRan ) ;
systemRan [ 0 ] = & rtAlwaysEnabled ; systemRan [ 1 ] = & rtAlwaysEnabled ;
systemRan [ 2 ] = & rtAlwaysEnabled ; systemRan [ 3 ] = & rtAlwaysEnabled ;
systemRan [ 4 ] = & rtAlwaysEnabled ; rteiSetModelMappingInfoPtr (
ssGetRTWExtModeInfo ( rtS ) , & ssGetModelMappingInfo ( rtS ) ) ;
rteiSetChecksumsPtr ( ssGetRTWExtModeInfo ( rtS ) , ssGetChecksums ( rtS ) )
; rteiSetTPtr ( ssGetRTWExtModeInfo ( rtS ) , ssGetTPtr ( rtS ) ) ; }
slsaDisallowedBlocksForSimTargetOP ( rtS ,
mr_Pendulum_GetSimStateDisallowedBlocks ) ; slsaGetWorkFcnForSimTargetOP (
rtS , mr_Pendulum_GetDWork ) ; slsaSetWorkFcnForSimTargetOP ( rtS ,
mr_Pendulum_SetDWork ) ; rt_RapidReadMatFileAndUpdateParams ( rtS ) ; if (
ssGetErrorStatus ( rtS ) ) { return rtS ; } return rtS ; }
#if defined(_MSC_VER)
#pragma optimize( "", on )
#endif
const int_T gblParameterTuningTid = 1 ; void MdlOutputsParameterSampleTime (
int_T tid ) { MdlOutputsTID1 ( tid ) ; }
