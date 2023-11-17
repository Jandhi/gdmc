from gdpc.block import Block as GDPCBlock

class Block:
    def __init__(self, name : str, properties : dict[str, str]) -> None:
        self.name = name
        self.properties = properties
    
    def __str__(self) -> str:
        string = self.name

        if len(self.properties) > 0:
            properties_string = ''

            for property in self.properties:
                properties_string += f',{property}={self.properties[property]}'

            string = f'{string}[{properties_string[1:]}]'
        
        return string

    def copy(self):
        return Block(self.name, self.properties.copy())
    
    def to_gdpc_block(self, data) -> GDPCBlock:
        if data != None:
            return GDPCBlock(id = self.name, states = self.properties, data = data)
        return GDPCBlock(id = self.name, states = self.properties)
