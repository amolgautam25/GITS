from subprocess import Popen, PIPE

def gits_init(args):
   """
   This function allows user to transform current
   directory into a Git repository.
   There are three ways to do it.
   1) Simple git init
        gits init
   2) Initialize with a bare flag
        gits init --bare
   3) Initialize using a preexisting template
        gits init --template path-to-template
   """ 
   try:
      if args.clone_url:
         process_commands = ["git","clone", args.clone_url]
      else:
         process_commands = ["git", "init"]
         if args.bare is not False and args.bare is not None:
            process_commands.append("--bare")
         elif args.template is not None:
            process_commands.append("--template")
            process_commands.append(args.template)
      
      process = Popen(process_commands, stdout=PIPE, stderr=PIPE)
      stdout, stderr = process.communicate()
      print(stdout.decode("UTF-8"))

   except Exception as e:
      print("ERROR: gits init command caught an exception")
      print("ERROR: {}".format(str(e)))
      return False
   
   return True
