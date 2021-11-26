import cgi, cgitb
cgitb.enable()

data = cgi.FieldStorage()
output = data.getvalue("user_input")
print(output)
