import time
from machine import Pin, I2C
from servo import Servo
try:
 import usocket as socket
except:
 import socket

servo_object1 = Servo(22)
servo_object2 = Servo(21)
servo_object3 = Servo(26)
servo_object4 = Servo(18)


#putting all the servos to a resting angle
def on_start():
    rest_angle1 = 0
    rest_angle2 = 150
    servo_object1.angle(rest_angle1)
    servo_object2.angle(rest_angle2)
    servo_object3.angle(rest_angle1)
    servo_object4.angle(rest_angle1)
#on button #Onpress allow the rest of the code to function

    


servo1 = [0]
servo2 = [0]
servo3 = [0]
servo4 = [0]

#increasing servo angle
def right(servo_object, servo_list):
    angle_increament = 10
    angle_limit = 180
    last_value_in_list = -1
    if servo_list[last_value_in_list] != angle_limit:
        value = servo_list[last_value_in_list]
        angle = value + angle_increament
        servo_list.append(angle)
        servo_object.angle(angle)
    else:
        servo_object.angle(angle_limit)
        print("limit reached")

#decreasing servo angle
def left(servo_object, servo_list):
    second2last_value_in_list = -2
    last_value_in_list = -1
    minimum_lenght = 2
    if len(servo_list) >= minimum_lenght:
        value = servo_list[second2last_value_in_list]
        servo_object.angle(value)
        servo_list.pop(last_value_in_list)
    else:
        value = servo_list[last_value_in_list]
        servo_object.angle(value)
    

