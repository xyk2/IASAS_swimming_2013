import xml.dom.minidom

data = [0] * 300 #memory buffer

def prettifyXML(filename):
    xml_pretty = xml.dom.minidom.parse(filename)
    new_string=''
    for line in xml_pretty.toprettyxml().split('\n'):
            if line.strip():
                    new_string += line + '\n'
    file = open(filename, 'w')
    file.write(new_string)
    file.close()
    
class xmlrw(object):
    def __init__(self, filename):
        self.filename = filename
        
    def get_tag(self, tag, index):
        file = open(self.filename, 'r')
        data = file.readlines()
        file.close()
        for line in data:
            if(line.find(tag)!=-1 and index==0):
                return line.lstrip().lstrip(tag).split('<')[0]
            elif(line.find(tag)!=-1):
                index=index-1;
    
    def rewrite_tag(self, tag, index, text):
        temp=0
        file = open(self.filename, 'r')
        data = file.readlines()
        file.close()
        file = open(self.filename, 'w')
        for line in data:
            if(line.find(tag)== -1):
                file.write(line)
            elif(line.find(tag)!= -1 and index==0 and temp==0):
                file.write(tag+text+tag[:1] + '/' + tag[1:]+'\n')
                temp=1
            elif(line.find(tag)!= -1):
                file.write(line)
                index=index-1
        file.close()
        prettifyXML(self.filename)
