start_time = [0,0]
def initialize():
    global hedons
    global health
    global duration_total
    global duration_run
    global duration_textbook
    global duration_rest
    global start_time
    global star
    global count
    global duration_total2
    global x
    global start_time
    start_time = [0,0]
    x = 0
    duration_total2 = 0
    hedons = 0
    health = 0
    duration_total = 0
    duration_run = 0
    duration_textbook = 0
    duration_rest = 0
    star = 0
    count = 0

def get_cur_hedons():
    return hedons

def get_cur_health():
    return health

def offer_star(activity):
    return star

def perform_activity(activity,duration):
    global hedons
    global health
    global duration_total
    global duration_run
    global duration_textbook
    global duration_rest
    global star
    global duration_total2

    start_time[0]+=duration
    start_time[1]+=duration


    if star == 'running' or star == 'textbooks':
        if duration<= 10:
            hedons+=duration*3
        if duration >10:
            hedons+=10*3
        star = 0

    if activity == 'running' and duration_rest < 120 and duration_total2!=duration_rest:
       if duration<=10:
           hedons+= duration*-2

       if duration > 10:
           hedons += duration*-2

    if activity == 'textbooks' and duration_rest < 120 and duration_total2 != duration_rest:
        if duration<=10:
            hedons += duration*-2

        if duration<10:
            hedons += duration*-2

    if activity == 'running' and (duration_rest >= 120 or duration_total2 == duration_rest):
        if duration_run + duration <= 10:
            hedons+= duration*2

        elif duration_run >= 10:
            hedons+=duration*-2

        else:                        # elif (duration_run + duration) >10:
            hedons+= (10 - duration_run)*2 + (duration - (10 - duration_run))*-2

    if activity == 'textbooks' and (duration_rest>=120 or duration_total2 == duration_rest):
        if duration_textbook+duration <= 20:
            hedons+= duration

        if duration_textbook >= 20:
            hedons += duration*-1

        else:                            # elif duration_textbook + duration > 20:
            hedons+= (20 - duration_textbook)*1 + (duration - (20 - duration_textbook))*-1

    if activity == 'resting':
        duration_rest+= duration
        duration_run = 0
        duration_textbook = 0
        duration_total2+=duration
        star = 0

    if activity == 'textbooks':
        health+= duration*2
        duration_textbook += duration
        duration_run = 0
        duration_rest = 0
        duration_total2+=duration

        star = 0

    if activity == 'running' and (duration_run + duration) <= 180:
        health += (duration*3)
        duration_run+= duration
        duration_rest = 0
        duration_textbook = 0
        duration_total2+=duration

        star = 0

    elif activity == 'running' and duration_run >= 180:
        health += duration
        duration_run+= duration
        duration_rest = 0
        duration_textbook = 0
        duration_total2+=duration

        star = 0

    elif activity == 'running' and (duration_run + duration) > 180:
        health += (180 - duration_run)*3 + (duration - (180- duration_run))
        duration_run+= duration
        duration_rest = 0
        duration_textbook = 0
        duration_total2+=duration
        star = 0

def offer_star(activity):
    global star
    global count
    global start_time
    global x
    if x == 'no':
        star = ''
        return None

    if start_time[0] >= 121 or start_time[1] >= 121:
        for i in range(0,2):
            if start_time[i] > 120:
                start_time[i] = 0
    else:
        x ='no'

    if activity == 'running' and x!='no':
        star = 'running'

    if activity == 'textbooks' and x!='no':
        star = 'textbooks'

def star_can_be_taken(activity):
    if x == 'no':
        return False
    else:
        if activity == star:
            return True
    return False






def most_fun_activity_minute():
    global star
    if star == 'running':
        return 'running'
    elif star == 'textbooks':
        return 'textbooks'

    elif duration_rest < 120:
        return 'resting'

    elif duration_run <=10:
        return 'running'

    elif duration_textbook<=20:
        return 'textbooks'

    else:
        return 'resting'

if __name__ == '__main__':
  initialize()







