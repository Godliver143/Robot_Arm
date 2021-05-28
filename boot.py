def ap():
    import network
    passwd = "arm"
    essid = "RobotArm"
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=essid, password=passwd)
    print(ap.ifconfig())

try:
    ap()
except KeyboardInterrupt:
    print("process stopped")


