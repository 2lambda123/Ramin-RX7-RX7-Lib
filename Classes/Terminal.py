import os as _os
import subprocess as _subprocess


class Terminal:
    """
    Run Terminal Commands with Terminal functions
    (ALL FUNCTIONS ARE STATIC METHODS)
    """
    @staticmethod
    def run(command:str) -> None:
        '''
        Execute the command in a subshell
        Returns exit code
        (LIVE EXECUTION, OUTPUT WILL BE PRINTED)
        '''
        return _os.system(command)

    @staticmethod
    def getoutput(command:str) -> str:
        '''
        Return output of executing command in a shell
        (RETURN STR, RETURN AFTER EXECUTING CODE)
        '''
        return _subprocess.getoutput(command)
terminal = Terminal