from typing import Literal, Annotated

from pydantic import BaseModel, Discriminator, Field


class ObjA(BaseModel):
    obj_type: Literal["ObjA"] = "ObjA"

    a: int
    b: str


class ObjB(BaseModel):
    obj_type: Literal["ObjB"] = "ObjB"

    c: float
    d: str


class Wrapper(BaseModel):
    obj: ObjA | ObjB = Field(..., discriminator="obj_type")


def hello():
    o1 = Wrapper.model_validate({"obj": {"obj_type": "ObjA", "a": 1, "b": "2"}})
    o2 = Wrapper.model_validate({"obj": {"obj_type": "ObjB", "c": 1.0, "d": "2"}})

    print(o1)
    print(o2)
    assert isinstance(o1.obj, ObjA)
    assert isinstance(o2.obj, ObjB)


if __name__ == "__main__":
    hello()
