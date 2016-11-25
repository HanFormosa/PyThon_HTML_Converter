#define DSP_Chip_Address    0x68
#define	DSP_Core            2076
#define	DSP_Serial_Out      2078
#define	DSP_Serial_In       2079
#define	DSP_MP0             2080
#define	DSP_MP1             2081
#define	DSP_Power           2082
#define	DSP_ADC_EN          2084
#define	DSP_OSC             2086
#define	DSP_DAC             2087

#define PROG_START_ADR 		1024
#define PROG_LENGTH 		1024
#define PARAM_START_ADR 	0
#define PARAM_LENGTH 		1023

#define SAFELOAD_ADDRESS_0 	2069
#define SAFELOAD_ADDRESS_1 	2070
#define SAFELOAD_ADDRESS_2 	2071
#define SAFELOAD_ADDRESS_3 	2072
#define SAFELOAD_ADDRESS_4 	2073

#define SAFELOAD_DATA_0 	2064
#define SAFELOAD_DATA_1 	2065
#define SAFELOAD_DATA_2 	2066
#define SAFELOAD_DATA_3 	2067
#define SAFELOAD_DATA_4 	2068

//*******DSP Function ADDR*************
#define LIMITER_OFFSET 9 - 1.5 //-minus 2dB to touch the peak of input signal
#define INT_LIMITER_OFFSET 9 // 9 to get 250W
#define COMPRESSOR_OFFSET 5.0 // not used.
#define VOLUME_OFFSET 4.3 // adjust this to get wattage, then adjust limiter to press at this volume.


#define LIMITER_ATTACK_OFFSET 3.0

#define DSP_XOVER_LF_SW     0x17
#define DSP_XOVER_LF_12dB   0x5
#define DSP_XOVER_LF_24dB   0x12

#define DSP_XOVER_HF_SW     0x11
#define DSP_XOVER_HF_12dB   0x0
#define DSP_XOVER_HF_24dB   0xA

#define DSP_VOLUME          0x1C

#define DSP_ROOM_COMP_SW    0x2D
//#define DSP_ROOM_COMP_6dB   0x25 //TODO: remove any reference to this
#define DSP_ROOM_COMP_12dB  0x23
#define DSP_ROOM_COMP_24dB  0x28

//#define DSP_SUB_TUNE_SW     0x33
//#define DSP_SUB_TUNE        0x2E


#define DSP_PEQ1            0x2E
#define DSP_PEQ2            0x33

#define DSP_PHASE           0x5B
#define DSP_LIMITER_1       0x8B // start from threshold?
#define DSP_LIMITER_2       0x7C 
#define DSP_LIMITER_XOVER   0x5D // TODO: involves 2 set of coefficients.

#define DSP_INT_LIMITER     0x9A

#define DSP_SUB_MUTE        0x9E

#define DSP_HF_Delay_L      0x18
#define DSP_HF_Delay_R      0x19
#define DSP_HF_MUTE         0x1A

#define DSP_INT_LPF         0x1E
//#define DSP_INT_HPF         0x9F

#define DSP_INT_PEQ1_SW     0x3D
#define DSP_INT_PEQ2_SW     0x44
#define DSP_INT_PEQ3_SW     0x4B
#define DSP_INT_PEQ4_SW     0x52
#define DSP_INT_PEQ5_SW     0x59

#define DSP_INT_PEQ1        0x38
#define DSP_INT_PEQ2        0x3F
#define DSP_INT_PEQ3        0x46
#define DSP_INT_PEQ4        0x4D
#define DSP_INT_PEQ5        0x54

//#define DSP_VOLUME_OUT 100
//************************************
//***********EE Address***************
//basically each address accommodate one byte (0xFF)
//#define Fact_PEQ2_SW_EE           33  // ???? 1 Bytes  ( 0x020 )
#define Fact_Hipass_SW_EE         0  // ???? 1 Bytes  ( 0x021 )
#define Fact_HiDelay_SW_EE        1  // ???? 1 Bytes  ( 0x022 )
#define Fact_RoomComp_SW_EE       2  // ???? 1 Bytes  ( 0x023 )
#define Fact_SubTune_SW_EE        3// ???? 1 Bytes  ( 0x024 )
#define Fact_PEQ2_SW_EE           4
#define Fact_Limite_AtcTime_EE    5  // ???? 4 Bytes  ( 0x025 ~ 0x028 )
#define Fact_Limite_Threshold_EE  6  // ???? 4 Bytes  ( 0x029 ~ 0x02C )
#define Fact_Limite_RlsTime_EE    7
#define Fact_Limite_AtcTime2_EE    8  // ???? 4 Bytes  ( 0x025 ~ 0x028 )
#define Fact_Limite_Threshold2_EE  9  // ???? 4 Bytes  ( 0x029 ~ 0x02C )
#define Fact_Limite_RlsTime2_EE    10
#define Fact_Limite_XOVER_EE          11
//#define Fact_Limiteh_AtcTime_EE   40  // ???? 4 Bytes  ( 0x025 ~ 0x028 )
//#define Fact_Limiteh_Threshold_EE 8  // ???? 4 Bytes  ( 0x02D ~ 0x030 )

