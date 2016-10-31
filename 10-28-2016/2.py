class TreeNode:		
	def __init__(self, data):
		self.data = data
		self.children = []
		
	def shade(self):
		for child in children:
			print child.data

x = TreeNode("woff")
print(x.data)

'''def solution (X):
	indent = 0
	index_of_root = 0
	index = 0
	lines = X.split(str="\n")
	roots = []
	for line in lines:
		#if line[indent] == " ":
		#	indent += 1
		# if a root dir
		if indent == 0
			roots[index_of_root] = TreeNode(len(line))
			index_of_root += 1
		else:
			if line[indent] != " ":
				#
			else:
				#
		index += 1
'''

def createTree(parent, lines, index, indent):
	while index < len(lines):
		line = lines[index]
		#dir = "." not in line
		#if !dir:
		if "." not in line:
			#check to make sure in same directory
			samedirectory = indent == line.count(' ')
			if samedirectory:
				parent.children.append(line)
				index += 1
			else:
				#done adding children to tree
				return index
		#this line IS a directory
		else:
			x = TreeNode(dirname)
			print("WOO RECURSION")
			index = createTree(x, lines, index, indent + 1)
			parent.children.append(x)
			
with open("2input.txt") as f:
	lines = f.readlines()

print lines
rootNode = TreeNode("root")
createTree(rootNode, lines, 0, 0)
for child in rootNode.children:
	print child
			
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