#ifndef RTW_HEADER_Pendulum_h_
#define RTW_HEADER_Pendulum_h_
#include <stddef.h>
#include <string.h>
#include "rtw_modelmap_simtarget.h"
#ifndef Pendulum_COMMON_INCLUDES_
#define Pendulum_COMMON_INCLUDES_
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
#include "Pendulum_types.h"
#include "multiword_types.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#include "mwmathutil.h"
#include "rt_defines.h"
#define MODEL_NAME Pendulum
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
typedef struct { real_T axschpirno ; real_T g4v5j4qgvt ; real_T ijcpe01hdq ;
real_T aebifh0pvl ; real_T bgxpngmvlh ; real_T o1bcqkln1h ; real_T pvtxzoiu5m
[ 2 ] ; real_T hzxm5aw2pv [ 2 ] ; real_T hvxvauopvm ; } B ; typedef struct {
real_T cgjsg2uzpw ; real_T a0wnci0dl4 ; real_T ki1hmp0vfz ; real_T ntkdb0tjdq
; struct { void * LoggedData ; } gvdyflzsjk ; } DW ; typedef struct { real_T
dofzbcbfvq [ 2 ] ; real_T oig2rykllt [ 2 ] ; } X ; typedef struct { real_T
dofzbcbfvq [ 2 ] ; real_T oig2rykllt [ 2 ] ; } XDot ; typedef struct {
boolean_T dofzbcbfvq [ 2 ] ; boolean_T oig2rykllt [ 2 ] ; } XDis ; typedef
struct { real_T dofzbcbfvq [ 2 ] ; real_T oig2rykllt [ 2 ] ; } CStateAbsTol ;
typedef struct { real_T dofzbcbfvq [ 2 ] ; real_T oig2rykllt [ 2 ] ; }
CXPtMin ; typedef struct { real_T dofzbcbfvq [ 2 ] ; real_T oig2rykllt [ 2 ]
; } CXPtMax ; typedef struct { rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ;
struct P_ { real_T OutputSamplePoints_Value [ 101 ] ; real_T TransferFcn3_A [
2 ] ; real_T TransferFcn3_C [ 2 ] ; real_T Gain_Gain ; real_T TransferFcn2_A
[ 2 ] ; real_T TransferFcn2_C [ 2 ] ; real_T Gain_Gain_euln0ijgco ; real_T
thets_ref1_Value ; real_T thrust1_Value ; } ; extern const char *
RT_MEMORY_ALLOCATION_ERROR ; extern B rtB ; extern X rtX ; extern DW rtDW ;
extern P rtP ; extern mxArray * mr_Pendulum_GetDWork ( ) ; extern void
mr_Pendulum_SetDWork ( const mxArray * ssDW ) ; extern mxArray *
mr_Pendulum_GetSimStateDisallowedBlocks ( ) ; extern const
rtwCAPI_ModelMappingStaticInfo * Pendulum_GetCAPIStaticMap ( void ) ; extern
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
