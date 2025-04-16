from abc import ABC, abstractmethod

class AdoptionEventDAO(ABC):
    @abstractmethod
    def get_all_events(self):
        pass

    @abstractmethod
    def register_participant(self, name, event_id, role):
        pass
