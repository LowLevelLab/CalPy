# import numba as nb
# from numba.experimental import jitclass
# import numpy as np


# s = nb.typeof(np.array([[1,2,3],[4,5,6]]))
# print((s))
# a = nb.core.types.npytypes.Array()
# # print(a)
# specs = [
#     ('dtype', nb.boolean),
#     ('ndim', nb.int64),
#     ('layout', nb.c16)
# ]

# @jitclass(specs)
# class Array(np.ndarray):
#     def __new__(cls, input_array, *, shape=None, order=None):
#         obj = np.asarray(input_array).astype(np.bool_)
#         if shape is not None:
#             obj = obj.reshape(shape)
#         if order is not None:
#             obj = obj.copy(order=order)
#         return obj.view(cls)

# a = Array([[True, False], [True, False]])


# import asyncio


# async def get_result(command):
#     out = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE)
#     out, _ = await out.communicate()
#     return out.decode("utf-8").splitlines()

# async def get_result_exec(command):
#     out = await asyncio.create_subprocess_exec(command, stdout=asyncio.subprocess.PIPE)
#     out, _ = await out.communicate()
#     return out.decode("utf-8").splitlines()

# async def main():
#     tasks = [asyncio.create_task(get_result('./test.exe')) for _ in range(10)]
#     lst = await asyncio.gather(*tasks)
#     print(lst)

# if __name__ == '__main__':
#     asyncio.run(main())



import numpy as np

