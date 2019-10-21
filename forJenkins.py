import re,sys

branch = sys.argv[1]
result = re.split(r'feature/', branch)
branch = re.split(r'\s|-', result[1])

namespace = 'project-feature' + '-' + branch[0] + '-' + branch[1]
print namespace.lower()
