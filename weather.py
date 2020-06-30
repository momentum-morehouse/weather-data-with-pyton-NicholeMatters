import requests
import matplotlib
print ("libraries imported")


#Tennessee State 36.1668° N, 86.8276° W
#Georgia Dome 33.7577° N, 84.4008° W
#UGA 33.9480° N, 83.3773° W
#Morehouse 33.7473° N, 84.4155° W
#Spelman 33.7464° N, 84.4121° W
#Clark Atlanta 33.7516° N, 84.4112° W
#Howard 38.9227° N, 77.0194° W
#Tuskegee 32.4308° N, 85.7073° W
#FAMU 30.4269° N, 84.2851° W
#Syndey, AU 33.8688° S, 151.2093° E

location = [("36.1668° N, 86.8276° W"), ("33.7577° N, 84.4008° W"), ("33.9480° N, 83.3773°"), ("33.7473° N, 84.4155° W"), ("33.7464° N, 84.4121° W"), ("33.7516° N, 84.4112° W"), ("38.9227° N, 77.0194° W"), ("32.4308° N, 85.7073° W"), ("30.4269° N, 84.2851° W"), ("33.8688° S, 151.2093° E")]
print(location[(0])