import ccm      
log=ccm.log(html=True)   

from ccm.lib.actr import *  

class MyEnvironment(ccm.Model):
    small=ccm.Model(size=1,location='left', state='clear')
    medium=ccm.Model(size=2,location='left', state='not_clear')
    big=ccm.Model(size=3,location='left', state='not_clear')

class MotorModule(ccm.Model):
    def small_right(self):                    
        print "moving small right"
        self.parent.parent.small.location='right' 
        self.parent.parent.medium.state='clear' 
    
    def medium_middle(self):           
        print "moving medium middle"
        self.parent.parent.medium.location='middle' 
        self.parent.parent.big.state='clear' 

    def small_middle(self):           
        print "moving small middle"
        self.parent.parent.small.location='middle' 
        self.parent.parent.medium.state='not_clear' 

    def big_right(self):           
        print "moving big right"
        self.parent.parent.big.location='right' 

    def small_left(self):           
        print "moving small left"
        self.parent.parent.small.location='left' 
        self.parent.parent.medium.state='clear' 

    def medium_right(self):
        print "moving medium right"
        self.parent.parent.medium.location='right' 
        self.parent.parent.big.state='not_clear' 

    def final_move(self):       
        print "moving small right"
        self.parent.parent.small.location='right' 
        self.parent.parent.medium.state='not_clear' 



class MyAgent(ACTR):
    focus=Buffer()
    DMbuffer=Buffer()               
    DM=Memory(DMbuffer) 
    motor=MotorModule()

    def init():
        focus.set('small right')

    def first_move(focus='small right', small='location:!right state:clear'):
        print "I have a small disk"     
        focus.set('medium middle')
        motor.small_right()

    def second_move(focus='medium middle', medium='location:!middle state:clear'):
        print "I have a medium disk"     
        focus.set('small middle')
        motor.medium_middle()

    def third_move(focus='small middle', small='location:!middle state:clear'):
        print "I have a small disk"     
        focus.set('big right')
        motor.small_middle()

    def fourth_move(focus='big right', big='location:!right state:clear'):
        print "I have a big disk"     
        focus.set('small left')
        motor.big_right()

    def fifth_move(focus='small left', small='location:!left state:clear'):
        print "I have a small disk"     
        focus.set('medium right')
        motor.small_left()

    def sixth_move(focus='medium right', medium='location:!right state:clear'):
        print "I have a medium disk"     
        focus.set('final move')
        motor.medium_right()

    def final_move(focus='final move', small='location:!right state:clear'):
        print "I have a small disk"     
        focus.set('stop')
        motor.final_move()

    def stop_production(focus='stop', small='location:right'): 
        print "I have made a ham and cheese sandwich"
        self.stop() 
    

ag = MyAgent()
envi=MyEnvironment()
envi.agent=ag
ccm.log_everything(envi)

envi.run() 
ccm.finished() 