def print_sum_avg_args(*args):
   count = 0

   for i in args:
      count += 1

   avg = count / len(args)

   print(count)
   print(avg)

print_sum_avg_args(2,4,1)
