# template for "Stopwatch: The Game"
import random
import simplegui
# define global variables
show = '0:00.0'
tenths = 0
show2 = '0/0'
stop_count = 0
correct_hit = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global show, show2
    a = tenths%10
    b = (tenths/10)%60
    c = tenths/600
    show = str(c) + ':' + str(b) + '.' + str(a)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()


def stop():
    global show2, correct_hit, stop_count
    stop_count += 1
    if tenths%10 == 0:
        correct_hit +=1
    show2 = str(correct_hit) + '/' + str(stop_count)
    timer.stop()

def reset():
    global show, tenths, correct_hit, stop_count, show2
    show = '0:00.0'
    tenths = 0
    correct_hit, stop_count = -1, -1
    show2 = '0/0'
    stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths
    tenths += 1
    format()

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(show, (80, 170), 50, 'White')
    canvas.draw_text(show2, (240, 25), 25, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 300)


# register event handlers
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
# Please remember to review the grading rubric
