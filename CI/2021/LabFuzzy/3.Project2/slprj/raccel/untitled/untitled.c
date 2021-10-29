#include "rt_logging_mmi.h"
#include "untitled_capi.h"
#include <math.h>
#include "untitled.h"
#include "untitled_private.h"
#include "untitled_dt.h"
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
& model_S ; static real_T ph2ixtnnou ( real_T x , const real_T params [ 3 ] )
; static void d5etfkgrm4 ( const real_T x [ 101 ] , const real_T params [ 3 ]
, real_T y [ 101 ] ) ; static real_T ph2ixtnnou ( real_T x , const real_T
params [ 3 ] ) { real_T y ; y = 0.0 ; if ( ( params [ 0 ] != params [ 1 ] )
&& ( params [ 0 ] < x ) && ( x < params [ 1 ] ) ) { y = 1.0 / ( params [ 1 ]
- params [ 0 ] ) * ( x - params [ 0 ] ) ; } if ( ( params [ 1 ] != params [ 2
] ) && ( params [ 1 ] < x ) && ( x < params [ 2 ] ) ) { y = 1.0 / ( params [
2 ] - params [ 1 ] ) * ( params [ 2 ] - x ) ; } if ( x == params [ 1 ] ) { y
= 1.0 ; } return y ; } static void d5etfkgrm4 ( const real_T x [ 101 ] ,
const real_T params [ 3 ] , real_T y [ 101 ] ) { real_T a ; real_T b ; real_T
c ; real_T x_p ; int32_T i ; a = params [ 0 ] ; b = params [ 1 ] ; c = params
[ 2 ] ; for ( i = 0 ; i < 101 ; i ++ ) { x_p = x [ i ] ; y [ i ] = 0.0 ; if (
( a != b ) && ( a < x_p ) && ( x_p < b ) ) { y [ i ] = 1.0 / ( b - a ) * (
x_p - a ) ; } if ( ( b != c ) && ( b < x_p ) && ( x_p < c ) ) { y [ i ] = 1.0
/ ( c - b ) * ( c - x_p ) ; } if ( x_p == b ) { y [ i ] = 1.0 ; } } } void
MdlInitialize ( void ) { rtX . at001at4im [ 0 ] = 0.0 ; rtX . nd323p10eu [ 0
] = 0.0 ; rtX . at001at4im [ 1 ] = 0.0 ; rtX . nd323p10eu [ 1 ] = 0.0 ; rtDW
. cn4fzdblmf = ( rtInf ) ; rtDW . ig2kcsvula = ( rtInf ) ; } void MdlStart (
void ) { { bool externalInputIsInDatasetFormat = false ; void *
pISigstreamManager = rt_GetISigstreamManager ( rtS ) ;
rtwISigstreamManagerGetInputIsInDatasetFormat ( pISigstreamManager , &
externalInputIsInDatasetFormat ) ; if ( externalInputIsInDatasetFormat ) { }
} MdlInitialize ( ) ; } void MdlOutputs ( int_T tid ) { real_T outputMFCache
[ 303 ] ; real_T ehk2phwpce [ 101 ] ; real_T tmp_e [ 101 ] ; real_T tmp_i [
101 ] ; real_T tmp_p [ 101 ] ; real_T jim1whkmvg [ 9 ] ; real_T inputMFCache
[ 6 ] ; real_T tmp [ 3 ] ; real_T lastTime ; real_T mfVal ; real_T n1irdaw4y5
; real_T x_idx_1 ; real_T * lastU ; int32_T i ; int32_T inputID ; static
const int8_T d [ 9 ] = { 3 , 2 , 1 , 1 , 3 , 2 , 1 , 2 , 3 } ; static const
real_T c [ 3 ] = { 0.0006152 , 12.5 , 25.0 } ; static const int8_T d_p [ 18 ]
= { 1 , 1 , 1 , 2 , 2 , 2 , 3 , 3 , 3 , 3 , 2 , 1 , 1 , 3 , 2 , 3 , 2 , 1 } ;
static const real_T b [ 3 ] = { - 25.0 , - 12.5 , - 0.0006152 } ; static
const real_T c_p [ 3 ] = { 0.0 , 2.0 , 5.0 } ; static const real_T b_p [ 3 ]
= { - 5.0 , - 2.0 , 0.0 } ; rtB . df0o0kcdix = 0.0 ; rtB . df0o0kcdix += rtP
. TransferFcn1_C [ 0 ] * rtX . at001at4im [ 0 ] ; rtB . df0o0kcdix += rtP .
TransferFcn1_C [ 1 ] * rtX . at001at4im [ 1 ] ; rtB . of21yu54hh = rtP .
Gain_Gain * rtB . df0o0kcdix ; rtB . jkb3o2dfgf = 0.0 ; rtB . jkb3o2dfgf +=
rtP . TransferFcn_C [ 0 ] * rtX . nd323p10eu [ 0 ] ; rtB . jkb3o2dfgf += rtP
. TransferFcn_C [ 1 ] * rtX . nd323p10eu [ 1 ] ; rtB . fdxn1nte3a = rtP .
Gain_Gain_kxei4o4340 * rtB . jkb3o2dfgf ; rtB . mzz3dbumyh = rtP .
thets_ref_Value - rtB . of21yu54hh ; if ( ( rtDW . cn4fzdblmf >= ssGetT ( rtS
) ) && ( rtDW . ig2kcsvula >= ssGetT ( rtS ) ) ) { rtB . gh32rfp5sa = 0.0 ; }
else { lastTime = rtDW . cn4fzdblmf ; lastU = & rtDW . jehkify5ki ; if ( rtDW
. cn4fzdblmf < rtDW . ig2kcsvula ) { if ( rtDW . ig2kcsvula < ssGetT ( rtS )
) { lastTime = rtDW . ig2kcsvula ; lastU = & rtDW . jkgiwbdcht ; } } else if
( rtDW . cn4fzdblmf >= ssGetT ( rtS ) ) { lastTime = rtDW . ig2kcsvula ;
lastU = & rtDW . jkgiwbdcht ; } rtB . gh32rfp5sa = ( rtB . mzz3dbumyh - *
lastU ) / ( ssGetT ( rtS ) - lastTime ) ; } rtB . kafhhzneq4 [ 0 ] = rtB .
mzz3dbumyh ; rtB . kafhhzneq4 [ 1 ] = rtB . gh32rfp5sa ; lastTime = 0.0 ; tmp
[ 0 ] = - 80.0 ; tmp [ 1 ] = - 40.0 ; tmp [ 2 ] = 0.0 ; inputMFCache [ 0 ] =
ph2ixtnnou ( rtB . kafhhzneq4 [ 0 ] , tmp ) ; tmp [ 0 ] = - 40.0 ; tmp [ 1 ]
= 0.0 ; tmp [ 2 ] = 40.0 ; inputMFCache [ 1 ] = ph2ixtnnou ( rtB . kafhhzneq4
[ 0 ] , tmp ) ; tmp [ 0 ] = 0.0 ; tmp [ 1 ] = 40.0 ; tmp [ 2 ] = 80.0 ;
inputMFCache [ 2 ] = ph2ixtnnou ( rtB . kafhhzneq4 [ 0 ] , tmp ) ;
inputMFCache [ 3 ] = ph2ixtnnou ( rtB . kafhhzneq4 [ 1 ] , b_p ) ; tmp [ 0 ]
= - 2.5 ; tmp [ 1 ] = 0.0 ; tmp [ 2 ] = 2.5 ; inputMFCache [ 4 ] = ph2ixtnnou
( rtB . kafhhzneq4 [ 1 ] , tmp ) ; inputMFCache [ 5 ] = ph2ixtnnou ( rtB .
kafhhzneq4 [ 1 ] , c_p ) ; for ( i = 0 ; i < 9 ; i ++ ) { x_idx_1 =
inputMFCache [ d_p [ i ] - 1 ] ; if ( 1.0 > x_idx_1 ) { n1irdaw4y5 = x_idx_1
; } else { n1irdaw4y5 = 1.0 ; } x_idx_1 = inputMFCache [ d_p [ i + 9 ] + 2 ]
; if ( ( n1irdaw4y5 > x_idx_1 ) || ( muDoubleScalarIsNaN ( n1irdaw4y5 ) && (
! muDoubleScalarIsNaN ( x_idx_1 ) ) ) ) { n1irdaw4y5 = x_idx_1 ; } lastTime
+= n1irdaw4y5 ; jim1whkmvg [ i ] = n1irdaw4y5 ; } rtB . fge3vtkizy [ 0 ] =
rtB . mzz3dbumyh ; rtB . fge3vtkizy [ 1 ] = rtB . gh32rfp5sa ; d5etfkgrm4 (
rtP . OutputSamplePoints_Value , b , tmp_p ) ; tmp [ 0 ] = - 12.5 ; tmp [ 1 ]
= 0.0 ; tmp [ 2 ] = 12.5 ; d5etfkgrm4 ( rtP . OutputSamplePoints_Value , tmp
, tmp_e ) ; d5etfkgrm4 ( rtP . OutputSamplePoints_Value , c , tmp_i ) ; for (
i = 0 ; i < 101 ; i ++ ) { ehk2phwpce [ i ] = 0.0 ; outputMFCache [ 3 * i ] =
tmp_p [ i ] ; outputMFCache [ 3 * i + 1 ] = tmp_e [ i ] ; outputMFCache [ 3 *
i + 2 ] = tmp_i [ i ] ; } for ( i = 0 ; i < 9 ; i ++ ) { x_idx_1 = jim1whkmvg
[ i ] ; for ( inputID = 0 ; inputID < 101 ; inputID ++ ) { n1irdaw4y5 =
ehk2phwpce [ inputID ] ; mfVal = outputMFCache [ ( 3 * inputID + d [ i ] ) -
1 ] ; if ( ( mfVal > x_idx_1 ) || ( muDoubleScalarIsNaN ( mfVal ) && ( !
muDoubleScalarIsNaN ( x_idx_1 ) ) ) ) { mfVal = x_idx_1 ; } if ( ( n1irdaw4y5
< mfVal ) || ( muDoubleScalarIsNaN ( n1irdaw4y5 ) && ( ! muDoubleScalarIsNaN
( mfVal ) ) ) ) { n1irdaw4y5 = mfVal ; } ehk2phwpce [ inputID ] = n1irdaw4y5
; } } if ( lastTime == 0.0 ) { rtB . pyxx1a5lgc = 0.0 ; } else { lastTime =
0.0 ; mfVal = 0.0 ; for ( i = 0 ; i < 101 ; i ++ ) { mfVal += ehk2phwpce [ i
] ; } if ( mfVal == 0.0 ) { rtB . pyxx1a5lgc = ( rtP .
OutputSamplePoints_Value [ 0 ] + rtP . OutputSamplePoints_Value [ 100 ] ) /
2.0 ; } else { for ( i = 0 ; i < 101 ; i ++ ) { lastTime += rtP .
OutputSamplePoints_Value [ i ] * ehk2phwpce [ i ] ; } rtB . pyxx1a5lgc = 1.0
/ mfVal * lastTime ; } } UNUSED_PARAMETER ( tid ) ; } void MdlOutputsTID1 (
int_T tid ) { UNUSED_PARAMETER ( tid ) ; } void MdlUpdate ( int_T tid ) {
real_T * lastU ; if ( rtDW . cn4fzdblmf == ( rtInf ) ) { rtDW . cn4fzdblmf =
ssGetT ( rtS ) ; lastU = & rtDW . jehkify5ki ; } else if ( rtDW . ig2kcsvula
== ( rtInf ) ) { rtDW . ig2kcsvula = ssGetT ( rtS ) ; lastU = & rtDW .
jkgiwbdcht ; } else if ( rtDW . cn4fzdblmf < rtDW . ig2kcsvula ) { rtDW .
cn4fzdblmf = ssGetT ( rtS ) ; lastU = & rtDW . jehkify5ki ; } else { rtDW .
ig2kcsvula = ssGetT ( rtS ) ; lastU = & rtDW . jkgiwbdcht ; } * lastU = rtB .
mzz3dbumyh ; UNUSED_PARAMETER ( tid ) ; } void MdlUpdateTID1 ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlDerivatives ( void ) { XDot * _rtXdot ;
_rtXdot = ( ( XDot * ) ssGetdX ( rtS ) ) ; _rtXdot -> at001at4im [ 0 ] = 0.0
; _rtXdot -> at001at4im [ 0 ] += rtP . TransferFcn1_A [ 0 ] * rtX .
at001at4im [ 0 ] ; _rtXdot -> at001at4im [ 1 ] = 0.0 ; _rtXdot -> at001at4im
[ 0 ] += rtP . TransferFcn1_A [ 1 ] * rtX . at001at4im [ 1 ] ; _rtXdot ->
at001at4im [ 1 ] += rtX . at001at4im [ 0 ] ; _rtXdot -> at001at4im [ 0 ] +=
rtB . pyxx1a5lgc ; _rtXdot -> nd323p10eu [ 0 ] = 0.0 ; _rtXdot -> nd323p10eu
[ 0 ] += rtP . TransferFcn_A [ 0 ] * rtX . nd323p10eu [ 0 ] ; _rtXdot ->
nd323p10eu [ 1 ] = 0.0 ; _rtXdot -> nd323p10eu [ 0 ] += rtP . TransferFcn_A [
1 ] * rtX . nd323p10eu [ 1 ] ; _rtXdot -> nd323p10eu [ 1 ] += rtX .
nd323p10eu [ 0 ] ; _rtXdot -> nd323p10eu [ 0 ] += rtP . thrust_Value ; } void
MdlProjection ( void ) { } void MdlTerminate ( void ) { } static void
mr_untitled_cacheDataAsMxArray ( mxArray * destArray , mwIndex i , int j ,
const void * srcData , size_t numBytes ) ; static void
mr_untitled_cacheDataAsMxArray ( mxArray * destArray , mwIndex i , int j ,
const void * srcData , size_t numBytes ) { mxArray * newArray =
mxCreateUninitNumericMatrix ( ( size_t ) 1 , numBytes , mxUINT8_CLASS ,
mxREAL ) ; memcpy ( ( uint8_T * ) mxGetData ( newArray ) , ( const uint8_T *
) srcData , numBytes ) ; mxSetFieldByNumber ( destArray , i , j , newArray )
; } static void mr_untitled_restoreDataFromMxArray ( void * destData , const
mxArray * srcArray , mwIndex i , int j , size_t numBytes ) ; static void
mr_untitled_restoreDataFromMxArray ( void * destData , const mxArray *
srcArray , mwIndex i , int j , size_t numBytes ) { memcpy ( ( uint8_T * )
destData , ( const uint8_T * ) mxGetData ( mxGetFieldByNumber ( srcArray , i
, j ) ) , numBytes ) ; } static void mr_untitled_cacheBitFieldToMxArray (
mxArray * destArray , mwIndex i , int j , uint_T bitVal ) ; static void
mr_untitled_cacheBitFieldToMxArray ( mxArray * destArray , mwIndex i , int j
, uint_T bitVal ) { mxSetFieldByNumber ( destArray , i , j ,
mxCreateDoubleScalar ( ( double ) bitVal ) ) ; } static uint_T
mr_untitled_extractBitFieldFromMxArray ( const mxArray * srcArray , mwIndex i
, int j , uint_T numBits ) ; static uint_T
mr_untitled_extractBitFieldFromMxArray ( const mxArray * srcArray , mwIndex i
, int j , uint_T numBits ) { const uint_T varVal = ( uint_T ) mxGetScalar (
mxGetFieldByNumber ( srcArray , i , j ) ) ; return varVal & ( ( 1u << numBits
) - 1u ) ; } static void mr_untitled_cacheDataToMxArrayWithOffset ( mxArray *
destArray , mwIndex i , int j , mwIndex offset , const void * srcData ,
size_t numBytes ) ; static void mr_untitled_cacheDataToMxArrayWithOffset (
mxArray * destArray , mwIndex i , int j , mwIndex offset , const void *
srcData , size_t numBytes ) { uint8_T * varData = ( uint8_T * ) mxGetData (
mxGetFieldByNumber ( destArray , i , j ) ) ; memcpy ( ( uint8_T * ) & varData
[ offset * numBytes ] , ( const uint8_T * ) srcData , numBytes ) ; } static
void mr_untitled_restoreDataFromMxArrayWithOffset ( void * destData , const
mxArray * srcArray , mwIndex i , int j , mwIndex offset , size_t numBytes ) ;
static void mr_untitled_restoreDataFromMxArrayWithOffset ( void * destData ,
const mxArray * srcArray , mwIndex i , int j , mwIndex offset , size_t
numBytes ) { const uint8_T * varData = ( const uint8_T * ) mxGetData (
mxGetFieldByNumber ( srcArray , i , j ) ) ; memcpy ( ( uint8_T * ) destData ,
( const uint8_T * ) & varData [ offset * numBytes ] , numBytes ) ; } static
void mr_untitled_cacheBitFieldToCellArrayWithOffset ( mxArray * destArray ,
mwIndex i , int j , mwIndex offset , uint_T fieldVal ) ; static void
mr_untitled_cacheBitFieldToCellArrayWithOffset ( mxArray * destArray ,
mwIndex i , int j , mwIndex offset , uint_T fieldVal ) { mxSetCell (
mxGetFieldByNumber ( destArray , i , j ) , offset , mxCreateDoubleScalar ( (
double ) fieldVal ) ) ; } static uint_T
mr_untitled_extractBitFieldFromCellArrayWithOffset ( const mxArray * srcArray
, mwIndex i , int j , mwIndex offset , uint_T numBits ) ; static uint_T
mr_untitled_extractBitFieldFromCellArrayWithOffset ( const mxArray * srcArray
, mwIndex i , int j , mwIndex offset , uint_T numBits ) { const uint_T
fieldVal = ( uint_T ) mxGetScalar ( mxGetCell ( mxGetFieldByNumber ( srcArray
, i , j ) , offset ) ) ; return fieldVal & ( ( 1u << numBits ) - 1u ) ; }
mxArray * mr_untitled_GetDWork ( ) { static const char * ssDWFieldNames [ 3 ]
= { "rtB" , "rtDW" , "NULL_PrevZCX" , } ; mxArray * ssDW =
mxCreateStructMatrix ( 1 , 1 , 3 , ssDWFieldNames ) ;
mr_untitled_cacheDataAsMxArray ( ssDW , 0 , 0 , ( const void * ) & ( rtB ) ,
sizeof ( rtB ) ) ; { static const char * rtdwDataFieldNames [ 4 ] = {
"rtDW.cn4fzdblmf" , "rtDW.jehkify5ki" , "rtDW.ig2kcsvula" , "rtDW.jkgiwbdcht"
, } ; mxArray * rtdwData = mxCreateStructMatrix ( 1 , 1 , 4 ,
rtdwDataFieldNames ) ; mr_untitled_cacheDataAsMxArray ( rtdwData , 0 , 0 , (
const void * ) & ( rtDW . cn4fzdblmf ) , sizeof ( rtDW . cn4fzdblmf ) ) ;
mr_untitled_cacheDataAsMxArray ( rtdwData , 0 , 1 , ( const void * ) & ( rtDW
. jehkify5ki ) , sizeof ( rtDW . jehkify5ki ) ) ;
mr_untitled_cacheDataAsMxArray ( rtdwData , 0 , 2 , ( const void * ) & ( rtDW
. ig2kcsvula ) , sizeof ( rtDW . ig2kcsvula ) ) ;
mr_untitled_cacheDataAsMxArray ( rtdwData , 0 , 3 , ( const void * ) & ( rtDW
. jkgiwbdcht ) , sizeof ( rtDW . jkgiwbdcht ) ) ; mxSetFieldByNumber ( ssDW ,
0 , 1 , rtdwData ) ; } return ssDW ; } void mr_untitled_SetDWork ( const
mxArray * ssDW ) { ( void ) ssDW ; mr_untitled_restoreDataFromMxArray ( (
void * ) & ( rtB ) , ssDW , 0 , 0 , sizeof ( rtB ) ) ; { const mxArray *
rtdwData = mxGetFieldByNumber ( ssDW , 0 , 1 ) ;
mr_untitled_restoreDataFromMxArray ( ( void * ) & ( rtDW . cn4fzdblmf ) ,
rtdwData , 0 , 0 , sizeof ( rtDW . cn4fzdblmf ) ) ;
mr_untitled_restoreDataFromMxArray ( ( void * ) & ( rtDW . jehkify5ki ) ,
rtdwData , 0 , 1 , sizeof ( rtDW . jehkify5ki ) ) ;
mr_untitled_restoreDataFromMxArray ( ( void * ) & ( rtDW . ig2kcsvula ) ,
rtdwData , 0 , 2 , sizeof ( rtDW . ig2kcsvula ) ) ;
mr_untitled_restoreDataFromMxArray ( ( void * ) & ( rtDW . jkgiwbdcht ) ,
rtdwData , 0 , 3 , sizeof ( rtDW . jkgiwbdcht ) ) ; } } mxArray *
mr_untitled_GetSimStateDisallowedBlocks ( ) { mxArray * data =
mxCreateCellMatrix ( 1 , 3 ) ; mwIndex subs [ 2 ] , offset ; { static const
char * blockType [ 1 ] = { "Scope" , } ; static const char * blockPath [ 1 ]
= { "untitled/Scope" , } ; static const int reason [ 1 ] = { 0 , } ; for (
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
ssSetChecksumVal ( rtS , 0 , 3171796158U ) ; ssSetChecksumVal ( rtS , 1 ,
980796643U ) ; ssSetChecksumVal ( rtS , 2 , 3806988549U ) ; ssSetChecksumVal
( rtS , 3 , 393953395U ) ; }
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
, & dtInfo ) ; dtInfo . numDataTypes = 18 ; dtInfo . dataTypeSizes = &
rtDataTypeSizes [ 0 ] ; dtInfo . dataTypeNames = & rtDataTypeNames [ 0 ] ;
dtInfo . BTransTable = & rtBTransTable ; dtInfo . PTransTable = &
rtPTransTable ; dtInfo . dataTypeInfoTable = rtDataTypeInfoTable ; }
untitled_InitializeDataMapInfo ( ) ; ssSetIsRapidAcceleratorActive ( rtS ,
true ) ; ssSetRootSS ( rtS , rtS ) ; ssSetVersion ( rtS ,
SIMSTRUCT_VERSION_LEVEL2 ) ; ssSetModelName ( rtS , "untitled" ) ; ssSetPath
( rtS , "untitled" ) ; ssSetTStart ( rtS , 0.0 ) ; ssSetTFinal ( rtS , 80.0 )
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
const char_T * rt_LoggedStateBlockNames [ ] = { "untitled/Transfer Fcn1" ,
"untitled/Transfer Fcn" } ; static const char_T * rt_LoggedStateNames [ ] = {
"" , "" } ; static boolean_T rt_LoggedStateCrossMdlRef [ ] = { 0 , 0 } ;
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
) ; rt_LoggedStateSignalPtrs [ 0 ] = ( void * ) & rtX . at001at4im [ 0 ] ;
rt_LoggedStateSignalPtrs [ 1 ] = ( void * ) & rtX . nd323p10eu [ 0 ] ; }
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
ssSetChecksumVal ( rtS , 0 , 3171796158U ) ; ssSetChecksumVal ( rtS , 1 ,
980796643U ) ; ssSetChecksumVal ( rtS , 2 , 3806988549U ) ; ssSetChecksumVal
( rtS , 3 , 393953395U ) ; { static const sysRanDType rtAlwaysEnabled =
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
mr_untitled_GetSimStateDisallowedBlocks ) ; slsaGetWorkFcnForSimTargetOP (
rtS , mr_untitled_GetDWork ) ; slsaSetWorkFcnForSimTargetOP ( rtS ,
mr_untitled_SetDWork ) ; rt_RapidReadMatFileAndUpdateParams ( rtS ) ; if (
ssGetErrorStatus ( rtS ) ) { return rtS ; } return rtS ; }
#if defined(_MSC_VER)
#pragma optimize( "", on )
#endif
const int_T gblParameterTuningTid = 1 ; void MdlOutputsParameterSampleTime (
int_T tid ) { MdlOutputsTID1 ( tid ) ; }
