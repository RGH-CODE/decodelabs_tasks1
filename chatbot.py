import random as rand
from knowledge_base import knowledge


def get_response(user_input, user_name=None):
    user_input = user_input.lower().strip()
        
    for keys, values in knowledge.items():

        # If the key is a tuple
        if isinstance(keys, tuple):

            if user_input in keys:
                matched = True

                if values == "your_name":
                    if user_name:
                        return f"Bot: Your name is {user_name}."
                
                    return "I don't know your name yet."
                
                response=rand.choice(values)
                return f"{user_name},{response}" if user_name else response

               
        else:
        # If the key is a normal string
           if user_input == keys:
               
            if isinstance(values, list):
                response = rand.choice(values)
            else:
                response = values

            if user_name:
               return f"{user_name}, {response}"

            return response
        

    if user_name:
        return f"Bot: Sorry {user_name}, I don't understand that."
    
    return "Bot: Sorry, I don't understand that."