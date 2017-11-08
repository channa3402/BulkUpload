from synapse.platforms import *

GREEN_LED = GPIO_1


@setHook(HOOK_STARTUP)
def startup():
    setPinDir(GREEN_LED, True) 

    
def LEDon():
    writePin(GREEN_LED, True)
    
def LEDoff():
    writePin(GREEN_LED, False)