## Importing libraries.
utils = Utils()
sound = Sound()
os = OS()

## Testing some functions
utils.console.info('Hi', 'there')
utils.console.warn('This is a warning')
utils.console.error('This is an error')
wait(2)
r = requests.get('http://example.com/')
utils.console.info('Status code from example.com is:', r.status_code)
utils.console.info('The current path is', os.path())

## Trying to play some random sound in my computer.
utils.console.info('Current XGIN Executor version is', version)
sound.playSound(f'{os.path()}/bloxxonova6.mp3')
