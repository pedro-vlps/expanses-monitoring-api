from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "email": "teste@email.com",
                "password": "senha123"
            }
        }
