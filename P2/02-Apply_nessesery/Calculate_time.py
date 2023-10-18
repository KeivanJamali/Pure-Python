class Find_Time:
    def __init__(self, here_now:str, there_now:str, here_what:str) -> None:
        here_minit = self.origin_time_now(here_now)
        there_minit = self.porpuse_time_now(there_now)
        what_minit = self.porpuse_time(here_what)
        result_minit = here_minit + (what_minit - there_minit)
        hour, minit = self.minit_to_time(result_minit)
        self.time = str(hour)+":"+str(minit)
        
    
    def origin_time_now(self, clock_now:str) -> int:
        hour, minit = clock_now.split(":")
        return self.time_to_minit(int(hour), int(minit))
        
    def porpuse_time_now(self, clock_now:str) -> int:
        hour, minit = clock_now.split(":")
        return self.time_to_minit(int(hour), int(minit))
        
    def porpuse_time(self, clock_porpuse:str) -> int:
        hour, minit = clock_porpuse.split(":")
        return self.time_to_minit(int(hour), int(minit))
        
    @staticmethod
    def time_to_minit(hour:int, minit:int) -> int:
        return hour * 60 + minit
    
    @staticmethod
    def minit_to_time(minit:int) -> list:
        return divmod(minit, 60)