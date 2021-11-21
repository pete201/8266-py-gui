# 8266-py-gui
read values from an 8266 and display on screen via python gui

file: "display window.py"
create a GUI window to display values
later this will display 8266 output
following notes from: https://pysimplegui.readthedocs.io/en/latest/
  and tutorial: https://www.youtube.com/watch?v=cLcfLm_GgiM

added .ino for 8266 from previous project
added readSerialTread.py which sets up a thread to read output from the 8266

works as intended.
No user input required at the GUI, it simply displays the current values from the 8266 MPU6050
