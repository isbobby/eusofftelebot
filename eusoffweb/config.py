import os

#config database uri here
#it is ignored during commits, change gitignore to enable commits

class Config:
    # SECRET_KEY = 'c9970460fc2c3ad324add53c94e3w3e4'
    SQLALCHEMY_DATABASE_URI = 'postgres://bobby:zmq,bs2008@localhost:5432/eusoffweb'
    #heroku uri
    #SQLALCHEMY_DATABASE_URI = 'postgres://cwlecfheoxozqr:8f40918c5884a2e2f701ae1ea39e15e6ee0bee561f2373a0faa3318c05081c51@ec2-54-235-89-123.compute-1.amazonaws.com:5432/d11ekc90u8on7p'
    
    USER_APP_NAME = "Eusoff Web"   # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