#define Fact_PEQ1_ON_EE 12
#define Fact_PEQ2_ON_EE 13
#define Fact_PEQ3_ON_EE 14
#define Fact_PEQ4_ON_EE 15
#define Fact_PEQ5_ON_EE 16

#define Fact_Lowpass_Freq_EE      17  // ???? 4 Bytes  ( 0x02D ~ 0x030 )

#define Fact_PEQ1_Freq_EE         18  // ???? 4 Bytes  ( 0x031 ~ 0x034 )
#define Fact_PEQ1_Level_EE        19  // ???? 4 Bytes  ( 0x035 ~ 0x038 )
#define Fact_PEQ1_Q_EE            20  // ???? 4 Bytes  ( 0x039 ~ 0x03C )

#define Fact_PEQ2_Freq_EE         21  // ???? 4 Bytes  ( 0x03D ~ 0x040 )
#define Fact_PEQ2_Level_EE        22  // ???? 4 Bytes  ( 0x041 ~ 0x044 )
#define Fact_PEQ2_Q_EE            23  // ???? 4 Bytes  ( 0x045 ~ 0x048 )

#define Fact_PEQ3_Freq_EE         24  // ???? 4 Bytes  ( 0x049 ~ 0x04C )
#define Fact_PEQ3_Level_EE        25  // ???? 4 Bytes  ( 0x04D ~ 0x050 )
#define Fact_PEQ3_Q_EE            26  // ???? 4 Bytes  ( 0x051 ~ 0x054 )

#define Fact_PEQ4_Freq_EE         27 // ???? 4 Bytes  ( 0x049 ~ 0x04C )
#define Fact_PEQ4_Level_EE        28  // ???? 4 Bytes  ( 0x04D ~ 0x050 )
#define Fact_PEQ4_Q_EE            29  // ???? 4 Bytes  ( 0x051 ~ 0x054 )

#define Fact_PEQ5_Freq_EE         30 // ???? 4 Bytes  ( 0x049 ~ 0x04C )
#define Fact_PEQ5_Level_EE        31  // ???? 4 Bytes  ( 0x04D ~ 0x050 )
#define Fact_PEQ5_Q_EE            32  // ???? 4 Bytes  ( 0x051 ~ 0x054 )

#define Fact_SubTune_Freq_EE      33  // ???? 4 Bytes  ( 0x055 ~ 0x058 )
#define Fact_SubTune_Slope_EE     34  // ???? 4 Bytes  ( 0x059 ~ 0x05C )
#define Fact_SubTuneFreq_Q_EE     35  // ???? 4 Bytes  ( 0x05D ~ 0x060 )

//-----< User Menu >-----------------------------------------------------------
#define User_Volume_EE            36  // ???? 4 Bytes  ( 0x100 ~ 0x103 )
#define User_LPF_Freq_EE          37  // ???? 4 Bytes  ( 0x104 ~ 0x107 )
#define User_LPF_Slope_EE         38  // ???? 4 Bytes  ( 0x108 ~ 0x10B )
#define User_HPF_Freq_EE          39  // ???? 4 Bytes  ( 0x10C ~ 0x10F )
#define User_HPF_Slope_EE         40  // ???? 4 Bytes  ( 0x110 ~ 0x113 )
#define User_PEQ1_Freq_EE         41  // ???? 4 Bytes  ( 0x114 ~ 0x117 )
#define User_PEQ1_Level_EE        42  // ???? 4 Bytes  ( 0x118 ~ 0x11B )
#define User_PEQ1_Q_EE            43  // ???? 4 Bytes  ( 0x11C ~ 0x11F )
#define User_PEQ2_Freq_EE         44  // ???? 4 Bytes  ( 0x120 ~ 0x123 )
#define User_PEQ2_Level_EE        45  // ???? 4 Bytes  ( 0x124 ~ 0x127 )
#define User_PEQ2_Q_EE            46  // ???? 4 Bytes  ( 0x128 ~ 0x12B )
#define User_Phase_EE             47  // ???? 4 Bytes  ( 0x12C ~ 0x12F )
#define User_Delay_EE             48  // ???? 4 Bytes  ( 0x130 ~ 0x133 )
#define User_RoomCom_Freq_EE      49  // ???? 4 Bytes  ( 0x134 ~ 0x137 )
#define User_RoomCom_Slope_EE     50  // ???? 4 Bytes  ( 0x138 ~ 0x13B )
#define User_SubTune_EE           51  // ???? 4 Bytes  ( 0x13C ~ 0x13F )


