class AlarmClock:
    def __init__(self):
        self.current_time = "00:00"
        self.is_on = False
        self.alarm_time = ""

    def set_current_time(self):
        self.current_time = input("Enter current time: ")
        print(self.current_time)
    
    def toggle_alarm_on_or_off(self):
        if self.is_on == False:
            self.is_on = True
        else:
            self.is_on = False

    def set_alarm_time(self):
        self.alarm_time = input("Enter alarm time: ")
        print(self.alarm_time)
