# Calcular a Soma das Frequências dos Elementos com Frequência Máxima

"""
Retorne as frequências totais dos elementos em nums de modo que todos esses 
elementos tenham a frequência máxima.
"""

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # contando a frequencia de cada elemento
        # para mapear cada elemento único de nums à sua frequência 
        # (ou seja, quantas vezes ele aparece na lista).
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
        
        
