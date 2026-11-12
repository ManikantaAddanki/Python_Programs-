# import logging

# logging.basicConfig(filename='student.log',
#                     filemode='a',
#                     level=logging.INFO,
#                     format="%(asctime)s / %(levelname)s / %(message)s")

# logging.debug("------debug-----")
# logging.info("------info-----")
# logging.error("------error-----")
# logging.critical("------critical-----")
# logging.warning("------warning-----")



""
# import logging
# import time



# baterry = 100

# while baterry>20:
#     baterry-=1
#     time.sleep(0.5)
#     print("Baterry level = ",baterry)
    
# logging.basicConfig(filename="b.log",filemode='w',
#                     level=logging.INFO,
#                     format="%(asctime)s / %(levelname)s / %(message)s")
# logging.warning("low baterry")
    
    
    
" "


import logging

logging.basicConfig(filename='reg.log',filemode='a',level=logging.INFO,format="(%(asctime)s / %(levelname)s / %(message)s)")

def registration():
    global username,password
    username = 'ajay'
    password = 'ajay123'
    con_password = 'ajay123'
    
    if password==con_password:
        logging.info('Registartion successful')
    else:
        logging.warning("invalid password")
        
        
def login():
    l_user = 'ajay1'
    l_password = 'ajay123'
    
    if l_user == username and l_password==password:
        logging.info('login successful')
    else:
        logging.warning('invalid password / username')
        
        
registration()
login()