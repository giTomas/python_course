# from subprocess import call, check_call, check_output, run
from subprocess import Popen, PIPE

# check_call
# exception when exit code is not 0

# run
# combine all other functions

# call(['ls', '-l', '/dev/null'])
# # call('ls')
#
# lines = check_output(['ls', '-l', '/dev/null'], )

p = Popen(
    ['python', 'echo.py'],
    stdin = PIPE,
    stdout = PIPE,
    bufsize = 0)

p.stdin.write(b'Hello\n')
p.stdout.flush()
p.stdin.flush()
