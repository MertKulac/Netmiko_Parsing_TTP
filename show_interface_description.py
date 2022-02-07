ciscoasr9k = {
    "host" : "192.168.10.2",
    "username" :"username",
    "password" :"password",
    "port" : 22,
    "device_type" : "cisco_xr",
 }

con = ConnectHandler(**ciscoasr9k)

data_to_parse = con.send_command_timing('show interface description')

ttp_template ="""
<group name="INTERFACES" method="table">
Interface          Status      Protocol    Description {{ignore}}
{{Interface}} {{Status}} {{Protocol}} {{ Description | re("") | re(".*")}} 
</group>
"""

parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]

#str to list **convert with json.loads

result = json.loads(results)

for i in result[0]["INTERFACES"]:
    print(f'Description: {i["Description"]},Interface: {i["Interface"]}, Status:{i["Status"]}')
