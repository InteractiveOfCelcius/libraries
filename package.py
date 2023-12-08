class Package:
    def __init__(self, package_data):
        self.required_version = package_data.get('required_version', None)
        self.name_package = package_data.get('name_package', None)
        self.author = package_data.get('author', None)
        self.variable = package_data.get('variable', None)

    def HolaMundo(self):
        print("¡Hola, Mundo!")
