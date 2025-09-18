from flask import Flask, request
import random

app = Flask(__name__)

def make_speech_bubble(message):
    bubble_len = len(message) + 4
    return f"""
 {"_" * bubble_len}
< {message} >
 {"-" * bubble_len}"""

def get_cow_art(cow_type):
    cows = {
        'cow': """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||""",
                
        'sheep': """
        \\
         \\
            __     
          UooU\\.'@@@@@@`.
          \\__/(@@@@@@@@@@)
               (@@@@@@@@)
               `YY~~~~YY'
                ||    ||""",
                
        'dragon': """
        \\                    / \\  //\\
         \\    |\\___/|      /   \\//  \\\\
              /0  0  \\__  /    //  | \\ \\    
             /     /  \\/_/    //   |  \\  \\  
             @_^_@'/   \\/_   //    |   \\   \\ 
             //_^_/     \\/_ //     |    \\    \\
          ( //) |        \\///      |     \\     \\
        ( / /) _|_ /   )  //       |      \\     _\\
      ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
    (( / / )) ,-{        _      `-.|.-~-.           .~         `.
   (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
   (( /// ))      `.   {            }                   /      \\  \\
    (( / ))     .----~-.\\        \\-'                 .~         \\  `. \\^-.
               ///.----..>        \\             _ -~             `.  ^-`  ^-_
                 ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                    /.-~""",
                                                                    
        'elephant': """
        \\
         \\
          \\     /~~\\  
           \\   |    |  ___
            \\ /~~~~~~\\/   \\
             |  * *  |\\   /
             |   o   | \\_/ 
             | \\___/ |   
            /|\\  |  /|\\  
           / | \\_|_/ | \\ 
              \\     /    
               |   |     
               |___|     """,
               
        'tux': """
        \\
         \\
          \\
            .--.
           |o_o |
           |:_/ |
          //   \\ \\
         (|     | )
        /'\\_   _/`\\
        \\___)=(___/"""
    }
    return cows.get(cow_type, cows['cow'])

@app.route('/cow')
def cow():
    message = request.args.get('msg', 'Hello')
    cow_type = request.args.get('type', 'cow')
    
    bubble = make_speech_bubble(message)
    art = get_cow_art(cow_type)
    
    return bubble + art

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
