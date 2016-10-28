class TreeNode:		
	def __init__(self, data):
		self.data = data
		self.children = []

x = TreeNode("woff")
print(x.data)

def solution (X):
	indent = 0
	index_of_root = -1
	lines = X.split(str="\n")
	roots = []
	for line in lines:
		if line[indent] != " ":
			indent += 1
		if indent == 0
			roots[index] = TreeNode(len(line))
			index_of_root += 1
		else:
			if line[indent] != " ":
				#
				
			else:
				#		


def createTree(parent, lines, index, indent):
	while index < lines.size()
		if !dir
			#check to make sure in same directory
			if samedirectory
				parent.children.append(lines[index])
				index++
			else
				return index
		else dir
			x = TreeNode(dirname)
			index = createTree(x, lines, index, indent + 1)
			parent.children.append(x)
			
'''

def create_tree(dict):
	x = NodeTree()
	for a in d.keys():
		if type(
		
		

def solution(X, indent)
	#call solution on each new directory
	#find the longest string at that indentation row and return its length
	lines = X.split(str="\n")
	
	for line in lines
		if 
	
	indent = 0
	dirlevel = []
	
	for line in lines:
		if line[indent] == " ":
			indent += 1
		 
	
	for line in X
		if line[X + indent] == " ":
			solution(line, indent+1)
	
def dirDive(indent, index, lines)
	.


	return index

	dir = []
	dir.append(line)
	if line[indent] != ' ':
		#it's at same level
		dir.append(line)
	if indent != 0:
		if line[indent - 1] != ' ':
			#that level is finished
			break
	

#while index < lines.size()
#if indent is == to current directory level
x.append(len(line))
#if not
x.append(size(line))

x.append(size(line,    '''