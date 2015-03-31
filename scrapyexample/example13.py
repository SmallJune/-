import re  
   
p = re.compile(r'\d+')  
for m in p.finditer('one111111two22232323three3four4'):
    print m.group(),  
   
### output ###  
# 1 2 3 4  