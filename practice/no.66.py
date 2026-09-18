def masahat_calculator(**kwargs):

    if 'tool' and 'arz' and 'ertefa' in kwargs:
            return (kwargs['tool'] * kwargs['arz']) * (kwargs['ertefa'])

    elif 'tool' and 'arz' in kwargs:
        return kwargs['tool'] * kwargs['arz']

    

    return False

print(masahat_calculator(tool=5, arz=3))