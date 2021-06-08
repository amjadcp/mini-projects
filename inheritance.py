class programm:
    def __init__(self, date = 0, time = 00, place = ""):
        self.date = date
        self.time = time
        self.place = place

    def _print(self):
        print(f'''
        
        Date : {self.date}
        Time : {self.time}
        Place: {self.place}
-----------------------------------------------------
        ''')

class song(programm):
    def __init__(self, judge, date, time, place):
        super().__init__(date, time, place)
        self.judge = judge
    
    def _print(self):
        print(f'''
        Judge : {self.judge}''')
        return super()._print()

class long_jump(song):
    def __init__(self, coach, judge, date, time, place):
        super().__init__(judge, date, time, place)
        self.coach = coach

    def _print(self):
        print(f'''
        Coach : {self.coach}
        Judge : {self.judge}''')
        return programm._print(self)

x = programm(1, 10, "kinassery")
y = song("jack", 2, 20, "kinassery")
z = long_jump("john", "jack", 3, 30, "kinassery")

x._print()
y._print()
z._print()
     