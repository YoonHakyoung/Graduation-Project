import re
from uuid import getnode
print("MAC : ",":".join(re.findall('..','%012x'%getnode())))