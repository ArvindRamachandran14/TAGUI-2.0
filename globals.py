# globals.pyxw
# Globals as needed
# Change history:
#   20191112:KDT - Original issue

# Global variables

import json

class globals_:

    def __init_(self) :

        with open('taui.json', 'r') as fCfg :
            self.config = json.loads(fCfg.read())
        
        self.tty = None

        self.cfg = {}

        self.initialize()

    def initialize(self):

        self.cfg = self.config  # Set the cfg
        self.tty = self.cfg["tty"]
        self.baud_rate = self.cfg["baud_rate"]
        self.time_out = self.cfg["time_out"]
        self.time_interval = self.cfg["time_interval"]
        self.bconnected = "False"


    def update(self):

        self.cfg["tty"] = self.tty

        self.cfg["baud_rate"] = self.baud_rate

        self.cfg["time_out"] = self.time_out

        self.cfg["time_interval"] = self.time_interval

        self.cfg["bconnected"] = self.bconnected

        print(self.cfg)

        with open(self.cfgFile, 'w') as fCfg:

            json.dump(self.cfg, fCfg)
