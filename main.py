# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting='Hello, <name>!'):
    greeting = greeting.replace('<name>', name)
    return greeting
    
(greet('Andre'))



def force(mass, body='earth'):
    arguments = {'sun': 274,
	             'jupiter':	24.92,	   
                 'neptune':	11.15,
	             'saturn': 10.44,
	             'earth': 9.798, 
	             'uranus': 8.87,
	             'venus': 8.87,
	             'mars': 3.71,
	             'mercury':	3.7,
                 'moon': 1.62,   
                 'pluto': 0.58
    }
    body = arguments[body]
    return round(body, 1) * mass
print(force(10, 'sun'))

def pull(m1, m2, d):
    g = 6.674*(10**-11)
    f = (g * m1 * m2) / (d **2)
    return f

print(pull(800, 1500, 3))
print(pull(0.1, 5.972 * 10**24, 6.371 * 10**6))









    





