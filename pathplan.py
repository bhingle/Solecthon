'''The approach of this method is to find cone B(which will be present at shortest distance) from cone A '''
import matplotlib.pyplot as plt
import math
def pathplan():
  left_box=[]
  right_box=[]

  #uncomment mybox to get variation in output
  #mybox=[[2,1],[5,1],[2,2],[5,2],[2,3],[5,3],[2,4],[5,4],[2,5],[5,5],[2,6],[5,6],[2,7],[5,7]]
  #mybox = [[3, 1.5], [5.5, 1.5], [3, 3], [5.5, 3], [2.5, 4.5], [5, 4.5], [2, 6], [4.5, 6], [1.5, 7.5], [4, 7.5], [1, 9],[3.5, 9], [1, 10.5], [3.5, 10.5], [2, 12], [4.5, 12], [2, 13.5], [4.5, 13.5]]
  #mybox=[[273 , 0],[144 , 28],[279 , 56],[156 , 84],[295 ,112],[177 ,140],[320 ,168],[203 ,196],[347 ,224],[229 ,252]]
  mybox=[[273  , 0],[143 , 14],[274 , 28],[147  ,42],[280,  56],[153 , 70],[288  ,84],[163 , 98],[299 ,112],[176, 126],[312 ,140],[189, 154],[327 ,168],[204 ,182],[341, 196],[219 ,210],[356, 224],[232 ,238],[368 ,252],[244 ,266]]
  mybox=sorted(mybox,key=lambda x:(x[1],x[0]))
  #print(mybox)

  #left-->first co-ordinate of left boundary
  #right-->first co-ordinate of right boundary
  left=mybox[0]
  right=mybox[1]
  left_box.append(left)
  mybox.remove(left)

  right_box.append(right)
  mybox.remove(right)

  #print(left_box)
  #print(right_box)

  #The loop runs until mybox contains the top view co-ordinates
  while(True):
    distance=[]
    j=left_box[len(left_box)-1]
    #finding distance from cone A to all the other cones
    for i in mybox:
      p=math.pow((i[0]-j[0]),2)
      q=math.pow((i[1]-j[1]),2)
      distance.append(math.sqrt(p+q))
    pos=distance.index(min(distance))
    #saving the nearest cone
    left_box.append(mybox[pos])
    mybox.remove(mybox[pos])
    
    
    distance=[]
    j=right_box[len(right_box)-1]
    for i in mybox:
      p=math.pow((i[0]-j[0]),2)
      q=math.pow((i[1]-j[1]),2)
      distance.append(math.sqrt(p+q))
    pos=distance.index(min(distance))
    right_box.append(mybox[pos])
    mybox.remove(mybox[pos])

    if(len(mybox)==0):
      break
  #end of while loop
  
  #print(left_box)
  #print(right_box)
  

  midpoints=[]
  if len(left_box)==len(right_box):
    for i in range(len(left_box)):
      k=[]
      k.append((left_box[i][0]+right_box[i][0])/2)
      k.append((left_box[i][1]+right_box[i][1])/2)
      midpoints.append(k)
  #print(midpoints)
  #if length is not equal, then ............(kam baki ahe)
  
  u=list(zip(*left_box))
  v=list(zip(*right_box))
  w=list(zip(*midpoints))
  #print(u)
  #print(v)
  plt.plot(u[0],u[1])
  plt.plot(v[0],v[1])
  plt.plot(w[0],w[1])
  plt.show()

pathplan()