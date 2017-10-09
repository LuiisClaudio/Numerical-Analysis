#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:37:34 2017

@author: LuisClaudio
"""

def lu(a, l, u, n):
    i = 0; j = 0; k = 0;
    for i in range(n): 
        for j in range(n):
            if j < i:
                l[j][i] = 0
            else:
                l[j][i] = a[j][i]
                for k in range(i):
                    l[j][i] = l[j][i] - l[j][k] * u[k][i]
                    
        for j in range(n):
            if j < i:
                u[i][j] = 0
            if i == j:
                 u[i][j] = 1
            else:
                u[i][j] = a[i][j] / l[i][i]
                for k in range(i):
                    u[i][j] = u[i][j] - ((l[i][k] * u[k][j]) / l[i][i])


""" 
void lu(float a[][10], float l[][10], float u[][10], int n)
{
    int i = 0, j = 0, k = 0;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (j < i)
                l[j][i] = 0;
            else
            {
                l[j][i] = a[j][i];
                for (k = 0; k < i; k++)
                {
                    l[j][i] = l[j][i] - l[j][k] * u[k][i];
                }
            }
        }
        for (j = 0; j < n; j++)
        {
            if (j < i)
                u[i][j] = 0;
            else if (j == i)
                u[i][j] = 1;
            else
            {
                u[i][j] = a[i][j] / l[i][i];
                for (k = 0; k < i; k++)
                {
                    u[i][j] = u[i][j] - ((l[i][k] * u[k][j]) / l[i][i]);
                }
            }
        }
    }
}
"""