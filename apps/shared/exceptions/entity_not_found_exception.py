class EntityNotFoundException(Exception):
    def __init__(self, entity_name: str):
        self.entity_name = entity_name
        self.message = f"{entity_name} not found"
        super().__init__(self.message)
