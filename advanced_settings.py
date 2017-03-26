import cgi
import NameSuggestions

name_l = ["key", "key1", "key2", "key3", "key4", "key5", "key6", "key7", "key8"]
i = 0
p_list = []
s_list = []
form = cgi.fieldStorage()

while i < 8:
    input_text = form.getfirst(name_l[i], "")
    if input_text != "":
        p_list = p_list.append(input_text)
    i = i + 1

while i < p_list.len():
    ss_list = NameSuggestions.ListOfElements(p_list[i])
    s_list = s_list.append(ss_list)
    i = i + 1

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
#print "<p>%s</p>" % form  #uncomment this line if you want
#to see what does form hashes look like
print("<p>%s</p>" % s_list)
print("</body>")
print("</html>")



