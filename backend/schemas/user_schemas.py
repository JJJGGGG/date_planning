from pydantic import BaseModel, EmailStr, Field, field_validator


class CreateUser(BaseModel):
    name: str = Field(min_length=1, max_length=128)
    email: EmailStr
    password: str = Field(
        min_length=8,
    )

    @field_validator("password")
    def validate_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain an uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain a lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain a digit")
        if not any(c in "#?!@$%^&*-" for c in v):
            raise ValueError("Password must contain a special character"
                             "(#?!@$%^&*-)")
        return v


class LoginUser(BaseModel):
    email: EmailStr
    password: str = Field()
