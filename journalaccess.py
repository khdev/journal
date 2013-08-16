#!/usr/bin/python2.7
#Viewer:
filename = 'WASHME.DAT'
fh = open(filename,'r')
el = "\n"
tab = "\t"
marker="%%\n"
fhlen = len(fh.read())
fh.seek(0)
def jump_next_entry(loc=fh.tell()):
	iloc = loc
	fh.seek(loc)
	for j in range(iloc,fhlen):
		fh.seek(j)
		if fh.read(2) == '%%':
			loc = j
			break
	fh.seek(iloc)
	return loc
def skip(interv = 1):
	fh.seek(fh.tell()+interv)
def trimendl(toolong):
	nottoolong = ''
	for i in range(len(toolong)-1):
		nottoolong += toolong[i]
	return nottoolong

def disp_next_entry(offset=0):
	fh.seek(jump_next_entry(fh.tell())+len(marker))
	timestamp = trimendl(fh.readline())
	sero = fh.read(1);skip()
	dopa = fh.read(1);skip()
	norep = fh.read(1);skip()
	jbo = trimendl(fh.readline())
	title = trimendl(fh.readline())
	body = ''
	while fhlen > fh.tell():
		buff = fh.readline()
		if trimendl(buff) == '%%': break
		else: body += buff
	body = trimendl(body)
	print timestamp,el,str(sero),str(dopa),str(norep),tab,jbo,el,title,el,body,el
	skip(-len(marker))
disp_next_entry()
disp_next_entry()
disp_next_entry()
fh.close()
