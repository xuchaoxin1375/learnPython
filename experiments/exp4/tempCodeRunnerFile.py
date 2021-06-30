import numpy as np
from numpy import random 
import itertools
class HDPoints():
    def __init__(self,HDPoints_list):
        self.points =HDPoints_list
    def centerpoint(self):
        ndarray=np.array(self.points)
        return sum(ndarray)/len(ndarray)
    
    def minkowski(self,x,y,p):
        abs_list= [abs(x-y)**p for x,y in zip(x,y)]
        return sum(abs_list)**(1/p)

    def farthestpoint(self,p):
        centerpoint=self.centerpoint()
        distances_list=[self.minkowski(centerpoint,point,p) for point in self.points ]
        max_distance= max(distances_list)
        return  distances_list.index(max_distance),max_distance
    def farthest2points(self,p):
        points_index_tuple_list=[(point,i)for i,point in enumerate(self.points)]
        point_pairs_tuples=(itertools.combinations(points_index_tuple_list,r=2))
            #element shape:(([point_list1],index2),([point_list2],index2))
            
        distances_list=[(self.minkowski(tuple[0][0],tuple[1][0],p),(tuple[0][1],tuple[1][1])) for tuple in point_pairs_tuples ]
            #element shape:(minkowski_distance,(index1,index2))
        max_distance_point=max(distances_list,key=lambda tuple:tuple[0])
        return max_distance_point[1],max_distance_point[0]

        
        

# a=random.rand(1,0.5,2,3,6,3)
a=random.uniform(0,1,5).tolist()
""" get points list: """
points=[random.uniform(0,1,5).tolist() for i in range(50)]
hd_Points=HDPoints(points)
p=random.randint(1,6)
print("the centerpoint is:",hd_Points.centerpoint())
""" the minkowski method will be test contained in the farthestpoint() method! """
print("the farthest point:",hd_Points.farthestpoint(p))
print(f"the farthest2point: index of the 2 pointes: {hd_Points.farthest2points(p)[0]},the max minkowski distance is {hd_Points.farthest2points(p)[1]}")