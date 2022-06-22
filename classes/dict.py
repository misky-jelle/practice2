data={1:"Misky",2:"Kiran",4:"Kiran"}
# when i want to add you say    data["Muna"]="Java"
# dete you say del data["Misky"]
# You can get a key or value by writting their index eg data[1] or data.get(1)

monthConversions={
    "jan":"january",
    "feb":"february",
    "mar":"march",
    "apr":"april",
    "may":"may",
}
# print(monthConversions("jan"))
print(monthConversions["apr"])
print(monthConversions.get("jan"))