def web_page():
        
    html ="""
        <html>
            <head>
                <style type="text/css">
                body{
                    /*background-image: linear-gradient(white,rgb(198,200,201));*/
                    background-color: white;
                    font-style:  open sans ;
                }
                .start{height: 100px; width: 100px;}
                svg{color: green;}
                .grip{
                    border-radius: 40%;
                    text-align: center;
                    background-color: #179c52;
                    color: white;
                    padding: 20px;
                    height: 80px;
                    width: 110px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }

                .border{
                    /*border: black solid 1px;*/
                    float: left;
                    padding: 30px;
                    padding-right: -25px;
                    width: 30%;
                    height: 390px;
                    margin: 35px;

                }

                .main{
                    float: left;
                    background-color:#fff; 
                    width: 100%;
                    /*border: 2px yellow solid;*/
                    padding-left: 8px;
                    box-sizing: border-box;
                    height: 40vh;
                    margin: auto;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    /*background-image: linear-gradient(rgb(198,200,201),white,rgb(198,200,201));*/
                }

                .up{
                -webkit-transform:rotate(180deg);
                -moz-transform: rotate(180deg);
                -ms-transform: rotate(180deg);
                -o-transform: rotate(180deg);
                transform: rotate(180deg);
                height: 20;
                width: 20;  /*150*/
                }

                input{
                    border-radius: 50%;
                }

                .left{
                    float: left;
                    -webkit-transform:rotate(90deg);
                    -moz-transform: rotate(90deg);
                    -ms-transform: rotate(90deg);
                    -o-transform: rotate(90deg);
                    transform: rotate(90deg);
                    height: 80;
                    width: 80;
                }

                
                .right{

                    float: right;
                    -webkit-transform:rotate(270deg);
                    -moz-transform: rotate(270deg);
                    -ms-transform: rotate(270deg);
                    -o-transform: rotate(270deg);
                    transform: rotate(270deg);
                    height: 80;
                    width: 80;
                }

                .down{
                    margin-top: 200px;
                    height: 200;
                    width: 200;
                }

                .clr{
                    clear: both;
                }

                 a{text-decoration-line: none;color: black;}
                 a:hover{color: blue;}
                 a:active{color: green;}

                 .copy{color: gray;position: fixed; top: 1700px; right: 10px}
                </style>
            </head>
        <body >
            <br><br><br><br>
            <center>
                <h1><strong>ROBOT ARM</strong></h1>
                <br><br><br>
                <div class="start" style="height: 100px; width: 100px">
                    <a href=\"?start\">
                        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="power-off" class="svg-inline--fa fa-power-off fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="green" d="M400 54.1c63 45 104 118.6 104 201.9 0 136.8-110.8 247.7-247.5 248C120 504.3 8.2 393 8 256.4 7.9 173.1 48.9 99.3 111.8 54.2c11.7-8.3 28-4.8 35 7.7L162.6 90c5.9 10.5 3.1 23.8-6.6 31-41.5 30.8-68 79.6-68 134.9-.1 92.3 74.5 168.1 168 168.1 91.6 0 168.6-74.2 168-169.1-.3-51.8-24.7-101.8-68.1-134-9.7-7.2-12.4-20.5-6.5-30.9l15.8-28.1c7-12.4 23.2-16.1 34.8-7.8zM296 264V24c0-13.3-10.7-24-24-24h-32c-13.3 0-24 10.7-24 24v240c0 13.3 10.7 24 24 24h32c13.3 0 24-10.7 24-24z"></path></svg>
                    </a>
                </div>
                <h1><strong>Reset Arms</strong></h1>
            </center>
            <br><br><br><br><br>
            


            <div class="main">
            <!-- ============================== servo1 ============================= --> 
            <div class="border">
                <center><h1><strong>Base Servo 1</strong></h1></center><br><br>
                <center>
                    <div >
                        <a href=\"?servo4open\">
                            <button class="grip">Open</button>
                        </a>
                    </div>
                </center>
                <br><br><br><br>
                <div class="left" style="height: 100px; width: 100px">
                    <a href=\"?servo1left\">
                        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-alt-circle-down" class="svg-inline--fa fa-arrow-alt-circle-down fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#f7b529" d="M504 256c0 137-111 248-248 248S8 393 8 256 119 8 256 8s248 111 248 248zM212 140v116h-70.9c-10.7 0-16.1 13-8.5 20.5l114.9 114.3c4.7 4.7 12.2 4.7 16.9 0l114.9-114.3c7.6-7.6 2.2-20.5-8.5-20.5H300V140c0-6.6-5.4-12-12-12h-64c-6.6 0-12 5.4-12 12z"></path></svg>
                    </a>
                </div>
                

                <div class="right" style="height: 100px; width: 100px">
                    <a href=\"?servo1right\">
                        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-alt-circle-down" class="svg-inline--fa fa-arrow-alt-circle-down fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#f7b529" d="M504 256c0 137-111 248-248 248S8 393 8 256 119 8 256 8s248 111 248 248zM212 140v116h-70.9c-10.7 0-16.1 13-8.5 20.5l114.9 114.3c4.7 4.7 12.2 4.7 16.9 0l114.9-114.3c7.6-7.6 2.2-20.5-8.5-20.5H300V140c0-6.6-5.4-12-12-12h-64c-6.6 0-12 5.4-12 12z"></path></svg>
                    </a>
                </div>

                <div class="clr"></div>
                
                <br><br><br><br>
                <center>
                    <div>
                        <a href=\"?servo4close\">
                        <button class="grip">Grip</button>
                    </a>
                    </div>
                </center>
            </div>



              <!-- ============================servo2=========================== -->
            <center>
                <div class="border">
                    <center><h1><strong>Servo 2</strong></h1></center><br>
                    <div class="up" style="height: 100px; width: 100px">
                        <a href=\"?servo2top\">
                            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-alt-circle-down" class="svg-inline--fa fa-arrow-alt-circle-down fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#ff3e30" d="M504 256c0 137-111 248-248 248S8 393 8 256 119 8 256 8s248 111 248 248zM212 140v116h-70.9c-10.7 0-16.1 13-8.5 20.5l114.9 114.3c4.7 4.7 12.2 4.7 16.9 0l114.9-114.3c7.6-7.6 2.2-20.5-8.5-20.5H300V140c0-6.6-5.4-12-12-12h-64c-6.6 0-12 5.4-12 12z"></path></svg>
                        </a>
                    </div>

                    <div class="down" style="height: 100px; width: 100px">
                            <a href=\"?servo2bottom\">
                            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-alt-circle-down" class="svg-inline--fa fa-arrow-alt-circle-down fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#ff3e30" d="M504 256c0 137-111 248-248 248S8 393 8 256 119 8 256 8s248 111 248 248zM212 140v116h-70.9c-10.7 0-16.1 13-8.5 20.5l114.9 114.3c4.7 4.7 12.2 4.7 16.9 0l114.9-114.3c7.6-7.6 2.2-20.5-8.5-20.5H300V140c0-6.6-5.4-12-12-12h-64c-6.6 0-12 5.4-12 12z"></path></svg></a>

                        </div>
                </div>
            </center>


             <!-- ============================servo3============================ -->
            <center>
                <div class="border">
                    <center><h1><strong>Servo 3</strong></h1></center><br>
                    <div class="up" style="height: 100px; width: 100px">
                        <a href=\"?servo3top\">
                            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-alt-circle-down" class="svg-inline--fa fa-arrow-alt-circle-down fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#176bef" d="M504 256c0 137-111 248-248 248S8 393 8 256 119 8 256 8s248 111 248 248zM212 140v116h-70.9c-10.7 0-16.1 13-8.5 20.5l114.9 114.3c4.7 4.7 12.2 4.7 16.9 0l114.9-114.3c7.6-7.6 2.2-20.5-8.5-20.5H300V140c0-6.6-5.4-12-12-12h-64c-6.6 0-12 5.4-12 12z"></path></svg>
                        </a>
                    </div>

                    <div class="down" style="height: 100px; width: 100px">
                            <a href=\"?servo3bottom\">
                            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-alt-circle-down" class="svg-inline--fa fa-arrow-alt-circle-down fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#176bef" d="M504 256c0 137-111 248-248 248S8 393 8 256 119 8 256 8s248 111 248 248zM212 140v116h-70.9c-10.7 0-16.1 13-8.5 20.5l114.9 114.3c4.7 4.7 12.2 4.7 16.9 0l114.9-114.3c7.6-7.6 2.2-20.5-8.5-20.5H300V140c0-6.6-5.4-12-12-12h-64c-6.6 0-12 5.4-12 12z"></path></svg></a>

                        </div>
                </div>
            </center>
            </div>
            
        </body>
        </html>
           """       
    return html



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    start_system = request.find('/?start')

    servo1right = request.find('/?servo1right')
    servo1left = request.find('/?servo1left')

    servo2top = request.find('/?servo2top')
    servo2buttom = request.find('/?servo2bottom')

    servo3top = request.find('/?servo3top')
    servo3buttom = request.find('/?servo3bottom')

    servo4open = request.find('/?servo4open')
    servo4close = request.find('/?servo4close')  


    if start_system == 6:
        on_start()

    

    if servo1right == 6:
        #decreasing
        left(servo_object1, servo1)

    if servo1left == 6:
        #increasing
        right(servo_object1, servo1)


    if servo2top == 6:
        #decreasing
        left(servo_object2, servo2)
        

    if servo2buttom == 6:
        #increasing
        right(servo_object2, servo2)
        

    if servo3top == 6:
        #increasing
        right(servo_object3, servo3)

    if servo3buttom == 6:
        #decreasing
        left(servo_object3, servo3)
      

    if servo4open == 6:
        #decreasing
        left(servo_object4, servo4)

    if servo4close == 6:
        #increasing
        right(servo_object4, servo4)




    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()



