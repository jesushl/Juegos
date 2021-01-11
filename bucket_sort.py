class BucketSort():

    def get_max_value(
        self,
        input_array:list
    )->int:
        max_val = input_array[0]
        for val in input_array[1:]:
            if val > max_val:
                max_val = val 
        return max_val

    def get_buckets(
        self,
        buckets:int
    )->list:# List of list
        buckets_array = []
        for i in range(0, buckets):
            buckets_array.append([])
        return buckets_array
    
    def insert_value_in_bucket(
        self,
        value:int,
        buckets_array:list,
        max_value:int
    ):
        position  = int( len((buckets_array) * value ) / max_value )
        buckets_array[position].append(value)
        return buckets_array

    def sort(
        self,
        input_array:list,
    ):
        # Apply a quick sort
        last_value = input_array[-1]


if __name__ == '__main__':
    import random
    input_list = random.sample(range(1,100), 10)
    print('Input list : {}'.format(input_list))
    bs =  BucketSort(
        input_array=input_list
    )
    print('Max value : {}'.format(bs._get_max_value()))

