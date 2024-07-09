from typing import List


def moveZeros(nums: List[int]) -> List[int]:
    j = 0  # Ponteiro para rastrear a posição de inserção

    for i in range(len(nums)):  # Ponteiro para iterar sobre o array
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # Preencher os espaços restantes com zeros
    for k in range(j, len(nums)):
        nums[k] = 0

    return nums


# Teste com um exemplo
nums = [0, 1, 0, 3, 12]
print(moveZeros(nums))  # Output: [1, 3, 12, 0, 0]
