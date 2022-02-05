#ifndef RTW_HEADER_untitled_types_h_
#define RTW_HEADER_untitled_types_h_
#include "rtwtypes.h"
#include "builtin_typeid_types.h"
#include "multiword_types.h"
#ifndef DEFINED_TYPEDEF_FOR_struct_QE1BuHHswdfNbaPCEXtrT_
#define DEFINED_TYPEDEF_FOR_struct_QE1BuHHswdfNbaPCEXtrT_
typedef struct { uint8_T SimulinkDiagnostic ; uint8_T Model [ 8 ] ; uint8_T
Block [ 32 ] ; uint8_T OutOfRangeInputValue ; uint8_T NoRuleFired ; uint8_T
EmptyOutputFuzzySet ; uint8_T sl_padding0 [ 4 ] ; }
struct_QE1BuHHswdfNbaPCEXtrT ;
#endif
#ifndef DEFINED_TYPEDEF_FOR_struct_RCP1oovUDF2zF6C9vcJmtG_
#define DEFINED_TYPEDEF_FOR_struct_RCP1oovUDF2zF6C9vcJmtG_
typedef struct { uint8_T type [ 5 ] ; uint8_T sl_padding0 [ 3 ] ; int32_T
origTypeLength ; uint8_T sl_padding1 [ 4 ] ; real_T params [ 3 ] ; int32_T
origParamLength ; uint8_T sl_padding2 [ 4 ] ; } struct_RCP1oovUDF2zF6C9vcJmtG
;
#endif
#ifndef DEFINED_TYPEDEF_FOR_struct_OTlcYhhT3UxB0PEhAC2ANE_
#define DEFINED_TYPEDEF_FOR_struct_OTlcYhhT3UxB0PEhAC2ANE_
typedef struct { struct_RCP1oovUDF2zF6C9vcJmtG mf [ 3 ] ; int32_T origNumMF ;
uint8_T sl_padding0 [ 4 ] ; } struct_OTlcYhhT3UxB0PEhAC2ANE ;
#endif
#ifndef DEFINED_TYPEDEF_FOR_struct_CJy5Aill7vxxqD7Hhzai6G_
#define DEFINED_TYPEDEF_FOR_struct_CJy5Aill7vxxqD7Hhzai6G_
typedef struct { uint8_T type [ 7 ] ; uint8_T andMethod [ 3 ] ; uint8_T
orMethod [ 3 ] ; uint8_T defuzzMethod [ 8 ] ; uint8_T impMethod [ 3 ] ;
uint8_T aggMethod [ 3 ] ; uint8_T sl_padding0 [ 5 ] ; real_T inputRange [ 4 ]
; real_T outputRange [ 2 ] ; struct_OTlcYhhT3UxB0PEhAC2ANE inputMF [ 2 ] ;
struct_OTlcYhhT3UxB0PEhAC2ANE outputMF ; real_T antecedent [ 18 ] ; real_T
consequent [ 9 ] ; real_T connection [ 9 ] ; real_T weight [ 9 ] ; int32_T
numSamples ; int32_T numInputs ; int32_T numOutputs ; int32_T numRules ;
int32_T numInputMFs [ 2 ] ; int32_T numCumInputMFs [ 2 ] ; int32_T
numOutputMFs ; int32_T numCumOutputMFs ; real_T outputSamplePoints [ 101 ] ;
int32_T orrSize [ 2 ] ; int32_T aggSize [ 2 ] ; int32_T irrSize [ 2 ] ;
int32_T rfsSize [ 2 ] ; int32_T sumSize [ 2 ] ; int32_T inputFuzzySetType ;
uint8_T sl_padding1 [ 4 ] ; } struct_CJy5Aill7vxxqD7Hhzai6G ;
#endif
typedef struct P_ P ;
#endif
