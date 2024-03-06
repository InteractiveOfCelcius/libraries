DATA = [
  "0.01", "porotical"
]

def program():
  ## Importing libraries.
  utils = Utils()
  sound = Sound()
  console = utils.Console()
  #os = OS()
  
  ## Testing some functions
  console.info('Hi', 'there')
  console.warn('This is a warning')
  console.error('This is an error')
  wait(2)
  r = requests.get('http://example.com/')
  console.info('Status code from example.com is:', r.status_code)
  #console.info('The current path is', os.path())
  
  ## Trying to play some random sound in my computer.
  console.info('Current XGIN Executor version is', version)
  print(os.getcwd())
