from netmiko import ConnectHandler


#Create SSH connection with R1 using ConnectHandler()
R1_CONN = ConnectHandler(
    host = "10.255.1.101",
    username = "admin",
    password = "cisco",
    device_type = "cisco_ios",
)
print(R1_CONN)

print("SSH Connection with R1 Established Successfully!")

 