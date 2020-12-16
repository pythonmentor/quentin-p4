class Tournament:
    
    def __init__(self):
        self.name = None
        self.location = None
        self.start_date = None
        self.end_date = None
        self.rounds_number = 4
        self.tours = None
        self.players = None
        self.times_control = None
        self.description = None
    
    def set_name(self, name):
        self.name = name
        return

    def set_location(self, location):
        self.location = location
        return
    
    def set_start_date(self, start_date):
        self.start_date = start_date
        return
    
    def set_end_date(self, end_date):
        self.end_date = end_date
        return
    
    def set_tours(self, tours):
        self.tours = tours
        return
    
    def set_players(self, players_ids):
        self.players = players_ids
        return
    
    def set_time_control(self, times_control):
        self.time_control = times_control
        return
    
    def set_description(self, description):
        self.description = description
        return