//#define Fact_2BandLimiter_XOVER_Freq_EE 71



#define Fact_Modle_EE            340  // ???? 16 Bytes ( 0x000 ~ 0x00F )
#define PowerMode_EE             360  // ???? 16 Bytes ( 0x010 ~ 0x01F )
#define Check_Save_EE            384// ???? 1 Byte   ( 0x3FF )
#define USBCMD_VOL 0xC0
#define USBCMD_DELAY 0xC3 
#define USBCMD_PHASE 0xC4
#define USBCMD_XOVER 0xC2
#define USBCMD_LPF 0x03 //channel 3 from "XOVER" USB CMD
#define USBCMD_HPF 0x04 //channel 4 from "XOVER" USB CMD
#define USBCMD_SUBSONIC 0x05 //channel 5 from "XOVER" USB CMD
#define USBCMD_PEQ 0xC6
#define USBCMD_DUALLIM 0xB7 //dual band limiter

//==slope constants as defined in labview , more to fill in==
#define USBCMD_kSLOPE12 0 //slope constants
#define USBCMD_kSLOPE24 1 //slope constants
//#define USBCMD_kSLOPE36 2 

//==Parameter header address, to identify which parameter table to send to GUI==
//used for specifying parameter table array[0xF3]
#define USBCMD_0xF3 0 //volume, phase , delay, lpf and hpf
#define USBCMD_0xF4 1 // 5 internal peq
#define USBCMD_0xF5 2 // limiters

//======< DSP constants > ===========
#define kSAMPLING_RATE_FS 48000

#define kLIM_REL_90MS 0
#define kLIM_REL_180MS 1
#define kLIM_REL_360MS 2
#define kLIM_REL_720MS 3
#define kLIM_REL_1Q5S 4
#define kLIM_REL_3S 5

#define kLIM_ATT_1MS 0
#define kLIM_ATT_5MS 1
#define kLIM_ATT_10MS 2
#define kLIM_ATT_20MS 3
#define kLIM_ATT_50MS 4
#define kLIM_ATT_100MS 5

//=====< DSP ??????? >==========================================================================================
void OpenDSP( void );
void LoadDSP( void );
void DSP_All_Write( const unsigned char *, const unsigned char * );
void DSP_Write( int, int, unsigned char *, unsigned char, unsigned char, int, unsigned char );
void SafeloadSingleParamWrite( int, float, int, unsigned char );
void SafeloadSingleParamWrite2( int Address, float Parameter, int Location, unsigned char Enable );
void Format_Fix( float );
void I2C_Write_Loop( unsigned char, unsigned char );
long DSPRealRead( int );
void Filter_Write( unsigned int, double * );
//=====< DSP ????? >==============================================================================================
void Volume_Slow( unsigned int, double, double );
void Mute( unsigned int Address, unsigned char Status );
void INVERT( unsigned int Address, unsigned char Status );

void Flash_PEQ( unsigned int type,double Freq, double Gain ,double Q,  unsigned int PEQ_ADDR );
void PEQ_ONOFF(unsigned int ON,unsigned int PEQ_SW_ADDR);
void DSP_Data_Capture_Read(unsigned int address,unsigned char *level_out);
double Level_ReadBack_to_dB(unsigned char *lvl , unsigned int addr);
void DSP_Register_Read(unsigned int address);

void Compressor(unsigned int Address,double threshold, double ratio, double Attack_ms ,double Release_ms);
//void Peaking( unsigned int, double, double, double, double );
void Peaking( unsigned int Address, double Boost, double Frequency, double Q, double Gain );
void AllPass( unsigned int, double, double, double );
//void Limiter( unsigned int, double, double, double);
void Limiter( unsigned int Address, int rms, int decay, double Threshold );
//void General_HighPass_2Order( unsigned int, double, double, double );
//void General_LowPass_2Order( unsigned int, double, double, double );
void HighPass_Filter_1Order( unsigned int, double, double );
void LowPass_filter_1Order( unsigned int, double, double );
void Filter_Write_1Order( unsigned int, double * );
void PHASE_Delay ( unsigned int, long );
void FUNCTION_SWITCH( unsigned int, unsigned char, unsigned char );
void High_shelving( unsigned int Address, double Boost, double Frequency, double S, double Gain );
void Low_shelving( unsigned int Address, double Boost, double Frequency, double S, double Gain );

void Post_Gain( unsigned int , double );
void General_HighPass_2Order( unsigned int Address, double Frequency, double Q, double Gain,unsigned char XOVER );
void General_LowPass_2Order( unsigned int Address, double Frequency, double Q, double Gain,unsigned char XOVER );
void Limiter_XOVER(unsigned int addr, double freq);
