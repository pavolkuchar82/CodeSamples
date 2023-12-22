'''ConnectHandler is how we get connected to device and issue commands'''
from netmiko import ConnectHandler

# from dotenv import load_dotenv
# load_dotenv()
router = {
    "host": "10.10.20.48",
    "port": 22,
    "username": "developer",
    "password": "C1sco12345",
    "device_type": "cisco_ios"
}

'''config is a variable that contains config commands once in config mode to create
 loopback interface. we no need to type 'config', beacuse netmiko handle this for us as '''
configs = ['int loopback101', 'ip address 10.99.98.1 255.255.255.0', 'no shut']

'''building the request by trying to connect to device by instantiating Connect Handler class.
We passing all details about the router by unpacking it as dictionary. Connection will be 
establish and stored as variable c. With that c connection in place, we specify the enable 
command to make sure we are in priviledge mode. Once in priviledge mode i want to issue a show
command, therefore i will use send_command method and specifying command in (). This will 
run the show command on device and store the response to variable 'response'. afterwards will
disconnect from device. If there are any exception I want to catch it as variable 'ex' and
print them on the terminal. Lastly i want to print that response to terminal as well'''

try:
    c = ConnectHandler(**router)
    c.enable()
    ''' send_config_set method enters into the config mode and is passing the 
    commnads from variable configs into session '''
    c.send_config_set(configs)
    '''we have an ability to parse cli output into the structured json in case we want to
     interact with these data programatically using tool called textfsm which comes as a part 
     of netmiko installation. after that we check if the loopback is added'''
    # response = c.send_command("show ip int brief", use_textfsm=True)
    response=c.send_command("show ip interface brief")
    c.disconnect()
except Exception as ex:
    print(ex)
else:
    print(response)
