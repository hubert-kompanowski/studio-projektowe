class TimetableEvent:
    def __init__(self, title, room, teacher, group, day, start, end, info, idx=None):
        self.idx = idx
        self.title = title
        self.room = room
        self.teacher = teacher
        self.group = group
        self.day = day
        self.start = start
        self.end = end
        self.info = info

    def __str__(self) -> str:
        return self.title + ", Sala: " + self.room + ", Prowadzący: " + self.teacher + ", Grupa: " + str(self.group) + ", Dzień tygodnia:" + str(
            self.day) + ", Czas rozpoczęcia/zakończenia: " + str(self.start) + " " + str(self.end)