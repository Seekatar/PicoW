import network
import socket
import time

from machine import Pin

led = Pin("LED", Pin.OUT)

ssid = 'Fluffy'
password = 'whitedogfromgalesburg'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>%s</p>
    </body>
</html>
"""

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print('listening on', addr)
stateIs = "Uninitialized"
cl = None
exit_now = -1
# Listen for connections
light_on = led.value() == 1
request_prefix = "b'GET " # prefix on request response
prefix_len = len(request_prefix)

while exit_now < 0:
    try:
        cl, addr = s.accept()
        print("-"*80)
        print('client connected from', addr)
        request = cl.recv(1024)
        print(">>",request,"<<")

        request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        exit_now = request.find('/exit')
        toggle = request.find('/light/toggle')

        print( 'led on = ' + str(led_on))
        print( 'led off = ' + str(led_off))
        print( 'toggle =', toggle, toggle == prefix_len)
        print( 'exit_now = ' + str(exit_now))

        if toggle == prefix_len:
            print("toggling from", light_on, "to", not light_on)
            light_on = not light_on
            led.value(light_on)
            stateIs = "LED is " + str(light_on)

        if led_on == prefix_len:
            print("led on")
            led.value(1)
            light_on = True
            stateIs = "LED is ON"

        if led_off == prefix_len:
            print("led off")
            led.value(0)
            light_on = False
            stateIs = "LED is OFF"

        if exit_now >= 0:
            print("exiting")
            led.value(0)
            stateIs = "exiting"

        response = html % stateIs

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        if cl:
            cl.close()
        print('connection closed')

led.value(0)
s.close()
print('exited')
