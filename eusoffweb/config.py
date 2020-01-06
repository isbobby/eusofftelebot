import os

#config database uri here
class Config:
    SECRET_KEY = 'c9970460fc2c3ad324add53c94e3w3e4'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@localhost:5432/eusoffweb'
    USER_APP_NAME = "Eusoff Web"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
