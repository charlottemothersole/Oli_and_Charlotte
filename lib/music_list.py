class Music_list :
    def __init__(self) :
        self.listened_to = []
    
    def add(self, artist, track) : 
        if(artist == '' and track == '') :
            raise Exception('No text given')
        if(type(artist) != str and type(track) != str) :
            raise Exception('Not text format')
        song = f'{artist}: {track}'
        self.listened_to.append(song)
    
    def list(self) :
        if(self.listened_to == []) :
            raise Exception('List empty!')
        return self.listened_to

