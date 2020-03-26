import model

m = model.Model()
print("default mode: {}".format(m))

print("setting a speed to motor 1 only")
m.m1.speed=0.2
linear_speed,rotational_speed = m.dk()
print("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed)

print("### setting same speed for both motors")
m.m1.speed=0.2
m.m2.speed=0.2
print("\n#################\nmodel: {}".format(m))
linear_speed,rotational_speed = m.dk()
print("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed)

print("### setting same speed for both motors")
m.m1.speed=0.2
m.m2.speed=-0.2
print("\n#################\nmodel: {}".format(m))
linear_speed,rotational_speed = m.dk()
print("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed)

print("### setting same speed for both motors")
m.m1.speed=0.3
m.m2.speed=0.2
print("\n#################\nmodel: {}".format(m))
linear_speed,rotational_speed = m.dk()
print("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed)

print("### setting same speed for both motors")
m.m1.speed=0.2
m.m2.speed=0.3
print("\n#################\nmodel: {}".format(m))
linear_speed,rotational_speed = m.dk()
print("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed)


