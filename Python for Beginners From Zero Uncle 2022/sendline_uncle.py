from songline import Sendline

token = 'HdAOGiFcmQovCRP7KYwsdZi2eYJTs6PH6kV3s8Q2GQO'
messenger = Sendline(token)
messenger.sendtext('Hello World')
messenger.sticker(1,1)
messenger.sendimage('https://picturetoyou.com/wp-content/uploads/2021/11/57.jpg')