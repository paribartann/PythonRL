#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:33:14 2018

@author: paribartandhakal
"""
########################################################################
# Copyright (C)                                                       #
# 2016 Shangtong Zhang(zhangshangtong.cpp@gmail.com)                  #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

#policy_iteration function is written by me

from __future__ import print_function
import numpy as np



WORLD_SIZE=5
threshold=0.000001
discount=0.9
Position_A=[0,1]
Position_A_prime=[4,1]
Position_B=[0,3]
Position_B_prime=[2,3]

states=np.zeros((5,5))
#5x5 gridworld of the RL environment
#where each box is considered as one state

actions=['U','R','L','D']

action_prob=[]
for i in range(WORLD_SIZE):
    action_prob.append([])
    for j in range(WORLD_SIZE):
        action_prob[i].append({'U':0.25, 'D':0.25, 'R':0.25, 'L':0.25})
        
#print (action_prob)
        
rewards=[]
next_state=[]

for i in range(WORLD_SIZE):
    rewards.append([])
    next_state.append([])
    for j in range(WORLD_SIZE):
        reward={}
        next_s={}
        
        if i==0:
            reward['U']=-1
            next_s['U']=[i,j]
        else:
            reward['U']=0
            next_s['U']=[i-1,j]
            
            
        if i==WORLD_SIZE-1:
            reward['D']=-1
            next_s['D']=[i,j]
        else:
            reward['D']=0
            next_s['D']=[i+1,j]
            
        if j==0:
            reward['L']=-1
            next_s['L']=[i,j]
        else:
            reward['L']=0
            next_s['L']=[i,j-1]
            
        if j==WORLD_SIZE-1:
            reward['R']=-1
            next_s['R']=[i,j]
        else:
            reward['R']=0
            next_s['R']=[i,j+1]
            
            
        #now checking for the special cases
        
        if [i,j]==Position_A:
            reward['U']=reward['D']=reward['R']=reward['L']=10
            next_s['U']=next_s['D']=next_s['R']=next_s['L']=Position_A_prime
            
        if [i,j]==Position_B:
            reward['U']=reward['D']=reward['R']=reward['L']=5
            next_s['U']=next_s['D']=next_s['R']=next_s['L']=Position_B_prime
            
            
        rewards[i].append(reward)
        next_state[i].append(next_s)

def policy_iteration(action_prob, rewards, next_state, states):
    iterations=0
    policy_stable=False
    while not policy_stable:
        iterations+=1
        policy_stable = True
        
        #for each state s ∈ S:
        for i in range(WORLD_SIZE):
            for j in range(WORLD_SIZE):
                old_distribution=(action_prob[i][j]).copy()
                Vs=0
                act_prob_sum = 0
                for action in actions:     
                    Tsa = next_state[i][j][action]
                    Vs+= action_prob[i][j][action]*(rewards[i][j][action]+discount*states[Tsa[0], Tsa[1]])
                    dist=(rewards[i][j][action]+discount*states[Tsa[0], Tsa[1]])-states[i, j]
                    action_prob[i][j][action]=(action_prob[i][j][action]+0.001*dist)
                    action_prob[i][j][action]=np.clip(action_prob[i][j][action],0,1)
                    act_prob_sum += action_prob[i][j][action]
                
                states[i][j]= Vs
                #normalizing π(a|s)
                for a in actions:
                    action_prob[i][j][a] /= act_prob_sum
                delta = sum([abs(action_prob[i][j][a]-old_distribution[a]) for a in actions])
                
                
		
                if delta>threshold:
                    policy_stable=False
    
    for i in range(WORLD_SIZE):
            for j in range(WORLD_SIZE):
                for action in actions:
                    action_prob[i][j][action]=round(action_prob[i][j][action],2)
                    
    return (action_prob, iterations)
                    
(prop2,its1)=policy_iteration(action_prob, rewards, next_state, states)
print("\nOptimal policy Function: Policy Iteration")
print("Iterations:{}".format(its1))
print(prop2)
