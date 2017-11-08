from synapse.platforms import *

YELLOW_LED = GPIO_2


@setHook(HOOK_STARTUP)
def startup():
    setPinDir(YELLOW_LED, True) 

    
def LEDon():
    writePin(YELLOW_LED, True)
    
def LEDoff():
    writePin(YELLOW_LED, False)