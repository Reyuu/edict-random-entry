import sys
argname = ""
class ArgParserX(object):
    """Simple sys.argv parser"""
    def __init__(self):
        global HELP
        HELP = ["Help of the program\n","--help shows this help\n",]
    def take_args(self):
        self.tuple_args = sys.argv[1:]
    def program_def(self, defpro):
        global DEFPRO
        HELP.remove("Help of the program\n")
        DEFPRO = defpro
        HELP.insert(0, DEFPRO+" "+sys.argv[0]+" [option]"+'\n')
    def object_arg(self, argname, helparg=argname+"\'s help", flag=0):
        HELP.append(argname+' '+helparg+"\n")
        if argname in self.tuple_args:
            if flag == 0:
                index_arg = self.tuple_args.index(argname)
                argument = self.tuple_args[index_arg+1]
                return argument
            elif flag == 1:
                index_arg = self.tuple_args.index(argname)
                argument = True
                if bool(index_arg):
                    return argument
                elif bool(index_arg) == False:
                    return False
        elif argname not in self.tuple_args:
            return 0
    def pos_arg(self, argname, pos="start"):
        HELP.insert(0, DEFPRO+" "+sys.argv[0]+" ["+argname+"] [option]"+'\n')
        if pos == 'start':
            start_arg = sys.argv[1]
            if "-" in list(start_arg):
                if "--help" in list(start_arg):
                    print "Not vailid positional argument! Checkout \'"+sys.argv[0]+" --help\'. Terminating now."
                    sys.exit()
                else:
                    return 0
            else:
                return start_arg
        elif pos == 'end':
            x = sys.argv[1:]
            x = len(x)
            end_arg = sys.argv[x]
            if "-" in list(end_arg):
                if "--help" in list(end_arg):
                    print "Not vailid positional argument! Checkout \'"+sys.argv[0]+" --help\'. Terminating now."
                    sys.exit()
                else:
                    return 0
            else:
                return end_arg
        else:
            return 0
    def help_arg(self, argname="--help"):
        if argname in self.tuple_args:
            x2 = ' '.join(HELP)
            print x2
            sys.exit()
        else:
            pass
