#use with MT-PowerDrumKit

def on_pulse():
   step = bespoke.get_step(16)
   if step % 4 == 0 or (step % 8 == 6 and random.random() < .2):
      this.play_note(36, 127, 1.0/16)
   if step % 4 == 2:
      this.play_note(42, 100, 1.0/16)
   if step % 12 == 2 or step % 11 == 9:
      this.play_note(40, 40, 1.0/16)
   this.play_note(44, get_hat_velocity(), 1.0/16)
      
def get_hat_velocity():
   velocities = [80,40,50,40,120]
   ret = velocities[(bespoke.get_step(16) % 32) % len(velocities)]
   this.output(str(ret))
   return ret 