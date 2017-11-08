# BulkUpload
Working example of BulkUpload problem

The script greenOnOff.py is loaded to a SN171 protoboard.

The GUITemplate is opened.
Clicking on the LED on button lights the green LED on the protoboard and the off button does the oppisite.

The command line to initiate a bulk upload  of the 'yellowOnOff.spy' file is coded into the GUI on the BulkUpload Button.

Clicking on the button uploads the spy file to the protoboard.
Clicking the on button should turn on the yellow but it shows a timeout on the DEBUG log.

Closing the GUI and opening it again will show the following error on the log:
  DEBUG:snaplib.snaplib.RpcCodec:Received RPC payload with invalid appended CRC *and* CRC validation 
  is currently active, packet discarded
  
 The LED buttons do not turn on or off the LED

