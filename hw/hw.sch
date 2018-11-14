EESchema Schematic File Version 4
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Raspberry_Pi_2_3 J?
U 1 1 5BEAA4A7
P 1950 3350
F 0 "J?" H 1950 4828 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 1950 4737 50  0000 C CNN
F 2 "" H 1950 3350 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 1950 3350 50  0001 C CNN
	1    1950 3350
	-1   0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5BEAA64A
P 1900 1350
F 0 "#PWR?" H 1900 1200 50  0001 C CNN
F 1 "+5V" H 1915 1523 50  0000 C CNN
F 2 "" H 1900 1350 50  0001 C CNN
F 3 "" H 1900 1350 50  0001 C CNN
	1    1900 1350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5BEAA6E3
P 2150 1350
F 0 "#PWR?" H 2150 1100 50  0001 C CNN
F 1 "GND" H 2155 1177 50  0000 C CNN
F 2 "" H 2150 1350 50  0001 C CNN
F 3 "" H 2150 1350 50  0001 C CNN
	1    2150 1350
	-1   0    0    1   
$EndComp
$Comp
L power:PWR_FLAG #FLG?
U 1 1 5BEAAC83
P 1900 1350
F 0 "#FLG?" H 1900 1425 50  0001 C CNN
F 1 "PWR_FLAG" H 1900 1523 50  0000 C CNN
F 2 "" H 1900 1350 50  0001 C CNN
F 3 "~" H 1900 1350 50  0001 C CNN
	1    1900 1350
	-1   0    0    1   
$EndComp
$Comp
L power:PWR_FLAG #FLG?
U 1 1 5BEAACC8
P 2150 1350
F 0 "#FLG?" H 2150 1425 50  0001 C CNN
F 1 "PWR_FLAG" H 2150 1523 50  0000 C CNN
F 2 "" H 2150 1350 50  0001 C CNN
F 3 "~" H 2150 1350 50  0001 C CNN
	1    2150 1350
	-1   0    0    1   
$EndComp
$Comp
L Motor:Motor_Servo M?
U 1 1 5BEAAEF1
P 3950 2950
F 0 "M?" H 4281 3015 50  0000 L CNN
F 1 "Yaw" H 4281 2924 50  0000 L CNN
F 2 "" H 3950 2760 50  0001 C CNN
F 3 "http://forums.parallax.com/uploads/attachments/46831/74481.png" H 3950 2760 50  0001 C CNN
	1    3950 2950
	1    0    0    -1  
$EndComp
$Comp
L Motor:Motor_Servo M?
U 1 1 5BEAAF40
P 3950 4150
F 0 "M?" H 4281 4215 50  0000 L CNN
F 1 "Pitch" H 4281 4124 50  0000 L CNN
F 2 "" H 3950 3960 50  0001 C CNN
F 3 "http://forums.parallax.com/uploads/attachments/46831/74481.png" H 3950 3960 50  0001 C CNN
	1    3950 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 2850 3650 2850
$Comp
L power:+5V #PWR?
U 1 1 5BEAB52E
P 3650 2950
F 0 "#PWR?" H 3650 2800 50  0001 C CNN
F 1 "+5V" V 3665 3078 50  0000 L CNN
F 2 "" H 3650 2950 50  0001 C CNN
F 3 "" H 3650 2950 50  0001 C CNN
	1    3650 2950
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2750 4050 3650 4050
$Comp
L power:+5V #PWR?
U 1 1 5BEAB756
P 3650 4150
F 0 "#PWR?" H 3650 4000 50  0001 C CNN
F 1 "+5V" V 3665 4278 50  0000 L CNN
F 2 "" H 3650 4150 50  0001 C CNN
F 3 "" H 3650 4150 50  0001 C CNN
	1    3650 4150
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5BEAB7AF
P 3650 4250
F 0 "#PWR?" H 3650 4000 50  0001 C CNN
F 1 "GND" V 3655 4122 50  0000 R CNN
F 2 "" H 3650 4250 50  0001 C CNN
F 3 "" H 3650 4250 50  0001 C CNN
	1    3650 4250
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5BEAB7FF
P 3650 3050
F 0 "#PWR?" H 3650 2800 50  0001 C CNN
F 1 "GND" V 3655 2922 50  0000 R CNN
F 2 "" H 3650 3050 50  0001 C CNN
F 3 "" H 3650 3050 50  0001 C CNN
	1    3650 3050
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5BEABB75
P 4900 3500
F 0 "J?" H 5006 3678 50  0000 C CNN
F 1 "Conn_01x02_Male" H 5006 3587 50  0000 C CNN
F 2 "" H 4900 3500 50  0001 C CNN
F 3 "~" H 4900 3500 50  0001 C CNN
	1    4900 3500
	1    0    0    -1  
$EndComp
$EndSCHEMATC
