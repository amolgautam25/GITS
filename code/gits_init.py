from subprocess import Popen, PIPE

def gits_init(args):
    
    try:
        process_commands = ["git", "init"]

        if args.bare is not False and args.bare is not None:
            process_commands.append("--bare")
        elif args.template is not None:
            process_commands.append("--template")
            process_commands.append(args.template)

        process = Popen(process_commands, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

    except Exception as e:
        print("ERROR: gits init command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
