#ifndef RTW_HEADER_untitled_h_
#define RTW_HEADER_untitled_h_
#include <stddef.h>
#include <string.h>
#include "rtw_modelmap_simtarget.h"
#ifndef untitled_COMMON_INCLUDES_
#define untitled_COMMON_INCLUDES_
#include <stdlib.h>
#include "rtwtypes.h"
#include "sigstream_rtw.h"
#include "simtarget/slSimTgtSigstreamRTW.h"
#include "simtarget/slSimTgtSlioCoreRTW.h"
#include "simtarget/slSimTgtSlioClientsRTW.h"
#include "simtarget/slSimTgtSlioSdiRTW.h"
#include "simstruc.h"
#include "fixedpoint.h"
#include "raccel.h"
#include "slsv_diagnostic_codegen_c_api.h"
#include "rt_logging_simtarget.h"
#include "dt_info.h"
#include "ext_work.h"
#endif
#include "untitled_types.h"
#include "multiword_types.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#include "mwmathutil.h"
#include "rt_defines.h"
#define MODEL_NAME untitled
#define NSAMPLE_TIMES (2) 
#define NINPUTS (0)       
#define NOUTPUTS (0)     
#define NBLOCKIO (9) 
#define NUM_ZC_EVENTS (0) 
#ifndef NCSTATES
#define NCSTATES (4)   
#elif NCSTATES != 4
#error Invalid specification of NCSTATES defined in compiler command
#endif
#ifndef rtmGetDataMapInfo
#define rtmGetDataMapInfo(rtm) (*rt_dataMapInfoPtr)
#endif
#ifndef rtmSetDataMapInfo
#define rtmSetDataMapInfo(rtm, val) (rt_dataMapInfoPtr = &val)
#endif
#ifndef IN_RACCEL_MAIN
#endif
typedef struct { real_T df0o0kcdix ; real_T of21yu54hh ; real_T jkb3o2dfgf ;
real_T fdxn1nte3a ; real_T mzz3dbumyh ; real_T gh32rfp5sa ; real_T fge3vtkizy
[ 2 ] ; real_T kafhhzneq4 [ 2 ] ; real_T pyxx1a5lgc ; } B ; typedef struct {
real_T cn4fzdblmf ; real_T jehkify5ki ; real_T ig2kcsvula ; real_T jkgiwbdcht
; struct { void * LoggedData ; } mbtuw4il0e ; } DW ; typedef struct { real_T
at001at4im [ 2 ] ; real_T nd323p10eu [ 2 ] ; } X ; typedef struct { real_T
at001at4im [ 2 ] ; real_T nd323p10eu [ 2 ] ; } XDot ; typedef struct {
boolean_T at001at4im [ 2 ] ; boolean_T nd323p10eu [ 2 ] ; } XDis ; typedef
struct { real_T at001at4im [ 2 ] ; real_T nd323p10eu [ 2 ] ; } CStateAbsTol ;
typedef struct { real_T at001at4im [ 2 ] ; real_T nd323p10eu [ 2 ] ; }
CXPtMin ; typedef struct { real_T at001at4im [ 2 ] ; real_T nd323p10eu [ 2 ]
; } CXPtMax ; typedef struct { rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ;
struct P_ { real_T OutputSamplePoints_Value [ 101 ] ; real_T TransferFcn1_A [
2 ] ; real_T TransferFcn1_C [ 2 ] ; real_T Gain_Gain ; real_T TransferFcn_A [
2 ] ; real_T TransferFcn_C [ 2 ] ; real_T Gain_Gain_kxei4o4340 ; real_T
thets_ref_Value ; real_T thrust_Value ; } ; extern const char *
RT_MEMORY_ALLOCATION_ERROR ; extern B rtB ; extern X rtX ; extern DW rtDW ;
extern P rtP ; extern mxArray * mr_untitled_GetDWork ( ) ; extern void
mr_untitled_SetDWork ( const mxArray * ssDW ) ; extern mxArray *
mr_untitled_GetSimStateDisallowedBlocks ( ) ; extern const
rtwCAPI_ModelMappingStaticInfo * untitled_GetCAPIStaticMap ( void ) ; extern
SimStruct * const rtS ; extern const int_T gblNumToFiles ; extern const int_T
gblNumFrFiles ; extern const int_T gblNumFrWksBlocks ; extern rtInportTUtable
* gblInportTUtables ; extern const char * gblInportFileName ; extern const
int_T gblNumRootInportBlks ; extern const int_T gblNumModelInputs ; extern
const int_T gblInportDataTypeIdx [ ] ; extern const int_T gblInportDims [ ] ;
extern const int_T gblInportComplex [ ] ; extern const int_T
gblInportInterpoFlag [ ] ; extern const int_T gblInportContinuous [ ] ;
extern const int_T gblParameterTuningTid ; extern DataMapInfo *
rt_dataMapInfoPtr ; extern rtwCAPI_ModelMappingInfo * rt_modelMapInfoPtr ;
void MdlOutputs ( int_T tid ) ; void MdlOutputsParameterSampleTime ( int_T
tid ) ; void MdlUpdate ( int_T tid ) ; void MdlTerminate ( void ) ; void
MdlInitializeSizes ( void ) ; void MdlInitializeSampleTimes ( void ) ;
SimStruct * raccel_register_model ( ssExecutionInfo * executionInfo ) ;
#endif
