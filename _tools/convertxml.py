""" list generator for converting xml collections into array for storing directly in python script """

import os
from xml.dom import minidom

class Generator:    
    def __init__( self ):
        # create initial variables needed later
        self.xmlFilename = 'inputfile.xml'
        self.tools_path=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))

        # generate files
        self._generate_arrays_from_xml()

        # notify user
        print "Finished parsing the xml. Output saved as output.txt"
        
    def _generate_arrays_from_xml ( self ):
        
        print "Reading XML File....."
        
        try:               
            output_string = ''
            _path = self.tools_path + os.path.sep + self.xmlFilename
            document = minidom.parse(_path)

            # Usually you need to create a root element, for example, in Jen files, to wrap all the content in. Such as <bullshit> at top of file, with </bullshit> at the end of it.
            # Convert any & symbols to the word and. If you get an error, it tells you the line to fix.

            for parent in document.getElementsByTagName("dir"):

                # for each entry you want to pull, add 2 lines for it like below.
                # Example: <title>300 Collection</title> is pulled using the two title lines below.
                title = parent.getElementsByTagName("title")[0]
                title = self.getText(title.childNodes).replace("'", "\\'")
                tmdb = parent.getElementsByTagName("tmdb")[0]
                tmdb = self.getText(tmdb.childNodes)
                thumbnail = parent.getElementsByTagName("thumbnail")[0]
                thumbnail = self.getText(thumbnail.childNodes)
                output_string = output_string + "{ '" + title + "', '" + tmdb + "', '" + thumbnail + "' } ,\n"
        except Exception, e:
            # missing or poorly formatted xml
            print "What the fuck dude? %s" % ( e )

        # save file
        with open("output.txt","w") as f:
            f.write(output_string)

    def getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)

if ( __name__ == "__main__" ):
    # start
    Generator()