import array
import binascii
import tempfile

array_a = array.array('i', range(10))

print(array_a)

output_write = tempfile.NamedTemporaryFile()

print(output_write.name)

# ouput to temp file
array_a.tofile(output_write.file)
output_write.flush()

with open(output_write.name, 'rb') as read_input:
    data_read = read_input.read()

    print(f'All data: {data_read}')

    # reading input data into an array
    # placing temp file reading to location 0
    read_input.seek(0)
    data_read_array = array.array('i')
    data_read_array.fromfile(read_input, len(array_a))

    print(data_read_array)