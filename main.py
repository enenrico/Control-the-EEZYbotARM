from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.properties  import NumericProperty
import RPi.GPIO as gpio
from gpiozero import LED
import time



servo1 = 14
gpio.setmode(gpio.BCM)
gpio.setup(servo1, gpio.OUT)

servo2 = 15
gpio.setmode(gpio.BCM)
gpio.setup(servo2, gpio.OUT)

servo3 = 16
gpio.setmode(gpio.BCM)
gpio.setup(servo3, gpio.OUT)

servo4 = 17
gpio.setmode(gpio.BCM)
gpio.setup(servo4, gpio.OUT)

p = gpio.PWM(servo1, 50)
aufzu = gpio.PWM(servo2, 50)
turn = gpio.PWM(servo3, 50)
frontBack = gpio.PWM(servo4, 50)

p.start(0)
aufzu.start(0)
turn.start(0)
frontBack.start(0)




class Controll(GridLayout):
    def __init__(self, **kwargs):

        super(Controll, self).__init__(**kwargs)
        self.inside = GridLayout()
        self.inside.cols = 8
        self.cols = 2
        self.add_widget(Label(text="Hoch" ))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.submit = Button(text="open",font_size=30)
	
	
	
        self.submit.bind(on_press=self.open)
        self.add_widget(self.submit)
	

        self.turn = Button(text="close", font_size=30, size_hint_x=None)
	
        self.turn.bind(on_press=self.close)
        self.add_widget(self.turn)
	
	
	self.brightnessControl = Slider(min = 0, max = 15)
        self.add_widget(Label(text="high/down"))
        self.add_widget(self.brightnessControl)        
	self.add_widget(Label(text ='Slider Value')) 
        self.brightnessValue = Label(text ='0') 
        self.add_widget(self.brightnessValue)
        self.brightnessControl.bind(value = self.highDown)
	
	self.pliersControll = Slider(min = 0, max = maxi)
	self.add_widget(Label(text="auf/zu"))
	self.add_widget(self.pliersControll)
	self.add_widget(Label(text="Slider Value"))
	
	self.pliersControllValue = Label(text="0")
	
	self.add_widget(self.pliersControllValue)
	self.pliersControll.bind(value = self.Zu)
	
	self.turnaround = Slider(min = 0, max = 20)
	self.add_widget(Label(text="turn around"))
	self.add_widget(self.turnaround)
	self.add_widget(Label(text="Slider Value"))
	self.turnaroundValue = Label(text="0")
	self.add_widget(self.turnaroundValue)
	self.turnaround.bind(value = self.Turn)
	
	self.frontback = Slider (min = 0, max = 20)
	self.add_widget(Label(text="front and Back"))
	self.add_widget(self.frontback)
	self.add_widget(Label(text="Slider Value"))
	self.frontbackValue = Label(text="0")
	self.add_widget(self.frontbackValue)
	self.frontback.bind(value =self.FrontAndBack)
	
	'''self.resett = Button(text="Reset", font_size = 30)
	self.resett.bind(on_press=self.reset)
	
	self.add_widget(self.resett)'''
	
	
    def Turn(self, instance, brightness):
	    
	    turn.start(0)
	    value = brightness
	    turn.ChangeDutyCycle(value)
	    self.turnaroundValue.text = "% d"% brightness
	
    def highDown(self, instance, brightness):
	    
	    p.start(0)
	    value = brightness
	    p.ChangeDutyCycle(value)
	    self.brightnessValue.text = "% d"% brightness
	    	    
    def Zu(self, instance, brightness):
	    aufzu.start(0)
	    value = brightness
	    aufzu.ChangeDutyCycle(value)
	    self.pliersControllValue.text = "% d"% brightness
	    #if self.close ==  True:
		#    aufzu.ChangeDutyCycle(0)
	    
	     
		    
	     
    def FrontAndBack(self, instance, brightness):
	    frontBack.start(0)
	    value = brightness
	    frontBack.ChangeDutyCycle(value)
	    self.frontbackValue.text = "% d"% brightness
		 
		




    def close(self, instance):
	aufzu.start(0)
	aufzu.ChangeDutyCycle(1)
	time.sleep(1)
	pliersControllValue =0
	

    def open(self, instance):
	aufzu.start(8)
	aufzu.ChangeDutyCycle(8)
		

    def reset(self, instance):
	p.start(0)
	p.ChangeDutyCycle(1)
	time.sleep(1)
	
	 
	aufzu.start(0)
	aufzu.ChangeDutyCycle(1)
	 
	time.sleep(1)
	
	turn.start(0)
	turn.ChangeDutyCycle(1)
	
	
	

class MyApp(App):
    def build(self):
        return Controll()

if __name__ == "__main__":
        MyApp().run()
