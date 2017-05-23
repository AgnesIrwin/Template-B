#aabb.py

class AABB(object):

    def __init__(self,lower_bound, upper_bound):

        self.lower_bound=lower_bound
        self.upper_bound=upper_bound

    def collides_with(self,other):

        a=self.lower_bound[0]
        b=self.lower_bound[1]
        c=self.upper_bound[0]
        d=self.upper_bound[1]
        e=other.lower_bound[0]
        f=other.lower_bound[1]
        g=other.upper_bound[0]
        h=other.upper_bound[1]


        x1=a<e<c
        x2=a<g<c
        y1=b<f<d
        y2=b<h<d

        collision=False

        if (x1 or x2) and (y1 or y2): collision=True

        return collision
