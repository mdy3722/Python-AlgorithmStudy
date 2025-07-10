# def summarize_string(input_str):
#     arr_occurence = [0] * 26
#
#     for char in input_str:
#         index = ord(char) - ord('a')
#         arr_occurence[index] += 1
#
#     result = ""
#
#     for i in range(len(arr_occurence)):
#         if arr_occurence[i] != 0:
#             result += chr(i + ord('a'))
#             result += str(arr_occurence[i])
#             result += '/'
#
#     result = result.rstrip('/')
#
#     return result
def summarize_string(target_string):
    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i+1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str

input_str = "acccdeee"

print(summarize_string(input_str))