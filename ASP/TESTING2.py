import cmd

class ComputerExpertSystem(cmd.Cmd):
    intro = "Welcome to the Computer Diagnostic Expert System. Type 'help' for a list of commands."
    prompt = ">> "

    def do_diagnose(self, arg):
        """Diagnose computer problems."""
        if "no power" in arg:
            print("Possible causes for no power:\n1. Dead battery\n2. Faulty power supply\n3. Loose power cable")
        elif "slow performance" in arg:
            print("Possible causes for slow performance:\n1. Insufficient RAM\n2. Malware\n3. Fragmented hard drive")
        else:
            print("Sorry, I cannot diagnose that problem.")

    def do_exit(self, arg):
        """Exit the expert system."""
        print("Exiting the Computer Diagnostic Expert System.")
        return True

if __name__ == '__main__':
    ComputerExpertSystem().cmdloop()