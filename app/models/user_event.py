from pydantic import BaseModel

class UserEvent(BaseModel):
    eventType: str
    email: str