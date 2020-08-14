# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:05:20 2020
-+

@author: WITLab
"""

import numpy as np
import pandas as pd

# 데이터 입력
data = pd.read_csv(r'C:\Users\이름\python\실습\경로설정\fullsearch11.csv')               # read CSV file
# 데이터 확인
data
# 데이터 정제
data =data.fillna(0)                                                    # fill NaN by 0                                                    
# 출발 노드 데이터 추출
Start = data['Start']                                                   # Select Start Node 
# 출발 노드 중복 배제(단일값만 생성)
S = list(np.unique(Start))

# 변수 설정
route = []                                                              # empty holder to save data                                               
node = []

# 네트워크 토폴로지 형성(노드-링크)
# Generate a road Network in term of Dictonary

# 노드 정보로부터 그래프(토폴로지) 형성 (노드: 인접 노드)
for each in S:                                                          # 'each' variable will get one value at a time from S 
    E = list(data[data['Start'] == each]['End'])                        # Generate the list of neighoburing node "END"
    form = (each, E)                                                    # hold "Start" node and "End" node together 
    route.append(form)                                                  # Save the list after each for loop 
graph = dict(route)                                                     # Convert road network list to Road Network Dictionary

# 링크(출발노드, 도착노드, 거리, 불법주정차 정보)
link = np.array(data[['Start','End','Length(m)','IllegalParking_index']])   # Select columns from input data

#Generate Road network with Length and Illegal Parking density

# 링크와 관련 정보(거리, 불법주정차 변수) 
link_dis_IPD = []
for each in range (0,len(link)):
    x = (link[each][0], link[each][1]), [link[each][2], link[each][3]]      # Strat -> End Node (combination) Length and Illegal Parking density
    link_dis_IPD.append(x)
dis_IP = dict(link_dis_IPD)                                                 # convert list to dictionary 

# 네트워크 토폴로지 형성(노드-링크)
graph
dis_IP


# 함수 정의
# (현재) 출발 노드, 도착 노드 : current_vertex, end_verte
# 직전 노드 : previous

# function defination for full Search Algorithm
def find_all_paths(dis_IP, graph, current_vertex, end_vertex, previous, distance, IP_Density, path=[]):
    
    # dis_IP : Start -> Node Pair with Distance and Illegal Parking Index
    # Graph : Start -> Neighoubour node
    # Start_vertex = end_vertex = Initial Node (predefined)
    # previous : last Node (at begining always fixed to 0)
    # distance: legnth of road for [previous_node, current_node]
    # IP_density : illegal parking index [previous_node, current_node]
    # Path : Start to end node route 
    
    
# 방문 노드셋
    path = path + [current_vertex]

    """ calculating route length and route IP density 
        during the route finding """
# 이전 노드 유무
    if previous != 0:                                                     # check the previous node
        # 이전 링크 거리
        dis = dis_IP[previous, current_vertex][0]                         # distance of [previous_node, current_node]
                                                # check the previous node
        # 이전 불법주정차
        density = dis_IP[previous, current_vertex][1]                     # Illegal parking density of [previous_node, current_node]
# 이전 노드 없음 조건(루트시작 노드)
    else: 
        dis = 0                                                           # distance and IP density is 0
        density = 0
    previous = current_vertex                                             # Pervious node is set as current node
        
    
    
    # 거리 누적 합산
    distance = distance + dis                                             # distance are added/stored after each for loop
    # 불법주정차 합산
    IP_Density = IP_Density + density                                     # IP_density are added/stored after each for loop

    # 종착 노드 여부(모든 정보 출력) 
    if (current_vertex == end_vertex):                                    # current_node is same as end_node return path, distance, and IP_density 
        return [path, np.around(distance, decimals = 4), np.around(IP_Density, decimals = 4)]

    # 노드 지속 여부 
    if current_vertex not in graph:                                       # current_node is not in Road network return null            
        return []

    # 루트 변수
    paths = []                                                            # empty array
    
    # 다음 노드(vertex) 선택
    for vertex in graph[current_vertex]:                                  # Select one node at a time from Road network
        # 다음 노드로 선택 조건(현재까지 미방문)
        if vertex not in path:                                            # if node is not visited by Full search Algorithm
            # 인접 노드 정보 수집
            extended_paths = find_all_paths(dis_IP, graph,  vertex, end_vertex, previous, distance, IP_Density, path) # recall itself with new Current_node
            for p in extended_paths:                                      # Append all the visited node, its total length and IP_density
                   # 각 루트에 인접 노드 추가 
                   paths.append(p)
    return paths                                                          # return result 

# 함수 종료

# 루트 생성
routes = find_all_paths(dis_IP,graph,8,80,0,0,0)                             # function call 8: startinf 80 : ending (same as 8)
print(routes)                                                               # print path

# 행렬 변환
solution = np.array(routes)      
solution                                          # convert all path into array
solution = solution.reshape(int(solution.shape[0]/3),3)                   # reshape to get individual route 
solution 
solutionDF = pd.DataFrame(solution)                                       # convert into dataframe (table)
solutionDF.columns = ['Routes','Distance', 'Density']                     # change column names

# sort by illegal parking density in descending (Highest value) followed by Distance in ascending order (Minimum distance)
solutionDF.sort_values(['Density','Distance'], ascending = [False, True], inplace = True)           
# solutionDF.to_csv(r'H:\Illegalparking\solutionSmall.csv')

print ('List of All Possible Route')
print(solutionDF)

print('Optimal Route')
print(solutionDF[0:1])

#%%
