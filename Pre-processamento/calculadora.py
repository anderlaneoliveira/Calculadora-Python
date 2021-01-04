#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calculadora em Python


# In[ ]:


# Desenvolvimento de uma calculadora simples usando linguagem Python.


# In[ ]:


print("\n******************* Python Calculator *******************")


# In[ ]:


intro = ("Selecione a opção desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
print(intro)


# In[ ]:


x = int(input("Digite sua opção: (1/2/3/4)"))


# In[ ]:


a = int(input("Digite o primeiro número: "))


# In[ ]:


b = int(input("Digite o segundo número: "))


# In[ ]:


def calculadora():
    if (x == 1): 
        resultado = (a + b)
        return resultado
    elif (x == 2):
        resultado = (a - b)
        return resultado
    elif (x == 3):
        resultado = (a * b)
        return resultado
    elif (x == 4):
        resultado = (a / b)
        return resultado
    else:
        print("Opção Inválida")


# In[ ]:


print('O resultado é %s' %calculadora())

