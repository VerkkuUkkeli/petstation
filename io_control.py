import RPi.GPIO as io
import time
import threading

class IOController(threading.Thread):
    def __init__(self):
        print("Starting IO control thread")
        threading.Thread.__init__(self)

        # setup GPIO
        io.cleanup()                # reset io pins
        io.setmode(io.BCM)          # set pin numbering

        self.yaw_state = 0.0        # which way to move
        self.pitch_state = 0.0      # which way to move
        self.servo_speed = 3.0
        self.yaw    = 90.0
        self.pitch  = 90.0

        self.laser_on = False

        """ start pin setup """        
        # laser turret
        self.yaw_pin = 22
        self.pitch_pin = 27
        self.laser_pin = 17
        io.setup(self.yaw_pin, io.OUT)
        io.setup(self.pitch_pin, io.OUT)
        io.setup(self.laser_pin, io.OUT)
        
        # buttons
        self.button_pins = [16, 20, 21]
        self.button_led_pins = [26, 19, 13]
        
        # lists for keeping track of the button states,
        # old state kept for detecting rising edges
        self.button_old_states = [0, 0, 0]
        self.button_states = [0, 0, 0]
        
        # list of button handlers, when a button is pressed
        # the corresponding handler function is called
        self.button_handlers = \
            [self.led_button_handler,
             self.led_button_handler,
             self.led_button_handler]
        
        # set pin modes
        for pin in self.button_pins:
            io.setup(pin, io.IN)
        for pin in self.button_led_pins:
            io.setup(pin, io.OUT)
        """ stop pin setup """


        # setup pwm
        self.yaw_servo = io.PWM(self.yaw_pin, 50)
        self.pitch_servo = io.PWM(self.pitch_pin, 50)
        self.yaw_servo.start(7.5)
        self.pitch_servo.start(7.5)

    # poll button GPIO values and update button state variables
    def poll_buttons(self):
        for i in range(len(self.button_pins)):
            self.button_old_states[i] = self.button_states[i]  # store old value
            self.button_states[i] = io.input(self.button_pins[i])  # update current value

    def handle_buttons(self):
        for i in range(len(self.button_pins)):
            if self.button_states[i] == 1 and self.button_old_states[i] == 0: # rising edge
                self.button_handlers[i](i)  # call handler associated with the button with an argument i
            if self.button_states[i] == 0 and self.button_old_states[i] == 1: # falling edge
                self.button_handlers[i](i)  # call handler associated with the button with an argument i

    # run thread
    def run(self):
        while True:
            # main loop
            self.update_servo_angles()
            self.update_laser_state()
            
            self.poll_buttons()
            self.handle_buttons()
            
            time.sleep(1/60)        # update at 60 Hz

    # turn on led when button is pressed
    def led_button_handler(self, number):
        print("Button {:d} pressed!".format(number))
        print("Setting pin {:d} as {:d}".format(self.button_led_pins[number], self.button_states[number]))
        io.output(self.button_led_pins[number], self.button_states[number])

    # print which button was pressed
    def default_button_handler(self, number):
        print("Button {:d} was pressed.".format(number))

    def set_laser_controls(self, yaw, pitch):
        if yaw is not None:
            self.yaw_state = yaw
        if pitch is not None:
            self.pitch_state = pitch

    def set_laser_state(self, state):
        self.laser_on = state

    def update_laser_state(self):
        if self.laser_on is True:
            io.output(self.laser_pin, io.HIGH)
        else:
            io.output(self.laser_pin, io.LOW)

    # change laser yaw angle by value
    def update_servo_angles(self):
        self.yaw += self.yaw_state*self.servo_speed
        self.pitch += self.pitch_state*self.servo_speed

        if self.yaw < 0:
            self.yaw = 0
        if self.yaw > 180:
            self.yaw = 180
        if self.pitch < 0:
            self.pitch = 0
        if self.pitch > 180:
            self.pitch = 180

        # map from angle to range [2.5, 12.5]
        yaw_duty = self.yaw/180*10+2.5
        pitch_duty = self.pitch/180*10+2.5

        self.yaw_servo.ChangeDutyCycle(yaw_duty)
        self.pitch_servo.ChangeDutyCycle(pitch_duty)


