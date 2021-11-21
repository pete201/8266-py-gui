# 8266-py-gui
read values from an 8266 and MPU6050 and display on screen via python gui

file: "display window.py"
create a GUI window to display 'Yaw, Pitch, Roll, Button' values from 8266 output
  following notes from: https://pysimplegui.readthedocs.io/en/latest/
  and tutorial: https://www.youtube.com/watch?v=cLcfLm_GgiM


added .ino for 8266 from previous project

added readSerialTread.py which sets up a thread to read output from the 8266


Wiring is really simple:
MPU-6050  (8266-mini): 
3.3V 	  (3.3V); 
0V        (0V);
SCL       (D2(gpio-5));
SDA       (D1(gpio-4));
INT       (D5(gpio-14))
 
NOTE: I also have a button; one side to ground, the other to D6(GPIO-12) but I am not using it in this sketch
I mention this for explanation as it is included in the serial output from the 8266 and read by readSerialThread.

INSTRUCTIONS
-------------------
After connecting the MPU6050 to the 8266, upload the 6050ypr.ino file to the 8266

With the 8266 connected via USB, run "display window.py"

To quit, close the window or click the "Exit" button

No user input required at the GUI, it simply displays the current values from the 8266 MPU6050

NOTE: sometimes i find i need to hard reset (unplug and replug USB) the 8266 before it will start outputing Serial data
