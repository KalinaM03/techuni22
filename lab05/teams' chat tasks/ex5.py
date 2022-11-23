#
def is_valid_triangle(a,b,c):
    if type(a)!=int or type(b)!=int or type(c)!=int:
        return False

    if a+b>c:
        if a+c>b:
            if b+c>a:
                return True
    return False


def can_triangle_exist(a,b,c):
    return is_valid_triangle(a,b,c)


print(is_valid_triangle(2,3,4))
print(can_triangle_exist(2,3,'4'))