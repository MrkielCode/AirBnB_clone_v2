#!/usr/bin/python3
import models
from os import getenv
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class that inherit the BaseModel
    and the Base ORM """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan'
            )
    else:
        @property
        def cities(self):
            """ return cities if not from DB"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
