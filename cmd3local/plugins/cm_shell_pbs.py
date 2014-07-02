from cmd3.shell import function_command
from cloudmesh_pbs.submit import shell_command_pbs

class cm_shell_pbs:
    
    def activate_cm_shell_pbs(self):
        self.register_command_topic('cloud','pbs')
        pass

    @function_command(shell_command_pbs)
    def do_pbs(self, args, arguments):
        shell_command_pbs(arguments)
        pass

#    def __pbs__(self):
#        pass
#
#if __name__ == '__main__':
#    command = cm_pbs()
#    command.do_pbs("")
