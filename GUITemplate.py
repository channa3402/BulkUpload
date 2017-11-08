import wx
from snapconnect import snap
import random
import snaplib
import logging
import sqlite3 as sqlite
import csv
import os

BRIDGE_NODE = {'type':snap.SERIAL_TYPE_RS232, 'port':2}
log = "C:/Users/Cathy/Desktop/log.txt"
NodeB = '\x60\x87\x18'  #Define nodes

class PumpFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title='GUI Template',size=(500,600))

        panel = wx.Panel(self)

        self.poller = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, lambda event : self.snap.poll())
        self.poller.Start(20,wx.TIMER_CONTINUOUS)
        self.log = logging.getLogger("PumpFrame")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.GridBagSizer(hgap=5,vgap=5)

        self.onUploadBtn = wx.Button(panel, -1, "Bulk Upload")
        self.Bind(wx.EVT_BUTTON, self.onBulkUpload, self.onUploadBtn)
        self.LEDonBtn = wx.Button(panel, -1, "LED on")
        self.Bind(wx.EVT_BUTTON, self.onLEDon, self.LEDonBtn)
        self.LEDoffBtn = wx.Button(panel, -1, "LED off")
        self.Bind(wx.EVT_BUTTON, self.onLEDoff, self.LEDoffBtn) 

        btnSizer.Add(self.onUploadBtn, pos=(0,0))
        btnSizer.Add(self.LEDonBtn, pos=(1,0))
        btnSizer.Add(self.LEDoffBtn, pos=(2,0))
        
        
        sizer.Add(btnSizer, flag=wx.CENTER|wx.ALL, border = 5)
        
        panel.SetSizer(sizer)
        panel.Fit()
        
        funcdir = {}
        
        self.snap = snap.Snap(funcs = funcdir)
        self.snap.open_serial(BRIDGE_NODE['type'],BRIDGE_NODE['port'])
        initial_mesh_seq_num = random.randint(1,255)
        self.snap.save_nv_param(snap.NV_MESH_SEQUENCE_NUMBER_ID, initial_mesh_seq_num)
        snaplib.MeshCodec.sequence_number=initial_mesh_seq_num

           
    def onBulkUpload(self,event):
        "Start BulkUpload.py"
        self.snap.close_serial(BRIDGE_NODE['type'],BRIDGE_NODE['port'])
        x = 'start bulkUpload.py -m MacList.txt -s yellowOnOff.spy' 
        os.system(x)


    def onLEDon(self,event):
        self.snap.rpc(NodeB, 'LEDon')

    def onLEDoff(self,event):
        self.snap.rpc(NodeB, 'LEDoff')



if __name__ == "__main__":
    app = wx.App(False)
    frame = PumpFrame(None, 'Pump Only')
    frame.Show()
    logging.basicConfig(level=logging.DEBUG)
#    logging.basicConfig(filename=log,level=logging.INFO,
#                        format='%(asctime)s %(levelname)s - %(funcName)s: %(message)s',
#                        datefmt="%Y-%m-%d %H:%M:%S")
    app.MainLoop()
